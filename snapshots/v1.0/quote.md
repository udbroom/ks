# Quote

> **Quick summary:** A large, decoratively framed pull-quote with an optional name + role attribution below it, used to spotlight a testimonial or executive quote. Authored as a single cell containing up to three top-level heading/paragraph elements, in order: quote (required), name (optional), role (optional, only used if a name is present). Variations control attribution alignment: default (left), `center-footer`, `right-footer`. Use a real typographic opening quote character (not a straight `"`) if you want the automatic hanging-punctuation effect.

---

A large, framed pull-quote: a big quote statement inside a decorative bordered frame (with corner dots and center guide lines), with an optional attribution (name + role/title) below it. Use it to spotlight a customer testimonial or executive quote on its own.

## Authoring instructions

The block reads a single cell — the first cell in the first row — and looks for up to three top-level heading/paragraph elements inside it, in order:

| Row | Content |
|---|---|
| 1, Cell 1 — Quote (required) | The **first** heading (`h1`–`h6`) or paragraph found directly in the cell is treated as the quote text itself. It's wrapped in a `<blockquote>`. If the text starts with a real opening curly/typographic quotation mark (e.g. `"` or `«`), that character is automatically pulled out into its own styled span for a "hanging punctuation" effect — you don't need to do anything special, just type the actual curly quote character (not a straight `"`) at the start of your quote if you want this effect. |
| 1, Cell 1 — Name (optional) | The **second** top-level heading/paragraph is treated as the attribution name (e.g. "Jane Doe"). If present, it's wrapped (together with the role, if any) in a `<figcaption>`. |
| 1, Cell 1 — Role (optional) | The **third** top-level heading/paragraph is treated as the person's role/title (e.g. "VP of Design, Acme Corp"). Only used if a name is also present — a role with no name is ignored. |

If the cell doesn't contain any heading or paragraph at all, the block won't build its quote frame — it's left mostly unprocessed.

## Variations

Variations are authored as modifier classes appended to the block name in parentheses, e.g. `Quote (center-footer)`.

| Variation | Effect | How to author |
|---|---|---|
| `center-footer`[^center-footer] | Centers the name/role attribution block (text-align + flex alignment) instead of the default left-aligned attribution. | `Quote (center-footer)` |
| `right-footer`[^right-footer] | Right-aligns the name/role attribution block instead of the default left alignment. | `Quote (right-footer)` |

[^center-footer]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^right-footer]: [`8206068`](https://github.com/adobecom/milo/commit/8206068) — Rares Munteanu, 2026-06-30

If neither variation is added, the attribution is left-aligned by default.

## Example

```
| Quote (right-footer) |
| --- |
| "Adobe's tools let our team ship campaigns twice as fast. |
| Jane Doe |
| VP of Marketing, Acme Corp |
```

## Notes

- Only the first three heading/paragraph elements directly in the cell are used (quote, name, role in that order); any additional headings/paragraphs beyond the third are discarded — the block replaces the entire cell's contents with just the built quote/attribution markup.
- The decorative frame (corner dots, horizontal/vertical guide lines, center dashed line) is entirely CSS-driven and marked `aria-hidden="true"` — it's automatic, not something you author.
- Use a real typographic opening quote character (e.g. `"`, `‘`, or `«`) if you want the hanging-punctuation treatment; a straight double-quote (`"`) does not match the Unicode "initial punctuation" pattern the code checks for (`\p{Pi}`), so it won't get the special hang-out styling.
