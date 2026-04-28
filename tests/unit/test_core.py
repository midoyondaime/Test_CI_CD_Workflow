import pytest
from pytest import approx
from calculator.core import add,substract


# Using Parametrize to test many cases at once
@pytest.mark.parametrize("a,b,expected",[(1,5,6),
                                         (-2,10,8),
                                         (3.4,6.4,9.8),
                                         (0,6,6)])

def test_add(a,b,expected):
    assert add(a,b) == expected


def test_substract(fixture_substract):
    for element in fixture_substract:
        assert substract(element[0],element[1]) == approx(element[2])

