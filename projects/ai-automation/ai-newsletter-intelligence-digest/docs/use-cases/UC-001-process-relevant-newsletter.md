UC-001 — Process Relevant Newsletter

Actor:
Gmail / Automation workflow

Trigger:
A new email is retrieved from Gmail.

Preconditions:
- Gmail connection is available.
- Email can be retrieved by the Make.com trigger.

Main Flow:
1. System receives an email.
2. System evaluates the filtering criteria.
3. Relevant newsletter is accepted.
4. Email body is extracted.
5. Content is prepared for downstream AI classification.

Alternative Flow:
3a. Email does not meet the filtering criteria.
3b. Email is rejected and does not continue to AI classification.

Expected Result:
Only relevant newsletter content continues through the workflow.