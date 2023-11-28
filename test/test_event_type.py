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
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../src"))
import datetime
import string
from random import randint, choices
import pytest
from event_type import event_type

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


def test_str():
    start = random_datetime()
    end = random_datetime()
    temp_type = event_type("Homework", start, end)
    actual_data= "Homework "+ str(start) +" "+str(end)
    assert actual_data == str(temp_type)
      
def test_get_end_time():
    start = random_datetime()
    end = random_datetime()
    temp_type = event_type("Homework", start, end)
    actual_data= end.strftime('%I:%M %p')
    assert actual_data == temp_type.get_end_time()
        
def test_get_start_time():
    start = random_datetime()
    end = random_datetime()
    temp_type = event_type("Homework", start, end)
    actual_data= start.strftime('%I:%M %p')
    assert actual_data == temp_type.get_start_time()

        
def test_list_type():
    start = random_datetime()
    end = random_datetime()
    temp_type = event_type("Homework", start, end)
    actual_data= ["Homework", start.strftime('%I:%M %p'), temp_type.get_end_time()]
    assert actual_data==temp_type.to_list_event()
      
