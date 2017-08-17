import pytest

import helpers


def test_sum():
    assert helpers.sum(4, 6) == 10


def test_subtract():
    assert helpers.subtract(6, 2) == 4


@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 0.5),
    (10, 5, 2),
    (9, 3, 3),
])
def test_divide(a, b, expected):
    assert helpers.divide(a, b) == expected


def test_multiply():
    assert helpers.multiply(6, 2) == 12
