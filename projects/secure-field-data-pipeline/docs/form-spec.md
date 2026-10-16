# Weekly Site Report — Form Specification

## Purpose

Defines the fields for the KoboCollect weekly site report form, derived
directly from the data classification in [`docs/threat-model.md`](../docs/threat-model.md),
so the form is designed from already-reviewed classification rather than
classified after the fact.

Relates to: Epic 1, `docs/agile-process.md`
("As a site engineer, I want the form to enforce required fields...")

---

## Fields

| Field | Type | Required | Classification | Notes |
|---|---|---|---|---|
| Project name | text | Yes | Internal | Selected from a predefined list where possible, to reduce free-text entry error |
| Report date | date | Yes | Internal | Defaults to current date |
| Worker count | integer | Yes | Internal | Validated as a positive number |
| Task / progress status | select_one | Yes | Internal | Fixed choice list (e.g. On track / Delayed / Blocked) — avoids inconsistent free-text status values downstream |
| Progress description / observations | text (long) | No | Internal | Free-text notes |
| Incident flag | select_one (yes/no) | Yes | Internal | Forces an explicit answer rather than an easily-skipped optional field |
| Incident details | text (long) | Conditional | Internal | Required only if Incident flag = yes |
| Site photo(s) | photo (multiple) | No | **Sensitive** — may contain identifiable individuals | Captured directly from device camera (offline-capable); access restricted per `threat-model.md` data classification table |
| Submitting user | system-captured | — | — | Not a form field — tied to the per-user KoboCollect credential, per the Spoofing mitigation in `threat-model.md` (no anonymous submission) |

## Offline behavior

No special handling required at the form-design level — KoboCollect's local-storage-then-sync model (see `docs/architecture.md`, step 1–2) covers the
"works fully offline" requirement natively.

## Open questions before building the XLSForm

- Fixed choice list values for "Task / progress status" (needs real options from the current paper/manual process)
- Whether "Incident flag" should trigger any notification, or just be recorded for later review (not in scope for Epic 1 — would belong to Epic 2 automation)