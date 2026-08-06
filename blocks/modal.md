# Modal

> **Quick summary:** Not a table-based block — it's applied automatically to any ordinary link whose URL ends in a `#hash`, turning that link into a trigger that opens the target page/fragment in an overlay dialog instead of navigating away (e.g. for pricing details, sign-up flows, or embedded checkout/plan-management tools). The dialog's appearance/behavior (size, curtain, close button, etc.) is controlled separately via a [Modal Metadata](./modal-metadata.md) block placed inside the target fragment, not on the link itself. Key gotcha: reused hash fragments across different links/fragments only resolve correctly for the first one encountered.

## Authoring instructions

Modal is **not** a table-based block you insert like most others — there is no "Modal" row to fill in. It is applied automatically to any ordinary link whose target URL includes a `#hash` fragment and points at a fragment/page (not `#_inline` or `#_replacecell`, which have other meanings). When Milo sees such a link, it rewrites it to `href="#hash"`, tags it with `data-modal-path` (the target page's path) and `data-modal-hash` (the fragment), and adds the `modal` class. Clicking that link — or loading the page directly with that hash in the URL (a deep link) — opens the target page's content inside a dialog.

| Row | Content |
|---|---|
| Link | A normal link/button whose URL points at the fragment or page you want shown in the modal, with a `#hash` at the end, e.g. `/fragments/pricing-details#pricing-modal`. The hash is just an identifier — it doesn't need to match anything on the target page. |
| Modal content | Authored separately, on the fragment/page the link points to. That page's content becomes the modal body. Add a [Modal Metadata](./modal-metadata.md) block (see below) inside that fragment to control the dialog's appearance/behavior. |

Style the trigger like a normal button using Milo's standard convention: bold (`**text**`) for a filled button, italic (`*text*`) for an outline button.

## Variations

Modal itself has no author-typed variant classes on the link. Its appearance/behavior is instead controlled from **inside the fragment that becomes the modal**, via a **[Modal Metadata](./modal-metadata.md)** block placed in that fragment, using a `style` key (comma-separated keywords, spaces become hyphens) that adds classes to the dialog:

| Style keyword | Effect |
|---|---|
| `three-in-one`[^three-in-one] | Full-height/full-width dialog for multi-step flows |
| `xl-size`[^xl-size] | Extra-large modal on smaller viewports |
| `s-size`[^s-size] | Smaller max-width (650px) on large desktop |
| `tall-video`[^tall-video] | Narrow, tall dialog sized for portrait/tall video content |
| `commerce-frame`[^commerce-frame] | Sized/optimized for embedded commerce iframes (e.g. mini-plans checkout) |
| `dynamic-height`[^dynamic-height] | Iframe content can resize the modal height dynamically via postMessage |
| `upgrade-flow-modal`[^upgrade-flow-modal] | Full-screen upgrade flow, hides the close button |
| `hide-close-button`[^hide-close-button] | Hides the "X" close control |
| `manage-plan-cancel`[^manage-plan-cancel] | Fixed 1280px-wide layout for the plan-cancellation flow |

[^three-in-one]: [#5692](https://github.com/adobecom/milo/pull/5692) — Rares Munteanu, 2026-03-30
[^xl-size]: [#5692](https://github.com/adobecom/milo/pull/5692) — Rares Munteanu, 2026-03-30
[^s-size]: [#5692](https://github.com/adobecom/milo/pull/5692) — Rares Munteanu, 2026-03-30
[^tall-video]: [#5692](https://github.com/adobecom/milo/pull/5692) — Rares Munteanu, 2026-03-30
[^commerce-frame]: [#5692](https://github.com/adobecom/milo/pull/5692) — Rares Munteanu, 2026-03-30
[^dynamic-height]: [#5692](https://github.com/adobecom/milo/pull/5692) — Rares Munteanu, 2026-03-30
[^upgrade-flow-modal]: [#5692](https://github.com/adobecom/milo/pull/5692) — Rares Munteanu, 2026-03-30
[^hide-close-button]: [#5692](https://github.com/adobecom/milo/pull/5692) — Rares Munteanu, 2026-03-30
[^manage-plan-cancel]: [#5692](https://github.com/adobecom/milo/pull/5692) — Rares Munteanu, 2026-03-30

A separate `curtain` key with value `off` removes the dimmed background curtain and skips locking page scroll/disabling the rest of the page — see [modal-metadata.md](./modal-metadata.md).

## Example

On the page where the trigger lives:

```
| Text |
| --- |
| **[See pricing details](/fragments/pricing-details#pricing-modal)** |
```

Inside `/fragments/pricing-details`, add a [Modal Metadata](./modal-metadata.md) block to make it a large modal:

```
| Modal Metadata |
| --- |
| style | xl-size |
```

## Notes

- Because this is link-based, not table-based, there is nothing to type into a "Modal" block — adding one from a block library will do nothing useful. Just link to the fragment with a `#hash`.
- The modal automatically closes on Escape, on clicking the dark curtain, or via its close ("X") button, and restores focus to the triggering link afterward — no extra authoring needed for this behavior.
- If two authors reuse the same hash for different links pointing at different fragments, only the first one encountered will resolve correctly; keep hash fragments unique per fragment.
- **[Section Metadata](./section-metadata.md) `layout`/`style` interaction:** `region selector text` (→ class `region-selector-text`) is a narrow, purpose-built value applied to a section *inside a modal fragment* to tighten that section's intro-copy padding/typography — it's used specifically by the region/locale-selector modal. It isn't a general Modal styling option; don't add it to unrelated modal content expecting a generic effect.
- With `tall-video`: the video itself is authored inside the target fragment using whatever block holds it (e.g. [Rich Content](./rich-content.md)'s `media` variant), not on Modal itself — `tall-video` only sizes the dialog. See that block's own Notes for the video-authoring gotcha (poster image adjacency, `#autoplay`/`viewportplay` hash options).
