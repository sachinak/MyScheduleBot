class event_type:
    
    def __init__(self, event_name, start_time, end_time):
        
        """
        Function:
            __init__
        Description:
            Creates a new event_type object instance
        Input:
            self - The current type object instance
            name - String representing the type of event
            start_time - datetime object representing the start time of preferred time range
            end_time - datetime object representing the end time of preferred time range
            priority - Priority value of the event (in a scale of 1-5)
        Output:
            - A new event_type object instance
        """
        self.event_name = event_name
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        """
        Function:
            __str__
        Description:
            Converts an event_type object into a string
        Input:
            self - The current event_type object instance
        Output:
            A formatted string that represents all the information about an type instance
        """
        output = (
            self.event_name 
            + " "
            + str(self.start_time)
            + " "
            + str(self.end_time)
            # + " "
            # + str(self.priority)
        )
        return output
    
    def get_start_time(self):
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
        return str(self.start_time.strftime('%I:%M %p'))

    def get_end_time(self):
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
        return str(self.end_time.strftime('%I:%M %p'))

    def to_list_event(self):
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
        array = [self.event_name, self.get_start_time(), self.get_end_time()]
        return array
