import os
import csv
import discord
import pandas as pd
import tempfile
from discord import Attachment
from functionality.shared_functions import create_event_tree, create_type_tree, add_event_to_file, turn_types_to_string
from Event import Event
from parse.match import parse_period


def verify_csv(data):
    """
    Function:
        verify_csv
    Description:
        Verifies that CSV data retrieved through pandas matches the expected format
    Input:
        data - A Pandas Dataframe of data pulled from a CSV
    Output:
        - True if the data matches the expectation, false otherwise
    """

    if data.columns[0] != "ID":
        return False
    if data.columns[1] != "Name":
        return False
    if data.columns[2] != "Start Date":
        return False
    if data.columns[3] != "End Date":
        return False
    if data.columns[4] != "Type":
        return False
    if data.columns[5] != "Notes":
        return False

    return True


def convert_time(old_str):
    """
    Function:
        convert_time
    Description:
        Converts a time string from the YYYY-MM-DD HH:MM:SS format to the mm/dd/yy hh:mm am/pm format
    Input:
        old_str - The string to be converted
    Output:
        - the converted string
    """

    new_str = old_str[5:7] + '/' + old_str[8:10] + '/' + old_str[2:4] + ' '

    hour_int = int(old_str[11:13])
    if hour_int >= 12:
        am_or_pm = "pm"
        hour_int = hour_int - 12
    else:
        am_or_pm = "am"

    hour = str(hour_int)
    if len(hour) == 1:
        hour = '0' + hour

    new_str = new_str + hour + ':' + old_str[14:16] + am_or_pm

    return new_str


async def import_file(ctx, client):
    """
    Function:
        importfile
    Description:
        Reads a CSV file containing events submitted by the user, and adds those events
    Input:
        ctx - Discord context window
        client - The Discord chat bot
    Output:
        - Events are added to a users profile.
    """
    channel = await ctx.author.create_dm()

    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author

    user_id = str(ctx.author.id)

    # Checks if the calendar csv file exists, and creates it if it does not
    await channel.send("Please upload your file below.")

    # Loops until we receive a file.
    while True:

        event_msg = await client.wait_for("message", check=check)

        return 0 #TODO: Delete this

        if len(event_msg.attachments) != 1:
            await channel.send("No file detected. Please upload your file below.\nYou can do this by dropping "
                               "the file directly into Discord. Do not write out the file contents in a message.")
        else:
            break

    temp_file = tempfile.TemporaryFile()

    await event_msg.attachments[0].save(fp=temp_file, seek_begin=True, use_cached=False)

    data = pd.read_csv(temp_file)

    if not verify_csv(data):
        await channel.send("Unexpected CSV Format. Import has failed.")
        return

    # creates an event tree if one doesn't exist yet.
    create_event_tree(str(ctx.author.id))

    for index, row in data.iterrows():
        time_period = parse_period(convert_time(row['Start Date']) + ' ' + convert_time(row['End Date']))
        current = Event(row['Name'], time_period[0], time_period[1], row['Type'], row['Notes'])
        add_event_to_file(str(ctx.author.id), current)

    await channel.send("Your events were successfully added!")
