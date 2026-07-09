# System Architecture

## Overview

web.de
   │
Forward
   │
   ▼
Gmail
   │
   ▼
Make.com
   │
   ▼
DeepSeek
   │
   ▼
Google Sheets
   │
   ▼
Digest


---

## Components

### Email Source

Technical newsletters are forwarded from web.de to Gmail.

### Workflow Engine

Make.com orchestrates the complete workflow.

### AI Layer

DeepSeek extracts structured information, classifies articles, and generates summaries.

### Data Layer

Google Sheets stores structured results and processing history.

### Output

A personalized digest is generated from relevant articles.
