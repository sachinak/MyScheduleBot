import os
import csv
import discord
import pandas as pd
from functionality.shared_functions import create_event_tree, create_type_tree, add_event_to_file, turn_types_to_string
from Event import Event


async def import_file(ctx, client):
    channel = await ctx.author.create_dm()

    def check(m):
        return len(m.attachments) == 1 and m.channel == channel and m.author == ctx.author

    user_id = str(ctx.author.id)

    # Checks if the calendar csv file exists, and creates it if it does not
    await channel.send("Please provide your file below:")
    event_msg = await client.wait_for("message", check=check)

    print(event_msg.attachments[0])

