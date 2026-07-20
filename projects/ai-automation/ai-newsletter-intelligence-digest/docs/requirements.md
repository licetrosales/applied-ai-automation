# Requirements

## Functional Requirements

### FR-001 Email Ingestion
The system shall monitor a dedicated Gmail inbox for forwarded technical newsletters.

### FR-002 Sender Filtering
The system shall process only newsletters from supported or explicitly configured senders.

### FR-003 Content Extraction
The system shall extract the subject, sender, publication date, and newsletter content.

### FR-004 AI Classification
The system shall classify newsletter articles into predefined technical categories.

### FR-005 Relevance Scoring
The system shall assign a relevance score to each article.

### FR-006 Summarization
The system shall generate concise summaries of relevant articles.

### FR-007 Data Storage
The system shall store structured results in Google Sheets.

### FR-008 Digest Generation
The system shall generate a personalized digest containing only relevant articles.

---

## Non-Functional Requirements

- Modular workflow design
- Extensible architecture
- Human-readable documentation
- Repeatable testing
- Reliable error handling
- Maintainable prompts
- Clear separation of responsibilities
