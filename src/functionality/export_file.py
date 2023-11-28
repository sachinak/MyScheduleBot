"""
MIT License

Copyright (c) 2023 SEGroup10

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import csv
import discord
from functionality.shared_functions import create_event_file, create_event_directory

from functionality.shared_functions import load_key, decrypt_file, encrypt_file


async def export_file(ctx):
    """
    Function:
        export_file
    Description:
        Sends the user a CSV file containing their scheduled events.
    Input:
        ctx - Discord context window
    Output:
        - A CSV file sent to the context that contains a user's scheduled events.
    """

    channel = await ctx.author.create_dm()
    print(ctx.author.id)

    user_id = str(ctx.author.id)

    # Checks if the calendar csv file exists, and creates it if it does not
    if not os.path.exists(os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv"):
        create_event_directory()
        create_event_file(user_id)

    key = load_key(user_id)
    decrypt_file(key, os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv")

    await channel.send(file=discord.File(os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv"))

    encrypt_file(key, os.path.expanduser("~/Documents") + "/ScheduleBot/Event/" + user_id + ".csv")