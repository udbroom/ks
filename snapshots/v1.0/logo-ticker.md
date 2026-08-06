# Logo Ticker

> **Quick summary:** A horizontal strip of partner/customer logos that auto-scrolls in a seamless loop (or centers statically if the logos already fit). Authored as one row of icon-shortcode cells, plus an optional second row with a plain-text description used only as the ticker's `aria-label`. No author-facing variations — the only class toggled (`is-static`) is computed automatically at runtime, not set by the author.

---

A horizontal row of partner/customer logos that auto-scrolls (drifts) sideways in a seamless loop. If the logos already fit within the container width, it just centers them statically instead of scrolling. Use it for "Trusted by" / partner-logo strips.

## Authoring instructions

| Row | Content |
|---|---|
| 1 | One or more cells, each containing a single logo authored with Milo's standard icon shortcode syntax — type `:some-icon-name:` in the cell (the authoring pipeline turns this into `<span class="icon icon-some-icon-name">`, which the icons feature then resolves to the actual logo image/SVG). The block reads every `span.icon` anywhere inside it, in document order, as one logo each. |
| 2 (optional) | A single text cell with a plain-language description of the logo set, e.g. "Logos of Adobe Creative Cloud partner brands." This text is **not displayed** — it's used only as the `aria-label` on the ticker (which is exposed to assistive tech as `role="img"`, i.e. one described image rather than a long list of individual logo names). |

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
- On dark backgrounds, any logo authored as an inline SVG automatically has its fill color switched to a light gray so it stays legible — this happens automatically whenever the surrounding section/page (or the block itself) is set to dark; there's no separate authoring step for the logos themselves.
