# Modal Metadata

> **Quick summary:** A hidden, config-only block (no visible output) authored as key/value rows (`style`, `curtain`, `background`) — but it only has any effect when placed inside a fragment that is being loaded into a [Modal](./modal.md) dialog; viewed as a standalone page, it does nothing. `style` accepts comma-separated keywords that add CSS classes to the dialog; `curtain: off` removes the dimmed background overlay.

---

A hidden, config-only block (`display: none`) that configures the appearance and behavior of a Modal dialog. It only has an effect when it is authored inside the fragment/page that is being loaded *into* a modal (see the Modal block) — if the same fragment is viewed as a normal standalone page, this block does nothing.

## Authoring instructions

Author a table named "Modal Metadata" inside the fragment that serves as a modal's content, with one key/value pair per row (same convention as a Section Metadata block).

| Row | Content |
|---|---|
| `style` | One or more modifier keywords, comma-separated (e.g. `xl-size, tall video`). Spaces in a keyword become hyphens, and each keyword is added as a CSS class to the modal dialog (`.dialog-modal`). See [modal.md](./modal.md) for the list of supported keywords (`three-in-one`, `xl-size`, `s-size`, `tall-video`, `commerce-frame`, `dynamic-height`, `upgrade-flow-modal`, `hide-close-button`, `manage-plan-cancel`). |
| `curtain` | Set the value to `off` to remove the dark background overlay behind the modal and skip disabling scroll/interaction on the rest of the page. Omit this row (or use any other value) to keep the default dimmed curtain. |
| `background` | Optional, only used when `style` includes `tall-video`: an image or a background color (same authoring pattern as Section Metadata's `background` key) applied to the modal. |

If the fragment isn't actually being rendered inside a modal dialog (e.g. you're previewing the fragment directly), this block has no effect.

## Variations

This block itself has no modifier classes on its own block name — all of its configurability comes from the key/value rows above, not from a "Modal Metadata (variant)" naming convention.

## Example

```
| Modal Metadata |
| --- |
| style | xl-size |
| curtain | off |
```

## Notes

- Because this block is invisible and only "activates" inside a modal, do not expect to see any change when previewing the fragment as a normal page — always test by opening the link that triggers the modal.
- `style` values are matched to specific CSS in `modal.css`; typing an arbitrary keyword that isn't one of the documented ones adds a class with no visual effect, so stick to the supported list.
- Only one `style` row is read per block; if you need multiple keywords, put them all in a single row separated by commas rather than adding multiple `style` rows.
