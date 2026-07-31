# Martech Metadata

> **Quick summary:** A hidden, config-only block that never renders visibly — it patches Adobe Analytics `daa-ll` tracking labels on localized pages so they match the canonical English label, without changing the visible on-page text. Authored as a simple key/value table (on-page label → replacement label), one row per label pair. It has no variations and produces no visible markup.

---

A hidden, config-only block (it is never rendered — `display: none` and it removes itself from the page after running). It lets an author fix up Adobe Analytics tracking labels (`daa-ll` attributes) on a translated/localized page so analytics stay consistent with the English/source label, without changing the visible link or button text.

## Authoring instructions

Author a table named "Martech Metadata" where every row has exactly two columns: a key and a value. The block reads each row and, for any row with two cells, treats the first cell as the key and the second as the value.

| Row | Content |
|---|---|
| Any row | Column 1: the on-page label text as it currently reads on **this** (localized) page — e.g. the visible text of a link, button, or heading used for analytics tracking. Column 2: the value you want substituted in its place when the analytics label is generated (typically the canonical English label). |

Both columns are required — a row with an empty key or empty value is silently skipped. Both the key and the value are run through the same sanitizer used for analytics labels (non-alphanumeric characters are stripped/normalized, leading/trailing underscores trimmed), so match the text as literally as possible.

## Variations

This block has no author-facing variations. It has no visible output and no modifier classes are checked anywhere in its code.

## Example

```
| Martech Metadata |
| --- |
| En savoir plus | Learn more |
| Achetez maintenant | Buy now |
```

This maps the French labels "En savoir plus" and "Achetez maintenant" back to their English tracking equivalents so cross-locale analytics reporting stays comparable.

## Notes

- Place this block anywhere on the page — it produces no visible markup and detaches itself from the DOM once processed.
- Only one Martech Metadata block's values are used per page; if you add more than one, later rows simply merge into (and can overwrite) the same lookup table.
- This block only affects the `daa-ll` analytics attribute value, never the visible text authors see on the page.
