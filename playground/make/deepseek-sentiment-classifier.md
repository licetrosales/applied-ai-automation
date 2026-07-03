# DeepSeek Sentiment Classifier (Make.com)

## Overview

This playground experiment demonstrates how to integrate the **DeepSeek AI** module into a **Make.com** workflow to perform sentiment analysis using an LLM.

The objective was to understand how AI modules can be invoked from automation workflows and how structured responses can be used by downstream modules.

---

## Technologies

- Make.com
- DeepSeek AI API
- DeepSeek V4 Flash
- Prompt Engineering
- JSON Output

---

## Workflow

```
User Prompt
      │
      ▼
DeepSeek Chat Completion
      │
      ▼
JSON Response
```

---

## Configuration

- **Platform:** Make.com
- **Module:** DeepSeek AI – Create a Chat Completion
- **Model:** deepseek-v4-flash
- **Prompting:** System and User messages
- **Output:** Structured JSON for downstream workflow processing

---
## Prompt Design

The model was instructed to:

- classify a movie review as **Positive**, **Negative**, or **Neutral**
- return **only valid JSON**
- avoid Markdown or additional text

Example input:

```
I am not impressed. I was hoping for something enjoyable, really.
```

Example output:

```json
{
  "sentiment": "Negative",
  "explanation": "The reviewer expresses disappointment and a lack of enjoyment, indicating a negative sentiment."
}
```

---

## Result

This experiment successfully validated:

- DeepSeek API integration with Make.com
- Prompt execution using System and User messages
- Structured JSON responses suitable for workflow automation

---

## Next Steps

This pattern can be extended to automate:

- Email classification
- Customer feedback analysis
- Support ticket routing
- Document processing
- Security alert triage