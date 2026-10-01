# Firefly Globe

> **Quick summary:** A large, rotating 3D showcase of AI-generated images pulled live from a Firefly community gallery — images arrange into a sphere (or a flat scrollable "wall" on narrow/touch viewports) that visitors can drag/rotate, with a detail modal on click and an optional pull-quote pin. Authored as exactly 4 rows: a gallery-config row, a hint-text row, a screen-reader-labels row, and an optional pull-quote row — everything is read positionally, not by keyword. No author-facing modifier classes; every layout/animation adaptation (reduced motion, mobile "wall" layout, WebGL fallback) is automatic.

## Authoring instructions

Rows are read purely by position — row 1 is always the gallery config, row 2 is always hint text, and so on. Leave a row blank rather than removing it if you want its content to just use defaults.

| Row | Content |
| --- | --- |
| 1 — Gallery source (1 cell) | A single line of text with up to four `\|\|`-separated parts: `<category ID> \|\| <machine tag> \|\| <campaign/promo ID> \|\| <CTA button label>`. Only the category ID is required — it's what tells the block which live image gallery to pull from; if it's blank, the block renders nothing at all. The other three parts are each optional and independently fall back to blank/default if omitted: the machine tag narrows which images are eligible, the campaign ID is appended to every "open in Firefly" link, and the CTA label sets the modal's button text. |
| 2 — Hint text (2 cells) | **Cell 1:** instructional copy shown along the bottom of the gallery (e.g. "Click and drag to rotate. Tap to dive deep into the artwork."). Supports multiple paragraphs. Falls back to a default English sentence if left blank. **Cell 2:** a short label shown as an on-canvas cursor badge (e.g. "Click & Drag"). Falls back to "Click & Drag" if left blank. |
| 3 — Accessibility labels (1 cell) | A single line of text with up to nine `\|\|`-separated parts, in this order: instructions read before entering keyboard mode, "rotate left" label, "rotate right" label, "pause spinning" label, "resume spinning" label, "previous card" label, a modal position-counter template, "next card" label, "close" label. Every part is independently optional — leave any of them blank to use its English default, without needing to fill in the rest. The counter-template part (7th) must literally contain both `{index}` and `{count}` placeholders (e.g. `{index} of {count}`) or it's discarded and the default template is used instead. |
| 4 — Pull quote (optional) | A blockquote (or, if none, a heading, or if neither, the first paragraph) becomes the quote text. Any paragraphs left over after the quote becomes the attribution: the first leftover paragraph is the name, the second is the role/title. Omit this row entirely to skip the pull-quote pin — leaving it blank isn't the same as omitting it; only omitting the row removes the quote pin. |

## Variations

No variations — this block has no modifier classes for authors to add. Its layout (full rotating sphere vs. flat scrollable wall) switches automatically based on viewport size and pointer type, not by anything you author.

## Example

```
| Firefly Globe |
| --- |
| my-category-id || acom_ff_globe_assets || my-promo-id || Open in Firefly |
| Click and drag to rotate. Tap to dive deep into the artwork. | Click & Drag |
| Press Enter to enter the gallery, then Tab through the images. || Rotate left || Rotate right || Pause spinning || Resume spinning || Previous card || {index} of {count} || Next card || Close |
| > A whole world of what's possible. |
```

(The pull-quote row above shows just the blockquote; to add attribution, follow it in the same cell with two plain paragraphs — name, then role/title.)

## Notes

- Images aren't authored directly — the entire visual set comes from a live lookup against an external Firefly gallery service, using the category ID from row 1. There's no way to author specific images, order, or captions per card. If the category ID is wrong or returns no results, the block silently renders nothing — no error message, no placeholder.
- Alt text for every image comes from the service automatically (based on the image's generation prompt) — authors can't supply custom alt text per image.
- Rows are read by position, not by keyword — reordering rows, or leaving a gap in the middle instead of at the end, misassigns content (e.g., an empty row 2 is read as blank hint text, not skipped).
- All nine accessibility label segments in row 3 are independent — you can override just one and leave the rest blank; each missing segment falls back to its own English default rather than the whole row falling back together.
- The row-3 position-counter template silently reverts to the English default if it doesn't contain both literal placeholder tokens `{index}` and `{count}` — a typo like `{Index} of {count}` is discarded without any authoring error.
- Full keyboard and screen-reader support is available via a hidden "enter gallery" control that expands into a linear, tab-through list of image buttons, bypassing the 3D scene entirely — each button is labeled with its alt text (or a generic "Image N" if none is available) and opens the same detail view as clicking the image directly.
- The 3D rotation/animation automatically simplifies to a static, non-spinning layout for visitors with reduced motion enabled, or on very short/high-density mobile screens — this isn't authorable.
- If WebGL isn't available in the visitor's browser, the block silently renders nothing rather than a fallback image — worth flagging to QA as a "nothing renders" scenario that isn't a content issue.

## GTK

No known gotchas beyond the Notes above yet — flag anything you find while authoring against this block so it can be added here.
