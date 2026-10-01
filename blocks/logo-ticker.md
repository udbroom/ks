# Logo Ticker

> **Quick summary:** A horizontal strip of partner/customer logos that auto-scrolls in a seamless loop (or centers statically if the logos already fit) — commonly used for "Trusted by" / partner-logo strips. Authored as one row of icon-shortcode cells, plus an optional second row that supplies the ticker's accessible label and, optionally, custom play/pause button labels. Visitors get a small play/pause control to stop the auto-scroll — it starts paused automatically if the visitor's device has reduced motion enabled. No author-facing modifier classes — the only class toggled (`is-static`) is computed automatically at runtime, not set by the author.

## Authoring instructions

| Row | Content |
|---|---|
| 1 | One or more cells, each containing a single logo authored with Milo's standard icon shortcode syntax — type `:some-icon-name:` in the cell (the authoring pipeline turns this into `<span class="icon icon-some-icon-name">`, which the icons feature then resolves to the actual logo image/SVG). The block reads every `span.icon` anywhere inside it, in document order, as one logo each. |
| 2 (optional) | A single text cell describing the logo set, e.g. "Logos of Adobe Creative Cloud partner brands." This text is **not displayed** — it's used as the `aria-label` on the ticker (exposed to assistive tech as `role="img"`, i.e. one described image rather than a long list of individual logo names). To also set custom accessible labels for the play/pause button, add two more segments separated by `\|\|`: `<description> \|\| <play button label> \|\| <pause button label>`, e.g. `Logos of Adobe partner brands \|\| Play logo scroll \|\| Pause logo scroll`. If you omit the button labels (or the whole row), they default to the English "Play logos" / "Pause logos." |

If no `span.icon` elements are found anywhere in the block, nothing renders.

## Variations

This block has no author-facing variations. There are no modifier classes checked in the JS, and the only class toggled (`is-static`) is computed automatically at runtime based on whether the logos already fit the container — not something an author sets.

## Example

```
| Logo Ticker                                         |
|-------------------------------------------------------|
| :adobe-logo: | :microsoft-logo: | :ibm-logo: | :sap-logo: |
| Logos of Adobe's technology partners                    |
```

## Notes

- The block clones the full logo set a second time internally to create a seamless scrolling loop; you only author the logos once (row 1) — do not duplicate them yourself.
- The duplicate (cloned) set is marked `aria-hidden="true"` so screen readers only encounter the logos once; combined with the row-2 description and `role="img"`, the whole ticker reads as a single described image rather than a list of links/logos.
- Scrolling uses a CSS scroll-driven animation (`animation-timeline`) and only runs when `prefers-reduced-motion: no-preference`; otherwise the logos stay static. It also only animates when there are enough logos to overflow the container — a short logo list will simply be centered, not looped.
- In RTL layouts the drift direction is automatically mirrored — no authoring action needed.
- A play/pause button now overlays the ticker so visitors can stop the auto-scroll; it's hidden automatically whenever the ticker is in its static (non-scrolling, already-fits) state. It starts paused automatically if the visitor's device has "reduce motion" enabled, and its accessible label switches between the play/pause text you authored (or the defaults) as it's toggled.
- Scroll speed also responds slightly to how the visitor scrolls the page (a small "boost" on top of the constant base drift) in addition to the steady loop — this is automatic, nothing to author.
- On dark backgrounds, any logo authored as an inline SVG automatically has its fill color switched to a light gray so it stays legible — this happens automatically whenever the surrounding section/page (or the block itself) is set to dark; there's no separate authoring step for the logos themselves.
