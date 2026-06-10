# Poppler Installation (macOS)

## Goal

Install Poppler on macOS to enable local PDF text extraction for AI and automation workflows.

## Tools Used

* macOS
* Homebrew
* Poppler
* pdftotext

## Prerequisites

Verify Homebrew is installed:

```bash
brew --version
```

If Homebrew is not available, install it before proceeding.

## Installation

### Install Poppler

Run:

```bash
brew install poppler
```

Homebrew downloads and installs Poppler along with the required dependencies.

### Verify Installation

Check that the PDF-to-text utility is available:

```bash
pdftotext -v
```

Expected result:

```text
pdftotext version <version>
```

Optionally verify the executable location:

```bash
which pdftotext
```

Expected result:

```text
/opt/homebrew/bin/pdftotext
```

## Verification

### Test PDF Text Extraction

Convert a PDF file to text:

```bash
pdftotext sample.pdf
```

Expected result:

```text
sample.txt
```

A text file containing the extracted PDF content is created in the same directory.

## Usage

Poppler provides utilities for processing PDF documents locally.

Common use case:

```text
PDF Document
      ↓
   pdftotext
      ↓
 Plain Text
      ↓
 AI / Automation Workflow
```

This approach enables document processing without relying on external OCR or cloud-based extraction services.

## Architecture

```text
PDF Document
      ↓
   Poppler
      ↓
   pdftotext
      ↓
 Plain Text
      ↓
 n8n Workflow
```

## Key Learnings

* Poppler provides local PDF processing utilities.
* The `pdftotext` tool extracts text directly from PDF files.
* Local document processing can be integrated into AI workflows.
* Homebrew simplifies dependency management on macOS.
* Poppler is commonly used as a preprocessing step before LLM-based document analysis.
