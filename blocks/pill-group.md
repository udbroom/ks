# Pill Group

> **Quick summary:** A centered row of pill-shaped link buttons, with an optional heading above them — a compact way to surface a handful of related links or CTAs, e.g. below a hero or section intro. Authored as an optional heading row followed by a row of plain links; no author-facing modifier classes, but link *formatting* controls the look (see Variations).[^added]

## Authoring instructions

| Row | Content |
| --- | --- |
| 1 (optional) | A heading (`H1`–`H6`) with the pill group's title, e.g. "Popular topics." If this row is omitted, the pills render with no heading above them. |
| 2 | One or more links. Each link becomes its own pill button — the link text is the pill's label, and the link's URL is where it goes. Pills wrap onto additional centered rows automatically once they no longer fit the available width, so there's no fixed limit on how many you can add. |

This block also supports Milo's per-viewport authoring shortcut: adding a row whose single cell reads exactly `mobile-viewport`, `tablet-viewport`, or `desktop-viewport` (bare `mobile`/`tablet`/`desktop` still works but is a legacy fallback being phased out) lets you author a different set of pills per breakpoint. Breakpoint is screen width: with all three defined, mobile = below 768px, tablet = 768–1279px, desktop = 1280px and up; with only mobile-viewport + desktop-viewport, the split is at 1280px. If you don't need that, ignore it and just author one set of pills.

## Variations

This block has no author-facing modifier classes. Instead, how you format each link's text determines its style:

| Link formatting | Result |
| --- | --- |
| Plain text (no bold/italic) | Renders as the dark pill button shown in the example — this is the block's signature look. |
| **Bold** | Renders as a standard blue button instead of a pill — Milo's usual bold-link-to-button formatting takes over. |
| *Italic* | Renders as a standard outline button instead of a pill, for the same reason. |

If you want actual pill styling, leave the link text unformatted.

## Example

```
| Pill Group |
| --- |
| Popular topics |
| [Photography](https://www.adobe.com/photography.html) |
| [Design](https://www.adobe.com/design.html) |
| [Video editing](https://www.adobe.com/video-editing.html) |
```

## Notes

- If a heading is authored and Milo assigns it an `id`, the pill list is automatically linked to it via `aria-labelledby` so screen readers announce the group's purpose — no authoring action needed.
- If the link row has no links in it at all, the block still renders the heading (if authored) but no pills — it won't produce empty pill markup.

[^added]: [`ca4423f`](https://github.com/adobecom/milo/commit/ca4423f) — Ratko Zagorac, "Add pill-group block", 2026-09-11 (landed on `site-redesign-foundation` via PR #6723, 2026-09-16)
