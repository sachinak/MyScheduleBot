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

    # Returns whether the current event comes before another
    def __lt__(self, other):
        return self.end_date < other.start_date

    # Returns whether the current event comes before or at the same time of another
    def __le__(self, other):
        return self.end_date <= other.start_date

    # Returns whether the current event comes after another
    def __gt__(self, other):
        return self.end_date > other.start_date

    # Returns whether the current event comes after or at the same time of another
    def __ge__(self, other):
        return self.end_date >= other.start_date

    # Returns whether the current event intersects with another event
    # Case 1: The start and end dates for the event occur inside another event
    # Case 2: The start and end dates for the event encompass another event
    # Case 3: Only the start date for the event occurs inside another event
    # Case 4: Only the end date for the event occurs inside another event
    def intersect(self, other):
        return (
            (
                (self.start_date >= other.start_date and self.start_date < other.end_date)
                or (self.end_date > other.start_date and self.end_date <= other.end_date)
            )
            or (self.start_date <= other.start_date and self.end_date >= other.end_date)
            or (
                (self.start_date >= other.start_date and self.start_date < other.end_date)
                and self.end_date >= other.end_date
            )
            or (
                (self.end_date > other.start_date and self.end_date <= other.end_date)
                and self.start_date <= other.start_date
            )
        )
