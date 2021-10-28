import sys, os

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../src"))

import pytest
import pandas as pd
from functionality.import_file import verify_csv, convert_time


def test_time():
    old_time = "1998-05-08 10:30:00"
    new_time = convert_time(old_time)

    assert "05/08/98 10:30am" == new_time


def test_time_pm():
    old_time = "1998-05-08 18:30:00"
    new_time = convert_time(old_time)

    assert "05/08/98 6:30pm" == new_time


def test_working_csv():
    data = {'ID': [''],
            'Name': ['test'],
            'Start Date': ["1998-05-08 18:30:00"],
            'End Date': ["1998-05-08 18:45:00"],
            'Type': '',
            'Notes': ''}

    table = pd.DataFrame(data=data)

    assert verify_csv(table)


def test_typo_csv():
    data = {'ID': [''],
            'Name': ['test'],
            'Stert Date': ["1998-05-08 18:30:00"],
            'End Date': ["1998-05-08 18:45:00"],
            'Type': '',
            'Notes': ''}

    table = pd.DataFrame(data=data)

    assert not verify_csv(table)