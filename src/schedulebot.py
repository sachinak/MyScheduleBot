import discord
import os
import json
import re
from Event import Event

# Loads data from commands json file
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file = open(root_dir + "/doc/commands.json")
json_data = json.load(json_file)


client = discord.Client()


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client)) # Outputs bot name to console once bot is started
  channel = client.get_channel(884864860859531347) # Gets the channel ID of the "schedule-manager channel"
  await channel.send("Hello! My name is Schedule Bot and I am here to help you plan your schedule!\n\n" +
  "React to this message with a '⏰' (\:alarm_clock\:) reaction so I can direct message you!")

@client.event
async def on_reaction_add(reaction, user):
  if reaction.emoji == '⏰':
    output = "Thank you for using Schedule Bot! Here is everything I can do:\n\n" # Initial output string
    for key in json_data['command']:
      output += (key + " or (" + json_data['command'][key]['aliases'][1] + "): " + 
      json_data['command'][key]['description'] + "\n") # Finds all the commands/descriptions and adds them to output string
    await user.send(output)

@client.event
async def on_message(message):
  # Prevents bot from responding to it's own messages
  if message.author == client.user:
    return

  # "help" command
  if message.content.startswith("help") or message.content.startswith("h"):
    output = "Here is everything I can do:\n\n" # Initial output string
    for key in json_data['command']:
      if key != "help":
        output += (key + " or (" + json_data['command'][key]['aliases'][1] + "): " + 
        json_data['command'][key]['description'] + "\n")  # Adds all commands/descriptions except "help" command to output string
    await message.author.send(output)
  
  # "schedule" command
  if message.content.startswith("schedule") or message.content.startswith("s"):
    await message.author.send("Lets add an event!\n" + "Follow the format:\n\n" + "name hh:mm am/pm(if not using military time) day(optional) mm/dd/yyyy type description(optional)\n\n" +
    "Example: \"Job Interview 12:30 pm Thursday 09/09/2021 meeting\" adds an event called 'Job Interview' at 12:30 pm on Thursday September 9th, 2021 with type 'meeting' with no description")
    event_msg = await client.wait_for('message')  # Waits for user input
    event_msg = event_msg.content   # Strips message to just the text the user entered
    event_array = re.split('\s|:|/', event_msg)   # splits the users response into an array to be converted into an "Event" object
    if event_array[3].lower() != "am" and event_array[3].lower() != "pm":  # If a user did not enter "am" or "pm"
      event_array.insert(3, None)                                          # a "None" element is inserted in its place
    if 10 > len(event_array):       # If a description was not included
      event_array.append(None)      # a "None" element is added to its place at the end of the array
    print(event_array)

    # Tries to create an Event object from the user input
    try:
      current = Event(event_array[0], int(event_array[1]), int(event_array[2]), event_array[3], event_array[4], int(event_array[5]), int(event_array[6]), int(event_array[7]), event_array[8], event_array[9])
      print(current.name + " " + current.hour + " " + current.minutes + " " + current.half + " " + current.day_of_week + " " + current.month + " " + current.date_day + " " + current.year + " " + current.event_type + " " + current.description)
      print("event created successfully")
    except:
      print("There was an error making the event") # Outputs an error message if the event could not be created
    # print(event_array)

client.run(os.environ['TOKEN']) # Runs the bot
