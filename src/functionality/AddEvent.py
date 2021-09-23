import re
import os
import csv
from datetime import datetime
from pathlib import Path
from types import TracebackType
from Event import Event


async def add_event(ctx, client):
    channel = await ctx.author.create_dm()
    # print(ctx.author.id)
    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author
    event_array = []
    await channel.send("Lets add an event!\n" + "First give me the name of your event:")
    event_msg = await client.wait_for("message", check = check)  # Waits for user input
    event_msg = event_msg.content  # Strips message to just the text the user entered
    event_array.append(event_msg)
    await channel.send(
        "Now give me the start & end dates for you event.\n"
        + "If you don't use military time, make sure you include 'am' or 'pm' so I know when to schedule your event, otherwise I will assume am\n\n"
        + "Here is the format you should follow (Start is first, end is second):\n"
        + "mm/dd/yy hh:mm am/pm mm/dd/yy hh:mm am/pm"
    )

    event_dates = False
    # A loop that keeps running until a user enters correct start and end dates for their event following the required format
    # Adds start and end dates to the array if both are valid
    while not event_dates:
        date_array = []
        msg_content = ""
        start_complete = False
        end_complete = True
        if ctx.message.author != client.user:
            # Waits for user input
            event_msg = await client.wait_for("message", check = check)
            # Strips message to just the text the user entered
            msg_content = event_msg.content
            # Splits response to prepare data to be appended to event_array
            date_array = re.split("\s", msg_content)

        # Adds a leading 0 if the user forgets to add one for single digit hour times for start date
        if ":" in date_array[1][0:2]:
            date_array[1] = "0" + date_array[1]

        # Checks to see if user entered am/pm for start/end dates and assumes am if nothing was entered and user isn't using military time
        # If military time was used, it adds an empty string into the array in the place of an am/pm
        if date_array[2].lower() != "am" and date_array[2].lower() != "pm":
            if int(date_array[1][0:2]) < 12:
                date_array.insert(2, "AM")
            else:
                date_array.insert(2, "")

        # Adds a leading 0 if the user forgets to add one for single digit hour times for end date
        if ":" in date_array[4][0:2]:
            date_array[4] = "0" + date_array[4]

        if date_array[5].lower() != "am" and date_array[5].lower() != "pm":
            if int(date_array[4][0:2]) < 12:
                date_array.insert(5, "AM")
            else:
                date_array.insert(5, "")

        # Tries to create the state_date datetime object
        try:
            if int(date_array[1][0:2]) >= 12 and date_array[2] == "":
                start_date = datetime.strptime(
                    date_array[0] + " " + date_array[1] + " " + date_array[2], "%m/%d/%y %H:%M"
                )
                start_complete = True
                print("Created start_date object: " + str(start_date))
            else:
                start_date = datetime.strptime(
                    date_array[0] + " " + date_array[1] + " " + date_array[2], "%m/%d/%y %I:%M %p"
                )
                start_complete = True
                print("Created start_date object: " + str(start_date))
        except Exception as e:
            print(e)
            await channel.send("Looks like you didn't enter your start dates correctly.")
            start_complete = False
            date_array = []
            event_msg = ""

        # Tries to create the end_date datetime object
        try:
            if int(date_array[4][0:2]) >= 12 and date_array[5] == "":
                end_date = datetime.strptime(
                    date_array[3] + " " + date_array[4] + " " + date_array[5], "%m/%d/%y %H:%M"
                )
                end_complete = True
                print("Created end_date object: " + str(end_date))
            else:
                end_date = datetime.strptime(
                    date_array[3] + " " + date_array[4] + " " + date_array[5], "%m/%d/%y %I:%M %p"
                )
                end_complete = True
                print("Created end_date object: " + str(end_date))
        except Exception as e:
            print(e)
            await channel.send("Looks like you didn't enter your end dates correctly.")
            end_complete = False
            date_array = []
            event_msg = ""

        # If both datetime objects were successfully created, they get appended to the list and exits the while loop
        if start_complete and end_complete:
            print("Both date objects created")
            event_dates = True
            event_array.append(start_date)
            event_array.append(end_date)

        # If both objects were unsuccessfully created, the bot notifies the user and the loop starts again
        else:
            await channel.send(
                "Make sure you follow this format(Start is first, end is second): mm/dd/yy hh:mm am/pm mm/dd/yy hh:mm am/pm"
            )
            date_array = []
            msg_content = ""

    await channel.send("Tell me what type of event this is. Here are a list of event types I currently know:")
    event_msg = await client.wait_for("message", check = check)  # Waits for user input
    event_msg = event_msg.content  # Strips message to just the text the user entered
    event_array.append(event_msg)
    await channel.send("Any additional description you want me to add about the event? If not, enter 'done'")
    event_msg = await client.wait_for("message", check = check)  # Waits for user input
    event_msg = event_msg.content  # Strips message to just the text the user entered
    if event_msg.lower() == "done":
        event_array.append("")
    else:
        event_array.append(event_msg)

    # Tries to create an Event object from the user input
    try:
        current = Event(event_array[0], event_array[1], event_array[2], event_array[3], event_array[4])
        await channel.send("Your event was successfully created!")

        # Creates ScheduleBot directory in users Documents folder if it doesn't exist
        if not os.path.exists(os.path.expanduser("~/Documents/ScheduleBot")):
            Path(os.path.expanduser("~/Documents/ScheduleBot")).mkdir(parents=True, exist_ok=True)

        # Checks if the calendar csv file exists, and creates it if it doesn't
        if not os.path.exists(os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv"):
            with open(os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv", "x") as new_file:
                csvwriter = csv.writer(new_file, delimiter=',')
                csvwriter.writerow(["ID", "Name", "Start Date", "End Date", "Type", "Notes"])

        with open(os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv", "r") as calendar_lines:
            calendar_lines = csv.reader(calendar_lines, delimiter=',')  # Stores all lines from calendar file as an array
            fields = next(calendar_lines)
            rows = []
            for row in calendar_lines:
                rows.append(row)
            line_number = 0
            if len(rows) > 0:
                print("IF")
                for i in rows:
                    # print("This is the content of i: " + i)
                    if len(i) > 0:
                        temp_event = Event("", datetime.strptime(i[2], "%d/%m/%Y %H:%M"), datetime.strptime(i[3], "%d/%m/%Y %H:%M"), "", "")
                        if current < temp_event:
                            print(str(current))
                            rows.insert(line_number, [''] + current.to_list())
                            print(rows)
                            break
                        if line_number == len(rows) - 1:
                            print(str(current))
                            rows.insert(len(rows), [''] + current.to_list())
                            print(rows)
                            break
                        line_number += 1
                with open(os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv", "w") as calendar_file:
                    csvwriter = csv.writer(calendar_file)
                    csvwriter.writerow(fields)
                    csvwriter.writerow([''] + current.to_list())
            else:
                print("Else")
                with open(os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv", "w") as calendar_file:
                    csvwriter = csv.writer(calendar_file)
                    print(str(current))
                    print("I am here")
                    csvwriter.writerow(fields)
                    csvwriter.writerow([''] + current.to_list())

            # Loop if the file is not empty
            # if len(calendar_lines) > 0:
            #     for i in calendar_lines:
            #         tstr = re.split("\s", i)  # Splits the string representation of an Event object

            #         # Converts the split string array into an Event object
            #         temp_event = Event(
            #             tstr[0],
            #             datetime.strptime(tstr[1] + " " + tstr[2], "%Y-%m-%d %H:%M:%S"),
            #             datetime.strptime(tstr[3] + " " + tstr[4], "%Y-%m-%d %H:%M:%S"),
            #             "",
            #             "",
            #         )
            #         # If the Event we want to add comes before the Event from current line in the file, insert it at that spot
            #         if current < temp_event:
            #             calendar_lines.insert(line_number, str(current) + "\n")
            #             break
            #         # If the end of the file is reached and the Event has not been added, insert it to the end of the file
            #         if line_number == len(calendar_lines) - 1:
            #             calendar_lines.insert(len(calendar_lines), str(current) + "\n")
            #             break
            #         line_number += 1
            #     calendar_file = open(os.path.expanduser("~/Documents") + "/ScheduleBot/calendar_file.txt", "w")
            #     calendar_file.writelines(calendar_lines)  # Rewrite the calendar back to the file with the new Event
            #     calendar_file.close()
            # # If the file is empty, add the Event to the beginning of the file
            # else:
            #     calendar_file = open(os.path.expanduser("~/Documents") + "/ScheduleBot/calendar_file.txt", "w")
            #     calendar_file.write(str(current))
            #     calendar_file.close()
    except Exception as e:
        # Outputs an error message if the event could not be created
        print(e)
        TracebackType.print_exc()
        await channel.send(
            "There was an error creating your event. Make sure your formatting is correct and try creating the event again."
        )
