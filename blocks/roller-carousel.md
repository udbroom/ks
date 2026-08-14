# Roller Carousel

> **Quick summary:** A full-viewport, scroll-driven showcase — a sticky panel with a blurred, crossfading background, a vertically scrolling list of item names grouped under category labels, and a media panel that crossfades in sync with whichever item is currently centered. Built for showcasing a lineup of items (e.g. "every app in Creative Cloud") where page scroll drives which item is highlighted. Authored as one header row followed by any number of single-cell category-label rows and multi-cell item rows. No author-facing modifier classes; it automatically falls back to a static list for `prefers-reduced-motion`, and automatically repositions its header when the viewport is too short for the roller to fit.

## Authoring instructions

| Row | Content |
| --- | --- |
| Row 1 — header (1 cell) | An optional short paragraph (eyebrow, e.g. "All the apps you need") followed by a heading (`H1`–`H6`) — becomes the panel's title. |
| Category row (1 cell) | Plain text naming a group, e.g. "Photography." Sets the category label shown above the list for every item row that follows it, until the next category row. Add one before your first item row — if you don't, the first group's category label renders blank. |
| Item row (2 or 3 cells) | **Cell 1:** the item's name (plain text) — this is what scrolls through the list. **Remaining cells:** one or two images. With one image, it's used as the item's main media (shown in the media panel); with two, the first image becomes a small icon badge overlaid on the media and the second is the main media. A row whose name cell is empty is skipped entirely — it won't appear in the list. |

## Variations

This block has no author-facing modifier classes — there's nothing to add to the block name. Two behaviors are automatic, not authored:

- **Reduced motion:** if the visitor's OS has `prefers-reduced-motion: reduce` set, the block renders as a static, non-scrolling list (grouped under its category headings, with one fixed blurred background from the first item's image) instead of the scroll-driven roller.
- **Reflow:** if the viewport is too short for the header, list, and media panel to fit together, the header automatically moves above the sticky panel to free up vertical room. This responds to available space at render/resize time — it isn't something you author.

## Example

```
| Roller Carousel |
| --- |
| All the apps you need <br> ## One place for every Creative Cloud app |
| Photography |
| Lightroom | ![lr-icon.svg](lr-icon.svg) | ![lightroom.jpg](lightroom.jpg) |
| Photoshop | ![ps-icon.svg](ps-icon.svg) | ![photoshop.jpg](photoshop.jpg) |
| Video |
| Premiere Pro | ![pr-icon.svg](pr-icon.svg) | ![premiere.jpg](premiere.jpg) |
| After Effects | ![ae-icon.svg](ae-icon.svg) | ![aftereffects.jpg](aftereffects.jpg) |
```

## Notes

- The total scroll distance scales with how many items you author (roughly one viewport height plus ~200px per item) — more items means more scrolling before the panel releases, and there's no per-instance way to shorten it.
- Category and item rows can be freely interleaved in any order or count — the code just walks rows top to bottom, treating any 1-cell row as a new category label and any 2+-cell row with a non-empty name as an item filed under whichever category label came most recently before it.
- Only one image is required per item; add a second only when you want the small icon badge over the main image. The icon is always whichever image appears first in the row, so order icon before main media if you use both.
- Media cells only read `<picture>` elements — video links are not supported here and won't display.
- Backgrounds are always heavily blurred and cropped to cover automatically; there's no authoring control over that treatment.
- Supports Milo's mobile/tablet/desktop content-override rows (see [rich-content.md](./rich-content.md)'s Notes for how that pattern works) — a viewport-delimiter row can give a different header, category set, or item lineup per breakpoint while inheriting anything left unchanged from the previous viewport.
