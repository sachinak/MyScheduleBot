import discord  # type: ignore
from discord.ext import commands  # type: ignore
import os
import json

from discord.ext.commands.help import MinimalHelpCommand
from config import TOKEN
from functionality.AddEvent import add_event  # type: ignore
from functionality.highlights import get_highlight
from functionality.create_event_type import create_event_type
from functionality.FindAvailableTime import find_avaialbleTime
from functionality.delete_event_type import delete_event_type

# from functionality.FindAvailableTime import find_availableTime

# Loads data from commands json file
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file = open(root_dir + "/doc/commands.json")
json_data = json.load(json_file)

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")


@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title="ScheduleBot Commands",
        description="Here are all the commands to use ScheduleBot\nAll events are prefaced by an '!'",
    )
    em.add_field(name="help", value="Displays all commands and their descriptions", inline=False)
    em.add_field(name="schedule", value="Creates an event", inline=False)
    em.add_field(name="day", value="Shows everything on your schedule for today", inline=False)
    em.add_field(name="typecreate", value="Creates a new event type", inline=True)
    em.add_field(name="typedelete", value="Deletes an event type", inline=True)
    await ctx.send(embed=em)


@bot.event
async def on_ready():
    # Outputs bot name to console once bot is started
    print("We have logged in as {0.user}".format(bot))
    # channel = bot.get_channel(884864860859531347) # Gets the channel ID of the "schedule-manager channel"
    # await channel.send("Hello! My name is Schedule Bot and I am here to help you plan your schedule!\n\n" +
    # "React to this message with a '⏰' (\:alarm_clock\:) reaction so I can direct message you!")


@bot.command()
async def schedule(self, ctx: commands.Context):
    await add_event(ctx, bot)
    await ctx.send("This is a test command")


@bot.command()
async def find_time(ctx):
    await find_avaialbleTime(ctx, bot)


@bot.command()
async def day(ctx):
    await get_highlight(ctx, bot)


# creating new event type
@bot.command()
async def typecreate(ctx):
    await create_event_type(ctx, bot)


# deleting event type
@bot.command()
async def typedelete(ctx):
    await delete_event_type(ctx, bot)


# Runs the bot (local machine)
bot.run(TOKEN)

# client.run(os.environ['TOKEN'])  # Runs the bot (repl.it)
