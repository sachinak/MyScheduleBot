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
"""
TESTING Find available time based on the preferred time and events
"""

from datetime import datetime
import sys
import os
from Event import Event
from datetime import datetime
from functionality.FindAvailableTime import findInter, findIntersection

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../src"))

def test_find_one():
    elist = []
    # Create one event
    start = "2021-11-01 11:00:00"
    end = "2021-11-01 12:00:00"
    e1 = Event("Make test cases", start, end, 1, "homework", "Make test cases for my code in SE")
    elist.append(e1)
    date = "11/01/21"
    range1 = datetime.strptime("11/01/21 10:00 am", "%m/%d/%y %I:%M %p")
    range2 = datetime.strptime("11/01/21 06:00 pm", "%m/%d/%y %I:%M %p")
    inte = findIntersection(date, range1, range2, elist)
    assert len(inte) == 2
    msg = inte[0].get('start').strftime("%Y-%m-%d %H:%M:%S") + " - " + inte[0].get('end').strftime("%Y-%m-%d %H:%M:%S")
    assert msg == "2021-11-01 10:00:00 - 2021-11-01 11:00:00"
    msg = inte[1].get('start').strftime("%Y-%m-%d %H:%M:%S") + " - " + inte[1].get('end').strftime("%Y-%m-%d %H:%M:%S")
    assert msg == "2021-11-01 12:00:00 - 2021-11-01 18:00:00"



def test_find():
    elist = []
    # Create two events
    start = "2021-11-01 11:00:00"
    end = "2021-11-01 12:00:00"
    e1 = Event("Make test cases", start, end, 1, "homework", "Make test cases for my code in SE")
    elist.append(e1)
    start = "2021-11-01 13:30:00"
    end = "2021-11-01 14:00:00"
    e2 = Event("Make another test cases", start, end, 1, "homework", "Make another test cases for my code in SE")
    elist.append(e2)
    date = "11/01/21"
    range1 = datetime.strptime("11/01/21 10:00 am", "%m/%d/%y %I:%M %p")
    range2 = datetime.strptime("11/01/21 06:00 pm", "%m/%d/%y %I:%M %p")
    inte = findIntersection(date, range1, range2, elist)
    assert len(inte) == 3
    msg = inte[0].get('start').strftime("%Y-%m-%d %H:%M:%S") + " - " + inte[0].get('end').strftime("%Y-%m-%d %H:%M:%S")
    assert msg == "2021-11-01 10:00:00 - 2021-11-01 11:00:00"
    msg = inte[1].get('start').strftime("%Y-%m-%d %H:%M:%S") + " - " + inte[1].get('end').strftime("%Y-%m-%d %H:%M:%S")
    assert msg == "2021-11-01 12:00:00 - 2021-11-01 13:30:00"
    msg = inte[2].get('start').strftime("%Y-%m-%d %H:%M:%S") + " - " + inte[2].get('end').strftime("%Y-%m-%d %H:%M:%S")
    assert msg == "2021-11-01 14:00:00 - 2021-11-01 18:00:00"



