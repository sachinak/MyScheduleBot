import os
import csv
import discord
from functionality.shared_functions import create_event_file


async def export_file(ctx):
    channel = await ctx.author.create_dm()
    print(ctx.author.id)

    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author

    user_id = str(ctx.author.id)

    # Checks if the calendar csv file exists, and creates it if it does not
    if not os.path.exists(os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv"):
        create_event_file(user_id)

    await channel.send(file=discord.File(os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv"))
