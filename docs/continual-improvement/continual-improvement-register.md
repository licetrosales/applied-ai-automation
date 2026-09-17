# Continual Improvement Register

## Purpose

This Continual Improvement Register (CIR) records improvement
opportunities identified while designing, implementing, testing,
and maintaining projects in the `applied-ai-automation` repository.

The register is inspired by the ITIL 4 Continual Improvement
practice and is adapted for a personal engineering and portfolio
environment.

Its purpose is to:

- capture lessons learned during project work,
- turn recurring lessons into reusable engineering practices,
- improve consistency across projects,
- support traceability between improvements and supporting documents,
- encourage continual improvement without creating unnecessary
  administrative overhead.

---

## CIR-001 — Standardize Git Commit Conventions

### Identification

**ID:** CIR-001

**Category:** Engineering Practice / Version Control

**Status:** WIP*

**Priority:** Medium

**Risk:** Low

**Size / Resources:** Small

**Timescale:** Short

**Action Owner:** Repository Owner

---

### Description

Establish a standardized Git commit convention for low-code,
AI automation, and Agile project work across the
`applied-ai-automation` repository.

The convention defines:

- commit types,
- scope naming,
- commit message structure,
- commit granularity,
- classification of low-code changes,
- examples for automation projects.

---

### Reason / Rationale

Traditional software projects primarily represent implementation
changes through source code.

Low-code and automation projects are different.

Significant engineering changes may occur through:

- Make.com scenario configuration,
- workflow modules and filters,
- API integrations,
- AI prompts,
- data mappings,
- external service configuration,
- architecture decisions,
- testing evidence,
- sprint documentation.

Using only generic commit messages can make these changes difficult
to understand later.

A standardized convention improves the clarity of Git history and
creates better traceability between engineering work, Agile sprint
activities, documentation, and automation changes.

---

### Expected Benefits

- More consistent Git history across projects.
- Clearer distinction between implementation and documentation changes.
- Better traceability of low-code engineering work.
- Easier understanding of project evolution.
- More professional repository documentation.
- A reusable version-control practice for future projects.

---

### Related Metrics / Indicators

The effectiveness of this improvement can be evaluated through:

- consistent use of defined commit types,
- use of meaningful scopes where appropriate,
- reduction of vague commit messages,
- ability to understand a change from the commit history,
- traceability between commits and project/sprint activities.

Formal KPI targets are not required at this stage because this is
an individually maintained portfolio and learning environment.

---

### Supporting Documents

- `docs/standards/git-commit-convention.md`

---

### Review Notes

Review the convention after it has been used across multiple sprints
and projects.

Potential future improvements should be recorded as separate CIR
entries rather than silently changing the working standard.

---

## CIR-002 — Add Standards Scope to Git Commit Convention

### Identification

**ID:** CIR-002

**Category:** Engineering Practice / Version Control

**Status:** Implemented

**Priority:** Low

**Risk:** Low

**Size / Resources:** Small

**Timescale:** Short

**Action Owner:** Repository Owner

---

### Description

Add a `standards` scope to the Git commit convention to cover
repository-wide conventions and standards documents (e.g. the
commit convention itself, coding standards).

---

### Reason / Rationale

Commits that modify governance documents — such as the commit
convention or future coding standards — did not have a scope that
clearly identified them as repository-wide process changes,
distinct from project-specific `docs` or `repo` changes.

---

### Expected Benefits

- Clear identification of commits that modify repository-wide
  process and governance documents.
- Consistent scope taxonomy as the standards library grows.

---

### Related Metrics / Indicators

- Consistent use of the `standards` scope for governance document
  changes going forward.

---

### Supporting Documents

- `docs/standards/git-commit-convention.md`

---

### Review Notes

This CIR was recorded retroactively to preserve traceability
between the convention's version history and its improvement
register. The `standards` scope itself was already implemented in
convention v1.2 (2026-08-28) prior to this entry being written.


## CIR-003 — Add Security Scope to Git Commit Convention

### Identification

**ID:** CIR-003

**Category:** Engineering Practice / Version Control

**Status:** Implemented

**Priority:** Low

**Risk:** Low

**Size / Resources:** Small

**Timescale:** Short

**Action Owner:** Repository Owner

---

### Description

Add a `security` scope to the Git commit convention to support
commits related to threat modeling, access control, secrets
management, and infrastructure hardening.

---

### Reason / Rationale

The repository now includes security-focused projects (e.g.
`secure-field-data-pipeline`) where significant engineering
decisions are security-specific: threat modeling, network exposure
design, least-privilege access control, and secrets management.

These changes did not fit cleanly under existing scopes and were
previously at risk of being generically classified under `docs` or
`repo`, reducing traceability of security engineering work
specifically — which is a core focus area of this portfolio.

---

### Expected Benefits

- Clear traceability of security-specific engineering decisions.
- Easier filtering of security-related commit history for
  portfolio review.
- Consistent scope taxonomy as security-focused projects grow.

---

### Related Metrics / Indicators

- Consistent use of the `security` scope across relevant commits
  in `secure-field-data-pipeline` and future security projects.

---

### Supporting Documents

- `docs/standards/git-commit-convention.md`

---

### Review Notes

None yet.


## Document Version History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | 2026-07-20 | Repository Owner | Initial CIR created and CIR-001 added |
| 1.1 | 2026-09-17 | Repository Owner | Add CIR-002 (retroactive) for `standards` scope; add CIR-003 for `security` scope |
---

## Approvals

Not applicable at this stage.

This register is maintained as part of an individual engineering
portfolio and learning environment.

---

## Document Distribution

Repository-level internal documentation.

Location:

`docs/continual-improvement/continual-improvement-register.md`

*WIP: Work in Progress
