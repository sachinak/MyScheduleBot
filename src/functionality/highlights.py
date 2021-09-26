import os
from datetime import datetime
import csv


async def get_highlight(ctx, bot):
    """
    Returns the events scheduled by user for today.

    Future implementation can take date/week/month as argument
    to show scheduled events as asked by user.
    """
    channel = await ctx.author.create_dm()

    try:
        # Open the calendar file for user
        with open(os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv", "r") as calendar_file:
            # Read the calendar file
            csv_reader = csv.reader(calendar_file, delimiter=',')
            # First line is just the headers
            fields = next(csv_reader)

            # Initialize variables
            event = {'name': '', 'startDate': '', 'startTime': '', 'endDate': '', 'endTime': '', 'type': '', 'desc': ''}
            events = []
            today = str(datetime.today()).split()[0]

            # For every row in calendar file
            for row in csv_reader:
                # Get event details
                event['name'] = row[1]
                start = row[2].split()
                event['startDate'] = start[0]
                event['startTime'] = convert_to_12(start[1][:-3]) # Convert to 12 hour format
                end = row[3].split()
                event['endDate'] = end[0]
                event['endTime'] = convert_to_12(end[1][:-3]) # Convert to 12 hour format
                event['type'] = row[4]
                event['desc'] = row[5]
                dates = [event['startDate'], event['endDate']]

                flag = check_start_or_end(dates, today)

                if flag == 1:
                    # If event starts and ends today
                    event['flag'] = 1
                    events.append(event)
                elif flag == 2:
                    # If event starts today but ends on a later date
                    event['endDate'] = event['endDate'].split('-')
                    event['endDate'] = event['endDate'][1] + '/' + event['endDate'][2] + '/' + event['endDate'][0]
                    event['flag'] = 2
                    events.append(event)
                elif flag == 3:
                    # If event is already in process and ends today
                    event['flag'] = 3
                    events.append(event)

                event = {'name': '', 'startDate': '', 'startTime': '', 'endDate': '', 'endTime': '', 'type': '', 'desc': ''}

        if len(events) != 0:
            for e in events:
                if e['flag'] == 1:
                    await channel.send(f"You have {e['name']} scheduled today, from {e['startTime']} to {e['endTime']}")
                elif e['flag'] == 2:
                    await channel.send(f"You have {e['name']} scheduled today, from {e['startTime']} to {e['endTime']} on {e['endDate']}")
                elif e['flag'] == 3:
                    await channel.send(f"You have {e['name']} scheduled today, till {e['endTime']}")
        else:
            await channel.send(f"You don't have any events scheduled for today")
    except FileNotFoundError as err:
        await channel.send("Looks like I cannot find your schedule. Try adding events using the '!schedule' command!")


# Helper Functions 

def check_start_or_end(dates, today):

    """ 
    Returns 0 if no event starts or ends today
    Returns 1 if event starts and ends today
    Returns 2 if event starts and ends on a later date
    Returns 3 if event started on a previous date and ends today
    """
    
    if today == dates[0]:
        if today == dates[1]:
            return 1
        else:
            return 2
    elif today == dates[1]:
        return 3
    else:
        return 0



def convert_to_12(time):

    """ Converts 24 hour time to 12 hour format"""

    if int(time[:2]) >= 12:
        new_time = "0" + str(int(time[:2]) - 12) + ":" + time[3:] + " PM"
    elif int(time[:2]) == 0:
        new_time = "12:" + time[3:] + " AM"
    else:
        new_time = time + " AM"

    return new_time
