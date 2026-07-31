# Offer Hero

> **Quick summary:** A full-viewport scroll-driven hero — headline/CTA above four preview cards that pile up, fan out, and settle into a 2-up grid as the visitor scrolls. Authored as a fixed row sequence: hero content (row 1), an optional pinned "What's included" label (row 2), then up to 4 feature cards (rows 3–6, text + media each). No author-facing variations; reduced-motion fallback and layout are automatic. Note: this block's own `-up` grid classes are unrelated to Section Metadata's `product-grid` layout system.

---

A full-viewport scroll-driven hero: an opening headline and CTA sit above four preview cards that start piled on top of each other, then fan out and settle into a 2-up grid as the visitor scrolls. Use it to open a product/offer landing page where you want a cinematic reveal of a few feature highlights before the visitor reaches the rest of the page.

## Authoring instructions

The block is authored as a sequence of table rows. Row 1 is required; row 2 is optional; the remaining rows are the feature cards (up to 4 for the full experience).

| Row | Content |
| --- | --- |
| 1 — Hero (1 cell) | Optional small product icon (an SVG image, either on its own line or inline with the eyebrow text) → optional eyebrow line (short text directly above the heading, e.g. "Acrobat Pro") → a heading (any level `H1`–`H6`; it is automatically promoted to a real `<h1>` for SEO) → one or more body paragraphs → one or more CTA buttons authored with Milo's standard **bold link** (filled button) or *italic link* (outline button) syntax. |
| 2 — "What's included" label (1 cell, optional) | A single heading (e.g. "What's included"). This becomes a small label that stays pinned near the top of the viewport while the visitor scrolls through the cards. **If you include this row it must contain exactly one cell** — anything else is left orphaned in the page instead of being removed. |
| 3–6 — Feature cards (2 cells each) | **Cell 1 (text):** a heading (any level, rendered small) + one short body paragraph + a plain-text "Learn more" link (do **not** bold/italic it — it must be a plain link so it gets the arrow-chevron treatment instead of becoming a button). **Cell 2 (media):** an image, or a Milo-standard autoplaying video (link to an `.mp4` with the usual video hash options). The whole card becomes clickable, linking to the "Learn more" URL. |

## Variations

This block has no author-facing variation classes. All visual states (piled cards, animation-complete grid, reduced-motion fallback) are computed automatically from scroll position and the visitor's OS motion preference — there is nothing to add to the block-name cell.

## Example

```
| Offer Hero |
| --- |
| ![](/icons/acrobat.svg) <br> Acrobat Pro <br> ## Turn any file into a polished PDF <br> Edit, sign, and share documents from anywhere. <br> **[Try for free](https://www.adobe.com/acrobat/free-trial.html)** |

| Offer Hero |
| --- |
| ###### What's included |

| Offer Hero |
| --- |
| ###### Edit text and images <br> Fix a typo or swap a photo without leaving your PDF. <br> [Learn more](https://www.adobe.com/acrobat/edit-pdf.html) | ![](/media/card-edit.png) |
| ###### Sign in seconds <br> Collect legally binding e-signatures from any device. <br> [Learn more](https://www.adobe.com/acrobat/sign.html) | ![](/media/card-sign.png) |
| ###### Compress large files <br> Shrink PDFs without losing quality. <br> [Learn more](https://www.adobe.com/acrobat/compress-pdf.html) | ![](/media/card-compress.png) |
| ###### Convert to Word or Excel <br> Turn a PDF into an editable file in one click. <br> [Learn more](https://www.adobe.com/acrobat/pdf-to-word.html) | ![](/media/card-convert.png) |
```

## Notes

- The scroll animation only runs with exactly 4 card rows; fewer cards still render (as a plain grid, no pile/fan animation) but the "cards pile up" effect is designed around 4.
- The "Learn more" link must be plain text, not wrapped in bold/italic — those get converted into filled/outline buttons elsewhere in Milo and would break the chevron-link styling this block expects.
- The optional row 2 ("What's included") only works with exactly one cell; if you add a second cell by mistake the row is left in the page unprocessed.
- Card media supports video: if reduced motion is on, or the browser lacks scroll-timeline support, any authored video is swapped for its poster image (or removed if no poster is set) — always give videos a poster image as a safety net.
- The animation and pinned-eyebrow behavior are automatically skipped for users with `prefers-reduced-motion` set, and inert for browsers without scroll-driven animation support (both are handled in code, no authoring needed).
- **[Section Metadata](./section-metadata.md) `layout`/`style` interaction:** adding `rounded corners bottom` (→ class `rounded-corners-bottom`) to this section's Section Metadata `layout`/`style` row rounds the bottom corners of the hero's background. This block's own CSS deliberately suppresses that rounding if the section *also* carries `parallax move up fast` or `parallax garage door reveal` (both part of Milo's shared scroll-transition system) — combining them would clip the background during the scroll animation, so don't expect rounded corners if either of those is also present.
- In an expanded version of this block, once a card finishes settling into the final grid it's tagged with a class that gives it a visible border in dark-mode sections and makes its tile background transparent; this expanded version also uses a slightly taller card aspect ratio. In a simpler deployment, settled cards get no dark-mode border/transparency treatment and use a slightly shorter card aspect ratio. Either way this is purely visual — the authoring contract (rows/cells/content) is identical.
