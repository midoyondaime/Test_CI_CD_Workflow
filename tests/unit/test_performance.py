"""Performance & Scale Testing for Calculator.

Demonstrates performance testing levels:
1. Benchmarking — measure individual operation speed
2. Load testing — system stability under repeated operations
"""

import time
import pytest
from calculator.core import Calculator


class TestBenchmarking:
    """Level 1: Simple benchmarks using time.perf_counter()"""

    def test_add_performance(self):
        """Addition should complete in microseconds."""
        calc = Calculator()
        # time.time() is unreliabe for intervals)
        # time.perf_counter() is designed to be immune
        start = time.perf_counter()
        result = calc.add(5, 3)
        duration = time.perf_counter() - start

        assert result == 8
        assert duration < 0.001  # Less than 1ms

    def test_multiply_performance(self):
        """Multiplication should complete in microseconds."""
        calc = Calculator()
        start = time.perf_counter()
        result = calc.multiply(10, 20)
        duration = time.perf_counter() - start

        assert result == 200
        assert duration < 0.001

    def test_divide_performance(self):
        """Division (with float conversion) should still be < 1ms."""
        calc = Calculator()
        start = time.perf_counter()
        result = calc.divide(10, 3)
        duration = time.perf_counter() - start

        assert abs(result - 3.333) < 0.01
        assert duration < 0.001


class TestLoadTesting:
    """Level 2: Load testing — repeated operations should scale linearly."""

    def test_repeated_operations(self):
        """1000 operations should complete in milliseconds."""
        calc = Calculator()
        operations = 1000

        start = time.perf_counter()
        for i in range(operations):
            calc.add(i, i + 1)
        duration = time.perf_counter() - start

        assert duration < 0.1  # Less than 100ms for 1000 operations
        assert (duration / operations) * 1_000_000 < 100  # < 100µs per operation

    def test_mixed_operations(self):
        """Realistic mix of operations should scale linearly."""
        calc = Calculator()

        start = time.perf_counter()
        for i in range(100):
            calc.add(i, 5)
            calc.multiply(i, 2)
            calc.substract(i, 3)
            calc.divide(i + 1, 2)
        duration = time.perf_counter() - start

        assert duration < 0.05  # Less than 50ms


    def test_calculator_stability_under_load(self):
        """10k operations shouldn't degrade performance."""
        calc = Calculator()
        iterations = 10_000

        # First half
        start = time.perf_counter()
        for i in range(iterations // 2):
            calc.add(i, 1)
        time_first_half = time.perf_counter() - start

        # Second half
        start = time.perf_counter()
        for i in range(iterations // 2, iterations):
            calc.add(i, 1)
        time_second_half = time.perf_counter() - start

        # Second half should not be significantly slower (< 2x)
        assert time_second_half < time_first_half * 2.0

    def test_calculator_memory_consistency(self):
        """Many operations shouldn't leak memory (basic check)."""
        import sys

        calc = Calculator()

        # Take baseline
        baseline = sys.getsizeof(calc)

        # Do lots of operations
        for i in range(1000):
            calc.add(i, i)

        # Size shouldn't grow significantly
        # (Calculator doesn't store results, so size stays constant)
        assert sys.getsizeof(calc) == baseline


# Benchmark summary for future reference
# Expected on modern hardware (< 0.1ms per operation):
# - add/subtract: ~1µs
# - multiply: ~1µs
# - divide: ~5µs (due to float conversion)
# - 1000 operations: < 10ms
# - 10000 operations: < 100ms
