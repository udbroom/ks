# Explore Card

> **Quick summary:** A full-bleed image/video card where the entire tile is one clickable link, with icon/title/description over a gradient scrim that fades in on hover/focus. Authored as a table: row 1 (required) holds content plus background; row 2 (optional) adds extra layered foreground content. Variations: `dark`, plus deployment-only extras like `center`, `show-link`, and per-breakpoint background stacking. Gotcha: when the section's Section Metadata `layout`/`style` includes `bento`, spacing/sizing (and in some deployments a mobile card-stack scroll animation) applies automatically.

---

A full-bleed image or video card where the entire tile is one clickable link: an icon, title, and description sit over a background image or video, with a gradient scrim (a dark overlay for text readability) that fades in on hover/focus. Use it for "explore" grids where each card links out to a bigger story or product page.

## Authoring instructions

The block is authored as a table. **Row 1 is required** and has two cells: content, then background. **Row 2 is optional** and adds extra layered content on top of the background.

| Row | Content |
|---|---|
| Row 1, Cell 1 — Content | One or more optional icon images, then a heading (any level, visually sized as "heading-5"), then body/description text, then a link. The link's destination is used to make the **entire card** clickable; by default the link's own visible text is removed since the whole card is already clickable (see `show-link` below to keep it visible). If the cell also happens to contain a video file link, that link is ignored when picking the card's destination — so you can safely include a video asset and a separate destination link in the same cell. |
| Row 1, Cell 2 — Background | An image or video that fills the card edge-to-edge. |
| Row 2 — Foreground (optional) | Extra content layered above the background but behind the text (e.g. a secondary line, badge, logo, or image/video). Only used if this row actually has content — an empty row is dropped automatically. Leave the row out entirely if you don't need it. |

## Variations

Variations are authored as modifier classes appended to the block name, e.g. `Explore Card (dark)`.

| Variation | Effect | How to author it |
|---|---|---|
| `dark`[^dark] | Switches the text color and background scrim tint for use on dark-themed pages/sections. | "Explore Card (dark)" |

[^dark]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23

Some deployments of this block also support:

- `center` — centers the card's text content (icon/heading/body) both horizontally and as centered text, instead of the default left-aligned layout.
- `show-link` — keeps the authored link text visible as a small standalone label, instead of hiding it, for when you want an explicit "Learn more" caption in addition to the whole card being clickable.
- A more advanced background pattern: stacking 1, 2, or 3 images/videos in the background cell (each as its own paragraph) to show different media at mobile / tablet / desktop widths, optionally with a second line of text giving a focal point (e.g. `left, top`) to control image cropping. If the background cell has no image/video at all, its plain text is used as a solid background color instead. Where this pattern isn't available, use a single image/video for all breakpoints.
- Authoring **multiple icon images** in the content cell — they're automatically consolidated into one icon row shown side by side. In a simpler deployment of this block, only the first icon image is recognized and any additional ones are not consolidated, so stick to one icon there.
- An advanced pattern (shared across several blocks) where inserting a row containing just `mobile-viewport`, `tablet-viewport`, or `desktop-viewport` (bare `mobile`/`tablet`/`desktop` still works but is a legacy fallback being phased out) lets you author entirely different content/background/foreground row sets per breakpoint, with later breakpoints inheriting anything left empty from the previous one. Breakpoint is screen width: with all three defined, mobile = below 768px, tablet = 768–1279px, desktop = 1280px and up; with only mobile-viewport + desktop-viewport, the split is at 1280px. Most authors won't need this.

## Example

```
| Explore Card                                                        |
| ---------------------------------------------------------------------------------- |
| ![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg)## Behind the shot [Read the story](https://www.adobe.com/stories/behind-the-shot.html) A photographer's guide to low-light portraits. | ![Photographer adjusting a camera at night](/night-shoot.jpg) |
```

Dark variation:

```
| Explore Card (dark)                                                  |
| ---------------------------------------------------------------------------------- |
| ## Firefly in the field [See how](https://www.adobe.com/firefly.html) Generative AI, used on set. | ![Video still of a film set](/set-still.mp4) |
```

## Notes

- If the content cell contains no link at all, the card renders as static (non-clickable) content.
- The icon image is optional and purely decorative — if you skip it, the heading simply becomes the first item and picks up extra top spacing automatically.
- The whole card is keyboard-focusable and shows a visible focus ring; don't nest another interactive element (e.g. a second button) inside the content cell, since only one link/destination is supported per card.
- Minimum card height grows at larger screen widths purely via styling — no extra authoring is needed to accommodate this.
- Dark-mode text/background contrast is standard Milo section-level theming (separate from the `dark` variation above) — it applies automatically when the enclosing section/page is set to dark, without any class on this block.
- **[Section Metadata](./section-metadata.md) `layout`/`style` interaction:** when this block sits in a section whose Section Metadata `layout`/`style` row includes `bento`, extra spacing/sizing rules kick in automatically (padding, heading margins, and content-aspect-ratio adjustments tuned for a bento grid) — nothing extra to author on the card itself. In some deployments, adding `bento, stack-mobile` together on that Section Metadata row also turns a bento section's Explore Cards into a sticky, depth-scaled mobile card-stack scroll animation (with a [Rich Content](./rich-content.md) title pinned above it) below the 768px breakpoint — see [section-metadata.md](./section-metadata.md).
