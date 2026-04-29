"""
Demonstrates MOCKING with pytest-mock: replacing external dependencies with fake objects.

Mocks are useful for:
1. Speed (no real database/API calls)
2. Isolation (test only your code, not dependencies)
3. Verification (check that your code calls dependencies correctly)

Using pytest-mock (cleaner than unittest.mock in pytest):
- mocker fixture handles mock creation and cleanup
- More readable syntax

Run with: python3 -m pytest tests/unit/test_mocking.py -v -s
"""

import pytest


class TestMockHistoryBasics:
    """Tests using pytest-mock via the mocker fixture."""

    def test_add_calls_mock_history(self, calculator, mocker):
        """Verify that add() calls history.log() with correct args."""
        # Create a mock for the history
        mock_history = mocker.Mock()
        calculator.history = mock_history

        result = calculator.add(2, 3)

        assert result == 5
        # Verify the mock was called once
        mock_history.log.assert_called_once_with("2 + 3", 5)

    def test_multiply_calls_mock_history(self, calculator, mocker):
        """Verify multiply calls history with correct operation."""
        mock_history = mocker.Mock()
        calculator.history = mock_history

        calculator.multiply(4, 5)

        # Was log() called? How many times? With what arguments?
        mock_history.log.assert_called_once_with("4 * 5", 20)

    def test_multiple_calls_tracked(self, calculator, mocker):
        """Mock tracks all calls, not just the last one."""
        mock_history = mocker.Mock()
        calculator.history = mock_history

        calculator.add(1, 1)
        calculator.multiply(2, 2)
        calculator.substract(5, 3)

        # How many times was log() called?
        assert mock_history.log.call_count == 3

        # What were the calls? (in order)
        calls = mock_history.log.call_args_list
        assert calls[0][0] == ("1 + 1", 2)      # First call: add
        assert calls[1][0] == ("2 * 2", 4)      # Second call: multiply
        assert calls[2][0] == ("5 - 3", 2)      # Third call: substract


class TestMockHistoryVerification:
    """More advanced mocking: verification patterns."""

    def test_history_not_called_without_operation(self, mocker):
        """Calculator with no operations means history is not called."""
        from calculator.core import Calculator

        # Create a calculator with a mock
        mock_history = mocker.Mock()
        calc = Calculator(history=mock_history)

        # No operations performed, so history should not be called
        assert mock_history.log.call_count == 0
        mock_history.log.assert_not_called()

    def test_divide_by_zero_does_not_log(self, calculator, mocker):
        """If an operation fails, history should not be logged."""
        mock_history = mocker.Mock()
        calculator.history = mock_history

        try:
            calculator.divide(10, 0)
        except ValueError:
            pass

        # History should NOT have been called (because divide failed)
        mock_history.log.assert_not_called()


class TestMockWithSideEffects:
    """Mocks can simulate complex behavior."""

    def test_history_raises_exception(self, mocker):
        """Simulate history service failing (e.g., database offline)."""
        from calculator.core import Calculator

        # Create a mock that raises an exception when log() is called
        mock_history = mocker.Mock()
        mock_history.log.side_effect = Exception("Database offline!")

        calc = Calculator(history=mock_history)

        # When calculator tries to log, the mock raises an exception
        with pytest.raises(Exception, match="Database offline"):
            calc.add(1, 2)

    def test_history_returns_custom_values(self, mocker):
        """Mocks can return custom values."""
        from calculator.core import Calculator

        mock_history = mocker.Mock()
        # Set up mock to return different values on successive calls
        mock_history.get_last.side_effect = [
            {"operation": "1 + 1", "result": 2},
            {"operation": "2 + 2", "result": 4},
        ]

        calc = Calculator(history=mock_history)
        calc.add(1, 1)

        # First call to get_last() returns the first value
        first = mock_history.get_last()
        assert first["result"] == 2

        # Second call returns the second value
        second = mock_history.get_last()
        assert second["result"] == 4
