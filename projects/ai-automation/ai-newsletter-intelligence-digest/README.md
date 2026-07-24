# AI Newsletter Intelligence Digest

An AI-powered automation system that transforms technical newsletters into structured, searchable intelligence.

The project demonstrates how workflow automation, large language models (LLMs), and structured information extraction can be combined to reduce information overload and improve the discovery of professionally relevant technical content.

---

## Objectives

- Automate the collection of technical newsletters.
- Extract structured information using AI.
- Classify articles into predefined technical domains.
- Generate concise, personalized intelligence digests.
- Build a searchable knowledge base of relevant technical insights.

---

## High-Level Workflow

WEB.DE
  ↓
Automated newsletter forwarding
  ↓
Gmail
  ↓
Make.com
  ↓
Email filtering and content extraction
  ↓
AI classification
  ↓
Structured data storage
  ↓
Personalized intelligence digest

---

## Engineering Highlights

- Workflow automation with Make.com
- Large Language Model (LLM) integration
- Prompt engineering
- Structured information extraction
- API integration
- Modular workflow design
- Agile project management
- Architecture Decision Records (ADRs)
- Test planning and validation
- Technical documentation and version control

---

## Technology Stack

- **Workflow Automation:** Make.com
- **AI:** DeepSeek API (LLM)
- **Email:** Gmail
- **Data Storage:** Google Sheets
- **Documentation:** Markdown
- **Version Control:** Git & GitHub
- **Future Platform:** n8n, Docker, Raspberry Pi 5

---

## Repository Structure

The repository follows an engineering-oriented project structure.

| Directory | Purpose |
|-----------|---------|
| `docs/` | Architecture, requirements, ADRs, roadmap, glossary, workflow documentation |
| `make/` | Make.com blueprints and workflow screenshots |
| `prompts/` | LLM prompts used for classification and summarization |
| `sprints/` | Sprint planning, reviews, and retrospectives |
| `testing/` | Test plan and validation scenarios |

---

## Development Process

The project is developed iteratively following Agile principles.

Each sprint delivers a working increment and includes:

- Sprint planning
- Implementation
- Testing
- Sprint review
- Retrospective
- Version-controlled documentation

---

## Project Status

**Current Sprint:** Sprint 1 – Email Ingestion

Current objectives:

- Configure Gmail trigger
- Filter supported newsletters
- Extract newsletter content
- Integrate DeepSeek classification
- Store structured results in Google Sheets

---

## Planned Roadmap

| Sprint | Goal | Status |
|---|---|---|
| Sprint 0 | Project Initiation | ✅ Completed |
| Sprint 1 | Email Ingestion | ✅ Completed |
| Sprint 2 | Email Processing | 🚧 Next |
| Sprint 3 | AI Classification | Planned |
| Sprint 4 | Data Storage | Planned |
| Sprint 5 | Digest Generation | Planned |
| Sprint 6 | Monitoring & Testing | Planned |
| Sprint 7 | Version 1.0 | Planned |
| Sprint 8 | n8n Migration | Future |
| Sprint 9 | Local LLM Support | Future |

---

## Future Enhancements

- n8n implementation
- Local LLM support
- Vector search
- Threat intelligence feeds
- Retrieval-Augmented Generation (RAG)
- Interactive dashboard
- Multi-source aggregation

---

## Project Documentation

Project documentation is organized within the `docs/` directory and includes:

- Vision
- Requirements
- Architecture
- Product Backlog
- Architecture Decision Records (ADRs)
- Roadmap
- Sprint documentation
- Workflow design
- Testing strategy
