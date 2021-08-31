from increment import *


def test_answer1():
    assert inc(3) != 5


def test_answer2():
    assert inc(3) != 2


def test_answer3():
    assert inc(3) != 3.1


def test_answer4():
    assert inc(3) != 2.9


def test_answer5():
    assert inc(3) == 4


def test_answer6():
    assert inc(2.9) == 3.9
