from maths import math


def test_add():
    assert math.add(7, 3) == 10
    assert math.add(7) == 9
    assert math.add(5) == 7


def test_product():
    assert math.product(7, 3) == 21
    assert math.product(7) == 14
    assert math.product(5) == 1