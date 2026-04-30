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


class TestEdgeCases:
    """Edge case testing for comprehensive coverage."""

    def test_zero_handling(self):
        """Test operations with zero."""
        assert add(0, 5) == 5
        assert multiply(0, 100) == 0
        assert divide(0, 5) == 0.0

    def test_negative_numbers(self):
        """Test operations with negative numbers."""
        assert add(-5, 3) == -2
        assert substract(-5, 3) == -8
        assert multiply(-4, 5) == -20

    def test_float_division(self):
        """Test division with float results."""
        assert approx(divide(5, 2), abs=0.001) == 2.5
        assert approx(divide(10, 3), abs=0.01) == 3.333
