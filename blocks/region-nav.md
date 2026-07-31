# Region Nav

> **Quick summary:** The country/language picker shown inside the footer's "change region" modal, with an intro heading plus a scrollable, multi-column list of region/language links. Authored as exactly 2 rows: row 1 is intro heading + body copy, row 2 holds one cell per region group (bold label + bulleted links). There are no author-facing variations — every link's `href` in row 2 is automatically rewritten to the equivalent page in the target locale. This block is meant to live inside a modal/dialog fragment, not as a normal in-page block.

---

Region Nav is the country/language picker shown inside the "change region" modal opened from the footer's language link (URL fragment `#langnav`). It shows an intro heading plus a scrollable, multi-column list of region/language links, and automatically rewrites each link's URL to preserve the visitor's current page when they switch locale.

## Authoring instructions

The block is authored as two rows. Row 1 is the modal's intro copy. Row 2 holds one or more "region group" columns, each with a group heading and a bulleted list of links — the JS reads every `<a>` inside row 2 and rewrites its `href`, so only the second row's links matter for the picker logic.

| Row | Content |
| --- | --- |
| 1 | Intro copy for the modal: a heading (renders as the large title, e.g. Heading 5) followed by a paragraph of body text (e.g. "Choose your region"). Both are required for the modal to read correctly, though the JS itself does not enforce them — this row is skipped if the block has fewer than 2 rows total, which breaks the whole block. |
| 2 | One cell per region/language group. Each cell should contain a short bold label (e.g. "Americas", "Europe") followed by a bulleted list (`<ul><li>`) of links, one per country/language, e.g. `[United States (English)](/us/)`. Every `<a>` found anywhere in this row is picked up and its `href` is rewritten automatically — do not hand-author the domain/locale prefix beyond a normal relative link to that locale's homepage. |

Each `<a>` href is rewritten by the block's script to point at the equivalent of the *current page* in the target locale, falling back to that locale's homepage if the equivalent page returns a 404 (checked via a `HEAD` request on hover/click). Authors do not control this behavior — it is automatic for every link in row 2.

## Variations

This block has no author-facing variations. (The `.hide` class referenced in the CSS is toggled by the loading code that inserts region-nav into the modal, not something an author adds in the table.)

## Example

```
| Region Nav |
| --- |
| **Change your region**<br>Choose the region and language you'd like to see this site in. |
| **Americas**<br>- [United States (English)](/us/)<br>- [Canada (English)](/ca/)<br>- [Brasil (Português)](/br/) | **Europe**<br>- [France (Français)](/fr/)<br>- [Deutschland (Deutsch)](/de/) |
```

## Notes

- Row 2's columns are not laid out 1:1 with the cells you author — the container applies a CSS multi-column layout (1 column on mobile, 3 columns at 600px+, 5 columns at 1200px+), so the browser reflows all the group headings/lists together into that many visual columns regardless of how many divs/cells you used.
- This block is meant to live inside a modal/dialog fragment (it's styled specifically for `.dialog-modal`); authoring it as a normal in-page block is not its intended use.
- Links are checked with a live `HEAD` request when a visitor hovers or clicks — broken destination pages silently fall back to the target locale's homepage rather than erroring, so there's no visual indicator in the doc if a link target doesn't exist for a given locale.
