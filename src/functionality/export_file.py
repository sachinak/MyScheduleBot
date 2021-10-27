import os
import csv
from functionality.shared_functions import create_event_file


async def export_file(ctx, client):
    channel = await ctx.author.create_dm()
    print(ctx.author.id)

    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author

    user = str(ctx.author.id)

    # Checks if the calendar csv file exists, and creates it if it does not
    if not os.path.exists(os.path.expanduser("~/Documents") + "/ScheduleBot/Type/" + str(user) + ".csv"):
        create_event_file(user)

    channel.send("test")
