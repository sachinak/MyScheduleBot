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

from functionality.export_file import export_file  # type: ignore


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
async def test_export_file(bot, client):
    guild = bot.guilds[0]
    channel = guild.text_channels[0]
    message = await channel.send("!exportfile")

    await export_file(message)