# PDF Space

> **Quick summary:** A large scroll-driven hero — eight preview cards fan out along an arc, peel onto a grid, then glide into an Acrobat app mockup while the headline/CTA slide in. Use it as a showcase hero for a PDF/Acrobat-style product page needing a long, cinematic scroll sequence rather than a static hero. Authored as exactly 6 fixed rows in strict order (two 4-cell card rows, marketing text, title, 3-cell mockup images, CTA); row order and column counts are rigid, and misauthoring silently misassigns content rather than erroring. No author-facing variations; falls back to a static layout automatically for reduced-motion visitors.

## Authoring instructions

The block's parsing code (`parseAuthoredContent`) reads **exactly 6 rows**, in this fixed order. Row order matters — this is not a flexible layout.

| Row | Columns | Content |
| --- | --- | --- |
| 1 — Card grid, row 0 | 4 cells | One cell per card (top row of the authored 2×4 grid). Each cell: an image (`<picture>`/`<img>`) plus a short label/caption as text. **Set the image's `width` and `height` attributes** — the code reads them to compute each card's aspect ratio; if omitted it silently assumes 192×230. |
| 2 — Card grid, row 1 | 4 cells | Same format as row 1. These 4 cards are **hidden on mobile** (only the first row's 4 cards show, reflowed into a 2×2 mobile grid). |
| 3 — Marketing text block | 1 cell | A heading + supporting paragraph (and optionally a link) shown as the copy that pans in once the cards settle onto the grid. |
| 4 — Title | 1 cell | The main headline (`<h2>`–`<h6>`) with optional subcopy paragraph, shown near the Acrobat mockup at the end of the sequence. |
| 5 — Mockup images | 3 cells | Cell 1: mobile mockup image. Cell 2: desktop mockup (app window) image. Cell 3: desktop side-panel image shown docked to the mockup. All as `<picture>`. |
| 6 — CTA | 1 cell | A single call-to-action link, shown next to the mockup at the end of the sequence. |

## Variations

This block has no author-facing variation classes to add to the block-name cell. The only alternate state — a static, non-scroll-animated layout showing the settled grid + slotted mockup end-state — is applied automatically for visitors with `prefers-reduced-motion` enabled; there is nothing an author authors to trigger it.

## Example

```
| PDF Space |
| --- | --- | --- | --- |
| ![](/media/card-edit.png){width="192" height="230"} Edit text | ![](/media/card-sign.png){width="192" height="230"} Sign documents | ![](/media/card-share.png){width="192" height="230"} Share securely | ![](/media/card-export.png){width="192" height="230"} Export to Word |

| PDF Space |
| --- | --- | --- | --- |
| ![](/media/card-scan.png){width="192" height="230"} Scan to PDF | ![](/media/card-compress.png){width="192" height="230"} Compress files | ![](/media/card-merge.png){width="192" height="230"} Merge files | ![](/media/card-protect.png){width="192" height="230"} Protect with a password |

| PDF Space |
| --- |
| ## Every tool you need for PDF <br> From editing to e-signatures, do it all in one app. |

| PDF Space |
| --- |
| ## Meet Acrobat <br> The all-in-one PDF and e-sign solution. |

| PDF Space |
| --- | --- | --- |
| ![](/media/mockup-mobile.png) | ![](/media/mockup-desktop.png) | ![](/media/mockup-panel.png) |

| PDF Space |
| --- |
| [Try Acrobat for free](https://www.adobe.com/acrobat/free-trial.html) |
```

## Notes

- Row order and column count are strict: the code destructures the 6 rows positionally (`[imageRow1, imageRow2, textRow, titleRow, mockupRow, ctaRow]`) with no validation, so an extra/missing row or a mockup row with fewer than 3 cells will silently misassign content rather than error.
- Always set `width` and `height` on the 8 card images — they're the only source of each card's aspect ratio; getting them wrong distorts the card during the animation.
- This block is very tall (650vh) and pins to the viewport while scrolling — it's meant to be used once per page as a hero, not repeated.
- All decorative animation elements (mockup chrome, dot-grid canvas, Adobe logo flourish, the animated card clones) are marked `aria-hidden` in the code, so screen reader/keyboard users only ever encounter the real authored content (cards' text, marketing copy, title, CTA) — authors don't need to do anything extra for this.
- The full engineering-level tuning reference (phase timings, arc geometry, z-index layering, etc.) lives in `libs/mep/ace1205/pdf-space/README.md` — that's for developers adjusting the animation feel, not for content authors.
