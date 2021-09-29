import os
import csv
import re
from Event import Event
from discord.ext.commands import bot
from functionality.highlights import convert_to_12
from functionality.create_event_type import create_event_type




def readfile(ctx):
    """
    Function:
        readfile
    Description:
        fetches the event_types file contents
    Input:
        ctx - Discord context window
    Output:
        - A csv_reader with the content of user's event_types
    """
        # Open the calendar file for user
    with open(os.path.expanduser("~/Documents") + "/ScheduleBot/Type/" + str(ctx.author.id) + "event_types" + ".csv", "r") as event_file:
        # Read the calendar file
        csv_reader = csv.reader(event_file, delimiter=',')
        # First line is just the headers
        fields = next(csv_reader)

    return  csv_reader 



async def find_avaialbleTime(ctx, client):
    """
    Function:
        find_avaialbleTime
    Description:
        Lets the user know about entered time range for event_type
    Input:
        ctx - Discord context window
        client - Discord bot user
    Output:
        - A new event type is added to the users event_type file
        - Provides users with the time range for the given event
    """
    channel = await ctx.author.create_dm()
    # print(ctx.author.id)
    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author

    await channel.send("Let's find time for your event. Enter the Event Type :-")
    event_msg = await client.wait_for("message", check=check)  # Waits for user input
    event = event_msg.content  # Strips message to just the text the user entered

    try:

        csv_reader = readfile(ctx)
        # For every row in calendar file
        flag = False
        for row in csv_reader:
        # Get event details
            if row[0] == event.event_type:
                flag = True                    
                await channel.send("You have a time range from "+row[1]+' to '+row[2]+' for events of type '+row[0])
                break

        event_created = False
        if flag == False:
            await channel.send("Looks like you don't have this event type present in your current file."
            + "Would you like to specify the time range for this event type?\n"
            + "Press y/n")
            event_msg1 = await client.wait_for("message", check=check)  # Waits for user input
            event_msg1 = event_msg1.content  # Strips message to just the text the user entered
            if event_msg1 == 'y':
                event_created = await create_event_type(ctx,client,event)

            if event_created == True:
                csv_reader = readfile(ctx)

        if event_created == True:
            for row in csv_reader:
            # Get event details
                if row[0] == event:
                    flag = True                    
                    await channel.send("You have a time range from "+row[1]+' to '+row[2]+' for events of type '+row[0])
                    break
                
        #matchedrows = getEventsOnDate(ctx,event.start_date)

    except FileNotFoundError as err:
        await channel.send("Looks like I cannot find your event types. Try adding event types using the '!event' command!")


def getEventsOnDate(ctx,yourdate):
    """
    Function:
        getEventsOnDate
    Description:
        Fetches the events on a particular day
    Input:
        ctx - Discord context window
        yourdate - Date for which events to be pulled
    Output:
        - Provides a list of events associated with that day
    """
    stdate = yourdate.date()
    with open(os.path.expanduser("~/Documents") + "/ScheduleBot/Event" + str(ctx.author.id) + ".csv", "r") as calendar_lines:
        calendar_lines = csv.reader(calendar_lines, delimiter=",")
        fields = next(calendar_lines)  # The column headers will always be the first line of the csv file
        rows = []
        line_number = 0
        for line in calendar_lines:
            if len(line) > 0:
                temp=re.split("\s", line[2])
                if str(temp[0]).__contains__(str(stdate)):
                    rows.append(line)
        
        Events = []
        for l in line:
            eve = Event(line[0], line[1], line[2], line[3], line[4])
            Events.append(eve)
        
        return Events
