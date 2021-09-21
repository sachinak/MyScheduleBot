class Event:
    def __init__(self, name, start_date, end_date, event_type, description):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.event_type = event_type
        self.description = description

    # Converts event object to a string
    def __str__(self):
        output = self.name + " " + str(self.start_date) + " " + \
            str(self.end_date) + " " + self.event_type + " " + self.description
        return output

    # # Compares two events to see which one is further away (less than)
    # def __lt__(self, other):
    #     if self.year != other.year:
    #         return self.year < other.year
    #     else:
    #         if self.month != other.month:
    #             return self.month < other.month
    #         else:
    #             if self.date_day != other.date_day:
    #                 return self.date_day < other.date_day
    #             else:
    #                 if self.hour != other.hour:
    #                     return self.hour < other.hour
    #                 else:
    #                     return self.minutes < other.minutes

    # # Compares two events to see which one is further away (less than or equal to)
    # def __le__(self, other):
    #     if self.year != other.year:
    #         return self.year <= other.year
    #     else:
    #         if self.month != other.month:
    #             return self.month <= other.month
    #         else:
    #             if self.date_day != other.date_day:
    #                 return self.date_day <= other.date_day
    #             else:
    #                 if self.hour != other.hour:
    #                     return self.hour <= other.hour
    #                 else:
    #                     return self.minutes <= other.minutes

    # # Compares two events to see which one is closer (greater than)
    # def __gt__(self, other):
    #     if self.year != other.year:
    #         return self.year > other.year
    #     else:
    #         if self.month != other.month:
    #             return self.month > other.month
    #         else:
    #             if self.date_day != other.date_day:
    #                 return self.date_day > other.date_day
    #             else:
    #                 if self.hour != other.hour:
    #                     return self.hour > other.hour
    #                 else:
    #                     return self.minutes > other.minutes

    # # Compares two events to see which one is closer (greater than or equal to)
    # def __ge__(self, other):
    #     if self.year != other.year:
    #         return self.year >= other.year
    #     else:
    #         if self.month != other.month:
    #             return self.month >= other.month
    #         else:
    #             if self.date_day != other.date_day:
    #                 return self.date_day >= other.date_day
    #             else:
    #                 if self.hour != other.hour:
    #                     return self.hour >= other.hour
    #                 else:
    #                     return self.minutes >= other.minutes

    # # Compares two events to see if they are at the same time (equal to)
    # def __eq__(self, other):
    #     if self.year == other.year:
    #         if self.month == other.month:
    #             if self.date_day == other.date_day:
    #                 if self.hour == other.hour:
    #                     return self.minutes == other.minutes
    #                 else:
    #                     return False
    #             else:
    #                 return False
    #         else:
    #             return False
    #     else:
    #         return False

    # # Compares two events to see if they are not at the same time
    # def __ne__(self, other):
    #     return not(self == other)

    # def intersect(self, other):
    #     return
