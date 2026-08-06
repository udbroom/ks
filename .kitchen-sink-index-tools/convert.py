import markdown, json, re, os, datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_ROOT = os.path.dirname(SCRIPT_DIR)  # kitchen-sink-docs/
src_dir = os.path.join(DOCS_ROOT, "blocks")
files = sorted(f for f in os.listdir(src_dir) if f.endswith(".md"))

# Per-block Figma "Tech spec" links, curated by hand (not auto-discovered —
# each block's Figma file has separate Cover / Usage guidelines / Tech spec
# pages, and only the Tech spec node should be linked here). Add more slugs
# as their links are confirmed.
TECH_SPEC_LINKS_PATH = os.path.join(SCRIPT_DIR, "tech_spec_links.json")
with open(TECH_SPEC_LINKS_PATH, "r", encoding="utf-8") as f:
    TECH_SPEC_LINKS = json.load(f)

FN_DEF_RE = re.compile(r'^\[\^([\w-]+)\]:[ \t]*(.+)$', re.MULTILINE)
FN_REF_RE = re.compile(r'\[\^([\w-]+)\]')

# The "#autoplay alone" gotcha sentence recurs (with minor per-block wording)
# across every video-authoring Notes bullet — flag it visually wherever it
# appears rather than leaving it as plain bullet text, since it's the most
# common way authors accidentally break scroll-triggered video playback.
AUTOPLAY_WARNING_RE = re.compile(
    r'Using <code>#autoplay</code> alone plays the video immediately on page load.*?frozen last frame\.',
    re.DOTALL,
)


def highlight_autoplay_warning(html):
    """Wrap the '#autoplay alone' gotcha sentence in a callout span so it
    visually stands out inside its Notes bullet, post markdown conversion."""
    return AUTOPLAY_WARNING_RE.sub(
        lambda m: f'<span class="autoplay-warn">{m.group(0)}</span>', html
    )


def extract_footnotes(raw):
    """Pull out [^id]: definition lines (repo convention: a PR/commit link +
    author + date noting when a variation was added), turn each inline
    [^id] reference into a clickable superscript marker instead of leaving
    a literal '[^id]' + a footnote dump at the bottom of the doc."""
    order = []
    defs = {}
    for match in FN_DEF_RE.finditer(raw):
        fid, content = match.group(1), match.group(2).strip()
        if fid not in defs:
            order.append(fid)
        defs[fid] = content

    # Remove the definition lines entirely.
    cleaned = FN_DEF_RE.sub('', raw)

    footnotes = {}
    for i, fid in enumerate(order, start=1):
        content_html = markdown.markdown(defs[fid], extensions=["tables"])
        content_html = re.sub(r'^<p>|</p>\s*$', '', content_html.strip())
        footnotes[fid] = {"num": i, "html": content_html}

    def replace_ref(m):
        fid = m.group(1)
        fn = footnotes.get(fid)
        if not fn:
            return m.group(0)  # no matching definition, leave as-is
        return f'<sup class="fn-ref" data-fn="{fid}" title="Click for details">{fn["num"]}</sup>'

    cleaned = FN_REF_RE.sub(replace_ref, cleaned)
    return cleaned, footnotes


# The Example section's fenced-code pipe mockups get converted into real
# rendered authoring tables (instead of a plain-text code block) for every
# block. A couple of blocks need bespoke handling beyond the generic table
# renderer — see COMPARISON_TABLE_SLUG and the "[Section break]" handling.
COMPARISON_TABLE_SLUG = "comparison-table-c2"

FENCE_RE = re.compile(r'```\n(.*?)```', re.DOTALL)
SEPARATOR_CELL_RE = re.compile(r'^:?-{2,}:?$')
# A bare pipe used as a cell boundary; "\|" is an author escaping a literal
# pipe character inside a cell (e.g. jump-link's "[A](#a) \| [B](#b)") and
# must NOT be treated as a column split.
PIPE_SPLIT_RE = re.compile(r'(?<!\\)\|')
VIEWPORT_ROW_RE = re.compile(
    r'^(mobile|tablet|desktop)(-viewport)?(\s*\([\w,\s-]+\))?$', re.IGNORECASE
)
# Stray kramdown/attr-list annotations (e.g. "{: .con-button}" or
# '{width="192" height="230"}') that show up in a couple of example mockups
# as documentation shorthand, not something an author actually types into
# the table — drop them rather than render literally.
ATTR_LIST_RE = re.compile(r'\{[^{}]{1,80}\}')
SECTION_BREAK_RE = re.compile(r'^\[section break\]$', re.IGNORECASE | re.MULTILINE)
IMAGE_LINE_RE = re.compile(r'^!\[([^\]]*)\]\(([^)]+)\)$')


def _split_row(line):
    stripped = line.strip()
    if stripped.startswith('|'):
        stripped = stripped[1:]
    if stripped.endswith('|'):
        stripped = stripped[:-1]
    return [c.strip().replace('\\|', '|') for c in PIPE_SPLIT_RE.split(stripped)]


HEX_COLOR_RE = re.compile(r'^#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$')

BR_RE = re.compile(r'<br\s*/?>', re.IGNORECASE)
# A couple of docs use a literal two-character "\n" (not a real newline) as
# their line-break convention inside a cell, instead of <br> — treat the same.
LITERAL_NL_RE = re.compile(r'\\n')


def _render_cell(text):
    if not text:
        return ''
    text = ATTR_LIST_RE.sub('', text).strip()
    # A bare hex color (e.g. a Background row's value) starts with '#', which
    # Python-Markdown misreads as an ATX heading — render it as a swatch instead.
    if HEX_COLOR_RE.match(text):
        return f'<span class="color-swatch" style="background:{text}"></span><code>{text}</code>'
    # A lone "-" marks "not included" / empty in several blocks' conventions.
    if text.strip() == '-':
        return '<span class="empty-dash" title="Not included">—</span>'
    # Cells are authored as a single logical line with literal <br> (or "\n")
    # standing in for the author pressing Enter inside a table cell. Without
    # real newlines, Markdown has no line boundary to stop an ATX heading at,
    # so a leading '##' would swallow the entire rest of the cell as one
    # heading. Turn each line-break marker into a real paragraph break first.
    text = BR_RE.sub('\n\n', text)
    text = LITERAL_NL_RE.sub('\n\n', text)
    # This Markdown library requires ATX headings to have zero leading
    # whitespace (stricter than CommonMark's "up to 3 spaces"), and several
    # docs write "<br> ## Heading" with a leading space after the break —
    # strip each line so headings after a break are recognized correctly.
    text = '\n'.join(l.strip() for l in text.split('\n'))
    html = markdown.markdown(text, extensions=["tables"]).strip()
    # Only unwrap a single wrapping <p> (the common one-line-cell case) —
    # verify there's exactly one <p> total, not just that the string starts
    # and ends with p tags (a greedy match across multiple blocks would strip
    # the wrong ends and leave orphaned tags in the middle).
    if html.startswith('<p>') and html.endswith('</p>') and html.count('<p>') == 1:
        html = html[len('<p>'):-len('</p>')]
    return html


def _merge_stacked_rows(body_rows):
    """Some examples author a 2-column card's foreground content as several
    stacked single-cell lines (icon, heading, body...) and only introduce the
    second (media) column on the very last line via extra pipes, e.g. Base
    Card / Tour / Elastic Carousel's slides. Detect that exact shape — every
    row but the last has 1 cell, and the last row has more than 1 — and merge
    the stacked lines into a single first column, joined by real line breaks,
    with the last row's first cell appended and any empty filler cells (typos
    from hand-typed '||') dropped."""
    if len(body_rows) < 2:
        return body_rows
    if not all(len(r) == 1 for r in body_rows[:-1]):
        return body_rows
    if len(body_rows[-1]) <= 1:
        return body_rows
    if any(VIEWPORT_ROW_RE.match(r[0].strip()) for r in body_rows[:-1]):
        return body_rows  # a viewport-delimited block, not a stacked card

    last = body_rows[-1]
    col1_parts = [r[0] for r in body_rows[:-1]] + [last[0]]
    col1 = '<br>'.join(p for p in col1_parts if p.strip())
    rest_cols = [c for c in last[1:] if c.strip()]
    return [[col1] + rest_cols]


def _split_groups(body_rows):
    """Split body rows on any further pure-dashes row (beyond the header
    separator already removed) — used by examples that stack more than one
    card/slide in a single fenced block (e.g. Elastic Carousel's 2 slides)."""
    groups, current = [], []
    for r in body_rows:
        if all(SEPARATOR_CELL_RE.match(c) or c == '' for c in r):
            if current:
                groups.append(current)
                current = []
            continue
        current.append(r)
    if current:
        groups.append(current)
    return groups or [[]]


def render_example_table(code_text):
    """Turn a fenced-block pipe mockup (block-name header row, a dashes
    separator row, then one content row per authoring row) into a real
    <table> that looks like what an author sees in their doc editor."""
    lines = [l for l in code_text.split('\n') if l.strip()]
    if not lines:
        return None

    rows = [_split_row(l) for l in lines]

    header_cells = rows[0]
    body_rows = rows[1:]
    # Drop a pure-dashes separator row if present (row 2 in the mockup).
    if body_rows and all(SEPARATOR_CELL_RE.match(c) or c == '' for c in body_rows[0]):
        body_rows = body_rows[1:]

    groups = [_merge_stacked_rows(g) for g in _split_groups(body_rows)]
    all_rows = [r for g in groups for r in g]
    ncols = max([len(r) for r in all_rows] + [len(header_cells)] + [1])

    out = ['<table class="authoring-example-table">']
    out.append(f'<tr class="ex-header-row"><th colspan="{ncols}">{_render_cell(" ".join(header_cells))}</th></tr>')
    for gi, group in enumerate(groups):
        for ri, r in enumerate(group):
            # A single-cell "mobile" / "desktop (dark)" style row is a
            # viewport delimiter, not real content — style it distinctly.
            if len(r) == 1 and VIEWPORT_ROW_RE.match(r[0].strip()):
                out.append(
                    f'<tr class="ex-viewport-row"><td colspan="{ncols}">&#9656; {r[0].strip()}</td></tr>'
                )
                continue
            cells = r + [''] * (ncols - len(r))
            tds = ''.join(f'<td>{_render_cell(c)}</td>' for c in cells)
            row_class = ' class="ex-group-start"' if gi > 0 and ri == 0 else ''
            out.append(f'<tr{row_class}>{tds}</tr>')
    out.append('</table>')
    return '\n'.join(out)


# ---- Comparison Table C2: bespoke parser -----------------------------------
# This block's example uses a convention the generic renderer can't safely
# guess at: raw "|" inside **bold** text as a label|position|tooltip triplet,
# "+++" rows that split the table into independently-collapsible sub-tables,
# and a "primary" marker cell that flags a plan column rather than rendering
# as a cell itself. See comparison-table-c2.md's Authoring instructions.
BOLD_SPAN_RE = re.compile(r'\*\*(.+?)\*\*')
PIPE_PLACEHOLDER = '\x00PIPE\x00'


def _protect_bold_pipes(line):
    def _protect(m):
        return '**' + m.group(1).replace('|', PIPE_PLACEHOLDER) + '**'
    return BOLD_SPAN_RE.sub(_protect, line)


def _split_row_protecting_bold(line):
    protected = _protect_bold_pipes(line)
    cells = _split_row(protected)
    return [c.replace(PIPE_PLACEHOLDER, '|') for c in cells]


def _render_tooltip_label(text):
    """Render a feature row's "**Label|position|Tooltip**" first cell as an
    underlined label with a native-tooltip title attribute."""
    m = re.match(r'^\*\*(.+?)\*\*$', text.strip())
    inner = m.group(1) if m else text.strip()
    parts = inner.split('|')
    label = parts[0].strip()
    tooltip = parts[2].strip() if len(parts) >= 3 else ''
    if tooltip:
        return f'<span class="tooltip-label" title="{tooltip}">{label}</span>'
    if len(parts) > 1:
        return f'<span class="tooltip-label">{label}</span>'
    return _render_cell(text)


def _render_plan_card_cell(text):
    """A header plan cell groups its lines into up to 3 chunks using a
    lone '---' line (written with the doc's literal '\\n' line-break
    convention) as the divider: eyebrow/heading/price, optional collapsible
    copy, then the CTA. Split on real dashes-only lines (not the two-sided
    regex, which misses a trailing divider with nothing after it) and join
    each group's lines with real paragraph breaks so they don't run together."""
    text = LITERAL_NL_RE.sub('\n', text)
    lines = [l.strip() for l in text.split('\n')]
    groups, current = [], []
    for l in lines:
        if re.fullmatch(r'-{2,}', l):
            groups.append(current)
            current = []
        elif l:
            current.append(l)
    groups.append(current)
    groups = [g for g in groups if g]
    rendered = [_render_cell('\n\n'.join(g)) for g in groups]
    return '<hr class="cell-group-divider">'.join(rendered)


def render_comparison_table(code_text):
    """Render one Comparison Table C2 mockup (header row of plan cards, then
    feature rows, optionally split by '+++' into independently-collapsible
    sub-tables) as one or more real tables."""
    lines = [l for l in code_text.split('\n') if l.strip()]
    if not lines:
        return None

    rows = [_split_row_protecting_bold(l) for l in lines]
    header_label = rows[0][0] if rows[0] else 'Comparison Table C2'
    body_rows = rows[1:]

    # Split into sub-tables on a row whose single cell is exactly "+++".
    subtables, current = [], []
    for r in body_rows:
        if len(r) == 1 and r[0].strip() == '+++':
            subtables.append(current)
            current = []
        else:
            current.append(r)
    subtables.append(current)

    out = []
    for si, sub in enumerate(subtables):
        if not sub:
            continue
        plan_header = None
        feature_rows = sub
        primary_idx = None
        # After a '+++' divider (i.e. every sub-table but the first), the
        # first row is that sub-table's own toggle heading, and one of its
        # other cells may contain the literal word "primary" flagging a plan.
        if si > 0:
            plan_header = sub[0]
            feature_rows = sub[1:]
            for i, c in enumerate(plan_header):
                if c.strip() == 'primary':
                    primary_idx = i
            plan_header = [c for i, c in enumerate(plan_header) if i != primary_idx]

        ncols = max([len(r) for r in feature_rows] + [len(plan_header or []), 1])

        out.append('<table class="authoring-example-table">')
        label = plan_header[0] if plan_header else header_label
        primary_badge = ' <span class="badge-primary">Primary</span>' if primary_idx is not None else ''
        out.append(f'<tr class="ex-header-row"><th colspan="{ncols}">{_render_cell(label)}{primary_badge}</th></tr>')

        for ri, r in enumerate(feature_rows):
            cells = r + [''] * (ncols - len(r))
            tds = []
            for ci, c in enumerate(cells):
                # First row (plan cards) uses "---" (via literal \n) to group
                # eyebrow/price, collapsible copy, and CTA into 3 chunks.
                if ri == 0 and si == 0:
                    tds.append(f'<td>{_render_plan_card_cell(c)}</td>')
                elif ci == 0:
                    tds.append(f'<td>{_render_tooltip_label(c)}</td>')
                else:
                    tds.append(f'<td>{_render_cell(c)}</td>')
            out.append(f'<tr>{"".join(tds)}</tr>')
        out.append('</table>')
    return '\n'.join(out)


def _render_chunk(chunk_lines, slug):
    """Render one blank-line-separated chunk of an Example fence: a pipe
    table, a standalone image (a section's background, authored outside any
    block), or — as a fallback — plain markdown text."""
    text = '\n'.join(chunk_lines).strip()
    if not text:
        return ''
    non_empty = [l for l in chunk_lines if l.strip()]

    if len(non_empty) == 1 and IMAGE_LINE_RE.match(non_empty[0].strip()):
        m = IMAGE_LINE_RE.match(non_empty[0].strip())
        alt, src = m.group(1), m.group(2)
        alt_attr = alt.replace('&', '&amp;').replace('"', '&quot;')
        src_attr = src.replace('&', '&amp;').replace('"', '&quot;')
        caption = (alt or src).replace('&', '&amp;').replace('<', '&lt;')
        return (f'<div class="ex-image-preview"><img src="{src_attr}" alt="{alt_attr}">'
                f'<span class="ex-image-caption">{caption}</span></div>')

    if all(l.strip().startswith('|') for l in non_empty):
        if slug == COMPARISON_TABLE_SLUG:
            return render_comparison_table(text) or ''
        return render_example_table(text) or ''

    return markdown.markdown(text, extensions=["tables"])


def render_example_block(code_text, slug):
    """Render one whole fenced Example block. Handles the common single- or
    multi-table case, examples that stack several separate mini-tables with
    blank lines between them (e.g. Offer Hero, PDF Space), and examples that
    use literal "[Section break]" markers to show content spanning multiple
    page sections (e.g. Carousel C2's slide illustration)."""
    segments = SECTION_BREAK_RE.split(code_text.strip('\n'))
    has_breaks = len(segments) > 1

    rendered_segments = []
    for seg in segments:
        chunks = re.split(r'\n\s*\n', seg.strip('\n'))
        chunk_html = [_render_chunk(c.split('\n'), slug) for c in chunks if c.strip()]
        rendered_segments.append('\n'.join(h for h in chunk_html if h))

    if not has_breaks:
        return '\n'.join(rendered_segments)

    out = []
    for i, seg_html in enumerate(rendered_segments):
        if not seg_html:
            continue
        label = 'New page section' if i > 0 else 'Page section'
        out.append(f'<div class="ex-section-divider">&#9656; {label}</div>')
        out.append(f'<div class="ex-section-body">{seg_html}</div>')
    return '\n'.join(out)


def convert_example_sections(raw, slug):
    """Within the '## Example' section only, replace fenced pipe-mockup code
    blocks with rendered authoring tables."""
    m = re.search(r'^## Example\s*$', raw, re.MULTILINE)
    if not m:
        return raw
    start = m.end()
    m2 = re.search(r'^## ', raw[start:], re.MULTILINE)
    end = start + m2.start() if m2 else len(raw)

    section = raw[start:end]

    def replace_fence(fm):
        block_html = render_example_block(fm.group(1), slug)
        if not block_html:
            return fm.group(0)
        # Blank lines around the raw HTML so python-markdown treats it as a
        # block-level HTML pass-through instead of trying to inline-process it.
        return '\n' + block_html + '\n'

    new_section = FENCE_RE.sub(replace_fence, section)
    return raw[:start] + new_section + raw[end:]


blocks = []
for fname in files:
    path = os.path.join(src_dir, fname)
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    slug = fname[:-3]
    # title = first H1
    m = re.search(r'^#\s+(.+)$', raw, re.MULTILINE)
    title = m.group(1).strip() if m else slug

    # quick summary = first blockquote block (lines starting with >)
    summary = ""
    m2 = re.search(r'^>\s*\*\*Quick summary:\*\*\s*(.+?)(?:\n\n|\Z)', raw, re.MULTILINE | re.DOTALL)
    if m2:
        summary = re.sub(r'\n>\s*', ' ', m2.group(1)).strip()
    else:
        # fallback: first paragraph after title
        parts = raw.split('\n\n')
        summary = parts[1].strip() if len(parts) > 1 else ""

    # section presence check
    sections = {
        "authoring": bool(re.search(r'^##\s+Authoring instructions', raw, re.MULTILINE)),
        "variations": bool(re.search(r'^##\s+Variations', raw, re.MULTILINE)),
        "example": bool(re.search(r'^##\s+Example', raw, re.MULTILINE)),
        "notes": bool(re.search(r'^##\s+Notes', raw, re.MULTILINE)),
    }

    cleaned_raw, footnotes = extract_footnotes(raw)
    cleaned_raw = convert_example_sections(cleaned_raw, slug)

    html = markdown.markdown(cleaned_raw, extensions=["tables", "fenced_code", "sane_lists"])
    html = highlight_autoplay_warning(html)

    mtime = os.path.getmtime(path)
    last_updated = datetime.datetime.fromtimestamp(mtime).strftime("%b %-d, %Y")

    blocks.append({
        "slug": slug,
        "title": title,
        "summary": summary,
        "sections": sections,
        "wordCount": len(raw.split()),
        "lastUpdated": last_updated,
        "lastUpdatedTs": mtime,
        "techSpecUrl": TECH_SPEC_LINKS.get(slug),
        "html": html,
        "footnotes": footnotes,
        "raw": raw,
    })

with open(os.path.join(SCRIPT_DIR, "blocks_data.json"), "w", encoding="utf-8") as f:
    json.dump(blocks, f)

print(f"Converted {len(blocks)} blocks")
for b in blocks[:3]:
    print(b["slug"], "-", b["title"], "-", b["summary"][:80])
