## schedulebot.py 
### async def help(ctx):
      
    Function:
        help
    Description:
        A command that allows the user to see all usable commands and their descriptions
    Input:
        ctx - Discord context window
    Output:
        An embed window sent to the context with all commands/descriptions
    
### async def on_ready():
    
    Function:
        on_ready
    Description:
        Displays a welcome message to the ScheduleBot server and allows user to receive
    a direct message from the bot by reacting to the welcome message with an alarm_clock reaction
    Input:
        None
    Output:
        The welcome message sent to the ScheduleBot server
    
### async def on_reaction_add(reaction, user):
    
    Function: on_reaction_add
    Description: The bot sends a message to the user when reacting to the server startup message
    and runs the 'help' command
    Input:
        reaction - The emoji the user reacted to the message with
        user - The user who reacted to the post
    Output:
        - A welcome message received as a direct message from the bot
        - The 'help' command is automatically run
    
 ### async def schedule(ctx):
    
    Function:
        schedule
    Description:
        Calls the add_event function to walk a user through the event creation process
    Input:
        ctx - Discord context window
    Output:
        - A new event added to the user's calendar file
        - A message sent to the context saying an event was successfully created
    
### async def find(ctx):
    
    Function:
        find
    Description:
        Calls the find_avaialbleTime function to walk a user through the range associated with the given event
    Input:
        ctx - Discord context window
    Output:
        - A new event type is added to the users event_type file
        - Provides users with the time range for the given event
    
 ### async def day(ctx, arg):
    
    Function:
        get_highlight
    Description:
        Shows the events planned for the day by the user
    Input:
        ctx - Discord context window
        arg - User input argument
    Output:
        - A message sent to the context with all the events that start and/or end today
    
 ### async def exportfile(ctx):
    
    Function:
        exportfile
    Description:
        Sends the user a CSV file containing their scheduled events.
    Input:
        ctx - Discord context window
    Output:
        - A CSV file sent to the context that contains a user's scheduled events.
    
 ### async def importfile(ctx):
    
    Function:
        importfile
    Description:
        Reads a CSV or ICS file containing events submitted by the user, and adds those events
    Input:
        ctx - Discord context window
    Output:
        - Events are added to a users profile.
    

## event_type.py 

### def get_start_time(self):
        
        Function:
            get_start_time
        Description:
            Converts an start time in event_type object into a string
        Input:
            self - The current event_type object instance
        Output:
            A formatted string of the start time
        
 ### def get_end_time(self):
        
        Function:
            get_end_time
        Description:
            Converts an end time in event_type object into a string
        Input:
            self - The current event_type object instance
        Output:
            A formatted string of end time
        
### def to_list_event(self):
        
        Function:
            to_list_event
        Description:
            Converts an event_type object into a list
        Input:
            self - The current event_type object instance
        Output:
            array - A list with each index being an attribute of the self event_type object
        
## Event.py

### def __init__(self, name, start_date, end_date, priority, event_type, description,location="None"):
        
        Function:
            __init__
        Description:
            Creates a new Event object instance
        Input:
            self - The current Event object instance
            name - String name of the event
            start_date - datetime object representing the start of an event
            end_date - datetime object representing the end of an event
            priority - priority value of an event
            event_type - String representing the type of event
            description - Optional text field that contains any additional notes about an event (can be blank)
        Output:
            - A new Event object instance
        
### def __lt__(self, other):
        
        Function:
            __lt__
        Description:
            Finds whether the current event starts before another
        Input:
            self - The current Event object instance
            other - The Event object we are comparing self to
        Output:
            True - self starts before other
            False - self starts after other
        
### def __le__(self, other):
        
        Function:
            __le__
        Description:
            Finds whether the current event starts before or at the same time as another
        Input:
            self - The current Event object instance
            other - The Event object we are comparing self to
        Output:
            True - self starts before or at the same time as other
            False - self comes after other
        
### def __gt__(self, other):
        
        Function:
            __gt__
        Description:
            Finds whether the current event starts after another
        Input:
            self - The current Event object instance
            other - The Event object we are comparing self to
        Output:
            True - self starts after other
            False - self comes before other
        
### def intersect(self, other):
        
        Function:
            intersect
        Description:
            Finds whether the current event intersects another in one of 4 possible ways:
            # Case 1: The start and end dates for the event occur inside another event
            # Case 2: The start and end dates for the event encompass another event
            # Case 3: Only the start date for the event occurs inside another event
            # Case 4: Only the end date for the event occurs inside another event
        Input:
            self - The current Event object instance
            other - The Event object we are comparing self to
        Output:
            True - self intersects with other
            False - self does not intersect with other
        
### def to_list(self):
        
        Function:
            to_list
        Description:
            Converts an Event object into a list
        Input:
            self - The current Event object instance
        Output:
            array - A list with each index being an attribute of the self Event object
            
## AddEvent.py

### def check_complete(start, start_date, end, end_date, array):
     
    Function:
        check_complete
    Description:
        Boolean function to check if both the date objects are created
    Input:
        start_date - start date
        end_date - end date
    Output:
        - True if both the date objects are created else False
     
    
### async def add_event(ctx, client):
     
    Function:
        add_event
    Description:
        Walks a user through the event creation process
    Input:
        ctx - Discord context window
        client - Discord bot user
    Output:
        - A new event added to the user's calendar file
        - A message sent to the context saying an event was successfully created
     
    
## Delete_Event.py

### async def delete_event(ctx, arg):
     
    Function:
        delete_event
    Description:
        A existing event is deleted from the user's schedule file
    Input:
        ctx: the current context
        arg: the instance of the bot
    Output:
        - A reply saying whether the event was deleted or not
     
## DisplayFreeTime.py

### async def get_free_time(ctx, bot):
     
    Function:
        get_free_time
    Description:
        giving the user the free time today according to the registered events by calling the function compute_free_time
    Input:
        ctx - Discord context window
        bot - Discord bot user
    Output:
        - A message sent to the user channel stating every free time slot that is avaliable today
     
### def compute_free_time(calendarDates):
     
    Function:
        compute_free_time
    Description:
        returning a string that contains the user the free time according to the registered events
    Input:
        calendarDates - list of the events that the user has in the calendar
    Output:
        - a string stating every free time slot that is avaliable today
     
## FinaAvailableTime.py

### async def find_avaialbleTime(ctx, client):
     
    Function:
        find_avaialbleTime
    Description:
        Lets the user know about entered time range for event_type
    Input:
        ctx - Discord context window
        client - Discord bot user
    Output:
        - A new event type is added to the users event_type file
        - Provides users with the time range for the given event
     
### def findInter(next_event, event_atime, idx, end):
     
    Function:
        findInter
    Description:
        The helper iterator function to find the intersection
    Input:
        next_event - available time based on the next event
        event_atime - a list of available time based on events on date
        idx - index of the current available time in the list
        end - lenght of the list
    Output:
        - A list of available time for the date
     
### def getEventsOnDate(ctx, stdate):
     
    Function:
        getEventsOnDate
    Description:
        Fetches the events on a particular day
    Input:
        ctx - Discord context window
        yourdate - Date for which events to be pulled
    Output:
        - Provides a list of events associated with that day
     
## FindAvailableTime.py 
### async def find_avaialbleTime(ctx, client):
     
    Function:
        find_avaialbleTime
    Description:
        Lets the user know about entered time range for event_type
    Input:
        ctx - Discord context window
        client - Discord bot user
    Output:
        - A new event type is added to the users event_type file
        - Provides users with the time range for the given event
     

## GoogleEvent.py
### async def get_events(ctx, arg):
    '''
    function oto extract events from google calendar
    Parameters
    ----------
    ctx : Discord context window
    arg : Discord bot user.
    Returns
    -------
    None.
    '''
    

## create_event_type.py
### async def create_event_type(ctx, client, event_msg):
     
    Function:
        create_event_type
    Description:
        Walks a user through the creation of types of event or updating time range for existing event types
    Input:
        ctx - Discord context window
        client - Discord bot user
    Output:
        - A new event type added to the user's calendar file or the time range will be update for the existing event type
        - A message sent to the context saying an event type was successfully added or updated
     
    

## delete_event_type.py
### def delete_type(rows, msg_content):
     
    Function:
        delete_type
    Description:
        A existing event type is deleted from the user's calendar file   
    Input:
        rows: lsit of lines in calendar
        msg_content: event type to be deleted
    Output:
        - A existing event type is deleted from the user's calendar file 
     
### def print_type(calendar_lines):
     
    Function:
        print_type
    Description:
        Sends the lsit of all event type in csv file
    Input:
        calendar_lines - object for csv.reader for user's calendar file
    Output:
        -  Sends the lsit of all event types as list and string
     
### async def delete_event_type(ctx, client):
     
    Function:
        delete_event_type
    Description:
        Walks a user through deleting the existing event types in the calender file
    Input:
        ctx - Discord context window
        client - Discord bot user
    Output:
        - A existing event type is deleted from the user's calendar file 
        - A message sent to the context saying an event type was successfully deleted
     
    

## distance.py
### def get_key():
    '''
    Function to extract API key
    Returns
    -------
    api_key_1 : reutrns the api key for google connection
    '''
### def get_lat_log( address,api_key_1):
     
    This function converts a textual address to a set of coordinates
    address : String
        the location for which coordinates are needed.
    Returns
    -------
    list
        the latitude and longitude of the given address using google maps.
     
### def get_distance( dest, src,mode):
     
    this gets the distace matrix which includes the travel time to the event
    Input:
    dest : Takes address of location for event as a string.
    src : Takes coordinates of source address as a list.
    mode: Takes Mode of transport as a string.
    Returns:
    travel time in seconds.
     
    

## export_file.py
### async def export_file(ctx):
     
    Function:
        export_file
    Description:
        Sends the user a CSV file containing their scheduled events.
    Input:
        ctx - Discord context window
    Output:
        - A CSV file sent to the context that contains a user's scheduled events.
     
    

## highlights.py 
### async def get_highlight(ctx, arg):
     
    Function:
        get_highlight
    Description:
        Shows the events planned for the day by the user.
    Input:
        - ctx - Discord context window
        - arg - The input arguments which specify the date
    Output:
        - A message sent to the context with all the events that start and/or end today
     

## import_file.py
    
### def verify_csv(data):
     
    Function:
        verify_csv
    Description:
        Verifies that CSV data retrieved through pandas matches the expected format
    Input:
        data - A Pandas Dataframe of data pulled from a CSV
    Output:
        - True if the data matches the expectation, false otherwise
     
### def convert_time(old_str):
     
    Function:
        convert_time
    Description:
        Converts a time string from the YYYY-MM-DD HH:MM:SS format to the mm/dd/yy hh:mm am/pm format
    Input:
        old_str - The string to be converted
    Output:
        - the converted string
     
### def get_ics_data(calendar):
     
    Function:
        get_ics_data
    Description:
        Fethces relevant data from an ICS calendar
    Input:
        calendar - The string to be converted
    Output:
        - A pandas table containing the calendar data.
     
### async def import_file(ctx, client):
     
    Function:
        importfile
    Description:
        Reads a CSV file containing events submitted by the user, and adds those events
    Input:
        ctx - Discord context window
        client - The Discord chat bot
    Output:
        - Events are added to a users profile.
     
    
    
    
    
 
        
        



