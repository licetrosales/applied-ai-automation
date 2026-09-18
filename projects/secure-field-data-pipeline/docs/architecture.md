# Architecture

## Data flow

```
[Android device, offline]
     |  (1) Local form fill + photo capture — no network required
     v
[KoboCollect app — local storage]
     |  (2) Sync over HTTPS when connectivity available
     v
[KoboToolbox server (cloud-hosted)]
     |  (3) Scheduled outbound polling (n8n → Kobo API, e.g. every 30 min)
     v
[n8n workflow engine — self-hosted via Docker]
     |  (4) Write to file share (SMB) — internal network only
     v
[Excel file on internal file server]
     |  (5) Accessed by supervisors via existing SMB share
     v
[Reviewed by site supervision engineer]
```

## Trust boundaries

| Boundary | Between | Notes |
|---|---|---|
| TB-1 | Field device ↔ Kobo server | Crosses public internet — HTTPS required. Field workers (temporary staff) never receive VPN/network access — their only touchpoint is the public Kobo form, with no visibility into internal infrastructure |
| TB-2 | Kobo server ↔ n8n | **Outbound polling only** (n8n queries the Kobo API on a schedule) instead of an inbound webhook — see design rationale below |
| TB-3 | n8n ↔ file server | Stays inside the private network — n8n runs on/near the internal server and writes to the SMB share without crossing the public internet |
| TB-4 | File server ↔ end users | Existing internal SMB share, access scoped by OS-level auth and NTFS permissions |

## Design decision: webhook vs. polling

An inbound webhook model (Kobo calling n8n directly when a submission arrives) was considered and rejected in favor of scheduled polling.

**Rationale:** the reporting workflow tolerates latency in the order of tens of minutes — a weekly report syncing 30 minutes late has no practical impact. The marginal benefit of near-instant delivery did not justify introducing a publicly reachable endpoint that would require ongoing patching, TLS certificate management, and rate-limiting. Polling keeps the automation layer entirely closed to inbound internet traffic, reducing the system's attack surface without any functional trade-off for this use case.

## Deployment environment

- Single on-premise server (Windows), resource-constrained, no dedicated IT budget
- n8n deployed via Docker to keep footprint minimal and the setup reproducible
- Remote administration over WireGuard (site-to-site style tunnel for the system administrator only — never extended to field staff or the data collection layer)
