# Product Marquee Grid

> **Quick summary:** A small product-highlight tile — an icon/heading "chiclet" stacked above body copy and a CTA — meant to sit alongside other tiles in a grid of products or offers (e.g. a row of app tiles each linking to its own product page). Authored as 1 row, 1 cell (icon, heading, body, optional label paragraph, then a bold/italic CTA link). Two variations: the default "soft offer" (label-style CTA) and `featured-offer` (large filled chip button, pinned to 25% width on desktop). Only the first cell of the first row is read — extra rows/cells are ignored.

## Authoring instructions

The block reads content from the **first cell of the first row only** — everything is authored in one column.

| Row | Content |
| --- | --- |
| 1 (1 cell used) | In order: an optional small SVG icon image → a heading (`H1`–`H6`, rendered as a large "super" style) → one or more body paragraphs → optionally, one extra short paragraph directly before the CTA link (see "Variations" — this becomes a price/label line next to the button in the default variation) → a CTA link authored as a plain link wrapped in **bold** or *italic* (Milo's standard button syntax: `**[Get it now](url)**` or `*[Get it now](url)*`). |

## Variations

| Variation | Effect | How to author it |
| --- | --- | --- |
| Default (soft offer) | The CTA renders as a light, label-style call-to-action: if you include an extra short paragraph right before the CTA link, it's pulled out and shown as a small label/price line next to the button (e.g. "Starting at $9.99/mo"). | Do nothing extra — this is the default when the block-name cell has no modifier. |
| `featured-offer`[^featured-offer] | The CTA renders instead as a large filled dark "chip" button with an arrow icon, and the promo area is pinned to take up 25% width on desktop. The extra paragraph described above is **not** treated as a label in this variation (it's simply included as body text if present). | Add `featured-offer` to the block name, e.g. `Product Marquee Grid (featured-offer)`. |

[^featured-offer]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23

## Example

```
| Product Marquee Grid |
| --- |
| ![](/icons/photoshop.svg) <br> ## Photoshop <br> Edit and composite images with the world's best imaging app. <br> Starting at $22.99/mo <br> **[Buy now](https://www.adobe.com/products/photoshop.html)** |
```

With the `featured-offer` variation:

```
| Product Marquee Grid (featured-offer) |
| --- |
| ![](/icons/creative-cloud.svg) <br> ## All Apps <br> Get Photoshop, Illustrator, Premiere Pro, and more — 20+ apps in one plan. <br> **[Explore All Apps](https://www.adobe.com/creativecloud/plans.html)** |
```

## Notes

- Only the first cell of the first row is read; if you author extra rows or a second cell, they are ignored.
- The CTA link must be bold/italic (button syntax) — a plain link will not be picked up as the CTA and will simply render as leftover inline text.
- In the default (non-`featured-offer`) variation, the "label" paragraph is only extracted when there are **two or more** body paragraphs remaining after the CTA line is removed — with only one paragraph, everything is treated as body copy and no label line appears.
