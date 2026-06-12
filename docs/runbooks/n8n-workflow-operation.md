# n8n Workflow Operations Runbook

## Purpose

This runbook documents the operational procedures for developing, testing, troubleshooting, and maintaining n8n workflows.

The procedures apply to all workflows in this repository.

---

## Prerequisites

Verify the following before working with workflows:

- n8n is installed and running
- Required credentials are configured
- External APIs are reachable
- Environment variables are configured where required

---

## Procedure: Start n8n

Start n8n locally:

```bash
n8n start
```

Default URL:

```text
http://localhost:5678
```

### Verification

- n8n editor loads successfully
- No startup errors appear in the terminal

---

## Procedure: Import a Workflow

1. Open the n8n editor.
2. Select **Import from File**.
3. Choose the workflow JSON file.
4. Verify all nodes are imported.
5. Reconnect credentials if required.

### Verification

- Workflow loads without errors
- All nodes display correctly
- Credentials are connected

---

## Procedure: Configure Credentials

### Gmail

Verify:

- OAuth authentication is valid
- Correct Google account is connected
- Required permissions are granted

### HTTP APIs

Verify:

- Endpoint URLs are correct
- Authentication tokens are valid
- API services are reachable

### AI Models

Verify:

- API keys are configured
- Model names are valid
- Usage quotas are available

---

## Procedure: Test a Workflow

### Execute Entire Workflow

1. Open the workflow.
2. Select **Execute Workflow**.
3. Monitor node execution.
4. Review outputs.

### Execute Individual Nodes

1. Open the node.
2. Select **Execute Step**.
3. Review inputs and outputs.
4. Validate returned data.

### Verification

- Workflow completes successfully
- Expected outputs are generated
- No node errors occur

---

## Procedure: Review Execution Data

### Input Validation

Verify:

- Required fields exist
- Data types are correct
- Values are populated

### Output Validation

Verify:

- Results match expectations
- No unexpected null values exist
- Required downstream fields are available

---

# Troubleshooting

## Workflow Node Failed

### Problem

A node returns an execution error.

### Cause

Common causes:

- Invalid credentials
- Incorrect expressions
- Missing input data
- API connectivity issues

### Resolution

Review:

- Error message
- Input payload
- Node configuration
- Credential settings

### Verification

Node executes successfully after correction.

---

## Workflow Stops Unexpectedly

### Problem

Execution terminates before workflow completion.

### Cause

Common causes:

- Missing fields
- Expression errors
- Conditional logic failures
- Invalid data mappings

### Resolution

Review:

- Execution order
- Expressions
- Conditions
- Input data

### Verification

Workflow reaches the final node successfully.

---

## External Service Error

### Problem

API or external service request fails.

### Cause

Common causes:

- Authentication failure
- Incorrect endpoint
- Invalid request format
- Service outage

### Resolution

Verify:

- Authentication configuration
- Request URL
- Request payload
- Service availability

### Verification

Request returns a successful response.

---

## AI Agent Tool Issues

### Problem

Agent does not use tools correctly.

### Cause

Common causes:

- Unclear tool descriptions
- Ambiguous prompts
- Unexpected tool output
- Missing validation instructions

### Resolution

Verify:

- Tool configuration
- Tool descriptions
- Agent prompt
- Tool outputs

Review execution logs to confirm:

- Tool selection
- Tool inputs
- Tool outputs
- Final response

### Verification

Agent selects the expected tool and produces the intended result.

---

## Monitoring

Review the **Executions** view regularly.

Verify:

- Successful executions
- Failed executions
- Execution duration
- Input/output data
- Error messages

---

## Export Procedure

Before committing workflow changes:

1. Save the workflow.
2. Export workflow JSON.
3. Update documentation.
4. Commit workflow and documentation changes.

### Verification

- Workflow JSON is current
- Documentation reflects latest implementation

---

## Documentation Standards

Each workflow should include:

### Implementation Note

Documents:

- Purpose
- Architecture
- Components
- Design decisions
- Lessons learned

### Troubleshooting Note

Documents:

- Problem
- Cause
- Resolution
- Verification

### Figures

Store workflow screenshots and diagrams in:

```text
docs/figures/
```

---

## Pre-Publish Checklist

- [ ] Workflow executes successfully
- [ ] Credentials are configured
- [ ] Secrets are excluded from Git
- [ ] Error handling is tested
- [ ] Documentation is updated
- [ ] Screenshots are captured
- [ ] Workflow JSON is exported
- [ ] Repository changes are committed

---

## Key Takeaways

- Test nodes individually before testing complete workflows.
- Validate credentials early during troubleshooting.
- Use execution logs as the primary debugging source.
- Keep documentation synchronized with workflow changes.
- Validate AI Agent decisions through execution logs and tool outputs.
- Treat AI workflows as systems that require verification and monitoring.
