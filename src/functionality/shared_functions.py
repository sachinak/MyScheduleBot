import os
import csv
from pathlib import Path
from src.Event import Event
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
    Description: Reads the event type file
    for those event types
    Input:
        user_id - String representing the Discord ID of the user
    Output:
        rows - List of rows
    """
    # Opens the event type file
    with open(
        os.path.expanduser("~/Documents") + "/ScheduleBot/Type/" + user_id + "event_types.csv", "r"
    ) as type_lines:
        type_lines = csv.reader(type_lines, delimiter=",")
        current_row = []
        rows = []
        for line in type_lines:
            for text in line:
                current_row.append(text)
            rows.append(current_row)
            current_row = []
    return rows


def turn_types_to_string(user_id):
    """
    Function: turn_types_to_string
    Description: Reads the event types file and turns all of them into a formatted string
    Input:
        user_id - String representing the Discord ID of the user
    Output:
        output - Formatted string of rows in event types file
    """
    output = ""
    space = [12, 5, 5]
    rows = read_type_file(user_id)
    line_number = 0
    for i in rows:
        if line_number != 0:
            output += f"{i[0]:<{space[0]}} Preferred range of {i[1]:<{space[1]}} - {i[2]:<{space[2]}}\n"
        line_number += 1
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


def read_event_file(user_id):
    """
    Function: read_event_file
    Description: Reads the calendar file and creates a list of rows
    Input:
        user_id - String representing the Discord ID of the user
    Output:
        rows - List of rows
    """
    # Opens the current user's csv calendar file
    with open(os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv", "r") as calendar_lines:
        calendar_lines = csv.reader(calendar_lines, delimiter=",")
        rows = []
        # Stores the current row in an array of rows if the row is not a new-line character
        # This check prevents an accidental empty lines from being kept in the updated file
        for row in calendar_lines:
            if len(row) > 0:
                rows.append(row)
        return rows


def add_event_to_file(user_id, current):
    """
    Function: add_event_to_file
    Description: Adds an event to the calendar file in chronological order
    Input:
        user_id - String representing the Discord ID of the user
        current - Event to be added to calendar
    Output: None
    """
    line_number = 0
    rows = read_event_file(user_id)
    # If the file already has events
    if len(rows) > 1:
        for i in rows:
            # Skips check with empty lines
            if len(i) > 0 and line_number != 0:

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
    else:
        rows.insert(len(rows), [""] + current.to_list())
    # Open current user's calendar file for writing
    with open(
        os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv",
        "w",
        newline="",
    ) as calendar_file:
        # Write to column headers and array of rows back to the calendar file
        csvwriter = csv.writer(calendar_file)
        csvwriter.writerows(rows)

