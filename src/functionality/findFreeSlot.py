import datetime
import discord
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import dateutil.parser
import pytz


async def find_and_schedule_free_time(ctx, summary, duration):
    '''
    Finds and schedules a free time slot in Google Calendar for all days.

    Parameters:
    - ctx: Discord context window
    - summary: Summary or name of the event
    - duration: Duration of the event in minutes

    Returns:
    - None
    '''
    channel = await ctx.author.create_dm()
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    
    token_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))), "json", "token.json")
    
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    else:
        await channel.send("You are not logged into Google. Please login using the ConnectGoogle command")
        return
    
    service = build('calendar', 'v3', credentials=creds)

    # Set the time range for all-day events
    start_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # UTC time
    end_time = start_time + datetime.timedelta(days=365)  # Schedule events for the next year
    
    # Find free time slots
    free_slots = await find_free_time_slots(service, start_time, end_time, duration)
    if not free_slots:
        await channel.send('No free time slots found.')
        return
    
    # Schedule the event in the first free time slot
    first_free_slot = free_slots[0]
    event_start = first_free_slot['start']
    event_end = event_start + datetime.timedelta(minutes=duration)
    
    # Set the timezone to EST
    est_timezone = pytz.timezone('US/Eastern')
    event_start_est = event_start.astimezone(est_timezone)
    event_end_est = event_end.astimezone(est_timezone)

    event_body = {
        'summary': summary,
        'start': {'dateTime': event_start_est.isoformat(), 'timeZone': 'America/New_York'},
        'end': {'dateTime': event_end_est.isoformat(), 'timeZone': 'America/New_York'},
    }

    try:
        service.events().insert(calendarId='primary', body=event_body).execute()
        
        # Print the scheduled time in EST
        event_start_formatted = event_start_est.strftime('%Y-%m-%d %H:%M:%S %Z')
        await channel.send(f'Event "{summary}" scheduled successfully at {event_start_formatted}.')
    except HttpError as e:
        await channel.send(f'Error scheduling event: {e}')

async def parse_date(raw_date):
    # Transform the datetime given by the API to a python datetime object.
    return dateutil.parser.isoparse(raw_date)  # Use isoparse to parse datetime strings

async def find_free_time_slots(service, start_time, end_time, duration):
    '''
    Finds free time slots in the specified time range.

    Parameters:
    - service: Google Calendar API service
    - start_time: Start time of the time range
    - end_time: End time of the time range
    - duration: Minimum duration of free time slots

    Returns:
    - A list of dictionaries representing free time slots
    '''
    # Retrieve events in the specified time range
    events_result = service.events().list(
        calendarId='primary',
        timeMin=start_time.astimezone(pytz.utc).isoformat(),
        timeMax=end_time.astimezone(pytz.utc).isoformat(),
        maxResults=10,  # Adjust as needed
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    async def parse_datetime(raw_date):
        return (await parse_date(raw_date)).replace(tzinfo=pytz.utc)

    busy_slots = [
        (await parse_datetime(event['start']['dateTime']), await parse_datetime(event['end']['dateTime']))
        for event in events
    ]
    #print(busy_slots)

    # Find free time slots
    free_slots = []
    current_time = start_time.astimezone(pytz.utc)
    while current_time + datetime.timedelta(minutes=duration) <= end_time.astimezone(pytz.utc):
        end_of_slot = current_time + datetime.timedelta(minutes=duration)
        is_slot_free = not any(start < end_of_slot and end > current_time + datetime.timedelta(minutes=duration) for start, end in busy_slots)


        # Debug print statements
        # print(f"Checking slot from {current_time} to {end_of_slot}. Is it free? {is_slot_free}")

        if is_slot_free:
            free_slots.append({'start': current_time, 'end': end_of_slot})
        current_time += datetime.timedelta(minutes=duration)

    # Debug print statement
    # print("Free slots:", free_slots)

    return free_slots
