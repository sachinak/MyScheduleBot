import os
import csv
import discord
import pandas as pd
from functionality.shared_functions import create_event_tree, create_type_tree, add_event_to_file, turn_types_to_string
from Event import Event

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

async def import_file(ctx, client):
    channel = await ctx.author.create_dm()

    def check(m):
        return len(m.attachments) == 1 and m.channel == channel and m.author == ctx.author

    user_id = str(ctx.author.id)

    # Checks if the calendar csv file exists, and creates it if it does not
    await channel.send("Please provide your file below:")
    event_msg = await client.wait_for("message", check=check)

    print(event_msg.attachments[0])

