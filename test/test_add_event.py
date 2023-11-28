"""
MIT License

Copyright (c) 2023 SEGroup10

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
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

from functionality.AddEvent import check_complete, add_event, check_event_url  # type: ignore


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
    async def test_add(ctx):
        thread = threading.Thread(target=add_event, args=(ctx, b), daemon=True)
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
async def test_add_event(bot):
    await test.message("!test_add")
    await asyncio.sleep(.25)

@pytest.mark.asyncio
async def test_check_event_url():
    assert check_event_url(" https://ncsu.zoom.us")
    assert not check_event_url("abc")
    assert not check_event_url("a.b.c")



def check_variables1():
    output = {
        "start": False,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": False,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "array": [],
        #"location": "",
    }
    return output


def check_variables2():
    output = {
        "start": True,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": False,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "array": [],
        #"location": "None",
    }
    return output


def check_variables3():
    output = {
        "start": True,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": True,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "array": [],
        #"location": "None",
    }
    return output


def check_variables4():
    output = {
        "start": True,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": True,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "array": ["Hello"],
        #"location": "None",
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
            #example1["location"],
        )
    )
    assert not (
        check_complete(
            example2["start"],
            example2["start_date"],
            example2["end"],
            example2["end_date"],
            example2["array"],
            #example1["location"],
        )
    )
    assert check_complete(
        example3["start"],
        example3["start_date"],
        example3["end"],
        example3["end_date"],
        example3["array"],
        #example1["location"],
    )
    assert check_complete(
        example4["start"],
        example4["start_date"],
        example4["end"],
        example4["end_date"],
        example4["array"],
        #example1["location"],
    )
