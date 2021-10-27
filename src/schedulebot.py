import discord  # type: ignore
from discord.ext import commands  # type: ignore
import os
import json

from discord.ext.commands.help import MinimalHelpCommand

from functionality.AddEvent import add_event  # type: ignore
from functionality.highlights import get_highlight
from functionality.create_event_type import create_event_type
from functionality.FindAvailableTime import find_avaialbleTime
from functionality.delete_event_type import delete_event_type
from functionality.DisplayFreeTime import get_free_time
from functionality.export_file import export_file

bot = commands.Bot(command_prefix="!")  # Creates the bot with a command prefix of '!'
bot.remove_command("help")  # Removes the help command, so it can be created using Discord embed pages later


@bot.group(invoke_without_command=True)
async def help(ctx):
    """
    Function:
        help
    Description:
        A command that allows the user to see all usable commands and their descriptions
    Input:
        ctx - Discord context window
    Output:
        An embed window sent to the context with all commands/descriptions
    """
    em = discord.Embed(
        title="ScheduleBot Commands",
        description="Here are all the commands to use ScheduleBot\nAll events are prefaced by an '!'",
    )
    em.add_field(name="help", value="Displays all commands and their descriptions", inline=False)
    em.add_field(name="schedule", value="Creates an event", inline=False)
    em.add_field(name="freetime", value="Displays when you are available today", inline=False)
    em.add_field(name="day", value="Shows everything on your schedule for today", inline=False)
    em.add_field(name="typecreate", value="Creates a new event type", inline=True)
    em.add_field(name="typedelete", value="Deletes an event type", inline=True)
    em.add_field(name="exportfile", value="Exports a CSV file of your events", inline=False)
    em.add_field(name="importfile", value="Import events from a CSV file", inline=False)
    await ctx.send(embed=em)


@bot.event
async def on_ready():
    """
    Function:
        on_ready
    Description:
        Displays a welcome message to the ScheduleBot server and allows user to receive
    a direct message from the bot by reacting to the welcome message with an alarm_clock reaction
    Input:
        None
    Output:
        The welcome message sent to the ScheduleBot server
    """
    # Outputs bot name to console once bot is started
    print("We have logged in as {0.user}".format(bot))
    channel = bot.get_channel(884864860859531347)  # Gets the channel ID of the "schedule-manager channel"
    # msg = await channel.send(
    #     "Hello! My name is Schedule Bot and I am here to help you plan your schedule!\n\n"
    #     + "React to this message with a '⏰' (\:alarm_clock\:) reaction so I can direct message you!"
    #     + "Make sure you have allowed non-friends to direct message you or I can't help you."
    # )
    # await msg.add_reaction("⏰")


@bot.event
async def on_reaction_add(reaction, user):
    """
    Function: on_reaction_add
    Description: The bot sends a message to the user when reacting to the server startup message
    and runs the 'help' command
    Input:
        reaction - The emoji the user reacted to the message with
        user - The user who reacted to the post
    Output:
        - A welcome message received as a direct message from the bot
        - The 'help' command is automatically run
    """
    emoji = reaction.emoji
    if emoji == "⏰" and user.id != 884865269867102249:
        try:
            await user.send(
                "Nice to meet you "
                + user.name
                + "! I am ScheduleBot and I am here to make managing your schedule easier!"
            )
            await help(user)
        except:
            print(user.name + " (" + user.id + ") does not have DM permissions set correctly")
            pass


@bot.command()
async def schedule(ctx):
    """
    Function:
        schedule
    Description:
        Calls the add_event function to walk a user through the event creation process
    Input:
        ctx - Discord context window
    Output:
        - A new event added to the user's calendar file
        - A message sent to the context saying an event was successfully created
    """
    await add_event(ctx, bot)


@bot.command()
async def find(ctx):
    """
    Function:
        find
    Description:
        Calls the find_avaialbleTime function to walk a user through the range associated with the given event
    Input:
        ctx - Discord context window
    Output:
        - A new event type is added to the users event_type file
        - Provides users with the time range for the given event
    """
    await find_avaialbleTime(ctx, bot)


@bot.command()
async def day(ctx):
    """
    Function:
        get_highlight
    Description:
        Shows the events planned for the day by the user
    Input:
        ctx - Discord context window
    Output:
        - A message sent to the context with all the events that start and/or end today
    """
    await get_highlight(ctx)

@bot.command()
async def exportfile(ctx):
    """
    Function:
        exportfile
    Description:
        Sends the user a CSV file containing their scheduled events.
    Input:
        ctx - Discord context window
    Output:
        - A CSV file sent to the context that contains a user's scheduled events.
    """

    await export_file(ctx)

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

    await create_event_type(ctx, bot, event_msg)


# deleting event type
@bot.command()
async def typedelete(ctx):
    await delete_event_type(ctx, bot)


"""
Function: get_free_time
Description: giving the user the free time today according to the registered events
Input:
    ctx - Discord context window
    bot - Discord bot user
Output:
    - A message sent to the user channel stating every free time slot that is avaliable today
"""

# showing the free time that the user has today
@bot.command()
async def freetime(ctx):
    await get_free_time(ctx, bot)


# Runs the bot (local machine)
if __name__ == "__main__":
    from config import TOKEN

    bot.run(TOKEN)

# client.run(os.environ['TOKEN'])  # Runs the bot (repl.it)
