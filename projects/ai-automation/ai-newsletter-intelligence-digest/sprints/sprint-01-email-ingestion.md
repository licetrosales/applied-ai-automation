# Sprint 1 – Email Ingestion

## Sprint Goal

Receive one forwarded newsletter from Gmail using Make.com and verify
that the workflow successfully retrieves the email for further processing.

---

## Sprint Backlog

- [x] Configure Gmail trigger
- [x] Connect Gmail account
- [x] Forward test newsletter
- [x] Retrieve one newsletter in Make

---

## Deliverables

- Working Gmail trigger
- Successful newsletter retrieval
- Make.com scenario
- Execution screenshots

---

## Sprint Review

Goal met: yes. One forwarded newsletter was successfully retrieved via 
the Gmail trigger in Make.com (see screenshots/01-gmail-watch-emails-config.png, 
02-gmail-trigger-output.png).

Deliverables completed: 4/4.

Deviations from plan: trigger Limit was set to 1 rather than a higher 
value, to conserve Make.com operation credits during testing — revisit 
in Sprint 2.

---

## Sprint Retrospective

What went well: Gmail/Make.com connection setup was straightforward; 
no credential issues.

What was harder than expected: understanding which output field 
("Full text body" vs "HTML body") to use for downstream extraction — 
not yet decided, carried into Sprint 2.

Change for next sprint: check available output fields before writing 
the sprint backlog, so tasks like "identify the appropriate email 
body field" (already in Sprint 2) aren't a late discovery.

---

### Progress Notes

- Gmail connection established.
- Test newsletter successfully forwarded from web.de to Gmail.
- Gmail trigger configured.
- Successfully retrieved one forwarded newsletter in Make.com. 
