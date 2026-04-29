"""
Demonstrates fixture dependencies: when one fixture uses another.

The calculator fixture depends on the history fixture.
Execution order: history is created FIRST, then calculator uses it.

Run with: python3 -m pytest tests/unit/test_fixture_dependencies.py -v -s
"""

import pytest


class TestCalculatorWithHistory:
    """Tests using the calculator fixture (which depends on history)."""

    def test_add_logs_to_history(self, calculator):
        """calculator fixture includes history dependency."""
        result = calculator.add(2, 3)

        assert result == 5
        assert calculator.history.count() == 1
        assert calculator.history.get_last()["result"] == 5

    def test_multiple_operations_logged(self, calculator):
        """History tracks multiple operations in order."""
        calculator.add(1, 1)
        calculator.multiply(2, 3)
        calculator.substract(10, 4)

        assert calculator.history.count() == 3
        # Verify operations in order
        entries = calculator.history.entries
        assert entries[0]["operation"] == "1 + 1"
        assert entries[1]["operation"] == "2 * 3"
        assert entries[2]["operation"] == "10 - 4"

    def test_divide_with_history(self, calculator):
        """Divide operation is also logged."""
        result = calculator.divide(10, 2)

        assert result == 5.0
        assert calculator.history.count() == 1
        assert calculator.history.get_last()["operation"] == "10 / 2"


class TestCalculatorWithoutHistory:
    """Tests using calculator_no_history fixture — faster, no logging."""

    def test_add_no_history(self, calculator_no_history):
        """Calculator works fine without history."""
        result = calculator_no_history.add(5, 5)
        assert result == 10
        # No history to check — simpler test

    def test_operations_no_history(self, calculator_no_history):
        """Multiple operations work without history."""
        assert calculator_no_history.add(1, 2) == 3
        assert calculator_no_history.multiply(3, 4) == 12
        assert calculator_no_history.substract(10, 3) == 7
