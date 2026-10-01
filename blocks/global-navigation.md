# Global Navigation

> **Quick summary:** The shared Adobe header bar (logo, primary nav, search, sign-in) that appears at the top of every Milo page. The block's own table content is never read — it just mounts the shared federal nav app, which pulls real content from a separate nav document (default `/gnav`, overridable via a `gnav-source` metadata key). Most behavior is controlled through page Metadata keys rather than block content or modifier classes — see Authoring instructions below.

## Authoring instructions

Add a block named "Global Navigation" to the page (typically the first block in the first section). This block never reads anything typed inside its own table — it ignores it completely. Instead, it loads the shared "federal" navigation app and mounts it into the block, pulling the actual nav content (logo, links, search, profile) from a separate navigation document.

| Row | Content |
|---|---|
| Global Navigation | Leave the cell empty (or put a placeholder note like "Global nav"). Nothing typed here is read or rendered. |

The nav's real content lives in a separate document, resolved as follows:
- By default, Milo fetches `/gnav` at the site's content root.
- If the page has a **Metadata** block with key `gnav-source`, its value (a path) is used instead, e.g. `gnav-source: /fr/gnav`.
- A Metadata key `universal-nav` with value `on` enables Universal Nav (the cross-Adobe app switcher/profile menu) alongside the standard nav. (This key was previously named `unav` — that old key no longer has any effect; existing pages using it should be updated to `universal-nav`.)
- A Metadata key `gnav-foundation` set to `c2` mounts this styled/sticky global nav on a page whose overall `foundation` metadata is *not* already `c2` — use this to bring the current-generation nav onto an otherwise older-generation page.
- An "App Prompt" can be shown to signed-in desktop visitors, offering to open a companion web app. It requires two Metadata keys to both be set — `app-prompt-entitlement` and `app-prompt-path` — and can be turned off outright with `app-prompt: off`.

Editing the logo, nav items, search behavior, or sign-in flow is done in that separate gnav document/federal nav system, not in this block's table.

## Variations

This block itself has no author-facing modifier classes — its own CSS file only styles the App Prompt and the `gnav-foundation: c2` host state described above. All other visual styling comes from the shared federal navigation stylesheet loaded at runtime; behavior changes are made through the page Metadata keys listed in Authoring instructions, not through block classes.

## Example

| Row | Content |
|---|---|
| Global Navigation | *(empty)* |

Paired page Metadata (optional):

| Row | Content |
|---|---|
| gnav-source | /gnav |
| universal-nav | on |
| gnav-foundation | c2 |
| app-prompt-entitlement | creative_cloud |
| app-prompt-path | /apps/creative-cloud |

## Notes

- Because the block ignores its own table content, authors cannot preview nav changes by editing this block directly — changes must be made in the gnav source document referenced above.
- If `gnav-source` metadata is missing and no `/gnav` document exists at the content root, the block logs an error (`window.lana`) and silently renders nothing.
- The nav's federal domain is auto-detected from the current hostname (`.aem.page`/`.aem.live`/`.aem.reviews` vs. stage/prod), and can be overridden for testing with a `?fedsbranch=<branch>` query parameter (or `local` to point at `http://localhost:3000/federal`) — this override only works on non-production environments (stage, local, PR previews); it's ignored on production.[^fedsbranch-prod]

[^fedsbranch-prod]: [#6436](https://github.com/adobecom/milo/pull/6436) — 2026-07
