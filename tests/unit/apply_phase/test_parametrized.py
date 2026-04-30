import pytest
from calculator.core import Calculator



def test_multiple_fixture(calculator_no_history,param_fixture):

    assert calculator_no_history.add(1,param_fixture) == 1 + param_fixture
    assert calculator_no_history.multiply(5,param_fixture) == 5 * param_fixture

