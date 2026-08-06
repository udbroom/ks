# Global Navigation

> **Quick summary:** The shared Adobe header bar (logo, primary nav, search, sign-in). The block's own table content is never read — it just mounts the shared federal nav app, which pulls real content from a separate nav document (default `/gnav`, overridable via a `gnav-source` metadata key). This block has no author-facing variations at all — its CSS is empty and it checks no modifier classes.

---

Global Navigation is the shared Adobe header bar (logo, primary nav, search, sign-in/profile) that appears at the top of every Milo page. It is a mount point only — its own authored table carries no content, so authors mainly interact with it through page-level Metadata keys.

## Authoring instructions

Add a block named "Global Navigation" to the page (typically the first block in the first section). This block never reads anything typed inside its own table — it ignores it completely. Instead, it loads the shared "federal" navigation app and mounts it into the block, pulling the actual nav content (logo, links, search, profile) from a separate navigation document.

| Row | Content |
|---|---|
| Global Navigation | Leave the cell empty (or put a placeholder note like "Global nav"). Nothing typed here is read or rendered. |

The nav's real content lives in a separate document, resolved as follows:
- By default, Milo fetches `/gnav` at the site's content root.
- If the page has a **Metadata** block with key `gnav-source`, its value (a path) is used instead, e.g. `gnav-source: /fr/gnav`.
- A Metadata key `unav` with value `on` enables Universal Nav (the cross-Adobe app switcher/profile menu) alongside the standard nav.

Editing the logo, nav items, search behavior, or sign-in flow is done in that separate gnav document/federal nav system, not in this block's table.

## Variations

This block has no author-facing variations. It doesn't check for any modifier classes, and its CSS file is empty — all visual styling comes from the shared federal navigation stylesheet loaded at runtime.

## Example

| Row | Content |
|---|---|
| Global Navigation | *(empty)* |

Paired page Metadata (optional):

| Row | Content |
|---|---|
| gnav-source | /gnav |
| unav | on |

## Notes

- Because the block ignores its own table content, authors cannot preview nav changes by editing this block directly — changes must be made in the gnav source document referenced above.
- If `gnav-source` metadata is missing and no `/gnav` document exists at the content root, the block logs an error (`window.lana`) and silently renders nothing.
- The nav's federal domain is auto-detected from the current hostname (`.aem.page`/`.aem.live`/`.aem.reviews` vs. stage/prod), and can be overridden for testing with a `?fedsbranch=<branch>` query parameter (or `local` to point at `http://localhost:3000/federal`).
