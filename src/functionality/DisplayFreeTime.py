from datetime import datetime
from Event import Event
import os
import csv
from datetime import timedelta
from datetime import time


async def get_free_time(ctx, bot):
    channel = await ctx.author.create_dm()
    
    # check if the user has a completely empty schedule
    if not os.path.exists(os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv"):
        await channel.send('You do not have any event at all')
        return

    rows = []

    # open the calendar file and read the events
    with open(
            os.path.expanduser("~/Documents") + "/ScheduleBot/" + str(ctx.author.id) + ".csv", "r"
        ) as calendar_lines:
            calendar_lines = csv.reader(calendar_lines, delimiter=",")
    
            for row in calendar_lines:
                if len(row) > 0:
                    rows.append(row)

    calendarDates = []
    rows.pop(0)
    for i in rows:
        if len(i) > 0:
            datetime.strptime(i[2], "%Y-%m-%d %H:%M:%S"),
            datetime.strptime(i[3], "%Y-%m-%d %H:%M:%S"),
            temp_event = Event(
                "",
                datetime.strptime(i[2], "%Y-%m-%d %H:%M:%S"),
                datetime.strptime(i[3], "%Y-%m-%d %H:%M:%S"),
                "",
                "",
            )
            calendarDates.append(temp_event)

    # two constants for the time at the start and end of the day
    start_time = time(hour=0, minute=0)
    end_time = time(hour=23, minute=59)

    # constant = 1 minute in time
    one_min = timedelta(hours=0, minutes=1)

    # setting up variables for the following dates: today , start and end of this current week

    today = datetime.today()

    start_week = today - timedelta(today.weekday())
    end_week = start_week + timedelta(7)

    # adding only the events that are happening today
    today_events = []
    for e in calendarDates:
        if e.start_date.date() == today.date() or e.end_date.date() == today.date():
            today_events.append(e)

    # sorting today's events
    today_events.sort()

    # removing the first event if it occurs at exactly 00:00 as there is no free time before it
    if today_events[0] == start_time:
        today_events.pop(0)

    # showing free time by iterating through the list of events ignoring the last one as it needs a special case

    for i in range(len(today_events) - 1):
        free_time_start = (today_events[i].end_date + one_min).time()
        free_time_end =  (today_events[i + 1].start_date - one_min).time()
        # ignoring if the free time is actually one minute or less
        if free_time_start < free_time_end:
            await channel.send("Free time from"
            , free_time_start
            , 'until',free_time_end)

    # showing the last free time slot if the last event in the day doesn't end exactly at:23:59
    if today_events[-1].end_date.time() < end_time:
        await channel.send('Free time from',
            (today_events[-1].end_date + one_min).time()
            , 'until 23:59 ')



    



