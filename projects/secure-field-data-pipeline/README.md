# Secure Field Data Pipeline

Offline-first field data collection pipeline with security-by-design, built for a small construction company's weekly site reporting workflow.

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![KoboToolbox](https://img.shields.io/badge/KoboToolbox-Data%20Collection-blue)
![n8n](https://img.shields.io/badge/n8n-Automation-orange)
![Security](https://img.shields.io/badge/Design-Security%20First-red)

---

## Problem

Field engineers at construction sites often have no reliable internet access, yet need to submit structured weekly progress reports (worker counts, task status, photos) that are consumed downstream as Excel spreadsheets. The existing process relies on manual data entry once engineers return to an office with connectivity — slow, error-prone, and not designed with any explicit security considerations.

## Solution

An offline-first data capture pipeline: field staff fill out a structured form (including photos) on Android devices with **zero connectivity required**, data syncs automatically once a connection is available, and a scheduled automation job transforms and writes the results into the existing Excel-based reporting format — without introducing any new public attack surface.

## Key design decision: no public attack surface

Rather than using a webhook (which would require the automation layer to expose a public, internet-reachable endpoint), this pipeline uses **outbound polling**: the automation layer queries the data collection API on a schedule instead of waiting to be called. Given the workflow tolerates latency in the order of minutes, this eliminates an entire class of attack surface — no open ports, no public endpoint to patch or rate-limit — at zero functional cost.

See [`docs/threat-model.md`](docs/threat-model.md) for the full analysis.

## Architecture

```
Android device (offline) → KoboCollect → KoboToolbox (cloud)
        → [scheduled polling] → n8n → internal file share → Excel report
```

Full diagram and trust boundaries: [`docs/architecture.md`](docs/architecture.md)

## Documentation

| Document | Contents |
|---|---|
| [`docs/architecture.md`](docs/architecture.md) | Data flow diagram, trust boundaries |
| [`docs/threat-model.md`](docs/threat-model.md) | STRIDE-lite threat analysis and mitigations |
| [`docs/agile-process.md`](docs/agile-process.md) | Kanban backlog, epics, user stories |

## Stack

- **KoboToolbox / KoboCollect** — offline-first structured data capture with photo support
- **n8n** — scheduled polling and data transformation, self-hosted via Docker
- **Docker** — containerized deployment on a resource-constrained on-premise server

## Status

🚧 In progress — see [`docs/agile-process.md`](docs/agile-process.md) for current backlog state.

## Note on data

All data, screenshots, and identifiers in this repository are anonymized and generalized. No real client, employee, or infrastructure information is included.