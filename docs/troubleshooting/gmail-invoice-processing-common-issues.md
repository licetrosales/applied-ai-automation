# Gmail Invoice Processing - Common Issues

## Duplicate Check Returns No Output

### Problem

```text
Google Sheets Get Row(s) returned no output data.
Workflow stopped unexpectedly.
```

### Cause

The workflow searched for a Message ID that did not yet exist in the spreadsheet.

When no matching row is found, the Google Sheets node returns no items, which can stop workflow execution.

### Resolution

Enable:

```text
Settings
→ Always Output Data
```

This allows the workflow to continue even when no matching row exists.

### Verification

The Google Sheets node completes successfully and forwards an item to the next node.

---

## IF Node Does Not Route Items Correctly

### Problem

The workflow always follows the wrong branch after checking for duplicates.

### Cause

The IF node is evaluating a field that does not exist or uses an incorrect condition.

### Resolution

Evaluate the Message ID field:

```javascript
{{ $json["Message ID"] }}
```

Configure the condition:

```text
String
→ Exists
```

Interpretation:

```text
TRUE  = invoice already processed
FALSE = new invoice
```

### Verification

Previously processed invoices follow the TRUE branch.

New invoices follow the FALSE branch.

---

## Binary Attachment Not Found

### Problem

```text
This operation expects the node's input data to contain a binary file 'attachment_0', but none was found.
```

### Cause

The binary PDF attachment was no longer available in the current workflow item.

Some nodes only forward JSON data and do not preserve binary content.

### Resolution

Reference the original Gmail Trigger binary data directly:

```javascript
$('Gmail Trigger').item.binary.attachment_0
```

Use the Gmail Trigger as the source for binary attachment metadata when configuring file operations.

### Verification

The PDF file is successfully written to disk.

---

## Message ID Not Stored in Spreadsheet

### Problem

The same invoice can be processed more than once.

### Cause

The workflow checks for duplicates using Gmail Message IDs but does not store the Message ID after processing.

Without persistence, future executions cannot identify previously processed emails.

### Resolution

Add a dedicated spreadsheet column:

```text
Message ID
```

Store the Gmail Message ID:

```javascript
{{ $('Gmail Trigger').item.json.id }}
```

when appending invoice data.

### Verification

Each processed invoice contains a Message ID value in the spreadsheet.

Duplicate invoices are skipped during future executions.

---

## Lessons Learned

- Email Message IDs provide a reliable mechanism for duplicate detection.
- Google Sheets can serve as a lightweight persistence layer for workflow state.
- Binary and JSON data are handled differently within n8n workflows.
- Workflow branching becomes more reliable when duplicate detection is implemented early in the process.
- Small persistence improvements can significantly increase automation reliability.
