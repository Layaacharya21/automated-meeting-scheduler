📌 Project Description

This project automates Google Calendar event and meeting scheduling using Python.

It uses the Google Calendar API to create events programmatically.

Users can schedule meetings without manually opening Google Calendar.

🔍 Existing System

Events are created manually using Google Calendar UI.

Users must enter details repeatedly for each event.

Adding attendees and recurring events takes more time.

⚠️ Drawbacks of Existing System

Time-consuming manual process

Prone to human errors (date, time, timezone mistakes)

No automation support

Not suitable for repeated or bulk scheduling

💡 Proposed Solution

A Python-based automated scheduler using Google Calendar API.

Allows event creation through a script.

Supports attendees, time zones, and recurring events.

Reduces manual effort and improves efficiency.

⚙️ How the Project Was Done

Enabled Google Calendar API from Google Cloud Console.

Used OAuth 2.0 for secure authentication.

Implemented Python script to:

Authenticate the user

Create calendar events

Invite attendees

Used Google API client libraries in Python.

Events are inserted using the events().insert() method.

✅ Outcome

Events are successfully created in Google Calendar.

Meeting links are generated automatically.

Scheduling becomes faster and easier.
