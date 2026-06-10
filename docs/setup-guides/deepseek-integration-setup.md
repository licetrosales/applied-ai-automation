# DeepSeek Integration (n8n)

## Goal

Configure DeepSeek as an AI model provider in n8n to enable LLM-powered workflows using the DeepSeek API.

## Tools Used

* n8n Community Edition
* DeepSeek Platform
* DeepSeek API
* Basic LLM Chain
* Chat Trigger

## Prerequisites

Verify n8n is running locally:

```bash
n8n
```

Open:

```text
http://localhost:5678
```

Create a DeepSeek Platform account.

## Configuration

### Create DeepSeek Account

Register an account on the DeepSeek Platform.

Verify account access and complete the registration process.

### Generate API Key

Navigate to:

```text
API Keys
```

Create a new API key and securely store it.

### Add API Credit

DeepSeek API usage requires a positive account balance.

Add API credit through:

```text
Top Up
```

### Configure DeepSeek Credential

Create a new credential in n8n:

```text
DeepSeek
```

Provide:

```text
API Key
```

Save the credential and verify the connection.

Expected result:

```text
Connection tested successfully
```

## Verification

### Create Chat Workflow

Create the following workflow:

```text
When Chat Message Received
          ↓
      Basic LLM Chain
          ↓
   DeepSeek Chat Model
```

Configure:

```text
Model: deepseek-v4-flash
```

### Test Workflow

Open the chat interface and submit:

```text
Hello
```

Expected result:

```text
AI-generated response returned successfully
```

## Architecture

```text
When Chat Message Received
          ↓
      Basic LLM Chain
          ↓
   DeepSeek Chat Model
```

## Key Learnings

* DeepSeek can be integrated into n8n using API-based authentication.
* API keys should be stored securely using n8n credentials.
* The Basic LLM Chain forwards user prompts to the selected AI model.
* Chat Trigger nodes provide an interactive interface for testing AI workflows.
* AI models can be connected to workflows through dedicated model nodes.
