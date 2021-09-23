import os
from datetime import datetime


async def get_highlight(ctx, bot):
    channel = await ctx.author.create_dm()

    # Open the calendar file for user
    calendar_file = open(os.path.expanduser("~/Documents") +
                         "/ScheduleBot/calendar_file.txt", "r")
    # Read the calendar file
    lines = calendar_file.readlines()

    # If calendar is not empty
    if len(lines) > 0:
        # Each line is an event
        for i in lines:
            line = i.split()
            # print(line)
            # Get the event name, start and end date and time and descriptions
            event_name = line[0][1:len(line[0])-1]
            start_date = line[1]
            start_time = line[2]
            end_date = line[3]
            end_time = line[4]
            event_type = line[5]
            if(len(line) == 7):
                desc = line[6]

            await channel.send(
                f"You have {event_name} scheduled on {start_date} from {start_time} to {end_time}")
            # Is date in event today?
            # how?
    else:
        # print("You have no events scheduled for today")
        await channel.send("You have no events scheduled for today")
