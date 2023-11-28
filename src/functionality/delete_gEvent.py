import discord
from discord.ext import commands
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
import os

async def delete_google_event(ctx, event_title: str):
    channel = await ctx.author.create_dm()

    SCOPES = ['https://www.googleapis.com/auth/calendar']
    token_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "json", "token.json")

    # If the user has already logged in, the details are extracted from token.js
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    else:
        await channel.send("You are not logged into Google. Please log in using the ConnectGoogle command")
        return

    service = build('calendar', 'v3', credentials=creds)

    # Get events
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=20,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    # Find and delete the event with the specified title
    for event in events:
        if 'summary' in event and event['summary'].lower() == event_title.lower():
            event_id = event['id']
            try:
                service.events().delete(calendarId='primary', eventId=event_id).execute()
                await ctx.send(f'Event "{event_title}" deleted successfully.')
                return
            except HttpError as e:
                await ctx.send(f'Error deleting event: {e}')
                return

    await ctx.send(f'Event "{event_title}" not found in Google Calendar.')
