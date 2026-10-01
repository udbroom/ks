# Product Marquee Grid

> **Quick summary:** A small product-highlight tile — an icon/heading "chiclet" stacked above body copy — meant to sit alongside other tiles in a grid of products or offers (e.g. a row of app tiles each linking to its own product page). Authored as 1 row; cell 1 holds the icon/heading/body copy, and an optional cell 2 adds a merch/pricing card with its own CTA. Five variations: `dark`, `transparent-bg`, `firefly`, `cta-pill`, and `special-promo`. Only the first row is read — extra rows are ignored.

## Authoring instructions

The block reads content from **row 1** only.

| Row | Content |
| --- | --- |
| 1, Cell 1 | In order: an optional small SVG icon image → a heading (`H1`–`H6`, rendered as a large "super" style) → any number of body paragraphs. All body content becomes "subtext" under the heading — there's no special label-paragraph position before a CTA anymore. |
| 1, Cell 2 (optional) | A merch/pricing card. Heading/body paragraphs become description copy. Merchandising-at-Scale (M@S) `mas-field` price and description fields are auto-styled as the price and description lines. A plain paragraph placed immediately after the price becomes a smaller commitment/fine-print line underneath it. Any bold/italic button link or M@S commerce link (carrying `data-wcs-osi`) in this cell is pulled out into its own CTA row below the pricing copy. |

## Variations

| Variation | Effect | How to author it |
| --- | --- | --- |
| `dark` | Dark background/text theme for the tile. | Add `dark` to the block name, e.g. `Product Marquee Grid (dark)`. |
| `transparent-bg` | Translucent, blurred background instead of a solid fill. Stacks with `dark`. | Add `transparent-bg` to the block name. |
| `firefly` | Rounds the bottom corners of the tile — intended for use under a Firefly-branded hero or section. | Add `firefly` to the block name. |
| `cta-pill` | Lays the merch card out as a pill/rounded, centered layout, arranged as a row on desktop (≥768px). | Add `cta-pill` to the block name. |
| `special-promo` | Automatically inverts the merch card's light/dark theme relative to the tile's own `dark` class, so the card always contrasts against the hero — e.g. a `dark` tile gets a light card, and a light (default) tile gets a dark card. | Add `special-promo` to the block name (combine with `dark` or leave the tile in its default light theme, depending on which contrast you want). |

## Example

```
| Product Marquee Grid |
| --- |
| ![](/icons/photoshop.svg) <br> ## Photoshop <br> Edit and composite images with the world's best imaging app. |
```

With a merch/pricing card and `cta-pill`:

```
| Product Marquee Grid (cta-pill) |
| --- |
| ![](/icons/creative-cloud.svg) <br> ## All Apps <br> Get Photoshop, Illustrator, Premiere Pro, and more — 20+ apps in one plan. | ### Starting at $59.99/mo <br> Billed annually <br> **[Buy now](https://www.adobe.com/creativecloud/plans.html)** |
```

## Notes

- Only row 1 is read; extra rows are ignored.
- In the merch card cell, the CTA must be either a bold/italic button link or a M@S commerce link carrying `data-wcs-osi`[^mas-cta] to be pulled into the CTA row — any other plain link is left in place as regular text.
- The tile's height and internal padding can shift automatically depending on other page chrome (for example, whether the page also has a breadcrumbs header or a local-nav header) — this is automatic, not something you author, but it's worth knowing if the same tile looks slightly different in height across pages.
- The previous `featured-offer` variation (a filled chip-button CTA style) has been removed as of this pull — if you have existing content authored with `featured-offer`, it no longer has any effect and should be migrated to one of the current variations above.

[^mas-cta]: [MWPW-203872](https://github.com/adobecom/milo/commit/72960f6) — Narcis Radu, 2026-08-11
