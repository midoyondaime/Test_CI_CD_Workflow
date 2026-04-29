import pytest
from pytest import approx
from calculator.core import add,substract,multiply, divide


# Using Parametrize to test many cases at once
@pytest.mark.parametrize("a,b,expected",[(1,5,6),
                                         (-2,10,8),
                                         (3.4,6.4,9.8),
                                         (0,6,6)])

def test_add(a,b,expected):
    assert add(a,b) == expected


# Used a fixture
def test_substract(fixture_substract):
    for element in fixture_substract:
        assert substract(element[0],element[1]) == approx(element[2])


# Using Parametrize to test many cases at once
@pytest.mark.parametrize("a,b,expected",[(1,5,5),
                                         (-2,10,-20),
                                         (4,6.5,26),
                                         (0,6,0)])
def test_multiply(a,b,expected):
    assert multiply(a,b) == expected 





def test_devide(fixture_devide):
    for element in fixture_devide:
        assert divide(element[0],element[1]) == approx(element[2],abs=0.1)


def test_divide_by_zero():
       with pytest.raises(ValueError):
        divide(10, 0)


