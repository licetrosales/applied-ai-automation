# ADR-003 — Technology Stack

**Status:** Accepted

---

# Context

The project requires an automation platform, an LLM, structured storage, and version control while remaining simple to implement and extend.

---

# Decision

Version 1 will use:

| Component | Technology |
|-----------|------------|
| Workflow Automation | Make.com |
| Email | Gmail |
| AI | DeepSeek |
| Data Storage | Google Sheets |
| Version Control | Git & GitHub |
| Documentation | Markdown |

---

# Rationale

The selected technologies provide:

- Low implementation effort
- Rapid prototyping
- Strong integration capabilities
- Modular architecture
- Easy migration to n8n in future versions

---

## Alternatives Considered

**n8n (self-hosted)** — Rejected for V1: requires hosting/maintenance overhead 
before the workflow logic itself was validated. Revisit in Sprint 8 once 
core logic is proven.

**OpenAI / Claude API** — Rejected for V1: DeepSeek offers comparable 
classification quality at lower cost for high-volume prototyping; 
revisit if classification accuracy proves insufficient.

**Airtable / PostgreSQL (storage)** — Rejected for V1: Google Sheets 
requires no setup and is sufficient for low-volume structured data 
during prototyping.

---

# Future Considerations

Potential future technologies include:

- n8n
- PostgreSQL
- Ollama
- ChromaDB
- Python
- FastAPI
