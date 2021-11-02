import asyncio
import sys, os

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../src"))

import pytest
import pandas as pd
import discord
import discord.ext.commands as commands
import discord.ext.test as test
import threading
from icalendar import Calendar
import time
from schedulebot import importfile
from functionality.import_file import verify_csv, convert_time, import_file, get_ics_data

'''
bot_test = commands.Bot(command_prefix="!")

@bot_test.command()
def unit_import(ctx):
    importfile(ctx)
'''


@pytest.fixture
def client(event_loop):
    c = discord.Client(loop=event_loop)
    test.configure(c)
    return c


@pytest.fixture
def bot(request, event_loop):
    intents = discord.Intents.default()
    intents.members = True
    b = commands.Bot(command_prefix="!", loop=event_loop, intents=intents)

    @b.command()
    async def test_import(ctx):
        thread = threading.Thread(target=importfile, args=(ctx, b), daemon=True)
        thread.start()

    marks = request.function.pytestmark
    mark = None
    for mark in marks:
        if mark.name == "cogs":
            break

    if mark is not None:
        for extension in mark.args:
            b.load_extension("tests.internal." + extension)

    test.configure(b)
    return b


@pytest.mark.asyncio
async def test_import_file(bot):
    await test.message("!test_import")
    await asyncio.sleep(.25)

def test_import_ics():

    file = open(r"test/files/test.ics", "r")
    gcal = Calendar.from_ical(file.read())
    file.close()

    data = get_ics_data(gcal)

    assert verify_csv(data)

def test_import_ics_empty():
    gcal = Calendar.from_ical("BEGIN:VCALENDAR\n"
                              "END:VCALENDAR")

    data = get_ics_data(gcal)

    assert verify_csv(data)

def test_time():
    old_time = "1998-05-08 10:30:00"
    new_time = convert_time(old_time)

    assert "05/08/98 10:30 am" == new_time


def test_time_pm():
    old_time = "1998-05-08 18:30:00"
    new_time = convert_time(old_time)

    assert "05/08/98 06:30 pm" == new_time


def test_working_csv():
    data = {'ID': [''],
            'Name': ['test'],
            'Start Date': ["1998-05-08 18:30:00"],
            'End Date': ["1998-05-08 18:45:00"],
            'Priority': '1',
            'Type': '',
            'Notes': ''}

    table = pd.DataFrame(data=data)

    assert verify_csv(table)


def test_typo_csv():
    data = {'ID': [''],
            'Name': ['test'],
            'Stert Date': ["1998-05-08 18:30:00"],
            'End Date': ["1998-05-08 18:45:00"],
            'Priority': '1',
            'Type': '',
            'Notes': ''}

    table = pd.DataFrame(data=data)

    assert not verify_csv(table)

def test_missing_column_csv():
    data = {'ID': [''],
            'Name': ['test'],
            'Stert Date': ["1998-05-08 18:30:00"],
            'Priority': '1',
            'Type': '',
            'Notes': ''}

    table = pd.DataFrame(data=data)

    assert not verify_csv(table)
