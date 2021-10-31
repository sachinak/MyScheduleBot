# From https://stackoverflow.com/questions/25827160/importing-correctly-with-pytest
# Change current working directory so test case can find the source files
import sys, os
import asyncio
import discord
import discord.ext.commands as commands
import discord.ext.test as test
import threading
import time

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../src"))

import pytest
from datetime import datetime

from functionality.AddEvent import check_complete, add_event  # type: ignore


@pytest.fixture
def client(event_loop):
    c = discord.Client(loop=event_loop)
    test.configure(c)
    return c


@pytest.fixture
def bot(request, event_loop):
    intents = discord.Intents.default()
    intents.members = True
    b = commands.Bot("!", loop=event_loop, intents=intents)

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
async def test_add_event(bot, client):
    guild = bot.guilds[0]
    channel = guild.text_channels[0]
    message = await channel.send("!addevent")

    def check_msg(msg): assert message.content.startswith("Lets add an")

    bot.on_message = check_msg

    assert len(bot.private_channels) == 0

    thread = threading.Thread(target=add_event, args=(message, bot), daemon=True)
    thread.start()

    time.sleep(.5)


def check_variables1():
    output = {
        "start": False,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": False,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "array": [],
    }
    return output


def check_variables2():
    output = {
        "start": True,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": False,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "array": [],
    }
    return output


def check_variables3():
    output = {
        "start": True,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": True,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "array": [],
    }
    return output


def check_variables4():
    output = {
        "start": True,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": True,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "array": ["Hello"],
    }
    return output


def test_check():
    example1 = check_variables1()
    example2 = check_variables2()
    example3 = check_variables3()
    example4 = check_variables4()
    assert not (
        check_complete(
            example1["start"],
            example1["start_date"],
            example1["end"],
            example1["end_date"],
            example1["array"],
        )
    )
    assert not (
        check_complete(
            example2["start"],
            example2["start_date"],
            example2["end"],
            example2["end_date"],
            example2["array"],
        )
    )
    assert check_complete(
        example3["start"],
        example3["start_date"],
        example3["end"],
        example3["end_date"],
        example3["array"],
    )
    assert check_complete(
        example4["start"],
        example4["start_date"],
        example4["end"],
        example4["end_date"],
        example4["array"],
    )
