# Iframe

> **Quick summary:** Embeds an external page (scheduling widget, calendar, third-party tool, etc.) inline in a responsive (16:9 by default) `<iframe>`, for when you need it directly in the page flow rather than just linking out. Authored as a single row/cell containing one link — its `href` becomes the iframe `src`; any other content in the cell is ignored. The only variation is passing an extra class in parentheses after the block name (e.g. `iframe-calendar`, which switches to a fixed 1500px height for scheduling widgets); there are no other author-facing variations.

## Authoring instructions

Author a one-row, one-column table named "Iframe" whose single cell contains a link. The block looks for the first link anywhere inside it and uses that link's URL as the iframe's source — any other content in the cell is ignored.

| Row | Content |
|---|---|
| Iframe | A single link (the link text can be anything; the URL is what matters, e.g. `https://example.com/scheduler`). |

Required: the cell must contain a real hyperlink — if no link is found, the block does nothing (no iframe is rendered and the block is left/removed with no visible output).

## Variations

Any extra class typed in parentheses after the block name (e.g. "Iframe (iframe-calendar)") is carried straight through onto the rendered embed wrapper (`<div class="milo-iframe iframe-calendar">`), so it can be targeted with CSS.

| Variation | Effect | How to author it |
|---|---|---|
| `iframe-calendar` | Fixed 1500px height, no padding-bottom (instead of the default responsive 16:9 box) — sized for scheduling/calendar embeds. | Name the block "Iframe (iframe-calendar)" |

## Example

```
| Iframe |
| --- |
| [Book a demo](https://example.com/scheduling-widget) |
```

With the calendar variation:

```
| Iframe (iframe-calendar) |
| --- |
| [Schedule a call](https://example.com/calendar-widget) |
```

## Notes

- If the linked page is same-origin, the block tries to read an `<h1>`–`<h6>` from inside the iframe once it loads and uses that as the iframe's accessible `title`; for cross-origin pages it falls back to the link's `aria-label` if one is set on the authored link (there is no simple authoring UI for `aria-label` in most doc editors, so accessible titling of cross-origin embeds is not guaranteed — flag this to a developer if the embedded page needs a specific title).
- When an Iframe block ends up inside a Modal (see the Modal block), sizing changes automatically (e.g., min-width 80vw, or full-bleed for `commerce-frame`/`three-in-one` modals) — no extra authoring needed.
- If the linked page posts messages from `https://plan.adobe.com` or `https://stage.plan.adobe.com` (Adobe's Manage Plan flow), the block listens for close/external-navigation events from it automatically; this only applies to those specific Adobe domains.
