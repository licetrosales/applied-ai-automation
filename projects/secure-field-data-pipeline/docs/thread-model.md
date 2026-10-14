# Threat Model (STRIDE-lite)

## Assets

- Field report data (project progress, worker counts, incident flags)
- Site photos (may contain identifiable individuals — treated as personal data)
- API tokens / credentials for the data collection and automation layers
- Internal file server contents

## Threats and mitigations

| Threat category | Scenario | Mitigation |
|---|---|---|
| **Spoofing** | Unauthorized device submits fake reports | Form access restricted per-user credential, not anonymous submission |
| **Tampering** | Data altered in transit between data collection and automation layers | HTTPS/TLS enforced on all API calls |
| **Repudiation** | No record of who submitted or synced what, when | Sync log maintained (timestamp, submission ID, form version) |
| **Information Disclosure** | API tokens leaked in source control | Secrets kept in `.env`, excluded via `.gitignore`; `.env.example` with placeholders only committed |
| **Information Disclosure** | Public endpoint reachable without auth | Avoided at the design level: outbound polling instead of an inbound webhook — no public listening endpoint exists to attack in the first place |
| **Denial of Service** | Automation workflow overloaded or file share locked during writes | Sequential write queue, bounded polling interval |
| **Elevation of Privilege** | Automation service account has broader file-share permissions than needed | Service account scoped to write access on the specific reports folder only (least privilege) |

## Data classification

| Field / data type | Classification | Handling |
|---|---|---|
| Project name, dates, worker counts | Internal | Standard access controls |
| Progress descriptions, observations | Internal | Standard access controls |
| Site photos | Sensitive (may contain identifiable individuals) | Access limited to project team; not published externally |
| API tokens, credentials | Confidential | Never committed to source control; stored in secrets manager / environment variables |

## Out of scope (for this iteration)

- Physical security of field devices
- Malware protection on end-user Android devices
- Formal incident response plan (tracked separately in operational documentation, not in this public repository)