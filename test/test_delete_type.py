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
from functionality.delete_event_type import delete_type, print_type

def test_delete_type():
    rows=[['hw1', '10:10 am', '12:10 pm'], ['hw2', '11:10 am', '12:20 pm']]
    msg_content1 = "hw1"
    msg_content2= "hw3"
    assert delete_type(rows, msg_content1)== [[['hw2', '11:10 am', '12:20 pm']], 1, 1]
   
def test_delete_type():
    rows=[['hw1', '10:10 am', '12:10 pm'], ['hw2', '11:10 am', '12:20 pm']]
    msg_content1 = "hw1"
    msg_content2= "hw3"
    assert delete_type(rows, msg_content2)== [[['hw1', '10:10 am', '12:10 pm'], ['hw2', '11:10 am', '12:20 pm']], 0, 2]


def test_print_type():
    rows=[['hw1', '10:10 am', '12:10 pm']]
    assert print_type(rows) == [[['hw1', '10:10 am', '12:10 pm']], '\nEvent Type: hw1 prefered time range from 10:10 am to 12:10 pm']
