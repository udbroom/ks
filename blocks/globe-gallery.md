# Globe Gallery

> **Quick summary:** A large, scroll-driven WebGL globe of photo cards — cards fan across the screen, peel into a grid, then fold onto a sphere (a scrollable barrel wall on phones and other touch devices) that visitors can drag, or use on-screen buttons, to spin and rotate, and tap into a full detail view. Built for an immersive "browse everyone/everything" hero — a directory of people, apps, or products — rather than a standard content section. Authored as up to five fixed rows: intro copy, a link to a fragment that supplies the actual cards, hint copy for touch and desktop visitors, accessibility labels for the on-screen controls, and an optional closing pull-quote. No modifier classes — reduced motion, a missing/broken fragment, WebGL failure, and device/card-count handling are all automatic.

## Authoring instructions

The block is authored with up to 5 rows, always in this order. Only the fragment-link row is required — you can leave the others out, but you can't reorder them (skipping a row just shifts the later ones up).

| Row | Purpose | Content |
| --- | --- | --- |
| 1 — Intro copy (optional) | The fixed caption shown while cards fan across the screen at the start of the scroll. | A heading (any level) for the title, followed by one or more paragraphs for the body copy. If you skip the heading, the first paragraph becomes the title instead. |
| 2 — Cards (required) | Points the block at the fragment that supplies every card. | One link to a Milo fragment, with `#_dnb` appended to the URL (e.g. `.../fragments/team-cards#_dnb`). The `#_dnb` suffix is required so Milo doesn't resolve the fragment before the block reads it itself. If this link is missing or wrong, or the fragment fetch fails, the block collapses to an empty section instead of showing a broken globe. |
| 3 — Hint copy, two cells (optional)[^controls] | Small copy telling visitors they can interact with the globe — shown in two different places, so it's split across two cells rather than one line. | **Cell 1** — the sentence shown on phones and other touch devices, between the on-screen rotate arrows (falls back to "Click and drag to rotate. Tap to dive deep into the artwork." if left out). You can author full paragraphs here. **Cell 2** — the short "Click & Drag" cursor hint shown on desktop (falls back to "Click & Drag"). You can leave either cell out to use its default without affecting the other. |
| 4 — Accessibility labels, one cell (optional)[^controls] | Names every on-screen control plus the screen-reader instructions, all on one line, `\|\|`-separated, in this order: instructions text, Rotate left, Rotate right, Pause spinning, Resume spinning, Previous card, card-position template, Next card, Close. | The globe always shows a pause/resume button for its auto-spin, and phones/touch devices also show rotate-left/rotate-right buttons — these nine labels are what screen readers and tooltips announce for all of that, plus the detail-view's Previous/Next/Close buttons and its "N of M" position announcement. The position template must literally contain both `{index}` and `{count}` (substituted at runtime) or it falls back to English; any other part left blank falls back to its own English default individually. |
| 5 — Pull-quote (optional) | A quote shown as the scroll winds down after the globe. | A heading or blockquote for the quote text, then a paragraph for the person's name and another for their role/title. |

**The cards themselves come only from the fragment linked in row 2, not from the block's own table.** In that fragment document, author one section per card (sections split the normal way, with `---`; a single section can also hold multiple cards separated by a horizontal rule). Each card section is flat paragraphs plus one list:

| Content | Becomes | Notes |
| --- | --- | --- |
| A paragraph containing only an image, or an image placed directly in the section | the card's photo | **Required** — a card section with no image is skipped entirely, with no warning. If more than one image is authored, the first one wins. |
| A heading, or a paragraph in **bold** | name | Optional. The bold text (or the whole heading) must be the entire line — bold used mid-sentence doesn't count. |
| A paragraph in *italics* | role | Optional. Same whole-line rule as name. |
| Any other plain paragraph(s) | description | Optional, and you can author as many as you like — they show in the detail view in the order you wrote them, with bold/italic/links preserved. |
| A bulleted list, one top-level item per badge | badges | Each badge item can hold a product name/link, and, nested one level under it, a second bullet with that badge's role text — e.g. `- [Photoshop](url)` with a nested `- Compositing`. A badge item may also carry a small logo alongside the product link — either an `.svg` logo link or a plain image. |

## Variations

This block has no author-facing modifier classes. Everything else is automatic, not authored:

- **No cards, a broken fragment link, or no WebGL support:** the block collapses to an empty section instead of showing a broken or blank globe.
- **Reduced motion:** if the visitor's OS has `prefers-reduced-motion` set, the globe renders already formed and static in normal page flow (no scroll choreography) — still draggable/spinnable, with the same pull-quote underneath.
- **Small screens and touch devices** automatically render a scrollable barrel/wall layout instead of a full sphere — every authored card appears on it, not just a subset.[^card-cap] These devices also get the on-screen rotate-left/rotate-right buttons (row 4's labels), since there's no drag cursor to hint at otherwise. This is all device-driven; there's nothing to author differently for it.

## Example

```
| Globe Gallery |
| --- |
| ## Meet the whole team <br> Every person behind the product, in one place. |
| [Team cards](https://main--milo--adobecom.aem.page/fragments/team-cards#_dnb) |
| Click and drag to rotate. Tap to dive deep into the artwork. | Click & Drag |
| Press Enter to enter the gallery, then Tab through the photos. \|\| Rotate left \|\| Rotate right \|\| Pause spinning \|\| Resume spinning \|\| Previous \|\| {index} of {count} \|\| Next \|\| Close |
| ### "The best part of this job is the people." <br> Jordan Lee <br> VP, Product Design |
```

Fragment (`team-cards`), one section per card:

```
![headshot.jpg](headshot.jpg)
*Product Design*
**Jordan Lee**
Leads the design systems team and has shipped three major redesigns.
Formerly led design ops at a Fortune 500 retailer.
- [Figma](https://figma.com)
  - Design tooling
```

## Notes

- Rows are read by **position**, not by markers — row 1 is intro copy, row 2 the fragment link, row 3 the two hint cells, row 4 the accessibility labels, row 5 the pull-quote. Omitting a row is fine (later rows shift up), but reordering them will misassign content.
- Row 2 only reads the link inside it — any other content authored in that row's cell is ignored.
- All visible chrome strings are authored, not hardcoded: leaving any hint cell in row 3, or any label in row 4, out falls back to its own English default individually — not the whole row.
- The card-position label (row 4's 7th `\|\|` segment) is a template, not plain text — it must contain the literal tokens `{index}` and `{count}` for the "N of M" counter to localize correctly. A string missing either token is discarded in favor of the English default.
- Content authored under the older 4-row shape (before the on-screen controls existed) is silently misread rather than falling back gracefully[^controls] — if this block was authored before 2026-08, republish it with the current 5-row layout rather than assuming it still works.
- A card section with no image is silently skipped — it never reaches the globe and nothing flags the omission, so a missing photo in the fragment is easy to miss during a content review.
- Cards don't necessarily appear on the globe or barrel in the order you wrote them in the fragment — their visual position is deliberately (but consistently) shuffled, the same way for every visitor. The position counter and Next/Previous buttons in the detail view still follow your authored order.[^card-cap]
- This is a large, purely visual/interactive hero experience — pair it with the intro copy (row 1) and pull-quote (row 5) it's designed around rather than expecting other page content to sit inside its scroll run.

[^controls]: [#6477](https://github.com/adobecom/milo/pull/6477) — Jingle Huang, 2026-08-18. Added the on-screen pause/resume-spin and rotate-left/right controls, split the old single hint/instructions/labels row into today's rows 3 and 4, and grew the label list from 4 to 9 parts.
[^card-cap]: [#6509](https://github.com/adobecom/milo/pull/6509) — Jingle Huang, 2026-08-25 ("Globe VQA Feedback"). Removed the earlier 24-card cap on small screens/touch devices and added the deterministic card-shuffle.
