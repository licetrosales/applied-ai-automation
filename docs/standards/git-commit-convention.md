# Git Commit Convention

## Purpose

This document defines the Git commit convention used across the
`applied-ai-automation` repository.

The convention is designed for projects involving:

- AI automation,
- low-code / no-code platforms,
- Make.com,
- n8n,
- API integrations,
- AI prompts and LLMs,
- Agile sprint-based development,
- technical documentation.

The goal is to create a Git history that clearly communicates
what changed, where it changed, and why the change matters.

---

## Commit Message Structure

Use the following format:

`type(scope): description`

Example:

`feat(make): configure Gmail watch emails trigger`

The scope is optional when it does not add useful context.

Example:

`docs: update repository README`

---

## Commit Types

### `feat` — New functionality

Use when adding new behavior or capability.

This includes low-code implementation.

Examples:

`feat(make): configure Gmail watch emails trigger`

`feat(email): add sender filtering`

`feat(ai): add newsletter classification prompt`

`feat(storage): store classification results in Google Sheets`

A Make.com configuration can therefore be a `feat` even when no
traditional source code was written.

---

### `fix` — Bug or workflow correction

Use when correcting behavior that does not work as intended.

Examples:

`fix(make): correct Gmail filter configuration`

`fix(ai): handle invalid classification response`

`fix(storage): correct Google Sheets field mapping`

---

### `docs` — Documentation-only changes

Use when the change affects documentation but does not change
system behavior.

Examples:

`docs(sprint-01): document successful Gmail trigger test`

`docs(architecture): update email ingestion flow`

`docs(repo): add Git commit convention`

Important:

Do not use `docs` simply because a low-code change is represented
in the repository through screenshots or Markdown.

Classify the commit according to the engineering change itself.

For example, configuring a new Make.com trigger is:

`feat(make): configure Gmail watch emails trigger`

not:

`docs: add Gmail trigger screenshot`

The screenshot is evidence of the feature, not the feature itself.

---

### `test` — Testing and validation

Use when adding or updating tests, test plans, validation procedures,
or test evidence.

Examples:

`test(email): validate Gmail trigger with forwarded newsletter`

`test(ai): validate classification JSON schema`

`test(make): document workflow execution test`

---

### `refactor` — Internal restructuring

Use when restructuring an implementation without intentionally
changing its external behavior.

Examples:

`refactor(make): simplify newsletter processing flow`

`refactor(ai): reorganize classification prompt structure`

---

### `perf` — Performance improvement

Use when improving efficiency, execution time, resource consumption,
or operational performance.

Examples:

`perf(make): reduce unnecessary workflow operations`

`perf(ai): reduce classification prompt token usage`

---

### `chore` — Repository or maintenance work

Use for maintenance that does not represent a feature, fix,
test, or meaningful documentation change.

Examples:

`chore(repo): reorganize project directories`

`chore(deps): update development dependencies`

Use this category sparingly.

---

## Recommended Scopes

Scopes identify the area affected by the change.

### Technology / Component Scopes

`make`
: Make.com scenario or module configuration.

`n8n`
: n8n workflow configuration.

`email`
: Email ingestion, filtering, parsing, or processing.

`ai`
: AI models, prompts, classification, or LLM behavior.

`storage`
: Google Sheets, databases, or persistence.

`digest`
: Digest generation and output.

`monitoring`
: Monitoring, logging, alerts, and observability.

---

### Engineering / Repository Scopes

`architecture`
: Architecture documentation or structural decisions.

`repo`
: Repository-level organization or configuration.

`testing`
: Cross-project testing infrastructure or standards.

`docs`
: General documentation when a more specific scope is not useful.

`standards` 
: Repository-wide conventions and standards (e.g. commit convention, coding standards).

---

### Sprint Scopes

Sprint identifiers may be used when the change is specifically
about sprint documentation.

Examples:

`sprint-00`

`sprint-01`

`sprint-02`

Example:

`docs(sprint-01): complete email ingestion progress notes`

Do not use the sprint as the scope automatically for every commit
made during that sprint.

Prefer the technical scope when it better describes the change.

For example:

`feat(email): add sender filtering`

is clearer than:

`feat(sprint-02): add sender filtering`

---

## Low-Code Classification Rule

Low-code does not mean "documentation only."

Classify a commit according to the engineering change represented
by the commit, not according to the file type stored in Git.

For example:

A Make.com scenario is configured with a new Gmail trigger.

The repository may contain:

- a screenshot,
- updated sprint notes,
- an exported blueprint.

The primary engineering change is still a feature.

Use:

`feat(make): configure Gmail watch emails trigger`

If a later commit only improves the explanation of that already
implemented trigger, use:

`docs(sprint-01): document Gmail trigger configuration`

---

## Commit Granularity

Follow this principle:

**One commit = one coherent engineering change.**

Avoid creating a separate commit for every small file when several
files describe the same logical change.

For example, suppose one task produces:

- a Make.com configuration screenshot,
- an exported blueprint,
- updated sprint documentation.

If all three represent one completed engineering change, they can
usually be committed together.

Example:

`feat(make): configure Gmail watch emails trigger`

---

## When to Separate Commits

Create separate commits when changes represent different logical
purposes.

Example:

1. Implement the feature:

`feat(email): add sender filtering`

2. Add independent testing:

`test(email): validate sender filtering`

3. Later improve documentation:

`docs(sprint-02): document email filtering results`

This makes Git history easier to understand without creating
unnecessary commits.

---

## Commit Message Style

Commit descriptions should:

- use lowercase after the colon,
- use the imperative style where practical,
- describe one coherent change,
- be concise but specific,
- avoid unnecessary punctuation at the end.

Prefer:

`feat(ai): add newsletter classification prompt`

Avoid:

`feat: changes`

Avoid:

`updated files`

Avoid:

`work on project`

Avoid:

`docs: screenshot added`

The commit message should help someone understand the project
history without opening every changed file.

---

## Verb Glossary

The `type(scope):` prefix identifies the *category* of change.
The verb that follows identifies *what was done*. Keep verbs
consistent so similar changes always read the same way in history.

### Creating something new

`add`
: New file, section, doc, module, or prompt.

`create`
: A new structure or artifact built from scratch (folder, register, template).

`configure`
: Setting up an existing tool or service for the first time.

`implement`
: A more substantial new capability, often multi-step.

### Changing something existing

`update`
: General revision to existing content. Default choice when nothing more specific fits.

`modify`
: A targeted adjustment to existing configuration or logic.

`revise`
: Wording or structure of documentation specifically.

`rename`
: A file, field, or variable renamed.

`extend`
: Adding capability onto something that already exists.

Avoid `change` — it is always vaguer than `update` or `modify`.
Use one of those instead.

### Removing something

`remove`
: Deliberate, permanent removal of a file, step, config, or content.

Use `remove` consistently rather than alternating with `delete`,
to keep history predictable.

### Fixing

Name the correction itself: `correct`, `resolve`, `handle`.

Example: `fix(ai): handle invalid classification response`

### Documentation-specific

`document`
: Adding coverage for something that already exists but wasn't written up.

`clarify`
: Improving unclear existing text. Note: clarifying wording is a
documentation change, not a fix — use `docs`, not `fix`, even when
the change resolves confusion.


---

## Decision Guide

Ask:

**Did I add new system behavior?**

Use `feat`.

**Did I correct broken or incorrect behavior?**

Use `fix`.

**Did I only change documentation?**

Use `docs`.

**Did I validate or test behavior?**

Use `test`.

**Did I restructure something without changing intended behavior?**

Use `refactor`.

**Did I improve performance or resource usage?**

Use `perf`.

**Is this repository maintenance that fits none of the above?**

Use `chore`.

---

## Examples from AI Automation Projects

`feat(make): configure Gmail watch emails trigger`

`test(email): verify forwarded newsletter ingestion`

`feat(email): filter supported newsletter senders`

`feat(email): extract newsletter text body`

`feat(ai): add cybersecurity newsletter classification prompt`

`test(ai): validate structured classification output`

`feat(storage): store classification results in Google Sheets`

`feat(digest): generate weekly newsletter digest`

`feat(monitoring): add workflow failure notification`

`refactor(n8n): migrate newsletter processing workflow`

`perf(ai): optimize local LLM prompt size`

`docs(architecture): document local LLM integration`

---

## Relationship to Continual Improvement

This standard was introduced through:

`CIR-001 — Standardize Git Commit Conventions`

The associated Continual Improvement Register is located at:

`docs/continual-improvement/continual-improvement-register.md`

Lessons learned from applying this convention should be reviewed
periodically.

Significant improvements to the convention may be recorded as new
CIR entries.

---

## Version History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-07-20 | Initial Git commit convention established |
| 1.1 | 2026-08-28 | Add standardized verb glossary for commit descriptions |
| 1.2 | 2026-08-28 | Add missing `standards` scope to Engineering/Repository Scopes |
