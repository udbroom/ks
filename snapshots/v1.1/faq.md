# FAQ

> **Quick summary:** An accordion of frequently-asked questions, each expanding/collapsing independently via native `<details>`/`<summary>`, with the first item open by default. Authored as one table row per FAQ item — only the row's first cell is used, with a heading as the question and everything after it as the answer. Variations: `seo` (adds FAQPage JSON-LD schema), `heading-<size>`, `body-<size>`. Gotcha: a row without a heading in its first cell is silently skipped, not rendered.

## Authoring instructions

The block is authored as a table where **each row is one FAQ item**, and **only the row's first cell is used** — everything else in that row (additional cells) is ignored.

| Row | Content |
|---|---|
| Any row = one FAQ item | In the row's first cell: a heading (`h1`–`h6`) whose text becomes the question, followed by one or more paragraphs/lists that become the answer (everything in that cell after the heading). **A row with no heading is silently skipped** and won't render as an item at all — always start each item's cell with a heading. |

The first FAQ item in the table is expanded (open) by default; all others start collapsed.

## Variations

Variations are authored as modifier classes appended to the block name in parentheses, e.g. `FAQ (seo)`.

| Variation | Effect | How to author |
|---|---|---|
| `seo`[^seo] | Injects a `FAQPage` JSON-LD schema (`<script type="application/ld+json">`) into the page `<head>`, built from the authored questions and answers, for search-engine rich-result eligibility. | `FAQ (seo)` |
| `heading-<size>` | Overrides the question text size (default is Milo's `heading-5` scale) with any other heading scale keyword, e.g. `heading-xl`. This uses Milo's generic text-override convention (`decorateTextOverrides`), not something specific to this block. | `FAQ (heading-xl)` |
| `body-<size>` | Overrides the answer text size scale the same way. | `FAQ (body-lg)` |

[^seo]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23

## Example

```
| FAQ (seo) |
| ## What is Adobe Creative Cloud? \n Creative Cloud is a suite of apps for photography, design, video, and web. |
| ## Can I cancel anytime? \n Yes, you can cancel your subscription at any time from your account page. |
```

## Notes

- Only the first cell of each row is read; if you accidentally split the question and answer across two cells in the same row (e.g. question in cell 1, answer in cell 2), the answer content will be dropped — keep the heading and all its answer content together in a single cell.
- A row without any heading element is treated as not-an-item and is filtered out entirely before rendering — blank spacer rows are effectively invisible, but a row with only a paragraph and no heading is also silently dropped, which can be a surprising authoring trap.
- No block-specific `dark` handling exists in either the JS or CSS for this block.
