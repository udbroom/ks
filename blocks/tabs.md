# Tabs

> **Quick summary:** An accessible pill-style tab-switcher that shows/hides whole page Sections as tab panels. Unlike most blocks, the Tabs table itself only holds the tab labels (a bulleted list) plus optional config rows (`id`, `remember`, `active-tab`, `pretext`) — each tab's actual content lives in a separate Section elsewhere on the page, linked back via a `tab` key in that Section's [Section Metadata](./section-metadata.md). Variations: `center`, `right`, `background-transparent`, `staggered-intro-merch-cards`. The most important gotcha: a Section only becomes a tab panel if its Section Metadata `tab` value matches a tab label exactly (after lowercasing/hyphenating) — a mismatch silently leaves that Section out of any tab.

---

An accessible tab-switcher (pill-style tab list) that shows/hides whole page **Sections** as tab panels. Authors use it to let visitors switch between alternate views of a page (e.g. plan tiers, product categories) without leaving the page. Unlike most blocks, a Tabs block's content is not authored inside the Tabs table itself — the tab labels live in the Tabs table, but each tab's *content* is a separate Section elsewhere on the page, linked to a tab via that Section's [Section Metadata](./section-metadata.md).

## Authoring instructions

**Part 1 — the Tabs block (the tab list + settings):**

| Row | Content |
|---|---|
| Row 1 (tab list) | A single cell containing a bulleted list. Each list item's text becomes one tab's label (e.g. `Overview`, `Plans & Pricing`). |
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

| Variation | Effect | How to author |
|---|---|---|
| `center`[^center] | Centers the tab pill list instead of left-aligning it (desktop only). | Add `center`. |
| `right`[^right] | Right-aligns the tab pill list (desktop only). | Add `right`. |
| `background-transparent`[^background-transparent] | Removes the tab bar's pill background so it sits directly on the section background. | Add `background-transparent`. |
| `staggered-intro-merch-cards`[^staggered-intro-merch-cards] | When the active tab panel contains merch cards, animates them in with a staggered fade/slide as the tab becomes active. | Add `staggered-intro-merch-cards`. |

[^center]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^right]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^background-transparent]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^staggered-intro-merch-cards]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23

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
- Keyboard users can move between tabs with Left/Right arrow keys once a tab is focused; this is automatic, no authoring needed.
- This block is unrelated to the [Section Metadata](./section-metadata.md) block's own key handling — the `tab`, `tab-background`, `link`, and `deeplink` keys are read directly by Tabs' own code, not by Section Metadata's decorate logic.
