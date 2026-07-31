# Tour

> **Quick summary:** A scrollable, numbered product-tour layout meant to run inside a modal dialog — a header (eyebrow + title), 2-3 image-plus-description steps, and a sticky footer promo/CTA. Authored with exactly two single-column rows (header and footer) plus one two-column row per step; rows are classified purely by cell count, not by position, so an extra/missing cell can misclassify a header or footer row as a step. Only variation: `dark` (not available in every deployment). Gotcha: this block is designed to live inside a modal link's content, not as a standalone in-page block.

---

A scrollable, numbered product-tour layout meant to run inside a modal dialog: a header (eyebrow + title), a series of 2–3 image-plus-description steps, and a sticky footer promo with a call-to-action link. On touch devices it gets a drag-to-dismiss handle. Authors use it for "what's new" or guided-feature walkthroughs launched from a modal link.

## Authoring instructions

The block is authored with **exactly two single-column rows** (a header and a footer) plus **one two-column row per tour step**, in any order — the code sorts them by column count, then assigns the first single-column row it finds as the header and the second as the footer:

| Row | Content |
|---|---|
| First single-cell row (header) | One cell containing an optional short paragraph (becomes the eyebrow line, e.g. `New in Creative Cloud`) followed by a Heading 3 (becomes the tour's title, e.g. `### See what's new`). |
| Two-cell rows (tour steps — author 1 to 3 of these) | **Cell 1**: body paragraph(s) describing the step. **Cell 2**: one image (or more than one — extra images after the first are placed in a centered secondary row below the main image). Steps are numbered automatically in document order and labeled `( 1/3 )`, `( 2/3 )`, etc. |
| Second single-cell row (footer) | One cell containing exactly two paragraphs: **first paragraph** = a small promo image/icon, **second paragraph** = the call-to-action link. The link text supports the pipe syntax `Button text\|Accessible label` to set a different `aria-label` than the visible text; if you don't include a link and just type text, that text becomes the CTA label with a non-functional `#` href. |

## Variations

| Variation | Effect | How to author |
|---|---|---|
| `dark`[^dark] | Switches the sticky footer's fade gradient (and the touch-device grab handle's color scheme) from a light/white fade to a dark/knockout fade — use when the tour's modal content sits on a dark background. | Add `dark` to the block name, e.g. `Tour (dark)`. |

[^dark]: [`26685af`](https://github.com/adobecom/milo/commit/26685af) — Dev Ashish Sardana, 2026-07-15

Some deployments of this block do not include the `dark` variant — check whether it's supported in your environment before relying on it.

The only other structural choice is how many two-column step rows you include (the CSS has specific spacing tuned for 3 steps via `.row-1`/`.row-2`/`.row-3`, so more than 3 steps will still render but may not be visually tuned).

## Example

```
| Tour (dark) |
| --- |
| New in Creative Cloud<br>### Discover the Creative Cloud desktop app |
| Manage every app from one place — install, update, and launch without leaving your desktop. | ![step1.jpg](step1.jpg) |
| Sync your files everywhere they're on every device the moment you save. | ![step2.jpg](step2.jpg) |
| Real-time collaboration lets your whole team co-edit the same file, live. | ![step3.jpg](step3.jpg) |
| ![cc-icon.png](cc-icon.png)<br>[Get started\|Get started with Creative Cloud](https://example.com/start) |
```

## Notes

- The block is designed to render inside a Milo modal dialog (its CSS specifically targets `.dialog-modal:has(.tour)` for sizing, slide-in animation, and a swipe-down-to-dismiss handle on touch devices) — author it as the content of a modal link elsewhere on the page, not as a standalone in-page block.
- Rows are classified purely by cell count: if you accidentally create a two-cell header or footer row (e.g. an extra empty second cell), it will be misclassified as a tour step instead — keep header and footer rows to exactly one cell.
- If a document has more or fewer than two single-column rows, the "footer" (or even the "header") may end up undefined and simply not render — always include exactly one header row and one footer row.
- Swipe-to-dismiss and the slide-in/out animation are automatically skipped for users with `prefers-reduced-motion: reduce`.
- In some deployments, the modal also closes when a visitor clicks outside the tour content, and the modal's close (×) button stays visually pinned in place (adjusting its position in sync with scroll) as the tour content scrolls; initial focus moves to the header eyebrow when the tour opens. None of this changes what authors put in the table, but it does affect screen-reader/focus behavior — worth knowing when testing a tour block if this UX isn't what you observe.
