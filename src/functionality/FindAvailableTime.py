import os
import csv

from discord.ext.commands import bot
from functionality.highlights import convert_to_12
from functionality.create_event_type import create_event_type
async def find_avaialbleTime(ctx, client):

    channel = await ctx.author.create_dm()
    # print(ctx.author.id)
    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author

    await channel.send("Let's find time for your event. Enter the Event Type :-")
    event_msg = await client.wait_for("message", check=check)  # Waits for user input
    event_msg = event_msg.content  # Strips message to just the text the user entered
    print(event_msg)

    try:
        # Open the calendar file for user
        with open(os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + "event_types" + ".csv", "r") as event_file:
            # Read the calendar file
            csv_reader = csv.reader(event_file, delimiter=',')
            # First line is just the headers
            fields = next(csv_reader)
        
        event_type = {'event_name': '','startTime': '','endTime': ''}
        event_types = []

        # For every row in calendar file
        for row in csv_reader:
            # Get event details
            event_type['event_name'] = row[1]
            event_type['startTime'] =  convert_to_12(row[1][:-3]) # Convert to 12 hour format
            event_type['endTime'] = convert_to_12(row[2][:-3]) # Convert to 12 hour format
    
            event_types.append(event_type)
        
        flag = False
        for val in event_type:
            if val['event_name'] == event_msg:
                    flag = True                    
                    await channel.send("You have a time range from "+val['startTime']+' to '+val['endTime']+' for events of type '+val['event_name'])

        if flag == False:
            await channel.send("Looks like you don't have this event type present in your current file."
            + "Would you like to specify the time range for this event type?\n"
            + "Press y/n")
            event_msg1 = await client.wait_for("message", check=check)  # Waits for user input
            event_msg1 = event_msg.content  # Strips message to just the text the user entered
            if event_msg1 == 'y':
                create_event_type(ctx,client)
            else:
                await channel.send("You have the entire day for the event of type "+event_msg)


    except FileNotFoundError as err:
        await channel.send("Looks like I cannot find your event types. Try adding event types using the '!event' command!")

#    get_val = SetTime[event_msg]    
#    startTime = get_val[0] if get_val[0]<12 else get_val[0]-12
#    range = 'am' if get_val[0]<12 else 'pm'
#    timeAvailable = 'You have '+event_msg+' time available between '+str(startTime)+' '+range
#    endTime = get_val[1] if get_val[1]<12 else get_val[1]-12
#    range = 'am' if get_val[1]<12 else 'pm'
#    timeMessage = timeAvailable+' to '+str(endTime)+' '+range

#    await message.author.send(timeMessage)

