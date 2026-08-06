# Comparison Table (C2)

> **Quick summary:** A responsive pricing/plan comparison table: a sticky row of plan cards (title, price, feature blurb, CTA button) above collapsible feature-comparison rows, with mobile column-switching, tooltips, and built-in accessibility labeling. Authored as one table — row 1 is the mandatory header (corner cell + plan cells split by `-` dividers into label/collapsible/CTA groups), every row after is a feature row, and a `+++` row splits the table into multiple independently-collapsible sub-tables. Variations: `static-header`, and a Section Metadata `expand` key controlling which sub-tables open by default. Gotcha: column alignment across rows is purely positional, so adding/removing a plan column means updating every row.

## Authoring instructions

The block is authored as one table. The **first row** is always treated as the header (the plan cards), and **every row after it** is feature-row content — so row order matters, and the header row is mandatory.

| Row | Content |
|---|---|
| Row 1 — Header | One cell per column. **Cell 1** is the "corner" cell — its content (e.g. a heading) becomes the label above the feature-name column and is not treated as a plan. **Cells 2+** are the plan/column cards: each cell's paragraphs are split into up to 3 stacked groups by inserting a paragraph containing only a hyphen (`-`) as a divider — Group 1 = eyebrow/label + heading (plan name) + price + short description; Group 2 (optional, appears between two `-` dividers) = extra bullet copy shown in a collapsible area; Group 3 (after the last `-`) = the CTA button(s) and/or fine-print description. Leave a plan cell completely empty to have that whole column removed. |
| Row 2+ — Feature rows | **Cell 1** = the feature/row label (supports the tooltip syntax below). **Cells 2+** = one cell per plan column (must line up positionally with the header's plan cells), each cell's value for that feature — plain text, an icon, or a dash (`-`) alone to mark "not included" (renders as a muted em-dash placeholder and is hidden from sighted users but announced to screen readers). |
| A row whose single cell contains exactly `+++` | Not a data row — a **divider** that splits the block into multiple independent, separately-collapsible comparison tables (e.g. "Individual plans" then "Teams plans"). The `+++` row itself is removed. The row immediately after each divider (or the very first row after the header) is that table's own toggle/heading row: cell 1 is the clickable heading that expands/collapses the section, and typing the word `primary` (case-sensitive, lowercase) in one of that row's other cells flags that column as the "primary/recommended" plan for that sub-table (the `primary` marker cell itself is removed). |

Row-label tooltip syntax: apply underline formatting to text in a feature-row's first cell and separate with pipes: `Label|position|Tooltip text`, e.g. `Storage|top|Includes 100GB of cloud storage`. `position` is one of `top`, `bottom`, `left`, `right` (optional — defaults to `right` on desktop / `bottom` on mobile). Underlined text with no pipes, or only a label and no tooltip text, just renders as a dotted-underline hint with no popup.

Buttons in the CTA group follow standard Milo convention: wrap link text in `**bold**` for a filled/primary button, or `_italic_` for an outline button.

## Variations

| Variation | Effect | How to author |
|---|---|---|
| `static-header`[^static-header] | Disables the sticky/collapsing behavior of the plan-card header on scroll — the header stays in its normal position instead of shrinking and sticking as the user scrolls down. | `Comparison Table C2 (static-header)` |
| [Section Metadata](./section-metadata.md) `expand`[^expand] key | Controls which of the `+++`-separated sub-tables render expanded by default. Value `all` expands every sub-table; a comma-separated list of 1-based numbers (e.g. `1, 3`) expands only those sub-tables (in document order); if omitted, only the first sub-table is expanded. | Add a **[Section Metadata](./section-metadata.md)** block in the same page section with a row: `expand` \| `1, 3` |

[^static-header]: [#6086](https://github.com/adobecom/milo/pull/6086) — Rares Munteanu, 2026-06-15
[^expand]: [#6086](https://github.com/adobecom/milo/pull/6086) — Rares Munteanu, 2026-06-15

## Example

```
| Comparison Table C2 |
| Compare plans | ## Standard \n Good for individuals \n $9.99/mo \n --- \n Cloud storage \n --- | ## Pro \n Best for teams \n $19.99/mo \n --- \n Cloud storage, Priority support \n --- |
| **Cloud storage|top|Includes automatic backups** | 100GB | 1TB |
| Priority support | - | Yes |
| _Sign up_ | - | - |

| Comparison Table C2 |
| +++ |
| Individual plans | | primary |
| **Cloud storage|top|Includes automatic backups** | 100GB | 1TB |

| Section Metadata |
| expand | all |
```

## Notes

- The number of `-` dividers you type inside a header plan cell determines how the content is grouped: exactly 2 dividers give you all 3 groups (label/price block, collapsible middle, CTA); with 0 or 1 dividers the collapsible/CTA styling (button decoration, description wrapping) may not apply correctly — always use 2 dividers per plan cell for the documented layout.
- The mobile column-switcher (a dropdown letting visitors swap which plan column is visible) only appears automatically when there are more than 2 plan columns (i.e. more than 3 total header cells including the corner cell); with 2 or fewer plan columns all columns just show on mobile.
- Column alignment between the header row and every feature row is purely positional — cell 2 of every row must always refer to the same plan, cell 3 to the next, etc. Adding/removing a plan column requires updating every single row in the table.
- A cell containing only `-` (or only dashes) is treated as "empty/not included" and is visually hidden with only a short line drawn — do not use `-` for an actual hyphenated value.
- No block-specific `dark` class check exists in this block's JS; the `.dark` CSS rules present are the standard Milo section-level dark theme and apply automatically when the enclosing section is set to dark, not something toggled via the block name.
