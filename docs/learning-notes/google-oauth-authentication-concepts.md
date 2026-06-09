# Google OAuth Authentication Concepts

## Goal

Document the key OAuth 2.0 concepts learned while integrating Google Sheets and Gmail with n8n.

---

## OAuth 2.0 Overview

OAuth 2.0 is an authorization framework that allows an application to access resources on behalf of a user without storing the user's password.

Example:

```text
n8n → requests access → Google Account
```

The user approves the request, and Google issues access tokens that n8n can use to interact with Google services.

---

## OAuth Consent Screen

The OAuth Consent Screen is the page displayed to users when an application requests access to Google resources.

Purpose:

* Identifies the application
* Displays requested permissions
* Allows users to approve or deny access

Example information:

```text
Application Name
Developer Information
Requested Scopes
```

During development, access can be restricted to test users.

---

## OAuth Client ID

The Client ID uniquely identifies an application to Google's authorization servers.

Example:

```text
Google recognizes:
"This request comes from application X"
```

Purpose:

* Identifies the application
* Used during the OAuth authentication flow
* Public information

---

## Client Secret

The Client Secret acts like a password for the application.

Purpose:

* Proves the application's identity
* Used together with the Client ID
* Must be stored securely

Best practice:

```text
Never commit Client Secrets to Git repositories.
```

---

## Redirect URI

After a user successfully authenticates, Google redirects the browser to a predefined URL.

Example:

```text
http://localhost:5678/rest/oauth2-credential/callback
```

Purpose:

* Returns authorization information to n8n
* Prevents unauthorized redirection

Google only allows registered redirect URIs.

---

## Test Users

While an OAuth application is in testing mode, only approved users can authenticate.

Purpose:

* Restricts access during development
* Prevents unauthorized use of unfinished applications

Example:

```text
Developer Account
Personal Test Account
```

---

## API Scopes

Scopes define the permissions requested by an application.

Examples:

```text
Read Google Sheets
Send Gmail Messages
Access Google Drive Files
```

Users can review and approve these permissions during authentication.

Principle:

```text
Request only the permissions that are required.
```

---

## Authentication Flow

OAuth authentication follows this sequence:

```text
User
  ↓
Google Consent Screen
  ↓
User Approves Access
  ↓
Google Issues Authorization Code
  ↓
n8n Exchanges Code for Access Token
  ↓
n8n Accesses Google APIs
```

---

## Relationship Between Components

```text
OAuth Consent Screen
        ↓
    Client ID
        ↓
   Client Secret
        ↓
   Redirect URI
        ↓
    User Login
        ↓
 Authorization
        ↓
 Access Token
        ↓
 Google APIs
```

All components work together to provide secure access without exposing user passwords.

---

## Reflection

Key concepts learned during this project:

* OAuth 2.0 authorization flow
* OAuth Consent Screen configuration
* Client ID and Client Secret management
* Redirect URI validation
* Test User configuration
* API scope permissions
* Google Sheets and Gmail OAuth integration in n8n

The project demonstrated how modern applications securely access third-party services through delegated authorization instead of direct credential sharing.
