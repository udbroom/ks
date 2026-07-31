# Quick Actions

> **Quick summary:** A section header (heading + optional CTA) followed by a responsive grid of image tiles that link out to tools or pages, showing 2 tiles per row on mobile, 3 on tablet, and 6 on desktop. Authored as an optional 1-cell header row, then one row per tile (link cell + image cell). There are no author-facing variation classes — the grid's column count is set automatically by JS. Note: the `two-up`/`three-up`/`six-up` classes this block applies internally are unrelated to Section Metadata's `product-grid` multi-block layout system.

---

A section header (heading + optional CTA) followed by a responsive grid of image tiles that link out to individual tools or pages — e.g. a "Quick actions" panel of shortcuts like "Compress a PDF," "Convert to Word," etc. The grid automatically shows 2 tiles per row on mobile, 3 on tablet, and 6 on desktop.

## Authoring instructions

| Row | Content |
| --- | --- |
| 1 — Section header (optional, 1 cell) | A heading (`H1`–`H6`) plus, optionally, a CTA button authored with Milo's bold/italic link syntax. **Only included if this row's first cell contains a heading** — otherwise the block assumes there is no header row and treats every row as a tile. |
| 2+ — Tiles (2 cells each) | **Cell 1:** a link — its text becomes the tile's visible label, and its URL becomes the tile's link target. **Cell 2:** an image (`<picture>`/`<img>`) used as the tile's background. Rows with fewer than 2 cells are skipped and not rendered as tiles. |

## Variations

This block has no author-facing variation classes. The grid's column count (`two-up` / `three-up` / `six-up`) is applied automatically by JS based on viewport width — it is not something an author sets.

## Example

```
| Quick Actions |
| --- |
| ## Quick actions <br> **[See all tools](https://www.adobe.com/acrobat/online/tools.html)** |

| Quick Actions |
| --- | --- |
| [Compress a PDF](https://www.adobe.com/acrobat/online/compress-pdf.html) | ![](/media/qa-compress.png) |
| [Convert to Word](https://www.adobe.com/acrobat/online/pdf-to-word.html) | ![](/media/qa-convert.png) |
| [Sign a document](https://www.adobe.com/acrobat/online/sign-pdf.html) | ![](/media/qa-sign.png) |
| [Merge files](https://www.adobe.com/acrobat/online/merge-pdf.html) | ![](/media/qa-merge.png) |
| [Fill and sign a form](https://www.adobe.com/acrobat/online/fill-sign-pdf-forms.html) | ![](/media/qa-fill.png) |
| [Edit a PDF](https://www.adobe.com/acrobat/online/edit-pdf.html) | ![](/media/qa-edit.png) |
```

## Notes

- The header row's CTA link must use bold/italic button syntax to render as a button — this row is decorated with the same button styling as other blocks (`decorateBlockText`).
- Tile labels are clamped to 2 lines of text in the layout — keep tile link text short (a few words) so it doesn't get visually truncated.
- If you omit the header row entirely, just start the table directly with tile rows (link + image, 2 cells) — the block correctly detects there's no heading and skips building a header.
- The `two-up`/`three-up`/`six-up` classes mentioned in Variations are applied automatically by this block's own code to its own internal tile grid — they're unrelated to [Section Metadata](./section-metadata.md)'s `product-grid` + `-up` multi-block layout system (which arranges separate blocks side by side in a section). Adding `product-grid` classes to this block's Section Metadata has no effect on its tile grid.
