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

# Test if event starts and ends on the same day
def test_start_and_end():
    # pick a random date
    day1 = random_date()
    # ending date is the same
    day2 = day1

    # for testing porpose, assume today is the same day
    today = day1
    assert check_start_or_end([day1, day2], today) == 1


# Test if event starts today but ends later
def test_ends_later():
    # Pick two random dates
    day1 = random_date()
    day2 = random_date()

    # day 1 should be the minimum of the two dates
    # day 2 should be the maximum
    day1, day2 = min(day1, day2), max(day1, day2)

    # For testing, assume today is the first day
    today = day1

    assert check_start_or_end([day1, day2], today) == 2

# Test if event started on an earlier date but ends today
def test_started_earlier():
    # pick two random dates
    day1 = random_date()
    day2 = random_date()

    # day 1 is the minimum of the two, day 2 is the maximum
    day1, day2 = min(day1, day2), max(day1, day2)

    # for testing, assume day 2 is today
    today = day2

    assert check_start_or_end([day1, day2], today) == 3

# Test if no event is scheduled for today
def test_no_event():
    # pick two random dates
    day1 = random_date()
    day2 = random_date()

    day1, day2 = min(day1, day2), max(day1, day2)

    # for testing, assume today to be a random date in the
    # range of year 2018-2019
    today = random_date(2018, 2019)

    assert check_start_or_end([day1, day2], today) == 0