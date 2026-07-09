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

# Future Considerations

Potential future technologies include:

- n8n
- PostgreSQL
- Ollama
- ChromaDB
- Python
- FastAPI
