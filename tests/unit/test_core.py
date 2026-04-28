import pytest
from src.calculator import add,supstract,multiply,divide


# Using Parametrize to test many cases at once
@pytest.mark.parametrize("a,b,expected",[(1,5,6),
                                         (-2,10,8),
                                         (3.4,6.4),
                                         (0,6,6)])

def test_add(a,b,expected):
    assert add(a,b) == expected


