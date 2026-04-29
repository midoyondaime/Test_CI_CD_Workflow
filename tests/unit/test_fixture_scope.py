"""
Demonstrates fixture scope: when fixtures are created and destroyed.

Run with: pytest tests/unit/test_fixture_scope.py -v -s
The -s flag shows print() output so you can SEE when setup/teardown runs.
"""

import pytest


def test_1_fresh_log(fresh_log):
    """Fresh log — created just for this test."""
    fresh_log.append("operation 1")
    assert len(fresh_log) == 1
    print(f"  Test 1: fresh_log has {fresh_log}")


def test_2_fresh_log(fresh_log):
    """Fresh log — a BRAND NEW one, not the same as test_1!"""
    # fresh_log is empty here, even though test_1 added to it
    assert len(fresh_log) == 0
    fresh_log.append("operation 2")
    assert len(fresh_log) == 1
    print(f"  Test 2: fresh_log has {fresh_log}")


def test_3_module_log(operation_log):
    """Module log — shared across all tests in this file."""
    operation_log.append("operation A")
    assert len(operation_log) == 1
    print(f"  Test 3: operation_log has {operation_log}")


def test_4_module_log(operation_log):
    """Module log — SAME one as test_3! Still has previous data."""
    # operation_log has the data from test_3!
    assert len(operation_log) == 1  # Still just 1 from test_3
    operation_log.append("operation B")
    assert len(operation_log) == 2
    print(f"  Test 4: operation_log has {operation_log}")


def test_5_module_log(operation_log):
    """Module log — STILL the same fixture."""
    assert len(operation_log) == 2  # Data from test_3 AND test_4
    operation_log.append("operation C")
    assert len(operation_log) == 3
    print(f"  Test 5: operation_log has {operation_log}")
