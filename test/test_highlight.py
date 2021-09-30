# From https://stackoverflow.com/questions/25827160/importing-correctly-with-pytest
# Change current working directory so test case can find the source files
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../src"))

import pytest
import datetime

from random import randint
from functionality.highlights import check_start_or_end


NUM_ITER = 1000


# Generate one random datetime object between an uniform range
def random_datetime(start = 2020, end = 2025):
    # Determine all posible days between the start and end
    start = datetime.date(start, 1, 1)
    end = datetime.date(end, 12, 31)

    # Give me one of them at random
    choices = end - start
    chosen_day = randint( 0, choices.days )

    # Randomly pick a time
    h = randint(0, 23)
    m = randint(0, 59)

    # Get the random date
    date = start + datetime.timedelta(days = chosen_day)

    # add time
    return datetime.datetime(date.year, date.month, date.day, h, m)



print(random_datetime())