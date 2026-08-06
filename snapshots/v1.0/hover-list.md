# Hover List

> **Quick summary:** A numbered list where hovering (or the active item on touch) reveals a stacked, parallax-following image pile. Authored as a heading row followed by one row per item (label cell + one-or-more-images media cell). Key feature: optional per-breakpoint content overrides via `mobile-viewport`/`tablet-viewport`/`desktop-viewport` divider rows, which can also carry per-breakpoint modifier classes.

---

A numbered list of items where hovering (desktop) or the current item (mobile/tablet) reveals stacked, layered thumbnail images that follow the cursor with a springy parallax motion. Use it for feature/benefit lists ("01 Fast performance", "02 Built-in AI", ...) where each item should preview an image or short set of images on hover.

## Authoring instructions

The block reads rows top to bottom. **Row 1** is the heading row, **every row after that** is a list item.

| Row | Content |
|---|---|
| 1, cell 1 | The block headline. Put a heading (e.g. `## My Headline`) here — it's auto-styled as `heading-2`. Any other cells in row 1 are ignored. |
| 2+, cell 1 (text) | The item's text/label, e.g. `### Real-time collaboration`. Rendered as `heading-5`. |
| 2+, cell 2 (media) | One or more images. Add multiple images to the same cell to get a stacked, layered "photo pile" that follows the cursor for that item (each extra image is progressively offset/rotated). If a row has no images in cell 2, that item just has no hover media. |

Item numbers ("1.", "2.", "3.", ...) are generated automatically — do not type them into the text cell.

## Variations

This block has no modifier classes on the block name. It does have one structural authoring feature: **per-viewport content overrides**, via `decorateViewportContent`.

| Feature | Effect | How to author it |
|---|---|---|
| Per-breakpoint content | Lets you author completely different rows for mobile / tablet / desktop instead of one shared set of rows. | Insert a row whose **only cell** contains just `mobile-viewport`, `tablet-viewport`, or `desktop-viewport` (case-insensitive; bare `mobile`/`tablet`/`desktop` still works but is a legacy fallback being phased out) as a divider. Every row after that divider (until the next divider or the end of the table) becomes that breakpoint's content. Breakpoints you don't define inherit content from the next-smaller breakpoint you did define (e.g. define `mobile-viewport` and `desktop-viewport` only — tablet reuses `mobile-viewport`'s content, or `desktop-viewport`'s if a row/cell is empty in the smaller viewport section but filled in a larger one already processed). Breakpoint is measured by screen **width**: with all three defined, mobile = below 768px, tablet = 768–1279px, desktop = 1280px and up; with only `mobile-viewport` + `desktop-viewport`, the split moves to 1280px (mobile = below 1280px). |
| Per-breakpoint modifier classes | Add extra CSS classes to the block only for a given breakpoint. | On the same divider row, add classes in parentheses after the keyword, e.g. `desktop-viewport (compact)` — `compact` is added to the block's class list only while that breakpoint is active. |

If you never add `mobile-viewport`/`tablet-viewport`/`desktop-viewport` divider rows, the same rows/content are used at every breakpoint (the default, and the common case).

## Example

```
| Hover List                              |
|------------------------------------------|
| ## Why creators choose Adobe             |
| ### Real-time collaboration | ![preview](/media_1.png) |
| ### Built-in generative AI  | ![preview](/media_2.png) ![preview 2](/media_3.png) |
| ### One subscription, every app | ![preview](/media_4.png) |
```

With a per-viewport override (mobile shows fewer items than desktop; breakpoint is 1280px since only two viewports are defined):

```
| Hover List                              |
|------------------------------------------|
| ## Why creators choose Adobe             |
| desktop-viewport                         |
| ### Real-time collaboration | ![preview](/media_1.png) |
| ### Built-in generative AI  | ![preview](/media_2.png) |
| ### One subscription, every app | ![preview](/media_4.png) |
| mobile-viewport                          |
| ### Real-time collaboration | ![preview](/media_1.png) |
| ### Built-in generative AI  | ![preview](/media_2.png) |
```

## Notes

- The hover/parallax image-follow effect is desktop-only (`width >= 1280px`); below that, images are simply shown inline/statically per item (no follower JS runs) per the responsive CSS.
- Respects `prefers-reduced-motion`: images snap directly into place under the cursor instead of animating in with spring physics.
- Keyboard/touch users don't get a cursor to "hover" with — on narrower viewports the media block for each item is shown inline instead of relying on mouse position, so content isn't lost, just presented differently.
- Because only the first cell of row 1 is used for the headline, don't rely on additional cells in the headline row — they're silently dropped.
