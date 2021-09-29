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

bot = commands.Bot(command_prefix="!") # Creates the bot with a command prefix of '!'
bot.remove_command("help") # Removes the help command, so it can be created using Discord embed pages later

"""
Function: help
Description: A command that allows the user to see all usable commands and their descriptions
Input:
    ctx - Discord context window
Output: An embed window sent to the context with all commands/descriptions
"""
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

"""
Function: on_ready
Description: Displays a welcome message to the ScheduleBot server and allows user to receive
a direct message from the bot by reacting to the welcome message with an alarm_clock reaction
Input: None
Output: The welcome message sent to the ScheduleBot server
"""
@bot.event
async def on_ready():
    # Outputs bot name to console once bot is started
    print("We have logged in as {0.user}".format(bot))
    # channel = bot.get_channel(884864860859531347) # Gets the channel ID of the "schedule-manager channel"
    # await channel.send("Hello! My name is Schedule Bot and I am here to help you plan your schedule!\n\n" +
    # "React to this message with a '⏰' (\:alarm_clock\:) reaction so I can direct message you!")

"""
Function: schedule
Description: Calls the add_event function to walk a user through the event creation process
Input:
    ctx - Discord context window
Output:
    - A new event added to the user's calendar file
    - A message sent to the context saying an event was successfully created
"""
@bot.command()
async def schedule(ctx):
    await add_event(ctx, bot)

"""
Function: find
Description: Calls the find_avaialbleTime function to walk a user through the range associated with the given event
Input:
    ctx - Discord context window
Output:
    - A new event type is added to the users event_type file
    - Provides users with the time range for the given event
"""
@bot.command()
async def find(ctx):
    await find_avaialbleTime(ctx,bot)
    
@bot.command()
async def day(ctx):
    await get_highlight(ctx, bot)

# creating new event type
@bot.command()
async def typecreate(ctx):
    
    channel = await ctx.author.create_dm()
    # print(ctx.author.id)
    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author

    await channel.send("First give me the type of your event:")
    event_msg = await bot.wait_for("message", check=check)  # Waits for user input
    event_msg = event_msg.content  # Strips message to just the text the user entered

    await create_event_type(ctx, bot,event_msg)


# deleting event type
@bot.command()
async def typedelete(ctx):
    await delete_event_type(ctx, bot)


# Runs the bot (local machine)
bot.run(TOKEN)

# client.run(os.environ['TOKEN'])  # Runs the bot (repl.it)
