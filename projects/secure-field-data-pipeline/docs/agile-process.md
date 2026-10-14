# Agile Process

Solo-developer project managed as a Kanban board (GitHub Projects) rather than Scrum, since sprint ceremonies add no value for single-contributor work. Board columns: `Backlog → To Do → In Progress → Testing → Done`.

## Epic 0: Security Foundations
*Completed before any implementation work began.*

- [x] Define data classification for each field in the report form
- [x] Draw and document the data flow diagram with trust boundaries
- [x] Define secrets management approach (`.env` strategy)
- [x] Decide network exposure model for the automation layer (polling vs. webhook)

## Epic 1: Field Data Capture Form

- [ ] As a site engineer, I want to fill out the weekly report fully offline, so that lack of site connectivity doesn't block reporting
- [ ] As a site engineer, I want to attach photos directly from the camera, so that progress is documented visually
- [ ] As a systems administrator, I want the form to enforce required fields, so incomplete reports are prevented at the source

## Epic 2: Secure Sync & Automation

- [ ] As a systems administrator, I want submissions to sync automatically to Excel once connectivity is available, so manual transcription is eliminated
- [ ] As a systems administrator, I want the automation-to-file-server connection restricted to the internal network, so the pipeline doesn't introduce a new external attack surface
- [ ] As a systems administrator, I want every successful sync logged with a timestamp and submission ID, so there's an audit trail for each report

## Epic 3: Documentation & Portfolio Presentation

- [x] Document the threat model and architecture so reviewers can evaluate design reasoning, not just the end result
- [x] Anonymize all data and identifiers throughout the repository

## Definition of Done (per story)

- Implementation matches the documented architecture
- No secrets or credentials present in committed files
- Relevant documentation updated (architecture, threat model, or this backlog)