import os
import re
import csv
from pathlib import Path
from types import TracebackType

async def delete_event_type(ctx, client):
    channel = await ctx.author.create_dm()
    print(ctx.author.id)
    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author

    filename =str(ctx.author.id) + "event_types"
    try:

        # Checks if the calendar csv file exists
        if not os.path.exists(os.path.expanduser("~/Documents") + "/ScheduleBot/Type" + str(filename) + ".csv"):
            await channel.send("You have not created any events type yet!!")
        else:
            
            # Opens the current user's csv calendar file
            with open(
                os.path.expanduser("~/Documents") + "/ScheduleBot/Type" + str(filename) + ".csv", "r"
            ) as calendar_lines:
                calendar_lines = csv.reader(calendar_lines, delimiter=",")
                fields = next(calendar_lines)  # The column headers will always be the first line of the csv file
                rows = []
                new_row=[]
                line_number = 0
                flag=0
                list_types=''
                #printing the list of event type
                for line in calendar_lines:
                    if len(line) > 0:
                        rows.append(line)
                        list_types= list_types + "\nEvent Type: " + str(line[0]) + " prefered time range from " + str(line[1]) +" to " +str(line[2])
                
                if list_types=='':
                    await channel.send("You have not created any events type yet!!")
                else:
                    await channel.send("List of your available events types are:" + list_types)

                    await channel.send("Please enter the event type to be deleted")
                    # Waits for user input
                    event_msg = await client.wait_for("message", check=check)
                    # Strips message to just the text the user entered
                    msg_content = str(event_msg.content)

                    # Searching and deleting the event type
                    for line in rows:
                        if str(line[0]) == msg_content :
                            await channel.send("Event type " + msg_content +" has been deleted.")
                            flag=1
                        else:
                            new_row.append(line)
                            line_number+=1
                    if flag==0:
                        await channel.send("Event type does not exist")
                 # Open current user's calendar file for writing
                with open(
                    os.path.expanduser("~/Documents") + "/ScheduleBot/Type" + str(filename) + ".csv", "w", newline=""
                ) as calendar_file:
                    # Write to column headers and array of rows back to the calendar file
                    csvwriter = csv.writer(calendar_file)
               # print (str(fields))
               # print (str(new_row))
                    csvwriter.writerow(fields)
                    if line_number > 1:
                        csvwriter.writerows(new_row)
                    elif line_number == 1:
                        csvwriter.writerow(new_row[0])

    except Exception as e:
        # Outputs an error message if the event could not be created
        print(e)
        TracebackType.print_exc()
        await channel.send(
            "There was an error deleting your event."
        )

