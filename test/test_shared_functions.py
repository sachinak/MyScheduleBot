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

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../src"))

import os
from Event import Event
from datetime import datetime
from functionality.shared_functions import (
    add_event_to_file,
    create_event_file,
    create_event_tree,
    create_event_directory,
    create_type_directory,
    create_type_file,
    create_type_tree,
    read_event_file,
    read_type_file,
    add_event_to_file,
    turn_types_to_string,
)

import pytest


def test_create_type_directory():
    create_type_directory()


def test_create_type_file():
    create_type_file("Test")


def test_create_type_tree():
    create_type_tree("Test")


def test_read_type_file():
    read_type_file("Test")


def test_turn_types_to_string():
    turn_types_to_string("Test")


def test_create_event_directory():
    create_event_directory()


def test_create_event_file():
    create_event_file("Test")


def test_create_event_tree():
    create_event_tree("Test")


def test_read_event_file():
    read_event_file("Test")


def test_add_event_to_file():

    add_event_to_file("Test", Event("", datetime(2021, 9, 29, 20, 30), datetime(2021, 9, 29, 20, 45), "", "", ""))