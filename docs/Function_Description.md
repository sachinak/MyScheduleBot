## schedulebot.py 
### async def help(ctx):
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
### async def on_ready():
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
### async def on_reaction_add(reaction, user):
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
 ### async def schedule(ctx):
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
### async def find(ctx):
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
 ### async def day(ctx, arg):
    """
    Function:
        get_highlight
    Description:
        Shows the events planned for the day by the user
    Input:
        ctx - Discord context window
        arg - User input argument
    Output:
        - A message sent to the context with all the events that start and/or end today
    """
 ### async def exportfile(ctx):
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
 ### async def importfile(ctx):
    """
    Function:
        importfile
    Description:
        Reads a CSV or ICS file containing events submitted by the user, and adds those events
    Input:
        ctx - Discord context window
    Output:
        - Events are added to a users profile.
    """

## event_type.py 

### def get_start_time(self):
        """
        Function:
            get_start_time
        Description:
            Converts an start time in event_type object into a string
        Input:
            self - The current event_type object instance
        Output:
            A formatted string of the start time
        """
 ### def get_end_time(self):
        """
        Function:
            get_end_time
        Description:
            Converts an end time in event_type object into a string
        Input:
            self - The current event_type object instance
        Output:
            A formatted string of end time
        """
### def to_list_event(self):
        """
        Function:
            to_list_event
        Description:
            Converts an event_type object into a list
        Input:
            self - The current event_type object instance
        Output:
            array - A list with each index being an attribute of the self event_type object
        """
        
