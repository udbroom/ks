import json, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_ROOT = os.path.dirname(SCRIPT_DIR)  # kitchen-sink-docs/

with open(os.path.join(SCRIPT_DIR, "blocks_data.json"), "r", encoding="utf-8") as f:
    blocks_json = f.read()

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  :root { color-scheme: light; }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background: #fff;
    color: #1d1d1f;
    display: flex;
    height: 100vh;
    overflow: hidden;
  }
  #sidebar {
    width: 300px;
    min-width: 300px;
    border-right: 1px solid #e5e5e7;
    display: flex;
    flex-direction: column;
    background: #fafafa;
  }
  #sidebar-header {
    padding: 16px 16px 12px;
    border-bottom: 1px solid #e5e5e7;
  }
  #sidebar-header h1 {
    font-size: 15px;
    font-weight: 600;
    margin: 0 0 2px;
  }
  #sidebar-header .count {
    font-size: 12px;
    color: #6e6e73;
  }
  #search {
    margin: 10px 16px;
    padding: 7px 10px;
    border: 1px solid #d2d2d7;
    border-radius: 7px;
    font-size: 13px;
    outline: none;
  }
  #search:focus { border-color: #FA0F00; }
  #block-list {
    flex: 1;
    overflow-y: auto;
    padding: 0 8px 12px;
  }
  .block-item {
    padding: 9px 10px;
    border-radius: 7px;
    cursor: pointer;
    margin-bottom: 2px;
  }
  .block-item:hover { background: #eee; }
  .block-item.active { background: #FA0F00; }
  .block-item.active .block-title { color: #fff; }
  .block-item.active .block-meta { color: #ffd6d3; }
  .block-title {
    font-size: 13.5px;
    font-weight: 600;
    color: #1d1d1f;
  }
  .block-meta {
    font-size: 11px;
    color: #6e6e73;
    margin-top: 1px;
  }
  #main {
    flex: 1;
    overflow-y: auto;
    padding: 36px 48px 80px;
  }
  #main-inner { max-width: 780px; margin: 0 auto; }
  .doc-summary {
    background: #fff5f4;
    border: 1px solid #ffd6d3;
    border-radius: 10px;
    padding: 14px 16px;
    font-size: 13.5px;
    line-height: 1.55;
    margin: 12px 0 28px;
    color: #4a2a28;
  }
  .doc-summary strong { color: #d1150f; }
  .doc-summary-footer {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 10px;
    padding-top: 10px;
    border-top: 1px solid #ffd6d3;
    font-size: 12px;
  }
  .doc-summary-footer .updated-date { color: #8a5f5c; }
  .doc-summary-footer .footer-sep { color: #e3a9a5; }
  .doc-summary-footer .tech-spec-link {
    color: #d1150f;
    font-weight: 600;
    text-decoration: none;
  }
  .doc-summary-footer .tech-spec-link:hover { text-decoration: underline; }
  .doc-summary-footer .tech-spec-link.tbd {
    color: #a3766f;
    font-weight: 500;
    cursor: default;
  }
  .doc-summary-footer .tech-spec-link.tbd:hover { text-decoration: none; }
  .doc-content h1 { font-size: 26px; margin-bottom: 4px; }
  .doc-content h2 {
    font-size: 17px;
    margin-top: 32px;
    padding-top: 12px;
    border-top: 1px solid #eee;
  }
  .doc-content h2:first-of-type { border-top: none; padding-top: 0; }
  .doc-content p, .doc-content li { font-size: 14px; line-height: 1.65; color: #2c2c2e; }
  .doc-content table {
    border-collapse: collapse;
    width: 100%;
    margin: 14px 0;
    font-size: 13px;
  }
  .doc-content th, .doc-content td {
    border: 1px solid #e5e5e7;
    padding: 8px 10px;
    text-align: left;
    vertical-align: top;
  }
  .doc-content th { background: #f5f5f7; font-weight: 600; }
  .doc-content code {
    background: #f5f5f7;
    padding: 1px 5px;
    border-radius: 4px;
    font-size: 12.5px;
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  }
  .doc-content pre {
    background: #1d1d1f;
    color: #f5f5f7;
    padding: 14px 16px;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 12.5px;
  }
  .doc-content pre code { background: none; padding: 0; color: inherit; }
  .authoring-example-table {
    border-collapse: collapse;
    width: 100%;
    margin: 14px 0;
    font-size: 13px;
    border: 1px solid #d2d2d7;
  }
  .authoring-example-table th.ex-header-row {
    background: #464646;
    color: #fff;
    font-weight: 600;
    text-align: left;
    padding: 8px 12px;
    font-size: 13px;
  }
  .authoring-example-table td {
    border: 1px solid #d2d2d7;
    padding: 10px 12px;
    vertical-align: top;
    background: #fff;
  }
  .authoring-example-table td h1,
  .authoring-example-table td h2,
  .authoring-example-table td h3,
  .authoring-example-table td h4,
  .authoring-example-table td h5,
  .authoring-example-table td h6 {
    font-size: 15px;
    margin: 0 0 6px;
  }
  .authoring-example-table td p { margin: 0 0 6px; }
  .authoring-example-table td p:last-child { margin-bottom: 0; }
  .authoring-example-table td img {
    max-width: 140px;
    max-height: 90px;
    display: block;
    margin-bottom: 6px;
    border-radius: 4px;
    object-fit: cover;
  }
  .authoring-example-table td img[alt="icon"] {
    width: 40px;
    height: 40px;
    max-width: 40px;
    max-height: 40px;
    border-radius: 6px;
    object-fit: contain;
  }
  .authoring-example-table tr.ex-viewport-row td {
    background: #eef3fc;
    color: #0265DC;
    font-weight: 600;
    font-size: 11.5px;
    letter-spacing: 0.02em;
    padding: 5px 12px;
  }
  .authoring-example-table .color-swatch {
    display: inline-block;
    width: 13px;
    height: 13px;
    border-radius: 3px;
    border: 1px solid rgba(0,0,0,0.15);
    vertical-align: -2px;
    margin-right: 6px;
  }
  .authoring-example-table tr.ex-group-start td {
    border-top: 2px dashed #c7c7cc;
  }
  .authoring-example-table .empty-dash {
    color: #b6b6ba;
    font-weight: 600;
  }
  .authoring-example-table .tooltip-label {
    text-decoration: underline dotted;
    text-underline-offset: 2px;
    cursor: help;
  }
  .authoring-example-table .badge-primary {
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    background: #FA0F00;
    color: #fff;
    padding: 1px 7px;
    border-radius: 100px;
    margin-left: 6px;
    vertical-align: 1px;
  }
  .authoring-example-table hr.cell-group-divider {
    border: none;
    border-top: 1px dashed #d2d2d7;
    margin: 8px 0;
  }
  .ex-image-preview {
    margin: 8px 0;
  }
  .ex-image-preview img {
    max-width: 220px;
    max-height: 120px;
    border-radius: 6px;
    display: block;
    object-fit: cover;
  }
  .ex-image-caption {
    display: block;
    font-size: 11px;
    color: #86868b;
    margin-top: 4px;
    font-style: italic;
  }
  .ex-section-divider {
    font-size: 11.5px;
    font-weight: 600;
    color: #6e6e73;
    background: #f5f5f7;
    border-radius: 6px;
    padding: 5px 10px;
    margin: 14px 0 8px;
    letter-spacing: 0.02em;
  }
  .ex-section-body {
    padding-left: 10px;
    border-left: 2px solid #eee;
    margin-bottom: 10px;
  }
  .doc-content blockquote {
    display: none; /* the quick-summary blockquote is rendered separately above */
  }
  .doc-content a { color: #0265DC; }
  .fn-ref {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 15px;
    height: 15px;
    padding: 0 3px;
    margin-left: 2px;
    border-radius: 100px;
    background: #eef3fc;
    color: #0265DC;
    font-size: 9.5px;
    font-weight: 700;
    line-height: 1;
    cursor: pointer;
    vertical-align: super;
    user-select: none;
  }
  .fn-ref:hover { background: #d9e6fb; }
  .fn-ref.open { background: #0265DC; color: #fff; }
  #fn-popup {
    position: fixed;
    background: #1d1d1f;
    color: #f5f5f7;
    font-size: 12px;
    line-height: 1.5;
    padding: 9px 12px;
    border-radius: 8px;
    max-width: 280px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    z-index: 50;
  }
  #fn-popup a { color: #8ec1ff; }
  #fn-popup::after {
    content: '';
    position: absolute;
    width: 9px;
    height: 9px;
    background: #1d1d1f;
    transform: rotate(45deg);
    left: var(--arrow-left, 14px);
  }
  #fn-popup.fn-below::after { top: -4px; }
  #fn-popup.fn-above::after { bottom: -4px; }
  .nav-bar {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 6px;
    flex-wrap: wrap;
  }
  #back-btn {
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 12.5px;
    font-weight: 600;
    color: #4a4a4f;
    background: #f0f0f2;
    border: 1px solid #e0e0e3;
    border-radius: 7px;
    padding: 4px 10px 4px 8px;
    cursor: pointer;
  }
  #back-btn:hover { background: #e7e7ea; }
  #back-btn[disabled] { opacity: 0.35; cursor: default; pointer-events: none; }
  #breadcrumb {
    font-size: 12.5px;
    color: #86868b;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 6px;
    position: relative;
  }
  #breadcrumb .crumb-current { color: #1d1d1f; font-weight: 600; }
  #breadcrumb .crumb-sep { color: #c7c7cc; }
  #history-toggle {
    display: flex;
    align-items: center;
    gap: 2px;
    font-size: 12.5px;
    color: #6e6e73;
    background: none;
    border: none;
    cursor: pointer;
    padding: 2px 4px;
    border-radius: 5px;
  }
  #history-toggle:hover { background: #eee; color: #1d1d1f; }
  #history-dropdown {
    position: absolute;
    top: 22px;
    left: 0;
    background: #fff;
    border: 1px solid #e5e5e7;
    border-radius: 9px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    min-width: 200px;
    max-width: 320px;
    padding: 6px;
    z-index: 10;
  }
  #history-dropdown .crumb-item {
    padding: 7px 10px;
    border-radius: 6px;
    font-size: 13px;
    color: #1d1d1f;
    cursor: pointer;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  #history-dropdown .crumb-item:hover { background: #f5f5f7; }
  .badges { display: flex; gap: 6px; margin: 10px 0 0; flex-wrap: wrap; }
  .badge {
    font-size: 10.5px;
    padding: 2px 8px;
    border-radius: 100px;
    background: #eef6ec;
    color: #2a6b1f;
    border: 1px solid #d3e9cd;
  }
  .badge.missing { background: #fdecea; color: #b3261e; border-color: #f6cfcb; }
  #empty-state {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: #86868b;
    font-size: 13px;
  }
</style>
</head>
<body>

<div id="sidebar">
  <div id="sidebar-header">
    <h1>Kitchen Sink Blocks</h1>
    <div class="count" id="block-count"></div>
  </div>
  <input id="search" type="text" placeholder="Search blocks...">
  <div id="block-list"></div>
</div>

<div id="main">
  <div id="main-inner"></div>
</div>

<script>
const BLOCKS = __BLOCKS_JSON__;

const listEl = document.getElementById('block-list');
const mainEl = document.getElementById('main-inner');
const searchEl = document.getElementById('search');
const countEl = document.getElementById('block-count');

let activeSlug = null;
let historyStack = []; // stack of slugs, last = current

function renderList(filter) {
  const q = (filter || '').toLowerCase().trim();
  const filtered = BLOCKS.filter(b =>
    !q || b.title.toLowerCase().includes(q) || b.summary.toLowerCase().includes(q) || b.slug.includes(q)
  );
  countEl.textContent = filtered.length + ' of ' + BLOCKS.length + ' blocks';
  listEl.innerHTML = filtered.map(b => `
    <div class="block-item${b.slug === activeSlug ? ' active' : ''}" data-slug="${b.slug}">
      <div class="block-title">${b.title}</div>
    </div>
  `).join('');
  listEl.querySelectorAll('.block-item').forEach(el => {
    el.addEventListener('click', () => selectBlock(el.dataset.slug));
  });
}

function selectBlock(slug, opts) {
  opts = opts || {};
  const b = BLOCKS.find(x => x.slug === slug);
  if (!b) return;
  activeSlug = slug;

  if (opts.push !== false) {
    // Normal forward navigation (sidebar click or cross-ref link): push,
    // but don't create a duplicate entry if we're already on this block.
    if (historyStack[historyStack.length - 1] !== slug) {
      historyStack.push(slug);
    }
  }

  const sectionNames = { authoring: 'Authoring instructions', variations: 'Variations', example: 'Example', notes: 'Notes' };
  const badges = Object.entries(b.sections).map(([k, present]) =>
    `<span class="badge${present ? '' : ' missing'}">${present ? '✓' : '✕'} ${sectionNames[k]}</span>`
  ).join('');

  mainEl.innerHTML = `
    <div class="nav-bar">
      <button id="back-btn" title="Go back">&larr; Back</button>
      <div id="breadcrumb"></div>
    </div>
    <div class="doc-summary">
      <div><strong>Quick summary:</strong> ${b.summary || '<em>No summary found.</em>'}</div>
      <div class="doc-summary-footer">
        <span class="updated-date">Updated ${b.lastUpdated}</span>
        <span class="footer-sep">&middot;</span>
        ${b.techSpecUrl
          ? `<a class="tech-spec-link" href="${b.techSpecUrl}" target="_blank" rel="noopener">Tech spec &#8599;</a>`
          : `<span class="tech-spec-link tbd">Tech spec: TBD</span>`}
      </div>
    </div>
    <div class="badges">${badges}</div>
    <div class="doc-content">${b.html}</div>
  `;
  mainEl.scrollTop = 0;
  document.getElementById('main').scrollTop = 0;
  renderList(searchEl.value);
  wireCrossRefLinks();
  wireFootnotes(b);
  renderNavBar();
}

// Footnote-style refs, e.g. `dark`[^dark], are a repo convention noting the
// PR/commit that added a variation. Rather than dumping them at the bottom
// of the page, convert.py already turned each [^id] into a small clickable
// <sup class="fn-ref" data-fn="id"> marker. Here we wire clicks to a popup
// anchored to that marker, flipping above/below depending on available space.
function wireFootnotes(b) {
  mainEl.querySelectorAll('.fn-ref').forEach(el => {
    el.addEventListener('click', (e) => {
      e.stopPropagation();
      const fn = b.footnotes && b.footnotes[el.dataset.fn];
      if (!fn) return;
      if (el.classList.contains('open')) {
        closeFootnotePopup();
        return;
      }
      showFootnotePopup(el, fn.html);
    });
  });
}

function closeFootnotePopup() {
  const existing = document.getElementById('fn-popup');
  if (existing) existing.remove();
  document.querySelectorAll('.fn-ref.open').forEach(el => el.classList.remove('open'));
}

function showFootnotePopup(anchorEl, html) {
  closeFootnotePopup();
  anchorEl.classList.add('open');

  const popup = document.createElement('div');
  popup.id = 'fn-popup';
  popup.innerHTML = html;
  document.body.appendChild(popup);

  const rect = anchorEl.getBoundingClientRect();
  const popupRect = popup.getBoundingClientRect();
  const gap = 10;
  const spaceBelow = window.innerHeight - rect.bottom;
  const spaceAbove = rect.top;
  const showAbove = spaceBelow < popupRect.height + gap && spaceAbove > spaceBelow;

  const top = showAbove ? rect.top - popupRect.height - gap : rect.bottom + gap;
  let left = rect.left - 10;
  const maxLeft = window.innerWidth - popupRect.width - 12;
  left = Math.max(12, Math.min(left, maxLeft));

  popup.style.top = top + 'px';
  popup.style.left = left + 'px';
  popup.classList.add(showAbove ? 'fn-above' : 'fn-below');
  // Point the little arrow at the marker regardless of popup horizontal shift.
  const arrowOffset = Math.max(10, Math.min(rect.left + rect.width / 2 - left - 4, popupRect.width - 18));
  popup.style.setProperty('--arrow-left', arrowOffset + 'px');

  setTimeout(() => {
    document.addEventListener('click', function closeOnce(e) {
      if (!popup.contains(e.target)) {
        closeFootnotePopup();
        document.removeEventListener('click', closeOnce);
      }
    });
  }, 0);
}

function renderNavBar() {
  const backBtn = document.getElementById('back-btn');
  const crumbEl = document.getElementById('breadcrumb');
  if (!backBtn || !crumbEl) return;

  backBtn.disabled = historyStack.length <= 1;
  backBtn.onclick = goBack;

  const hasHistory = historyStack.length > 1;
  const currentSlug = historyStack[historyStack.length - 1];
  const currentBlock = BLOCKS.find(x => x.slug === currentSlug);
  const currentTitle = currentBlock ? currentBlock.title : currentSlug;

  // One visible level (the current block); everything earlier collapses
  // into a "History" dropdown, most recent first.
  crumbEl.innerHTML = `
    ${hasHistory ? `
      <button id="history-toggle">History (${historyStack.length - 1}) &#9662;</button>
      <span class="crumb-sep">/</span>
    ` : ''}
    <span class="crumb-current">${currentTitle}</span>
  `;

  if (hasHistory) {
    const toggle = document.getElementById('history-toggle');
    toggle.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleHistoryDropdown(crumbEl);
    });
  }
}

function toggleHistoryDropdown(crumbEl) {
  const existing = document.getElementById('history-dropdown');
  if (existing) {
    existing.remove();
    return;
  }

  const dropdown = document.createElement('div');
  dropdown.id = 'history-dropdown';

  // Most recent first, excluding the current (already shown) entry.
  const past = historyStack.slice(0, -1).slice().reverse();
  dropdown.innerHTML = past.map((slug) => {
    const b = BLOCKS.find(x => x.slug === slug);
    const title = b ? b.title : slug;
    const idx = historyStack.lastIndexOf(slug);
    return `<div class="crumb-item" data-index="${idx}">${title}</div>`;
  }).join('');

  dropdown.querySelectorAll('.crumb-item').forEach(el => {
    el.addEventListener('click', () => {
      const idx = parseInt(el.dataset.index, 10);
      const targetSlug = historyStack[idx];
      historyStack = historyStack.slice(0, idx + 1);
      selectBlock(targetSlug, { push: false });
    });
  });

  crumbEl.appendChild(dropdown);

  // Close on outside click.
  setTimeout(() => {
    document.addEventListener('click', function closeOnce(e) {
      if (!dropdown.contains(e.target)) {
        dropdown.remove();
        document.removeEventListener('click', closeOnce);
      }
    });
  }, 0);
}

function goBack() {
  if (historyStack.length <= 1) return;
  historyStack.pop(); // drop current
  const prev = historyStack[historyStack.length - 1];
  selectBlock(prev, { push: false });
}

// Markdown cross-reference links like [Section Metadata](./section-metadata.md)
// or (section-metadata.md) point to other blocks' .md files. There's no real
// file at that path inside the artifact, so intercept them and route to the
// matching block in the sidebar instead of letting the <a> navigate nowhere.
function wireCrossRefLinks() {
  mainEl.querySelectorAll('.doc-content a[href]').forEach(a => {
    const href = a.getAttribute('href');
    if (/^https?:\/\//i.test(href)) {
      a.target = '_blank';
      a.rel = 'noopener';
      return;
    }
    const slug = href.replace(/^\.?\//, '').replace(/\.md$/i, '');
    const match = BLOCKS.find(b => b.slug === slug);
    if (match) {
      a.href = 'javascript:void(0)';
      a.title = 'Jump to ' + match.title;
      a.addEventListener('click', (e) => {
        e.preventDefault();
        selectBlock(match.slug);
      });
    }
  });
}

searchEl.addEventListener('input', () => renderList(searchEl.value));

renderList('');
if (BLOCKS.length) selectBlock(BLOCKS[0].slug);
</script>

</body>
</html>
"""

html = html.replace("__BLOCKS_JSON__", blocks_json)

out_path = os.path.join(DOCS_ROOT, "kitchen-sink-index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("wrote", len(html), "bytes to", out_path)
