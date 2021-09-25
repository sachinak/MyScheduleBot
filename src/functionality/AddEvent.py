import re
import os
import csv
from datetime import datetime
from pathlib import Path
from types import TracebackType
from Event import Event
from parse import parse_period

async def add_event(ctx, client):
    channel = await ctx.author.create_dm()
    # print(ctx.author.id)
    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author

    event_array = []
    await channel.send("Lets add an event!\n" + "First give me the name of your event:")
    event_msg = await client.wait_for("message", check=check)  # Waits for user input
    event_msg = event_msg.content  # Strips message to just the text the user entered
    event_array.append(event_msg)
    await channel.send(
        "Now give me the start & end dates for you event. "
        + "Make sure you use 12-hour formatting\n\n"
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
            event_msg = await client.wait_for("message", check=check)
            # Strips message to just the text the user entered
            msg_content = event_msg.content
            # Splits response to prepare data to be appended to event_array

        print(date_array)

        try:
            parse_result = parse_period(msg_content)
        except Exception as e:
            await channel.send(
                "Looks like " + str(e) + ". Please re-enter your dates.\n"
                + "Here is the format you should follow (Start is first, end is second):\n"
                + "mm/dd/yy hh:mm am/pm mm/dd/yy hh:mm am/pm"
            )
            start_complete = False
            continue

        start_complete = True
        start_date = parse_result[0]
        end_date = parse_result[1]

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
    event_msg = await client.wait_for("message", check=check)  # Waits for user input
    event_msg = event_msg.content  # Strips message to just the text the user entered
    event_array.append(event_msg)
    await channel.send("Any additional description you want me to add about the event? If not, enter 'done'")
    event_msg = await client.wait_for("message", check=check)  # Waits for user input
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
            with open(
                os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv", "x", newline=""
            ) as new_file:
                csvwriter = csv.writer(new_file, delimiter=",")
                csvwriter.writerow(["ID", "Name", "Start Date", "End Date", "Type", "Notes"])

        # Opens the current user's csv calendar file
        with open(
            os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv", "r"
        ) as calendar_lines:
            calendar_lines = csv.reader(calendar_lines, delimiter=",")
            fields = next(calendar_lines)  # The column headers will always be the first line of the csv file
            rows = []

            # Stores the current row in an array of rows if the row is not a new-line character
            # This check prevents an accidental empty lines from being kept in the updated file
            for row in calendar_lines:
                if len(row) > 0:
                    rows.append(row)
            line_number = 0

            # If the file already has events
            if len(rows) > 0:
                for i in rows:

                    # Skips check with empty lines
                    if len(i) > 0:

                        # Temporarily turn each line into an Event object to compare with the object we are trying to add
                        temp_event = Event(
                            "",
                            datetime.strptime(i[2], "%Y-%m-%d %H:%M:%S"),
                            datetime.strptime(i[3], "%Y-%m-%d %H:%M:%S"),
                            "",
                            "",
                        )

                        # If the current Event occurs before the temp Event, insert the current at that position
                        if current < temp_event:
                            rows.insert(line_number, [""] + current.to_list())
                            break

                        # If we have reached the end of the array and not inserted, append the current Event to the array
                        if line_number == len(rows) - 1:
                            rows.insert(len(rows), [""] + current.to_list())
                            break
                        line_number += 1

                # Open current user's calendar file for writing
                with open(
                    os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv", "w", newline=""
                ) as calendar_file:
                    # Write to column headers and array of rows back to the calendar file
                    csvwriter = csv.writer(calendar_file)
                    csvwriter.writerow(fields)
                    csvwriter.writerows(rows)

            # If the file has no events, add the current Event to the file
            else:
                with open(
                    os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv", "w", newline=""
                ) as calendar_file:
                    csvwriter = csv.writer(calendar_file)
                    csvwriter.writerow(fields)
                    csvwriter.writerow([""] + current.to_list())

    except Exception as e:
        # Outputs an error message if the event could not be created
        print(e)
        TracebackType.print_exc()
        await channel.send(
            "There was an error creating your event. Make sure your formatting is correct and try creating the event again."
        )


def convert24(str1):

    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:

        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]
