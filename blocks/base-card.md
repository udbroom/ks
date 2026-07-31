# Base Card

> **Quick summary:** A single promotional card pairing an image with a heading/body/link, for use in a grid of simple tiles. Authored as one table row with two cells — text (foreground) and image (media). Only variation: `featured`, which enlarges the card and adds a parallax reveal. Worth knowing: a Section Metadata `layout`/`style` value (`base card section`) can fix mobile stacking when several of these sit in a grid.

---

A single card with an image (or icon-badged image) on one side and a heading/body/link on the other. Use it for simple promotional tiles in a grid — product callouts, feature highlights, or "learn more" teasers — where you need one image, one short block of text, and one link per card.

## Authoring instructions

The block is authored as **one table row with two columns** (cells). Column 1 is the text ("foreground"); column 2 is the image ("media").

This block only picks up the first row you add — if you include more than one, the extras are ignored unless you use the mobile-viewport/tablet-viewport/desktop-viewport syntax (see Notes).

| Row / Column | Content |
|---|---|
| Column 1 — Foreground (text) | Optional: an image on its own line at the very top of the cell (nothing else in that line) — this is treated as a small **icon** and is automatically moved onto the media image as a 24×24 badge in the top corner. Then: a heading (any level, h1–h6 — it's visually sized as "heading-5" regardless of the level you pick), then body paragraph(s). Optionally end with a link on its own line (not bold/italic) — a "standalone" text link that becomes the whole card's click target. A link wrapped in **bold** or *italic* instead becomes a normal button. |
| Column 2 — Media (image) | Required if you want a card image. A single image, authored normally (with alt text describing the image for screen readers). Milo requires `width`/`height` attributes on the image, which are set automatically when you paste/insert the image — do not strip them. |

## Variations

| Variation | Effect | How to author it |
|---|---|---|
| Featured | Enlarges the card: the media gets an animated rounded-corner reveal (parallax), and on desktop the heading and CTA link sit side-by-side above the image in a two-column layout instead of stacking. | Add "featured" to the block name cell, e.g. "Base Card (featured)". |

## Example

```
| Base Card                                                          |
| ------------------------------------------------------------------ |
| ![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg)                                           |
| ## Creative Cloud                                                  |
| Get every Adobe app, plus AI tools and 100GB of storage.            |
| [Learn more](https://www.adobe.com/creativecloud.html)              || ![Person editing photos on a laptop](https://www.adobe.com/cc-shared/fragments/cco/q1-2026/media_1a42db9c41aec37e5576b44dceb116b48e2963303.jpg?width=750&format=jpg&optimize=medium) |
```

Featured variation:

```
| Base Card (featured)                                                |
| ------------------------------------------------------------------ |
| ## Photoshop                                                        |
| Now with Generative Fill.                                           |
| [Try it free](https://www.adobe.com/photoshop.html)                  || ![Collage created in Photoshop](/media_banner.jpg) |
```

(In an actual authoring table each `|` group above column 1 and column 2 is a separate table cell — the pipe mockup just shows cell boundaries; refer to your doc/table tool's normal 2-column row.)

## Notes

- Only the **first row** of the table is read. If you add a second row without using the `mobile-viewport`/`tablet-viewport`/`desktop-viewport` delimiter keywords, it will be silently ignored.
- This block supports Milo's per-viewport authoring shortcut: adding a row whose single cell reads exactly `mobile-viewport`, `tablet-viewport`, or `desktop-viewport` (bare `mobile`/`tablet`/`desktop` still works but is a legacy fallback being phased out; optionally add variant classes in parentheses, e.g. `desktop-viewport (featured)`) lets you author different content per breakpoint. Breakpoint is screen width: with all three defined, mobile = below 768px, tablet = 768–1279px, desktop = 1280px and up; with only mobile-viewport + desktop-viewport, the split is at 1280px. If you don't need that, ignore it and just use one row.
- The "icon" detection is strict: it only triggers if the first thing in the foreground cell is a paragraph/line containing **only** an image and nothing else. If any text shares that first line, the icon behavior won't trigger and the image will render as ordinary body content instead.
- The standalone link's clickable area is expanded (via an invisible overlay) to cover the entire foreground text area — so avoid putting two links directly in the foreground cell, or the overlay from the first will intercept clicks meant for the second.
- Always provide meaningful alt text on the media image; it is not decorative in most uses of this card.
- **[Section Metadata](./section-metadata.md) `layout`/`style` interaction:** if a section holds several Base Card blocks side-by-side as a grid, you can add `base card section` (→ class `base-card-section`) to that section's Section Metadata `layout`/`style` row (see [section-metadata.md](./section-metadata.md)). On mobile, this forces the grid to a single column with extra vertical spacing, overriding whatever column count the page's default grid CSS would otherwise apply. This isn't required — only add it if the default mobile stacking looks wrong for your specific grid.
