import discord
from discord.ext import commands
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime
import os

async def get_events_for_date(ctx, date_str: str):
    channel = await ctx.author.create_dm()

    try:
        target_date = datetime.datetime.strptime(date_str, '%m/%d/%y')
    except ValueError:
        await ctx.send('Invalid date format. Please use MM/DD/YY.')
        return

    SCOPES = ['https://www.googleapis.com/auth/calendar']
    token_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "json", "token.json")

    # If the user has already logged in, the details are extracted from token.js
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    else:
        await channel.send("You are not logged into Google. Please log in using the ConnectGoogle command")

    service = build('calendar', 'v3', credentials=creds)

    start_of_day = datetime.datetime(target_date.year, target_date.month, target_date.day, 0, 0, 0, 0)
    end_of_day = datetime.datetime(target_date.year, target_date.month, target_date.day, 23, 59, 59, 999999)

    events_result = service.events().list(
        calendarId='primary',
        timeMin=start_of_day.isoformat() + 'Z',
        timeMax=end_of_day.isoformat() + 'Z',
        maxResults=20,  # You can adjust this based on your needs
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    if not events:
        await ctx.send(f'No upcoming events found for {date_str}.')
        return

    keys_to_keep = ['summary', 'description', 'start', 'end', 'location']

    for e in events:
        embed = discord.Embed(colour=discord.Colour.magenta(), timestamp=ctx.message.created_at,
                              title=f'Events for {date_str}:')
        embed.set_footer(text=f"Requested by {ctx.author}")

        # Extracting necessary information from the event
        event_info = {key: value for key, value in e.items() if key in keys_to_keep}

        embed.add_field(name="Event Name:", value=event_info['summary'], inline=False)
        embed.add_field(name="Start Time:", value=event_info['start'], inline=True)
        embed.add_field(name="End Time:", value=event_info['end'], inline=True)

        if 'location' in event_info:
            embed.add_field(name="Location:", value=event_info['location'], inline=False)
        else:
            embed.add_field(name="Location:", value='None', inline=False)

        # embed.add_field(name="Description:", value=event_info['description'], inline=False)
        await ctx.send(embed=embed)
