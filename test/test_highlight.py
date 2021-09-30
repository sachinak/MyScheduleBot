# From https://stackoverflow.com/questions/25827160/importing-correctly-with-pytest
# Change current working directory so test case can find the source files
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../src"))

import pytest
import datetime

from random import randint
from functionality.highlights import check_start_or_end, convert_to_12


NUM_ITER = 1000


# Generate one random datetime object between an uniform range
def random_date(start = 2020, end = 2025):
    # Determine all posible days between the start and end
    start = datetime.date(start, 1, 1)
    end = datetime.date(end, 12, 31)

    # Give me one of them at random
    choices = end - start
    chosen_day = randint( 0, choices.days )

    # Get the random date
    date = start + datetime.timedelta(days = chosen_day)

    # add time
    return str(datetime.datetime(date.year, date.month, date.day)).split()[0]


def test_start_and_end():
    day1 = random_date()
    day2 = day1

    today = day1
    assert check_start_or_end([day1, day2], today) == 1

def test_ends_later():
    day1 = random_date()
    day2 = random_date()

    day1, day2 = min(day1, day2), max(day1, day2)
    today = day1

    assert check_start_or_end([day1, day2], today) == 2

def test_started_earlier():
    day1 = random_date()
    day2 = random_date()

    day1, day2 = min(day1, day2), max(day1, day2)
    today = day2

    assert check_start_or_end([day1, day2], today) == 3

def test_no_event():
    day1 = random_date()
    day2 = random_date()

    day1, day2 = min(day1, day2), max(day1, day2)
    today = random_date(2018, 2019)

    assert check_start_or_end([day1, day2], today) == 0