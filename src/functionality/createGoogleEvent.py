import discord
from discord.ext import commands
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import dateutil.parser
import datetime
import os
import pytz

async def add_event_to_calendar(ctx, summary, start_datetime, end_datetime, location=None):
    # Load Google Calendar credentials
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    
    token_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))), "json", "token.json")

    # If the user has already logged in, the details are extracted from token.js
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    else:
        await channel.send("You are not logged into Google. Please log in using the ConnectGoogle command")

    print("token found")
    service = build('calendar', 'v3', credentials=creds)

    start_time = dateutil.parser.isoparse(start_datetime)
    end_time = dateutil.parser.isoparse(end_datetime)

    # Set the timezone to EST
    est_timezone = pytz.timezone('US/Eastern')
    start_time = start_time.replace(tzinfo=est_timezone)
    end_time = end_time.replace(tzinfo=est_timezone)

    # Convert to UTC
    start_time_utc = start_time.astimezone(pytz.utc)
    end_time_utc = end_time.astimezone(pytz.utc)

    # Create event body
    event_body = {
        'summary': summary,
        'start': {'dateTime': start_time_utc.isoformat(), 'timeZone': 'UTC'},
        'end': {'dateTime': end_time_utc.isoformat(), 'timeZone': 'UTC'},
    }

    if location:
        event_body['location'] = location

    try:
        # Insert the event into Google Calendar
        service.events().insert(calendarId='primary', body=event_body).execute()
        await ctx.send(f'Event "{summary}" added successfully to Google Calendar.')
    except HttpError as e:
        await ctx.send(f'Error adding event: {e}')
