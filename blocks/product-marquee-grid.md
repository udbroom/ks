# Product Marquee Grid

> **Quick summary:** A small product-highlight tile — an icon/heading "chiclet" stacked above body copy and a CTA — meant to sit alongside other tiles in a grid of products or offers (e.g. a row of app tiles each linking to its own product page). Authored as 1 row; most deployments only read 1 cell (icon, heading, body, optional label paragraph, then a bold/italic CTA link). In one deployment, a second cell in that same row adds a pricing/merch card with its own CTA. Two variations: the default "soft offer" (label-style CTA) and `featured-offer` (large filled chip button, pinned to 25% width on desktop) — `featured-offer` currently has no effect in the deployment with the pricing cell. Only the first row is read — extra rows are ignored.

## Authoring instructions

The block reads content from **row 1**. Most deployments only read that row's first cell; one deployment also reads a second cell for pricing.

| Row | Content |
| --- | --- |
| 1, Cell 1 | In order: an optional small SVG icon image → a heading (`H1`–`H6`, rendered as a large "super" style) → one or more body paragraphs → optionally, one extra short paragraph directly before the CTA link (see "Variations" — this becomes a price/label line next to the button in most deployments) → a CTA link, either a plain link wrapped in **bold** or *italic* (Milo's standard button syntax: `**[Get it now](url)**` or `*[Get it now](url)*`), or a Merchandising-at-Scale (M@S) commerce link[^mas-cta] — those are recognized as the CTA even unwrapped, since M@S applies its own `data-wcs-osi` attribute to the link before this block reads it. |
| 1, Cell 2 (only in some deployments)[^merch-card] | An optional second "merch card": any heading/body paragraphs become pricing/description copy (including M@S `mas-field` elements, which are auto-tagged and styled as price/description) — a plain paragraph right after the price line is treated as a commitment/fine-print line. Any bold/italic buttons or M@S commerce links in this cell are pulled into their own CTA row below the pricing copy. Where this cell isn't supported, a second cell in row 1 is simply not read. |

## Variations

| Variation | Effect | How to author it |
| --- | --- | --- |
| Default (soft offer) | The CTA renders as a light, label-style call-to-action: if you include an extra short paragraph right before the CTA link, it's pulled out and shown as a small label/price line next to the button (e.g. "Starting at $9.99/mo"). | Do nothing extra — this is the default when the block-name cell has no modifier. |
| `featured-offer`[^featured-offer] | The CTA renders instead as a large filled dark "chip" button with an arrow icon, and the promo area is pinned to take up 25% width on desktop. The extra paragraph described above is **not** treated as a label in this variation (it's simply included as body text if present). Currently has no effect in the deployment that supports the pricing/merch-card second cell (see Authoring instructions) — its chip-button code was removed there.[^merch-card] | Add `featured-offer` to the block name, e.g. `Product Marquee Grid (featured-offer)`. |

[^featured-offer]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^merch-card]: [#6534](https://github.com/adobecom/milo/pull/6534) / [#6551](https://github.com/adobecom/milo/pull/6551) — 2026-08. This is recent and may still be in flux — confirm with engineering before treating `featured-offer`'s removal here as final.

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

- Only row 1 is read; extra rows are ignored. Most deployments only read that row's first cell — a second cell is ignored there too — except the one deployment described above, which also reads a second cell for the pricing/merch card.
- The CTA link must be either bold/italic (button syntax) or a M@S commerce link carrying `data-wcs-osi`[^mas-cta] — any other plain link will not be picked up as the CTA and will simply render as leftover inline text.
- In the default (non-`featured-offer`) variation, the "label" paragraph is only extracted when there are **two or more** body paragraphs remaining after the CTA line is removed — with only one paragraph, everything is treated as body copy and no label line appears.

[^mas-cta]: [MWPW-203872](https://github.com/adobecom/milo/commit/72960f6) — Narcis Radu, 2026-08-11
