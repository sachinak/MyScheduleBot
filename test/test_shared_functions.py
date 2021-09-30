# From https://stackoverflow.com/questions/25827160/importing-correctly-with-pytest
# Change current working directory so test case can find the source files
import sys, os

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../src"))

import os
from Event import Event
from datetime import datetime
from functionality.shared_functions import (
    create_event_file,
    create_event_tree,
    create_event_directory,
    create_type_directory,
    create_type_file,
    create_type_tree,
    read_event_file,
    read_type_file,
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


def test_create_event_directory():
    create_event_directory()


def test_create_event_file():
    create_event_file("Test")


def test_create_event_tree():
    create_event_tree("Test")


def test_read_event_file():
    read_event_file("Test", Event("", datetime(2021, 9, 29, 20, 30), datetime(2021, 9, 29, 20, 45), "", ""))
