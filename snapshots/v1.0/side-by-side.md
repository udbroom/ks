# Side by Side

> **Quick summary:** A two-card layout pairing a large overlay card (text on image) with a smaller stacked card (text below media). Authored as two rows — a media row and a text row — with one cell per card, cells lining up between rows. Variations: `dark`, `reverse`, `equal`, `featured`, `small-left`. Only `dark` is guaranteed everywhere; the other four variations depend on which deployment of the block you're using, and `featured` expects exactly one media/text cell pair, not two.

---

A two-card layout pairing a large image/video overlay card (text sits on top of the image) with a smaller stacked text-and-media card (text sits below the image). Authors use it to showcase two related pieces of content (e.g. a feature highlight next to a supporting story) side by side on desktop, stacked on mobile. Some deployments of this block also support single-card and matched-pair layouts for building mixed hero-plus-grid arrangements (see Variations).

## Authoring instructions

The block is authored as **two rows**: a media row and a text row.

| Row | Content |
|---|---|
| Row 1 (media) | One cell per card, each containing one image or video for that card. In the default two-card layout, use exactly two cells: Cell 1 = media for Card 1 (the large "overlay" card), Cell 2 = media for Card 2 (the smaller "stacked" card). With the `featured` variant (where available — see Variations), use only **one** cell. |
| Row 2 (text) | One cell per card, matching the media row's cell count, each containing that card's text: a heading (any level) and/or a bold paragraph (bold text becomes a `title`-styled line rather than a button), plus body copy. Cell 1 pairs with Card 1's media, Cell 2 with Card 2's. |

If either row is missing, or the two rows don't line up, the block's decoration logic bails out silently and nothing renders — always author matching row/cell structure for whichever variant you're using.

## Variations

| Variation | Effect | How to author |
|---|---|---|
| `dark`[^dark] | Suppresses the automatic dark-overlay treatment normally added to the overlay card — use when the block already sits inside a section with a dark background, so the card doesn't get a redundant dark treatment. | Add `dark` to the block name, e.g. `Side by Side (dark)`. |

In an expanded version of this block, four additional variations are available:

| Variation | Effect | How to author |
|---|---|---|
| `reverse`[^reverse] | Swaps which card gets the "overlay" treatment and which gets "stacked": Card 1 (left cell) becomes the small stacked card, Card 2 (right cell) becomes the large overlay card. The desktop column widths flip to match (small column first, wide column second). | Add `reverse` to the block name. |
| `equal`[^equal] | Both cards render as "stacked" cards (no large overlay card) — useful for a matched pair of cards, commonly placed directly after a `featured` Side by Side block to build a mixed 1-large + 2-small layout. On desktop the grid reserves an extra empty leading column so the two cards line up under a preceding `featured` block. | Add `equal` to the block name. |
| `featured`[^featured] | Renders as a **single** full-width overlay card instead of two cards. Author only **one** cell in the media row and **one** cell in the text row — do not add a second pair of cells, since the variant only expects one card. | Add `featured` to the block name; author only one media cell + one text cell. |
| `small-left`[^small-left] | Cosmetic tweak for the stacked card's inner padding — moves its indent padding from the left side to the right (the default already pads on the left; `small-left` flips it). Used to mirror a stacked card's layout when paired with `reverse`/`equal` arrangements. | Add `small-left` to the block name alongside another variant. |

[^dark]: [`43647d6`](https://github.com/adobecom/milo/commit/43647d6) — Ratko Zagorac, 2026-07-08
[^reverse]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^equal]: [`4114fbe`](https://github.com/adobecom/milo/commit/4114fbe) — Ratko Zagorac, 2026-07-08
[^featured]: [`4114fbe`](https://github.com/adobecom/milo/commit/4114fbe) — Ratko Zagorac, 2026-07-08
[^small-left]: [`4114fbe`](https://github.com/adobecom/milo/commit/4114fbe) — Ratko Zagorac, 2026-07-08

In a simpler deployment of this block, only `dark` is available — there is no `reverse`, `equal`, `featured`, or `small-left` option, and the block always renders exactly two cards (one fixed overlay + one fixed stacked). Check which behavior your environment supports before authoring one of these four variants.

## Example

Default two-card layout:

```
| Side by Side |     |
| --- | --- |
| ![overlay.jpg](overlay.jpg) | ![stacked.jpg](stacked.jpg) |
| ## Built for creators<br>Everything you need to bring your ideas to life. | **Community spotlight**<br>See what others are making with Creative Cloud. |
```

With the dark variant:

```
| Side by Side (dark) |     |
| --- | --- |
| ![overlay.jpg](overlay.jpg) | ![stacked.jpg](stacked.jpg) |
| ## Built for creators<br>Everything you need to bring your ideas to life. | **Community spotlight**<br>See what others are making with Creative Cloud. |
```

Featured + equal pair (hero card followed by a matched two-up row, where the expanded variant set is available):

```
| Side by Side (featured) |
| --- |
| ![hero.jpg](hero.jpg) |
| ## Meet the new Creative Cloud |

| Side by Side (equal) |     |
| --- | --- |
| ![story-a.jpg](story-a.jpg) | ![story-b.jpg](story-b.jpg) |
| **Story A**<br>Short supporting copy. | **Story B**<br>Short supporting copy. |
```

## Notes

- If either row is missing, or either row has fewer cells than expected for the variant, nothing renders — always author exactly matching row/cell structure.
- Videos in either card are managed automatically: an intersection observer pauses off-screen video and resumes on-screen video; authors do not need to configure autoplay behavior manually beyond adding the video.
- Supports Milo's mobile/tablet/desktop content-override rows (see [rich-content.md](./rich-content.md)'s Notes for how that pattern works) — a viewport-delimiter row can override just one card's media or text while leaving the other card's content inherited from the previous viewport.
- Where the `featured` variant is available, it only assigns a card type to the first media/text cell pair. If you accidentally author a second media/text cell pair alongside `featured`, that second card gets an invalid/blank card-type class and won't render its overlay/stacked styling correctly — keep `featured` blocks to exactly one media cell + one text cell.
