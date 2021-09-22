class Event:
    def __init__(self, name, start_date, end_date, event_type, description):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.event_type = event_type
        self.description = description

    # Converts event object to a string
    def __str__(self):
        output = (
            self.name
            + " "
            + str(self.start_date)
            + " "
            + str(self.end_date)
            + " "
            + self.event_type
            + " "
            + self.description
        )
        return output
