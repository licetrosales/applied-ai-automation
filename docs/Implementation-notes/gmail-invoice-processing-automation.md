# Gmail Invoice Processing Automation

## Overview

This workflow automates the extraction of key invoice information from PDF attachments received via Gmail.

It combines PDF text extraction, AI-powered data processing, and Google Sheets integration to transform unstructured invoice documents into structured records.

The workflow also includes duplicate detection to prevent the same invoice email from being processed multiple times.

## Workflow Architecture
![alt text](../figures/gmail-invoice-processing-workflow.png)
**Figure 1:** Workflow that retrieves invoice PDFs from Gmail, extracts invoice data using DeepSeek, and stores the results in Google Sheets.

## Workflow Components

### Gmail Trigger

Monitors incoming emails and retrieves PDF invoice attachments.

### Google Sheets Lookup

Checks whether the email Message ID already exists in the invoice database.

### IF Node

Determines whether the email has been processed previously.

- Existing Message ID → workflow stops
- New Message ID → processing continues

### Read/Write Files from Disk

Stores the PDF attachment locally for text extraction.

### Execute Command (Poppler)

Uses the Poppler utility to extract raw text from the PDF document.

### Basic LLM Chain

Sends the extracted invoice text to the language model and requests structured data extraction.

### DeepSeek Chat Model

Identifies and extracts key invoice fields:

- Supplier name
- Order date
- Order number
- Supplier email
- Total amount
- Currency

### JavaScript Processing

Parses and validates the JSON response returned by the model.

### Google Sheets Append Row

Stores the extracted invoice data together with the email Message ID.

## Data Flow

1. Gmail receives an email containing a PDF invoice.
2. The workflow retrieves the email Message ID.
3. Google Sheets is queried for an existing record with the same Message ID.
4. If the invoice was already processed, the workflow stops.
5. If no record exists, the PDF is written to disk.
6. Poppler extracts the invoice text.
7. DeepSeek analyzes the text and extracts structured invoice data.
8. JavaScript parses the model response.
9. The extracted data and Message ID are stored in Google Sheets.

## Key Concepts Learned

- Gmail automation
- Google Sheets integration
- Duplicate detection using Message IDs
- PDF text extraction with Poppler
- LLM-based information extraction
- JSON data processing
- Workflow orchestration with n8n

## Outcome

The workflow successfully:

- Processes invoice PDFs automatically
- Extracts structured business data from unstructured documents
- Prevents duplicate processing
- Stores invoice information in a searchable spreadsheet
- Reduces manual data entry effort

## Next Steps

- Support multiple invoice formats and languages
- Add invoice status tracking
- Generate notifications for failed extractions
