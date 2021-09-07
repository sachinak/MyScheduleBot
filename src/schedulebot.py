import discord
import os

client = discord.Client()


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  channel = client.get_channel(884864860859531347) # Gets the channel ID of the "schedule-manager channel"
  await channel.send("Hello! My name is Schedule Bot and I am here to help you plan your schedule!\n\n" + 
  "Here are a list of commands you can use:\n" +
  "add: Adds a single event\n" + "batch: Adds multiple events at once\n" + "delete: Deletes an event\n")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$hello"):
    await message.channel.send("Hello")

client.run(os.environ['TOKEN'])