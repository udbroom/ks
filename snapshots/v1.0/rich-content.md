# Rich Content

> **Quick summary:** A flexible text-and-media block for heroes and general content sections — heading, body, and CTA buttons, optionally with a section background, a jump-link nav strip, or paired media. Authored as one row/cell of free-form rich text (heading, body, bold/italic button links), with viewport-delimiter rows (`mobile-viewport`/`tablet-viewport`/`desktop-viewport`) for per-viewport content. Key variations: `hero`, `center`, `dark`, `max-width-8`/`max-width-10`, `left-split`, `jump-link`, `narrow`/`narrow-xs`, `grid-full-width`, `media`, `no-overlay`, `indent`, `glass-border`, `merch-moment` — not all are available in every deployment (see the Availability column). Note the Section Metadata interaction: pairing `media` with a scroll-driven "garage door" reveal style on the section has no effect without `media` also present.

---

A flexible text-and-media block for hero banners and general content sections: a heading, body copy, and call-to-action buttons, optionally layered over a section background image/video, paired with a jump-link navigation strip, or paired with its own media (image/video). Use it whenever you need a headline + supporting copy + CTA(s) without a fixed two-column layout.

Not every variation described below is available everywhere this block is used — see the "Availability" column in Variations. Always check how the block actually renders on your page before relying on a less-common variation.

## Authoring instructions

The block is authored as **one row with one cell** (the "foreground" content) in the simple case. Everything inside that cell is free-form rich text, decorated automatically:

| Row | Content |
| --- | --- |
| Row 1 (required) | A single cell containing, in order: an optional heading (any level `H1`–`H6`) — if you omit a heading, the first paragraph is auto-promoted to *look* like a Heading 2 (visually only — screen readers and SEO still see a plain paragraph, so use a real heading whenever the text is structurally a heading). If the text starts with a typographic opening quote (curly quote, e.g. `"`), the mark is pulled into its own styled span for a "hanging quote" effect — no special authoring needed. If the paragraph immediately before the heading is a small image (icon) followed by short text, it becomes an "eyebrow" line with an inline icon. Below the heading, add body paragraphs. Add one or more buttons/links using standard Milo button syntax: bold text (`**text**`) = filled/primary button, italic text (`*text*`) = outline/secondary button, a plain link on its own line = link-styled (no button chrome). Bold and italic links are often paired together in one emphasized line, e.g. `_**[Get started](#)** [Learn more](#)_`. |
| Row 2, second cell (optional, only with `hero`, and only in some deployments) | A second cell in the same row. If present and text-only, its content is treated as a CSS gradient/color value and applied as a custom hero-overlay override on the surrounding section, letting you replace the default dark hero gradient for that instance. Not every deployment of this block reads this cell — if you add it and see no effect, this deployment doesn't support the override and the default hero overlay is used instead. |

**Jump-link contract (most deployments, not all):** if the block name includes `jump-link` (see Variations), add one additional paragraph anywhere in the cell containing only links separated by the pipe character `|`, e.g. `[Overview](#overview) | [Pricing](#pricing) | [FAQ](#faq)` — the code detects this row by looking for a `|` character among the links. That paragraph becomes a horizontal (or vertical, on mobile) jump-link nav with numbered/arrow badges that smooth-scroll to the matching `id` on the page. The simplest deployments of this block don't support `jump-link` at all.

**Media contract (most deployments, not all):** if the block name includes `media` (see Variations), the table structure changes to hold both a CTA cell and a media cell (a picture, video, or a link to an `.mp4` file) — both optional, but at least one is expected for the variant to render meaningfully. How strictly cell order matters, and the resulting media's aspect ratio/shape, both vary by deployment — some require a fixed "CTA cell first, media cell second" order and render a narrow portrait clip; others scan every cell to find whichever one looks like media regardless of order, and render a wider, closer-to-square shape. When in doubt, author CTA first and media second — that order works everywhere media is supported. The simplest deployments of this block don't support `media` at all.

## Variations

Add these as modifier text in the block name cell, comma-separated, e.g. `Rich Content (hero, center)`:

| Variation | Effect | Availability |
| --- | --- | --- |
| `hero`[^hero] | Fixes the block/section to a tall hero height (640px mobile/tablet, 1040px desktop). | All deployments |
| `center`[^center] | Center-aligns the heading/body/buttons instead of left-aligned. | All deployments |
| `dark`[^dark] | Removes the block's own background color (used when content sits over a section background image/video). | All deployments |
| `max-width-8`[^max-width-8] / `max-width-10`[^max-width-10] | With `hero` on desktop, constrains the content column to an 8- or 10-column grid width. | All deployments |
| `left-split`[^left-split] | On desktop, lays content out with buttons pinned to the right side of the text instead of stacked below it. | Most deployments |
| `jump-link`[^jump-link] | Enables the jump-link paragraph described above; implies knockout/white text. Commonly combined with `hero`. | Most deployments |
| `narrow`[^narrow] / `narrow-xs`[^narrow-xs] | Caps the max-width of the heading/body text for a tighter reading column, tablet+ only (`narrow-xs` is tighter). | Most deployments |
| `grid-full-width`[^grid-full-width] | Used inside a `bento` Section (see [Section Metadata](./section-metadata.md)) so the block spans the full masonry grid width with adjusted spacing. | Most deployments |
| `media`[^media] | Switches to the CTA + media layout described above; renders on a dark background. (Older authoring/docs may reference this as `video` — that name has been retired everywhere this block is used; use `media`.) | Most deployments |
| `no-overlay`[^no-overlay] | Used with `media`: skips the blurred/darkened section background treatment behind the media. | Most deployments |
| `indent`[^indent] | Used inside a `bento` Section: indents the block with adjusted spacing (an alternative to `grid-full-width`). | Only some deployments |
| `glass-border`[^glass-border] | Used with `media`: adds a translucent "glass" frame/border around the media instead of plain rounded corners. | Only some deployments |
| `merch-moment`[^merch-moment] | A commerce/merchandising layout: the section becomes a two-row grid (content row + inline, non-cover background-image row) at a fixed aspect ratio, with any price text (`inline-price`) bolded. Typically paired with a scroll-reveal [Section Metadata](./section-metadata.md) style. | Only some deployments |
| Per-viewport variant | Swaps a class in/out only while a given viewport's content is active (see Notes). | All deployments |

[^hero]: [#6266](https://github.com/adobecom/milo/pull/6266) — Dušan Kosanović, 2026-07-15
[^center]: [`e6f7950`](https://github.com/adobecom/milo/commit/e6f7950) — Dusan Kosanovic, 2026-07-17
[^dark]: [`e6f7950`](https://github.com/adobecom/milo/commit/e6f7950) — Dusan Kosanovic, 2026-07-17
[^max-width-8]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^max-width-10]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^left-split]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^jump-link]: [#6266](https://github.com/adobecom/milo/pull/6266) — Dušan Kosanović, 2026-07-15
[^narrow]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^narrow-xs]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^grid-full-width]: [`418ad2f`](https://github.com/adobecom/milo/commit/418ad2f) — Ryan Clayton, 2026-07-09
[^media]: [`29632b7`](https://github.com/adobecom/milo/commit/29632b7) — Dusan Kosanovic, 2026-07-20
[^no-overlay]: [`29632b7`](https://github.com/adobecom/milo/commit/29632b7) — Dusan Kosanovic, 2026-07-20
[^indent]: [`418ad2f`](https://github.com/adobecom/milo/commit/418ad2f) — Ryan Clayton, 2026-07-09
[^glass-border]: [`a0ce466`](https://github.com/adobecom/milo/commit/a0ce466) — Dusan Kosanovic, 2026-07-20
[^merch-moment]: [`e6f7950`](https://github.com/adobecom/milo/commit/e6f7950) — Dusan Kosanovic, 2026-07-17

## Example

Standard hero:

```
| Rich Content (hero, center) |
| --- |
| ## Design without limits<br>Create stunning content faster with AI-powered tools built for every skill level.<br><br>**Start for free**{: .con-button} *See plans*{: .con-button} |
```

Jump-link hero:

```
| Rich Content (hero, jump-link) |
| --- |
| ![icon](https://main--milo--adobecom.aem.live/libs/mep/ace1205/rich-content/assets/arrow.svg) Product update<br># What's new in Creative Cloud<br>[Overview](#overview) \| [Apps](#apps) \| [Pricing](#pricing) |
```

Media variant:

```
| Rich Content (media, glass-border) |
| --- |
| **Watch the film** | [video.mp4](https://example.com/video.mp4) |
```

Per-viewport example (breakpoint is width, not device):

```
| Rich Content (center) |
| --- |
| mobile-viewport |
| ## Shop on the go |
| desktop-viewport (dark) |
| ## Shop the full collection <br> Browse our entire lineup on the big screen. |
```

## Notes

- To give mobile/tablet/desktop different text, insert single-cell delimiter rows containing `mobile-viewport`, `tablet-viewport`, or `desktop-viewport` before each viewport's content row(s) (bare `mobile`/`tablet`/`desktop` still works but is a legacy fallback being phased out — use the `-viewport` form in new authoring). Rows group between delimiters; using only `mobile-viewport` + `desktop-viewport` gives a simple two-way split at the **1280px** breakpoint (mobile = below 1280px, desktop = 1280px and up); adding `tablet-viewport` gives a three-way split at **768px** and **1280px** (mobile = below 768px, tablet = 768–1279px, desktop = 1280px and up). Any cell left empty in a higher viewport's row inherits content from the nearest lower viewport that has content — you only need to re-author what actually changes. A variant can be added per viewport in parentheses after the delimiter keyword, e.g. `desktop-viewport (dark)`.
- The whole block only has one authored "row" of real content per viewport (plus the optional hero-overlay second cell where supported) — don't spread content across multiple top-level rows outside the viewport-delimiter pattern; extra rows there are simply not read.
- The jump-link arrow icon is a static asset baked into the CSS via `mask-image`; authors cannot swap it per instance.
- `hero` height is CSS-driven and shared with the parent `.section` — combine with a section background image/video (via [Section Metadata](./section-metadata.md)'s `background` key) for the typical full-bleed hero look.
- **[Section Metadata](./section-metadata.md) interaction:** pairing the `media` variant with a scroll-driven "garage door" reveal style on the containing section's Section Metadata `layout`/`style` row (only available in some deployments) animates the section open as the visitor scrolls, with extra spacing tuned for this block's media layout — has no effect without the `media` variant also present. See [section-metadata.md](./section-metadata.md).
- If you don't add a real heading tag, the first paragraph is only visually promoted to heading size — check the visual result if you intended plain body copy only, since it will look like a headline even though it stays a `<p>` for accessibility/SEO.
