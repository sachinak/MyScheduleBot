import os
import csv
from pathlib import Path
from Event import Event
from datetime import datetime


def create_type_directory():
    """
    Function: create_type_directory
    Description: Creates ScheduleBot type directory in users Documents folder if it doesn't exist
    Input: None
    Output: Creates Type folder if it doesn't exist
    """
    #
    if not os.path.exists(os.path.expanduser("~/Documents/ScheduleBot/Type")):
        Path(os.path.expanduser("~/Documents/ScheduleBot/Type")).mkdir(parents=True, exist_ok=True)


def create_type_file(user_id):
    """
    Function: create_type_file
    Description: Checks if the event type file exists, and creates it if it doesn't
    Input:
        user_id - String representing the Discord ID of the user
    Output: Creates the event type file if it doesn't exist
    """
    if not os.path.exists(os.path.expanduser("~/Documents") + "/ScheduleBot/Type/" + user_id + "event_types.csv"):
        with open(
            os.path.expanduser("~/Documents") + "/ScheduleBot/Type/" + user_id + "event_types.csv",
            "x",
            newline="",
        ) as new_file:
            csvwriter = csv.writer(new_file, delimiter=",")
            csvwriter.writerow(["Event Type", "Start time", "End time"])


def create_type_tree(user_id):
    """
    Function: create_type_tree
    Description: Checks if the event type directory and file exists, and creates them if they don't
    Input:
        user_id - String representing the Discord ID of the user
    Output: Creates the event type folder and file if they don't exist
    """
    create_type_directory()
    create_type_file(user_id)


def read_type_file(user_id):
    """
    Function: read_type_file
    Description: Reads the event type file and displays all event types and preferred time ranges
    for those event types
    Input:
        user_id - String representing the Discord ID of the user
    Output:
        output - Formatted string of all the event types and their preferred time ranges
    """
    output = ""
    # Opens the event type file
    with open(
        os.path.expanduser("~/Documents") + "/ScheduleBot/Type/" + user_id + "event_types.csv", "r"
    ) as type_lines:
        type_lines = csv.reader(type_lines, delimiter=",")
        fields = next(type_lines)
        space = [10, 5, 5]
        current_line = []
        for line in type_lines:
            for text in line:
                current_line.append(text)
            output += f"{current_line[0]:<{space[0]}} Preferred range of {current_line[1]:<{space[1]}} - {current_line[2]:<{space[2]}}"
            current_line = []
    return output


def create_event_directory():
    """
    Function: create_event_directory
    Description: Creates ScheduleBot event directory in users Documents folder if it doesn't exist
    Input: None
    Output: Creates Event folder if it doesn't exist
    """
    if not os.path.exists(os.path.expanduser("~/Documents/ScheduleBot/Event")):
        Path(os.path.expanduser("~/Documents/ScheduleBot/Event")).mkdir(parents=True, exist_ok=True)


def create_event_file(user_id):
    """
    Function: create_event_file
    Description: Checks if the calendar file exists, and creates it if it doesn't
    Input:
        user_id - String representing the Discord ID of the user
    Output: Creates the calendar file if it doesn't exist
    """
    # Checks if the calendar file exists, and creates it if it doesn't
    if not os.path.exists(os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv"):
        with open(
            os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv",
            "x",
            newline="",
        ) as new_file:
            csvwriter = csv.writer(new_file, delimiter=",")
            csvwriter.writerow(["ID", "Name", "Start Date", "End Date", "Type", "Notes"])


def create_event_tree(user_id):
    """
    Function: create_event_tree
    Description: Checks if the calendar directory and file exists, and creates them if they don't
    Input:
        user_id - String representing the Discord ID of the user
    Output: Creates the calendar folder and file if they don't exist
    """
    create_event_directory()
    create_event_file(user_id)


def read_event_file(user_id, current):
    """
    Function: read_event_file
    Description: Reads the calendar file and adds an Event into the file in chronological order
    Input:
        user_id - String representing the Discord ID of the user
    Output:
        output - Formatted string of all the event types and their preferred time ranges
    """
    # Opens the current user's csv calendar file
    with open(os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv", "r") as calendar_lines:
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
                os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv",
                "w",
                newline="",
            ) as calendar_file:
                # Write to column headers and array of rows back to the calendar file
                csvwriter = csv.writer(calendar_file)
                csvwriter.writerow(fields)
                csvwriter.writerows(rows)
        # If the file has no events, add the current Event to the file
        else:
            with open(
                os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv",
                "w",
                newline="",
            ) as calendar_file:
                csvwriter = csv.writer(calendar_file)
                csvwriter.writerow(fields)
                csvwriter.writerow([""] + current.to_list())
