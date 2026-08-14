# Globe Gallery

> **Quick summary:** A large, scroll-driven WebGL globe of photo cards — cards fan across the screen, peel into a grid, then fold onto a sphere (a scrollable barrel wall on phones and other touch devices) that visitors can drag to spin and tap into a full detail view. Built for an immersive "browse everyone/everything" hero — a directory of people, apps, or products — rather than a standard content section. Authored as up to four fixed rows: intro copy, a link to a fragment that supplies the actual cards, optional hint/instruction/label copy, and an optional closing pull-quote. No modifier classes — reduced motion, a missing/broken fragment, WebGL failure, and device/card-count handling are all automatic.

## Authoring instructions

The block is authored with up to 4 rows, always in this order. Only the fragment-link row is required — you can leave the others out.

| Row | Purpose | Content |
| --- | --- | --- |
| 1 — Intro copy (optional) | The fixed caption shown while cards fan across the screen at the start of the scroll. | A heading (any level) for the title, followed by a paragraph for the body copy. If you skip the heading, the first paragraph becomes the title instead and there's no separate body. |
| 2 — Cards (required) | Points the block at the fragment that supplies every card. | One link to a Milo fragment, with `#_dnb` appended to the URL (e.g. `.../fragments/team-cards#_dnb`). The `#_dnb` suffix is required so Milo doesn't resolve the fragment before the block reads it itself. If this link is missing or wrong, or the fragment fetch fails, the block collapses to an empty section instead of showing a broken globe. |
| 3 — Hint, instructions, and labels (optional) | Small pieces of localizable UI copy. | Up to 3 paragraphs: **1st** — the "Click & Drag" hint shown over the globe (falls back to "Click & Drag" if omitted). **2nd** — the instructions read to screen reader/keyboard users for entering the gallery (falls back to an English default). **3rd** — the four modal/gallery labels on one line, `\|\|`-separated, in this order: previous-arrow label, card-position template, next-arrow label, close-button label — e.g. `Previous \|\| {index} of {count} \|\| Next \|\| Close`. The position template must literally contain both `{index}` and `{count}` (substituted at runtime) or it falls back to English; any of the other three parts left blank between the `\|\|`s falls back to its own English default individually. |
| 4 — Pull-quote (optional) | A quote shown as the scroll winds down after the globe. | A heading or blockquote for the quote text, then a paragraph for the person's name and another for their role/title. |

**The cards themselves come only from the fragment linked in row 2, not from the block's own table.** In that fragment document, author one section per card (sections split the normal way, with `---`; a single section can also hold multiple cards separated by a horizontal rule). Each card section is flat paragraphs plus one list:

| Content | Becomes | Notes |
| --- | --- | --- |
| A paragraph containing only an image | the card's photo | **Required** — a card section with no image is skipped entirely, with no warning. |
| A paragraph in *italics* | role | Optional. |
| A paragraph in **bold** | name | Optional. |
| A plain paragraph | description | Shown in the detail view when the card is opened. |
| A bulleted list, one top-level item per badge | badges | Each badge item can hold a product name/link, and, nested one level under it, a second bullet with that badge's role text — e.g. `- [Photoshop](url)` with a nested `- Compositing`. A badge item may also carry a small `.svg` logo link alongside the product link. The older single-line `Name \| Role` format inside one bullet still works too. |

## Variations

This block has no author-facing modifier classes. Everything else is automatic, not authored:

- **No cards, a broken fragment link, or no WebGL support:** the block collapses to an empty section instead of showing a broken or blank globe.
- **Reduced motion:** if the visitor's OS has `prefers-reduced-motion` set, the globe renders already formed and static in normal page flow (no scroll choreography) — still draggable/spinnable, with the same pull-quote underneath.
- **Small screens and touch devices** automatically render a scrollable barrel/wall layout instead of a full sphere, showing only the first 24 authored cards on that barrel — but tapping into the detail view still lets visitors page through every card in the fragment. This is device-driven; there's nothing to author differently for it.

## Example

```
| Globe Gallery |
| --- |
| ## Meet the whole team <br> Every person behind the product, in one place. |
| [Team cards](https://main--milo--adobecom.aem.page/fragments/team-cards#_dnb) |
| Click & Drag <br> Press Enter to enter the gallery, then Tab through the photos. <br> Previous \|\| {index} of {count} \|\| Next \|\| Close |
| ### "The best part of this job is the people." <br> Jordan Lee <br> VP, Product Design |
```

Fragment (`team-cards`), one section per card:

```
![headshot.jpg](headshot.jpg)
*Product Design*
**Jordan Lee**
Leads the design systems team and has shipped three major redesigns.
- [Figma](https://figma.com)
  - Design tooling
```

## Notes

- Rows are read by **position**, not by markers — row 1 is always treated as intro copy, row 2 as the fragment link, row 3 as hint/instruction/label copy, row 4 as the pull-quote. Omitting a row is fine (later rows just shift up), but reordering them will misassign content.
- Row 2 only reads the link inside it — any other content authored in that row's cell is ignored.
- All visible chrome strings are authored, not hardcoded: to fully customize the hint/instructions/labels, author all three paragraphs in row 3. Leaving any one of them out falls back to its own English default individually, not the whole row.
- The card-position label (row 3's 3rd paragraph) is a template, not plain text — it must contain the literal tokens `{index}` and `{count}` for the "N of M" counter to localize correctly. A string missing either token is discarded in favor of the English default.
- On phones and other touch devices, only the first 24 authored cards appear on the sphere/barrel itself — this is a rendering limit, not a content limit. The detail view (opened by tapping any card, or via the keyboard/screen-reader gallery) can still page through every card in the fragment, so nothing is actually hidden from those visitors.
- A card section with no image is silently skipped — it never reaches the globe and nothing flags the omission, so a missing photo in the fragment is easy to miss during a content review.
- This is a large, purely visual/interactive hero experience — pair it with the intro copy (row 1) and pull-quote (row 4) it's designed around rather than expecting other page content to sit inside its scroll run.
