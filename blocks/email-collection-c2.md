# Email Collection C2

> **Quick summary:** A dialog-form block that collects a signed-in visitor's email (plus optional profile fields like name/organization/country/phone) into an Adobe subscription list, shown as a promo panel — an image beside marketing copy, a submit button, and separate success/error states swapped in after submitting. Requires an Adobe ID sign-in by default (auto-redirects if the visitor isn't signed in). Meant to live inside a page/fragment that gets opened as a [Modal](./modal.md) — the button that opens it is authored elsewhere, on the page linking to this fragment. The actual form fields and business config (subscription list, consent copy, sign-in requirement) come from a **Section Metadata** block placed in the same section, not from this block's own table.

## Authoring instructions

The block is authored as **3 fixed rows**, always in this order:

| Row | Cells | Content |
| --- | --- | --- |
| 1 — Content (required) | 1 or 2 | **2 cells:** an image, then the text cell. **1 cell:** just the text cell (no image — see Variations). The text cell holds: an optional heading, an optional icon line (an image placed alone in its own paragraph, immediately followed by bold text on the same line, styled as a small credential/logo-plus-label row), one or more body paragraphs, and a CTA styled as a button (`**bold**` or `*italic*`) whose link is `#submit` — this is what becomes the form's Submit button. |
| 2 — Success message (required) | 1 | Shown in place of the form after a successful signup (or immediately, if the visitor already subscribes). Same shape as row 1's text: heading, body paragraph(s), and a CTA linking to `#close-form` (closes the dialog). Optionally include a second link ending in `#show-form` inside the body copy — its text becomes a clickable "show the form again" toggle, used for the already-subscribed case. |
| 3 — Error message (required) | 1 | Shown instead of the success message if the submit request fails. Same shape as row 2. |

**The actual form fields don't come from this block's table — they come from a Section Metadata block in the same section.** Section Metadata needs:

| Key | Required? | Value |
| --- | --- | --- |
| `mps-sname` | Always | The backend subscription-list/service identifier the signup is associated with. |
| `subscription-name` | One of this or `consent-id` | Fills a `{{subscription-name}}` token inside the legal consent copy (see Notes — the consent text itself isn't authored here). |
| `consent-id` | One of this or `subscription-name` | Selects which centrally-hosted consent/legal copy to show. Defaults to `cs4` if left out. |
| `sign-in` | Optional | `off` skips the Adobe ID sign-in requirement (any other value, or omitting the key, requires sign-in). |
| `runtime-endpoint` | Optional, non-prod only | Overrides the submit API endpoint — for QA/testing, ignored in production. |

Then one row per form field you want to include, each formatted as `Label text|Placeholder text` (the placeholder is optional and falls back to the label):

| Field key | Notes |
| --- | --- |
| `email` | **Required in every instance** — the only field guaranteed to render. |
| `first-name` / `last-name` | Pre-filled and locked (read-only) from the visitor's Adobe profile when it has a name on file; editable only if the profile doesn't. |
| `organization` / `occupation` | Plain text fields. |
| `country` | Dropdown. Options come from a shared, centrally-managed list — not authored per instance. |
| `state` | Dropdown, but **only renders if `country` is also included** — and only for the countries that shared list defines states for. Including `state` without `country` silently drops the field. |
| `phone-number` / `phone-country-code` | Must be authored **together** — including one without the other is rejected. The country-code field is read-only, auto-filled with a flag + calling code from the visitor's locale, and phone validation/formatting is only implemented for two locales (see Notes). |

## Variations

Add these to the block name cell (e.g. `Email Collection C2 (mailing-list)`):

| Class | Effect |
| --- | --- |
| `mailing-list` | Compact "mailing list" promo layout — rounded image corners, tighter spacing, fields stack full-width instead of splitting the first two into a row. |
| `large-image` | The image fills the full block height with no padding, instead of sitting in a fixed-height frame beside the text. |
| `small-width` | Only affects the no-image layout (see below) — caps its max-width at 500px instead of 700px. |

**No-image is automatic, not a class:** leave the image out of row 1 (author only the text cell) and the block detects it has one cell and renders full-width text with no image column.

Also automatic: if the visitor is already subscribed when the dialog opens, the success message is shown immediately (skipping the form) with their email filled in — unless `consent-id` starts with `cs8a`, which always shows the form regardless of prior subscription status.

## Example

Content row (2-cell, with image):

```
| Email Collection C2 |
| --- | --- |
| ![promo image](/media/email-promo.png){width="442" height="304"} | ## Get product updates first <br> Sign up to hear about new features before anyone else. <br> **[Submit](#submit)** |
```

Success and error messages (each its own row, same block):

```
| Email Collection C2 |
| --- |
| ## You're in <br> We'll let you know as soon as there's news. <br> *[Back to the website](#close-form)* |

| Email Collection C2 |
| --- |
| ## Something went wrong <br> Please try again in a moment. <br> *[Close](#close-form)* |
```

Section Metadata in the same section, configuring the fields and business data:

```
| Section Metadata |
| --- |
| mps-sname | product-updates-list |
| subscription-name | Product Updates |
| email | Email address\|you@example.com |
| first-name | First name |
| last-name | Last name |
| organization | Company |
```

## Notes

- **Sign-in is required by default.** A signed-out visitor is redirected straight to Adobe ID sign-in when the dialog opens (and again if the submit request comes back unauthorized); set Section Metadata's `sign-in` to `off` to allow guest submissions instead.
- **Phone number support is locale-limited.** `phone-country-code` only auto-fills (and `phone-number` only validates/formats) for Brazil and India — for any other visitor locale, including both phone fields together will render inputs that never populate a country code and never pass validation. Confirm the target locale before relying on this field pair.
- **The legal consent copy is not authored in this block** — it's fetched at runtime from a centrally-hosted snippet keyed by `consent-id` (default `cs4`), with `{{subscription-name}}` inside it replaced by Section Metadata's `subscription-name`. To change the legal text, change which `consent-id` you reference, not the block's own content.
- **First/last name are conditionally locked:** if the signed-in visitor's Adobe profile already has a name on file, those fields render read-only and pre-filled; only a visitor with no name on file can type into them.
- Row order and cell count are read positionally with no validation — an extra/missing cell will silently misassign content rather than error, same as this project's other strict-row blocks.
- This block is authored inside a fragment/page that's opened as a dialog via [Modal](./modal.md) — the trigger link (styled as a button) lives on whatever page links to this fragment, not inside this block itself.
- The `icons/` assets bundled with this block (asterisk, attention glyph, chevron, country flags) are internal UI chrome, not authorable content.
