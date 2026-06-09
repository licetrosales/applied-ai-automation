# Google OAuth Integration (n8n)

## Goal

Configure OAuth 2.0 authentication between n8n and Google services to enable secure access to Google Sheets and Gmail workflows.

## Tools Used

* n8n Community Edition
* Google Cloud Console
* Google Auth Platform
* OAuth 2.0
* Google Sheets API
* Gmail API
* Google Drive API

## Prerequisites

Verify n8n is running locally:

```bash
n8n
```

Open:

```text
http://localhost:5678
```

Create a Google Cloud project dedicated to the integration.

## Configuration

### Enable Required APIs

Enable the following APIs in Google Cloud Console:

* Google Sheets API
* Gmail API
* Google Drive API

### Configure OAuth Consent Screen

Create an OAuth application using Google Auth Platform.

Application settings:

```text
Application Name: <application-name>
User Type: External
```

Add a test user for development and validation.

### Create OAuth Client

Create an OAuth Client ID.

Application type:

```text
Web Application
```

Authorized JavaScript Origin:

```text
http://localhost:5678
```

Authorized Redirect URI:

```text
http://localhost:5678/rest/oauth2-credential/callback
```

Generate and securely store:

* Client ID
* Client Secret

### Configure Google Sheets Credential

Create a new credential in n8n:

```text
Google Sheets OAuth2 API
```

Provide:

* Client ID
* Client Secret

Authenticate using the Google account selected for testing.

### Configure Gmail Credential

Create a new credential in n8n:

```text
Gmail OAuth2 API
```

Provide:

* Client ID
* Client Secret

Authenticate using the same Google account.

## Verification

### Google Sheets Test

Create a spreadsheet containing sample data:

| Name   | Email                                         | City   |
| ------ | --------------------------------------------- | ------ |
| User A | [usera@example.com](mailto:usera@example.com) | Berlin |
| User B | [userb@example.com](mailto:userb@example.com) | London |
| User C | [userc@example.com](mailto:userc@example.com) | Madrid |

Create workflow:

```text
Manual Trigger
    ↓
Google Sheets (Get Row(s))
```

Execute the workflow.

Expected result:

```text
3 items returned
```

### Gmail Test

Create workflow:

```text
Manual Trigger
    ↓
Gmail (Send Email)
```

Send a test email to the authenticated account.

Expected result:

```text
Email successfully delivered
```

## Key Learnings

* OAuth 2.0 enables secure delegated access to Google services.
* Google Sheets and Gmail require separate credentials within n8n.
* Google Drive API is required for spreadsheet access.
* Test users must be configured while the OAuth application remains in testing mode.
* Each spreadsheet row is processed as an individual item in n8n.
* n8n executes downstream nodes once per incoming item.
