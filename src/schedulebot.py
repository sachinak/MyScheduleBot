import discord  # type: ignore
import os
import json
from config import TOKEN
from functionality.AddEvent import add_event  # type: ignore
from functionality.FindAvailableTime import find_availableTime

# Loads data from commands json file
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file = open(root_dir + "/doc/commands.json")
json_data = json.load(json_file)


client = discord.Client()


@client.event
async def on_ready():
    # Outputs bot name to console once bot is started
    print("We have logged in as {0.user}".format(client))
    # channel = client.get_channel(884864860859531347) # Gets the channel ID of the "schedule-manager channel"
    # await channel.send("Hello! My name is Schedule Bot and I am here to help you plan your schedule!\n\n" +
    # "React to this message with a '⏰' (\:alarm_clock\:) reaction so I can direct message you!")


@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "⏰":
        # Initial output string
        output = "Thank you for using Schedule Bot! Here is everything I can do:\n\n"
        for key in json_data["command"]:
            output += (
                key
                + " or ("
                + json_data["command"][key]["aliases"][1]
                + "): "
                + json_data["command"][key]["description"]
                + "\n"
            )  # Finds all the commands/descriptions and adds them to output string
        await user.send(output)


@client.event
async def on_message(message):
    # Prevents bot from responding to it's own messages
    if message.author == client.user:
        return

    # "help" command
    if message.content.startswith("help") or message.content.startswith("h"):
        output = "Here is everything I can do:\n\n"  # Initial output string
        for key in json_data["command"]:
            if key != "help":
                output += (
                    key
                    + " or ("
                    + json_data["command"][key]["aliases"][1]
                    + "): "
                    + json_data["command"][key]["description"]
                    + "\n"
                )  # Adds all commands/descriptions except "help" command to output string
        await message.author.send(output)

    # "schedule" command
    if message.content.startswith("schedule") or message.content.startswith("s"):
        await add_event(client, message)

    # "find" command Recommendation based on Event Type
    if message.content.startswith("find") or message.content.startswith("f"):
        await find_availableTime(client, message)


# Runs the bot (local machine)
client.run(TOKEN)

# client.run(os.environ['TOKEN'])  # Runs the bot (repl.it)
