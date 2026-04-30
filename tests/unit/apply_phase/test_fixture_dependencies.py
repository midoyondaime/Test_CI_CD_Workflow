import pytest
from calculator.history import OperationHistory
from calculator.core import Calculator

class TestCalculWithHistory():
    def test_basic_calculator(self,Cal,history_1):
        assert history_1.count() == 0
        assert Cal.add(1,2) == 3
        assert Cal.substract(1,2) == -1
        assert Cal.multiply(1,2) == 2
        assert history_1.get_last() == {"operation": "1 * 2", "result": 2}
        assert Cal.divide(1,2) == 0.5
        assert history_1.count() == 4

    def test_large_numbers(self,Cal,history_1):
        assert history_1.count() == 0
        assert Cal.add(1000,2) == 1002
        assert Cal.substract(1000,2) == 998
        assert Cal.multiply(100000,2) == 200000
        assert history_1.get_last() == {"operation": "100000 * 2", "result": 200000}
        assert Cal.divide(10000,2) == 5000
        assert history_1.count() == 4


