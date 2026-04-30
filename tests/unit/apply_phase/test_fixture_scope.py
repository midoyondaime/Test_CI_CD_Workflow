import pytest
from calculator.history import OperationHistory
from calculator.core import Calculator


# ============================================
# MODULE SCOPE TESTS: State accumulates!
# ============================================

def test_1_module_scope_first(calculator_with_history, history):
    """First test with module-scoped history.
    History count starts at 0 (first test in file)."""
    assert history.count() == 0, "Module scope: first test, count should be 0"

    result = calculator_with_history.add(1, 3)
    assert result == 4
    assert history.count() == 1, "After add: count should be 1"


def test_2_module_scope_second(calculator_with_history, history):
    """Second test with module-scoped history.
    Notice: state ACCUMULATED from previous test!"""
    assert history.count() == 1, "Module scope: accumulated from previous test!"

    result = calculator_with_history.multiply(5, 4)
    assert result == 20
    assert history.count() == 2, "After multiply: count should be 2 (accumulated)"


def test_3_module_scope_third(calculator_with_history, history):
    """Third test with module-scoped history.
    State continues to accumulate."""
    assert history.count() == 2, "Module scope: still accumulated!"

    result = calculator_with_history.divide(-4, 4)
    assert result == -1
    assert history.count() == 3, "After divide: count should be 3"


# ============================================
# FUNCTION SCOPE TESTS: State resets each test!
# ============================================

def test_1_function_scope_first(calculator_with_fresh, fresh_history):
    """First test with function-scoped history.
    History count starts at 0 (fresh for this test)."""
    assert fresh_history.count() == 0, "Function scope: fresh history for this test"

    result = calculator_with_fresh.add(10, 20)
    assert result == 30
    assert fresh_history.count() == 1


def test_2_function_scope_second(calculator_with_fresh, fresh_history):
    """Second test with function-scoped history.
    Notice: state RESET! It's a fresh history instance."""
    assert fresh_history.count() == 0, "Function scope: count resets to 0!"

    result = calculator_with_fresh.substract(100, 50)
    assert result == 50
    assert fresh_history.count() == 1


def test_3_function_scope_third(calculator_with_fresh, fresh_history):
    """Third test with function-scoped history.
    Fresh instance again."""
    assert fresh_history.count() == 0, "Function scope: fresh again!"

    result = calculator_with_fresh.multiply(7, 8)
    assert result == 56
    assert fresh_history.count() == 1
