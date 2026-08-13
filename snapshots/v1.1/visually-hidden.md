# Visually Hidden

> **Quick summary:** A CSS-only utility block, not a content block — it doesn't process anything you author, so there's no real authoring contract or row/cell shape to follow. Use it to add text assistive technology should announce (extra context, a label, an instruction) without displaying it on screen: whatever content you put in the table (typically one row, one cell of plain text) is clipped to a 1px box and hidden visually while staying readable by screen readers. No variations exist. Avoid putting interactive content (links, buttons) inside it, since it will be functionally present but invisible and effectively untappable.

## Authoring instructions

Because there's no decoration logic, there's no special row/column contract — the block simply wraps whatever content you author inside its table and hides it visually. Typically this is a single row with a single cell of plain text.

| Row | Content |
| --- | --- |
| 1 | Any text you want announced to screen readers but not shown visually — e.g. supplemental context for an icon-only control elsewhere on the page, or a short instruction. Plain text is typical; there is no author-facing formatting convention since the JS does not process the content at all. |

## Variations

This block has no author-facing variations — there are no modifier classes checked anywhere in its JS or CSS, and no decoration logic to vary.

## Example

```
| Visually Hidden |
| --- |
| Opens in a new tab |
```

## Notes

- The block does nothing to the content you author — all behavior comes purely from CSS that clips the content offscreen while keeping it in the page's structure. Nothing about the authored content is transformed, validated, or reformatted.
- Because the content isn't visually rendered, always preview with a screen reader (or check the accessibility tree in devtools) rather than relying on the live preview to confirm the text is present and reads correctly.
- Don't put interactive content (links, buttons) inside this block expecting normal visual behavior — it will be functionally present but invisible and effectively untappable/unclickable for sighted mouse/touch users, which is usually not what's intended for interactive elements.
