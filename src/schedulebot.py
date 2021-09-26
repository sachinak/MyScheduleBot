import discord  # type: ignore
from discord.ext import commands  # type: ignore
import os
import json

from discord.ext.commands.help import MinimalHelpCommand
from pretty_help import PrettyHelp, DefaultMenu  # type: ignore
from config import TOKEN
from functionality.AddEvent import add_event  # type: ignore
from functionality.highlights import get_highlight
from functionality.create_event_type import create_event_type

# from functionality.FindAvailableTime import find_availableTime

# Loads data from commands json file
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file = open(root_dir + "/doc/commands.json")
json_data = json.load(json_file)

bot = commands.Bot(command_prefix="!", help_command=PrettyHelp())


@bot.event
async def on_ready():
    # Outputs bot name to console once bot is started
    print("We have logged in as {0.user}".format(bot))
    # channel = bot.get_channel(884864860859531347) # Gets the channel ID of the "schedule-manager channel"
    # await channel.send("Hello! My name is Schedule Bot and I am here to help you plan your schedule!\n\n" +
    # "React to this message with a '⏰' (\:alarm_clock\:) reaction so I can direct message you!")


menu = DefaultMenu(page_left="\U0001F44D", page_right="👎", active_time=5)
bot.help_command = PrettyHelp(menu=menu, no_category="ScheduleBot Commands", index_title="ScheduleBot Commands")


@bot.command()
async def schedule(ctx):
    await add_event(ctx, bot)


@bot.command()
async def day(ctx):
    await get_highlight(ctx, bot)

# creating new event type
@bot.command()
async def event_type(ctx):
    await create_event_type(ctx, bot)

# Runs the bot (local machine)
bot.run(TOKEN)

# client.run(os.environ['TOKEN'])  # Runs the bot (repl.it)
