import re
from datetime import datetime
from Event import Event


async def add_event(client, message):
    event_array = []
    await message.author.send("Lets add an event!\n" + "First give me the name of your event:")
    event_msg = await client.wait_for('message')  # Waits for user input
    event_msg = event_msg.content   # Strips message to just the text the user entered
    event_array.append(event_msg)
    await message.author.send("Now give me the start & end dates for you event.\n" +
                              "If you don't use military time, make sure you include 'am' or 'pm' so I know when to schedule your event, otherwise I will assume am\n\n" +
                              "Here is the format you should follow (Start is first, end is second):\n" + "mm/dd/yy hh:mm am/pm mm/dd/yy hh:mm am/pm")

    event_dates = False
    # A loop that keeps running until a user enters correct start and end dates for their event following the required format
    # Adds start and end dates to the array if both are valid
    while(not event_dates):
        date_array = []
        msg_content = ""
        start_complete = False
        end_complete = True
        if message.author != client.user:
            # Waits for user input
            event_msg = await client.wait_for('message')
            # Strips message to just the text the user entered
            msg_content = event_msg.content
            # Splits response to prepare data to be appended to event_array
            date_array = re.split('\s', msg_content)

        # Adds a leading 0 if the user forgets to add one for single digit hour times for start date
        if ':' in date_array[1][0:2]:
            date_array[1] = '0' + date_array[1]

        # Checks to see if user entered am/pm for start/end dates and assumes am if nothing was entered and user isn't using military time
        # If military time was used, it adds an empty string into the array in the place of an am/pm
        if (date_array[2].lower() != "am" and date_array[2].lower() != "pm"):
            if int(date_array[1][0:2]) < 12:
                date_array.insert(2, "AM")
            else:
                date_array.insert(2, "")

        # Adds a leading 0 if the user forgets to add one for single digit hour times for end date
        if ':' in date_array[4][0:2]:
            date_array[4] = '0' + date_array[4]

        if (date_array[5].lower() != "am" and date_array[5].lower() != "pm"):
            if int(date_array[4][0:2]) < 12:
                date_array.insert(5, "AM")
            else:
                date_array.insert(5, "")

        # Tries to create the state_date datetime object
        try:
            if int(date_array[1][0:2]) >= 12 and date_array[2] == "":
                start_date = datetime.strptime(
                    date_array[0] + " " + date_array[1] + " " + date_array[2], "%m/%d/%y %H:%M")
                start_complete = True
                print("Created start_date object: " + str(start_date))
            else:
                start_date = datetime.strptime(
                    date_array[0] + " " + date_array[1] + " " + date_array[2], "%m/%d/%y %I:%M %p")
                start_complete = True
                print("Created start_date object: " + str(start_date))
        except Exception as e:
            print(e)
            await message.author.send("Looks like you didn't enter your start dates correctly.")
            start_complete = False
            date_array = []
            event_msg = ""

        # Tries to create the end_date datetime object
        try:
            if int(date_array[4][0:2]) >= 12 and date_array[5] == "":
                end_date = datetime.strptime(
                    date_array[3] + " " + date_array[4] + " " + date_array[5], "%m/%d/%y %H:%M")
                end_complete = True
                print("Created end_date object: " + str(end_date))
            else:
                end_date = datetime.strptime(
                    date_array[3] + " " + date_array[4] + " " + date_array[5], "%m/%d/%y %I:%M %p")
                end_complete = True
                print("Created end_date object: " + str(end_date))
        except Exception as e:
            print(e)
            await message.author.send("Looks like you didn't enter your end dates correctly.")
            end_complete = False
            date_array = []
            event_msg = ""

        # If both datetime objects were successfully created, they get appended to the list and exits the while loop
        if start_complete and end_complete:
            print("Both date objects created")
            event_dates = True
            event_array.append(start_date)
            event_array.append(end_date)

        # If both objects were unsuccessfully created, the bot notifies the user and the loop starts again
        else:
            await message.author.send("Make sure you follow this format(Start is first, end is second): mm/dd/yy hh:mm am/pm mm/dd/yy hh:mm am/pm")
            date_array = []
            msg_content = ""

    await message.author.send("Tell me what type of event this is. Here are a list of event types I currently know:")
    event_msg = await client.wait_for('message')  # Waits for user input
    event_msg = event_msg.content   # Strips message to just the text the user entered
    event_array.append(event_msg)
    await message.author.send("Any additional description you want me to add about the event? If not, enter 'done'")
    event_msg = await client.wait_for('message')  # Waits for user input
    event_msg = event_msg.content   # Strips message to just the text the user entered
    if event_msg.lower() == "done":
        event_array.append("")
    else:
        event_array.append(event_msg)

    # Tries to create an Event object from the user input
    try:
        current = Event(event_array[0], event_array[1],
                        event_array[2], event_array[3], event_array[4])
        await message.author.send("Your event was successfully created!")
        print(current)
        return current
    except Exception as e:
        # Outputs an error message if the event could not be created
        print(e)
        await message.author.send("There was an error creating your event. Make sure your formatting is correct and try creating the event again.")
