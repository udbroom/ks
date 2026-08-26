# Tabs

> **Quick summary:** An accessible tab-switcher that shows/hides whole page Sections as tab panels, letting authors offer alternate views (plan tiers, product categories) without leaving the page. Styled by default as a pill bar; only some deployments also support `radio`, `quiet`, and `dark` treatments. Variations: `center`, `right`, `background-transparent`, `staggered-intro-merch-cards` (all deployments), `radio`, `quiet`, `dark` (only some deployments). Gotcha: a Section only becomes a tab panel if its Section Metadata `tab` value matches a tab label exactly — a mismatch silently drops it.

## Authoring instructions

**Part 1 — the Tabs block (the tab list + settings):**

| Row | Content |
|---|---|
| Row 1 (tab list) | A single cell containing a bulleted list. Each list item's text becomes one tab's label (e.g. `Overview`, `Plans & Pricing`). Optionally, add a paragraph *before* the list: with the `radio` variation this becomes a visible label next to the tab group; with any other variation it's dropped — use the `pretext` config row below instead for an invisible screen-reader label in that case. |
| Any additional rows | Each is a `key | value` config pair (removed from the DOM at build time, never visible). Recognized keys: `id` — a custom string ID for this tab set (needed only if the page has more than one Tabs block, or you want a query-string deep link, e.g. `?plans=business`); `remember` — set to `on` to remember the visitor's last-selected tab (via session storage) and restore it on return; `active-tab` — the label text of the tab that should be selected by default instead of the first one; `pretext` — an accessible label (`aria-label`) read by screen readers for the tab list, e.g. `Choose a plan`. |

**Part 2 — each tab's content (a separate Section, placed anywhere after the Tabs block):**

Add a **[Section Metadata](./section-metadata.md)** block at the top of the Section you want to appear inside a tab, with these rows:

| Section Metadata row | Content |
|---|---|
| `tab` | The tab's label (lowercased, spaces→hyphens automatically), e.g. `plans-pricing` for a tab labeled "Plans & Pricing". If the Tabs block has a custom `id` config row, write this as `id,tab-label` instead (comma-separated), e.g. `plans,business`. |
| `tab-background` (optional) | A color value applied to that tab button's background only while it is selected. |
| `link` (optional) | A URL — if set, clicking this tab navigates to that URL instead of switching panels in place (used to make one "tab" of a shared tab bar actually live on a different page). |
| `deeplink` (optional) | A custom query-string value (e.g. `edu`) — visiting the page with `?<id>=<deeplink-value>` auto-selects this tab on load. |

## Variations

Add these as modifier text on the Tabs block name, e.g. `Tabs (center, background-transparent)`:

| Variation | Effect | How to author | Availability |
|---|---|---|---|
| `center`[^center] | Centers the tab pill list instead of left-aligning it (desktop only). | Add `center`. | All deployments |
| `right`[^right] | Right-aligns the tab pill list (desktop only). | Add `right`. | All deployments |
| `background-transparent`[^background-transparent] | Removes the tab bar's pill background so it sits directly on the section background. | Add `background-transparent`. | All deployments |
| `staggered-intro-merch-cards`[^staggered-intro-merch-cards] | When the active tab panel contains merch cards, animates them in with a staggered fade/slide as the tab becomes active. | Add `staggered-intro-merch-cards`. | All deployments |
| `radio`[^radio] | Restyles the tab list as a row of radio buttons instead of a pill bar (announced to screen readers as a radio group, not a set of tabs). Pair with the optional leading paragraph above for a visible label next to the group. | Add `radio`. | Only some deployments |
| `quiet`[^quiet] | Restyles the tab list as plain text labels with an underline on the active tab, removing the pill background entirely. | Add `quiet`. | Only some deployments |
| `dark`[^dark] | Switches the tab bar's color treatment for a dark background. Combines with either the default pill style or `radio`. | Add `dark` (e.g. `Tabs (radio, dark)`). | Only some deployments |

[^center]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^right]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^background-transparent]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^staggered-intro-merch-cards]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^radio]: [#6340](https://github.com/adobecom/milo/pull/6340) — Rares Munteanu, 2026-08-03
[^quiet]: [#6340](https://github.com/adobecom/milo/pull/6340) — Rares Munteanu, 2026-08-03
[^dark]: [#6340](https://github.com/adobecom/milo/pull/6340) — Rares Munteanu, 2026-08-03
[^radio-keys]: [#6504](https://github.com/adobecom/milo/pull/6504) — Jan Ivan Viloria, 2026-08-19. `radio` now renders as actual `input type="radio"` + `label` elements (previously a styled button with `role="radio"`) — purely an internal accessibility fix, the authoring table above is unchanged.

## Example

```
| Tabs |     |
| --- | --- |
| • Overview<br>• Plans & Pricing<br>• FAQ |
| pretext | Choose a section |
| remember | on |
```

Then, further down the page, the "Plans & Pricing" tab's content section starts with:

```
| Section Metadata |     |
| --- | --- |
| tab | plans-pricing |
| tab-background | #FA0F00 |
```

## Notes

- If you don't set a custom `id` on the Tabs block, it's auto-numbered by its position among all Tabs blocks in the document (1st Tabs block on the page, 2nd, etc.). With only one Tabs block this is fine; with multiple Tabs blocks on the same page, give each an explicit `id` and use the `id,tab-label` format in every associated Section Metadata `tab` row — otherwise sections can attach to the wrong tab set.
- A Section only becomes a tab panel if its `tab` value successfully matches a tab button generated from the Tabs list — a typo in either the list item text or the `tab` value (after lowercasing/hyphenating) means that section is silently left out of any tab and stays in normal page flow.
- Keyboard users can move between tabs once a tab is focused; this is automatic, no authoring needed. For the default/`quiet`/`dark` pill style, that's Left/Right arrow keys (RTL-aware). For `radio`[^radio-keys], since it's a real native radio group, it's Up/Down instead, matching how radio buttons normally behave.
- This block is unrelated to the [Section Metadata](./section-metadata.md) block's own key handling — the `tab`, `tab-background`, `link`, and `deeplink` keys are read directly by Tabs' own code, not by Section Metadata's decorate logic.
- `radio` and `quiet` are visual restyles only — the same authoring table (bulleted list + config rows) and the same Section Metadata `tab` linking work identically regardless of which style variation you choose.
