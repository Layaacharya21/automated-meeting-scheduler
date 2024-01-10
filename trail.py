import datetime as dt
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        event = {
    "summary": "My Python Event",
    "location": "Hyderabad",
    "description": "Event for undergrads - Workshop",
    "colorid": 6,
    "start": {
        "dateTime": "2024-01-06T03:24:00",
        "timeZone": "Asia/Kolkata"  # Update the time zone identifier
    },
    "end": {
        "dateTime": "2024-01-06T05:00:00",
        "timeZone": "Asia/Kolkata"  # Update the time zone identifier
    },
    "recurrence": ["RRULE:FREQ=DAILY;COUNT=3"],
    "attendees": [
        {"email": "srilayakarampudi@gmail.com"},
        {"email": "rsreeprada1@gmail.com"}
    ]
}
        event = service.events().insert(calendarId="primary", body=event).execute()

        print(f"Event Created: {event.get('htmlLink')}")

        # Call the Calendar API
        
    except HttpError as error:
        print(f"An error occurred:", error)
def scheduleMeeting(service):
    print("Welcome to the Automated Meeting Scheduler!")

    summary = input("Enter meeting title: ")
    location = input("Enter meeting location: ")
    description = input("Enter meeting description: ")

    # Input meeting start and end times
    start_time_str = input("Enter meeting start time (YYYY-MM-DD HH:MM): ")
    end_time_str = input("Enter meeting end time (YYYY-MM-DD HH:MM): ")

    # Convert string input to datetime objects
    start_time = dt.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
    end_time = dt.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")

    # Convert datetime objects to string format compatible with Google Calendar API
    start_time_str = start_time.isoformat() + "Z"
    end_time_str = end_time.isoformat() + "Z"

    # Input attendee emails
    attendees = input("Enter attendee emails (comma-separated): ").split(",")

    try:
        event = {
            "summary": summary,
            "location": location,
            "description": description,
            "colorId": 6,
            "start": {
                "dateTime": start_time_str,
                "timeZone": "Europe/Berlin"
            },
            "end": {
                "dateTime": end_time_str,
                "timeZone": "Europe/Berlin"
            },
            "recurrence": ["RRULE:FREQ=DAILY;COUNT=1"],
            "attendees": [{"email": email} for email in attendees]
        }

        event = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Meeting scheduled: {event.get('htmlLink')}")

    except HttpError as error:
        print(f"An error occurred:", error)


if __name__ == "__main__":
    main()

