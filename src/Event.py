class Event:
  def __init__(self, name, hour, minutes, half, day_of_week, month, date_day, year, event_type, description):
    self.name = name
    self.hour = hour
    self.minutes = minutes
    if half == None:
      if hour >= 12:
        print("there")
        self.half = "pm"
      else:
        print("over there")
        self.half = "am"
    else:
      self.half = half
    self.day_of_week = day_of_week
    print(self.day_of_week)
    self.month = month
    print(self.month)
    self.date_day = date_day
    print(self.date_day)
    self.year = year
    print(self.year)
    self.event_type = event_type
    print(self.event_type)
    if description != None:
      self.description = description
    else:
      self.description = ""
    print(self.description)