# News

> **Quick summary:** A headlined grid of short news/press items — headline, optional body snippet, optional standalone "read more" link — authored as a table with a header row (icon + section label) followed by one row per item. Item count (2, 3, or 4, sometimes 6) determines the grid layout (`two-up`/`three-up`/`four-up`/`six-up`). Only variation: `quiet`, for a lower-emphasis "read more" link style.

---

A headlined grid of short news/press items (headline + snippet + optional "read more" link), such as a press-mentions or in-the-news section. Use it when you need to list several short news items under one section heading, each with its own optional link out to the full story.

## Authoring instructions

Author a table named "News" whose **first row** is the section header and whose **remaining rows** are the individual news items (the block requires at least 2 rows total — a header plus at least one item; a single-row table is ignored entirely).

| Row | Content |
|---|---|
| Header row (row 1) | Two columns: **Column 1** — an optional icon image (a small `picture`/image; leave empty for no icon). **Column 2** — a heading (any level h1–h6) or a plain paragraph, used as the section's eyebrow/label text (e.g. "Latest News"). |
| Item rows (row 2+) | Each item is a single column containing, in order: a heading or paragraph for the item's **headline** (required, must be the first text element in the cell), then optionally one or more body paragraphs (truncated to 3 lines visually), then optionally one final paragraph containing **only** a link (nothing else in that paragraph) to act as a "read more"-style standalone link for that item. |

The number of item rows determines the grid layout: 2, 3, or 4 items map to a `two-up`/`three-up`/`four-up` grid class. Other counts fall back to `three-up` styling, which may not lay out cleanly — stick to 2, 3, or 4 items. Some deployments of this block also recognize 6 items as a dedicated `six-up` grid; in others, authoring 6 items falls back to the `three-up` styling instead, so if a 6-item layout looks wrong, that's likely why.

## Variations

| Variation | Effect | How to author it |
|---|---|---|
| `quiet`[^quiet] | Applies a quieter/lower-emphasis style to each item's standalone "read more" link. | Name the block "News (quiet)" |

[^quiet]: [#6086](https://github.com/adobecom/milo/pull/6086) — Rares Munteanu, 2026-06-15

## Example

```
| News |
| --- |
| ![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg) | ## Latest News |
| ### Adobe announces new Firefly features<br>A short summary of the announcement.<br>[Read more](https://example.com/story-1) |
| ### Partnership with example.com<br>A short summary of the partnership.<br>[Read more](https://example.com/story-2) |
| ### Q3 earnings report<br>A short summary of the results.<br>[Read more](https://example.com/story-3) |
```

With the quiet variation:

```
| News (quiet) |
| --- |
| ![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg) | ## Latest News |
| ### Headline one<br>Body text.<br>[Read more](https://example.com/1) |
| ### Headline two<br>Body text.<br>[Read more](https://example.com/2) |
```

## Notes

- The item's headline must be the very first piece of content in the cell — anything placed before it (other than nothing) will be misread as the headline instead.
- The "read more" link only becomes a standalone styled link if its paragraph contains **nothing but** the link; if there's any surrounding text in that paragraph (e.g. "Read more about it here"), it's treated as regular body text instead and the link stays inline.
- A single-row News table (header only, no items) is silently ignored — the block renders nothing.
- Icon images that are SVGs are automatically rewritten to load from Adobe's federated asset root, so authors can reference local/relative SVG icon paths without worrying about federation.
- Card body text is clamped to 3 lines via CSS — longer copy is truncated with an ellipsis, not scrollable, so keep summaries short.
- There is no explicit handling for images placed inside an item's body (only the header row's icon is handled) — an image added inside an item cell isn't actively broken, but it won't be positioned or styled by this block.
- The `two-up`/`three-up`/`four-up`/`six-up` classes mentioned above are applied automatically by this block's own code to its own internal item grid — they're unrelated to [Section Metadata](./section-metadata.md)'s `product-grid` + `-up` multi-block layout system (which arranges separate blocks side by side in a section). Adding `product-grid, two-up` to this block's Section Metadata does not change how many items per row News shows; only the item count does.
