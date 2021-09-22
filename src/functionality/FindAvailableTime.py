import re
from config import EventTypes
from config import SetTime

async def find_availableTime(client, message):

    st = "Let's find time for your event. Enter the event type from the following :-\n"
    st1 = ' '
    for val in EventTypes:
        st1+=val+'\n'

    await message.author.send(st+st1)
    event_msg = await client.wait_for('message')  # Waits for user input
    event_msg = event_msg.content   # Strips message to just the text the user entered
    print(event_msg)

    get_val = SetTime[event_msg]
    startTime = get_val[0] if get_val[0]<12 else get_val[0]-12
    range = 'am' if get_val[0]<12 else 'pm'
    timeAvailable = 'You have '+event_msg+' time available between '+str(startTime)+' '+range
    endTime = get_val[1] if get_val[1]<12 else get_val[1]-12
    range = 'am' if get_val[1]<12 else 'pm'
    timeMessage = timeAvailable+' to '+str(endTime)+' '+range

    await message.author.send(timeMessage)

    try:
        await message.author.send("Your event was successfully created!")
    except:
        # Outputs an error message if the event could not be created
        await message.author.send("There was an error creating your event. Make sure your formatting is correct.")
