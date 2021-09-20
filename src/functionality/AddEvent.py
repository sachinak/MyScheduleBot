import re
from Event import Event

async def add_event(client, message):
  await message.author.send("Lets add an event!\n" + "Follow the format:\n\n" + "name hh:mm am/pm(if not using military time) day(optional) mm/dd/yyyy type description(optional)\n\n" +
    "Example: \"Job Interview 12:30 pm Thursday 09/09/2021 meeting\" adds an event called 'Job Interview' at 12:30 pm on Thursday September 9th, 2021 with type 'meeting' with no description")
  event_msg = await client.wait_for('message')  # Waits for user input
  event_msg = event_msg.content   # Strips message to just the text the user entered
  event_array = re.split('\s|:|/', event_msg)   # splits the users response into an array to be converted into an "Event" object
  if event_array[3].lower() != "am" and event_array[3].lower() != "pm":  # If a user did not enter "am" or "pm"
    event_array.insert(3, None)                                          # a "None" element is inserted in its place
  if 10 > len(event_array):       # If a description was not included
    event_array.append(None)      # a "None" element is added to its place at the end of the array

  # Tries to create an Event object from the user input
  try:
    current = Event(event_array[0], int(event_array[1]), int(event_array[2]), event_array[3], event_array[4], int(event_array[5]), int(event_array[6]), int(event_array[7]), event_array[8], event_array[9])
    await message.author.send("Your event was successfully created!")
    return current
  except:
    await message.author.send("There was an error creating your event. Make sure your formatting is correct.") # Outputs an error message if the event could not be created