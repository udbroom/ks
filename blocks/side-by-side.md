# Side by Side

> **Quick summary:** A two-card layout pairing a large overlay card (text on image) with a smaller stacked card (text below media), letting authors show two related pieces of content side by side on desktop, stacked on mobile. Authored as two rows — a media row and a text row — with one cell per card, cells lining up between rows. Variations: `dark`, `reverse`, `equal`, `featured`, `small-left`, `content-subtle`/`content-solid`, `scrim-off`, plus a `first-card-<token>`/`second-card-<token>` system for applying any of these to just one card. Only `dark` is guaranteed everywhere; the rest depend on which deployment of the block you're using, and `featured` expects exactly one media/text cell pair, not two.

## Authoring instructions

The block is authored as **two rows**: a media row and a text row.

| Row | Content |
|---|---|
| Row 1 (media) | One cell per card, each containing one image or video for that card. In the default two-card layout, use exactly two cells: Cell 1 = media for Card 1 (the large "overlay" card), Cell 2 = media for Card 2 (the smaller "stacked" card). With the `featured` variant (where available — see Variations), use only **one** cell. On a `card-stacked` card, you can add a **second** image or video to the same cell: the first item becomes a small icon badge in the corner of the media (e.g. an app icon), and the second becomes the card's main media. |
| Row 2 (text) | One cell per card, matching the media row's cell count, each containing that card's text: a heading (any level) and/or a bold paragraph (bold text becomes a `title`-styled line rather than a button), plus body copy. Cell 1 pairs with Card 1's media, Cell 2 with Card 2's. You can also end a cell with one paragraph containing only a link (the link text must equal the whole paragraph's text)[^standalone-link] — it renders as a small standalone label-link instead of body text. Wrapping the link in bold/italic instead still produces a normal button. |

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
| `content-subtle`[^content-tokens] | Dims the body copy in both cards' text to a muted gray tone instead of the card's normal text color. | Add `content-subtle` to the block name to apply it to both cards. |
| `content-solid`[^content-tokens] | Per-card override that forces one card's body copy back to full color — useful when `content-subtle` is set at the block level but one card should stay full-contrast. | Add `first-card-content-solid` or `second-card-content-solid` (see per-card customization below); not meaningful as a plain block-level class. |
| `scrim-off`[^scrim-off] | Forces off the darkening gradient normally layered behind the overlay card's text for legibility, even when that card is otherwise in its "dark" state. | Add `scrim-off` to the block name. |

**Per-card customization**[^per-card]: prefix any of the above token names (or `dark`/`light`) with `first-card-` or `second-card-` to apply it to only one card instead of the whole block — e.g. `first-card-content-subtle`, `second-card-dark`, `first-card-light`. This is most useful for mixing themes within one block: pairing the block-level `dark` variant with `first-card-light` (or `second-card-light`) exempts just that one card from the dark treatment while the other card stays dark.

[^dark]: [`43647d6`](https://github.com/adobecom/milo/commit/43647d6) — Ratko Zagorac, 2026-07-08
[^reverse]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^equal]: [`4114fbe`](https://github.com/adobecom/milo/commit/4114fbe) — Ratko Zagorac, 2026-07-08
[^featured]: [`4114fbe`](https://github.com/adobecom/milo/commit/4114fbe) — Ratko Zagorac, 2026-07-08
[^small-left]: [`4114fbe`](https://github.com/adobecom/milo/commit/4114fbe) — Ratko Zagorac, 2026-07-08
[^content-tokens]: [#6656](https://github.com/adobecom/milo/pull/6656) — Ryan Clayton, 2026-09-09
[^scrim-off]: [#6628](https://github.com/adobecom/milo/pull/6628) — Ratko Zagorac, 2026-09-04
[^per-card]: [#6628](https://github.com/adobecom/milo/pull/6628) — Ratko Zagorac, 2026-09-04
[^standalone-link]: [#6639](https://github.com/adobecom/milo/pull/6639) — Ratko Zagorac, 2026-09-07

In a simpler deployment of this block, only `dark` is available — there is no `reverse`, `equal`, `featured`, `small-left`, `content-subtle`/`content-solid`, `scrim-off`, or per-card customization, and the block always renders exactly two cards (one fixed overlay + one fixed stacked). Check which behavior your environment supports before authoring one of these variants.

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
- Video gotcha: pair the video link with its poster image as two adjacent cells/lines — Milo grabs the poster from whichever image sits next to the video link, and won't show one otherwise. Using `#autoplay` alone plays the video immediately on page load (before the intersection observer above ever gets a chance to manage it) — by the time the card scrolls into view it has already finished, so visitors just see its frozen last frame. If you want it scroll-gated instead, its hash needs both `autoplay` and `viewportplay`, e.g. `#autoplay#viewportplay`.
- Supports Milo's mobile/tablet/desktop content-override rows (see [rich-content.md](./rich-content.md)'s Notes for how that pattern works) — a viewport-delimiter row can override just one card's media or text while leaving the other card's content inherited from the previous viewport.
- Where the `featured` variant is available, it only assigns a card type to the first media/text cell pair. If you accidentally author a second media/text cell pair alongside `featured`, that second card gets an invalid/blank card-type class and won't render its overlay/stacked styling correctly — keep `featured` blocks to exactly one media cell + one text cell.
- `reverse`/`equal`/`featured` now work correctly together with mobile/tablet/desktop viewport-override rows[^viewport-fix] — previously, combining a variation class with viewport overrides could silently fall back to the default card layout instead of applying the variant, since the code checked the wrong element's class list for viewport-override content. If you saw a variant "not take" on a viewport-override authored block before, it should now.
- `card-stacked` icon badge[^icon-badge]: only applies when the media cell has **two** images/videos — with one, the card renders as before. The icon is meant for small app/product marks (an SVG works well here since it's federated automatically), sized and positioned in the corner regardless of what you use for the main media beside it.
- **Behavior change, not just an addition** — stacked card body-text color: previously the stacked card's body copy always rendered dimmed/subtle by default. As of the `content-subtle`/`content-solid` update[^content-tokens], the default is now full-color (matching the card's normal text color); already-published content relying on the old dimmed look will render brighter unless `content-subtle` is added.
- **Possible regression, flagging to confirm with engineering** — overlay card legibility scrim: the overlay card's darkening gradient (behind its text, over the media) now only renders while that card carries the internal `dark` state. Previously it rendered unconditionally. By default (no `dark` variant authored) the block still applies this automatically, so most default-styled blocks are unaffected — but a block authored with the plain `dark` variant and *no* per-card customization class no longer gets the gradient restored, since the per-card system that re-adds it only runs when a `first-card-*`/`second-card-*` class is also present. If a published `dark`-variant Side by Side looks like it lost its image-legibility gradient, pairing `dark` with `first-card-dark`/`second-card-dark` (whichever cell is the overlay card) should restore it — worth confirming this is the intended fix with engineering rather than an oversight.

[^viewport-fix]: [`c025f84`](https://github.com/adobecom/milo/commit/c025f84) — Ratko Zagorac, 2026-08-07
[^icon-badge]: [#6468](https://github.com/adobecom/milo/pull/6468) — Ratko Zagorac, 2026-08-19

## GTK

### Video Flags and Attributes

Add one or more of these to the end of the video's link URL, after a `#`. To combine more than one, put each behind its own `#`, e.g. `#autoplay#viewportplay` — don't use `|` to join them: `|` is also how a poster image's embedded video URL is separated from its own alt text (see the video gotcha above), so a `|` inside the video's hash breaks that split.

| Flag | Effect |
| --- | --- |
| `autoplay` | Plays automatically, muted, and loops. Used alone, playback starts as soon as the page loads — if the video isn't visible yet, it can finish before a visitor scrolls to it. Pair with `viewportplay` to avoid that. |
| `autoplay1` | Same as `autoplay`, but plays once instead of looping. |
| `viewportplay` | Delays playback until the video scrolls into view, and pauses it again once it scrolls out. Combine with `autoplay` (`#autoplay#viewportplay`) so it doesn't finish before becoming visible. |
| `hoverplay` | No autoplay — instead, the video is muted and plays only while a visitor hovers over or focuses it, pausing otherwise. |
| `_hide-controls` | Skips the pause/play accessibility control overlay that autoplay/hoverplay videos normally get layered on top of them — use for purely decorative video where a visible, keyboard-focusable pause button doesn't add value. When combining with another flag, put it first, e.g. `#_hide-controls#autoplay`. |
