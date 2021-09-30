# From https://stackoverflow.com/questions/25827160/importing-correctly-with-pytest
# Change current working directory so test case can find the source files
import sys, os

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../src"))

import pytest
from datetime import datetime

from functionality.AddEvent import check_complete


def check_variables1():
    output = {
        "start": False,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": False,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "complete": False,
        "array": [],
    }
    return output


def check_variables2():
    output = {
        "start": True,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": False,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "complete": False,
        "array": [],
    }
    return output


def check_variables3():
    output = {
        "start": True,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": True,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "complete": True,
        "array": [],
    }
    return output


def check_variables4():
    output = {
        "start": True,
        "start_date": datetime(2021, 9, 29, 21, 30),
        "end": True,
        "end_date": datetime(2021, 9, 29, 23, 30),
        "complete": True,
        "array": ["Hello"],
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
            example1["complete"],
            example1["array"],
        )
    )
    assert not (
        check_complete(
            example2["start"],
            example2["start_date"],
            example2["end"],
            example2["end_date"],
            example2["complete"],
            example2["array"],
        )
    )
    assert check_complete(
        example3["start"],
        example3["start_date"],
        example3["end"],
        example3["end_date"],
        example3["complete"],
        example3["array"],
    )
    assert check_complete(
        example4["start"],
        example4["start_date"],
        example4["end"],
        example4["end_date"],
        example4["complete"],
        example4["array"],
    )
