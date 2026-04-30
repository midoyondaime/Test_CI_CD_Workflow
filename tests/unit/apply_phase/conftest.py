import pytest
# import mocker
from calculator.history import OperationHistory
from calculator.core import Calculator



# ============================================
# Fixtures for the test_fixture_scope.py
# ============================================

@pytest.fixture(scope="module")
def history():
    """Module scope: created ONCE per test file, reused across all tests.
    Notice how state accumulates across tests."""
    print("\n[SETUP] Creating history (runs once per file)")
    H = OperationHistory()
    yield H
    print("\n[TEARDOWN] history")


@pytest.fixture(scope="function")
def calculator_with_history(history):
    """Calculator using module-scoped history (shared across tests)."""
    C = Calculator(history=history)
    yield C

@pytest.fixture(scope="function")
def calculator_without_history():
    print("\nStarting Processing the Calculator 2")
    C = Calculator()
    yield  C
    print("\nDone Processing the History 2")


@pytest.fixture(scope="function")
def fresh_history():
    """Function scope: created BEFORE each test, destroyed AFTER.
    Notice how state resets for each test."""
    print("\n[SETUP] Creating fresh_history (runs for each test)")
    H = OperationHistory()
    yield H
    print("\n[TEARDOWN] fresh_history")


@pytest.fixture(scope="function")
def calculator_with_fresh(fresh_history):
    """Calculator using function-scoped history (fresh per test)."""
    C = Calculator(history=fresh_history)
    yield C



# ============================================
# Fixtures for the test_fixture_dependencies.py
# ============================================

@pytest.fixture
def history_1():
    HH = OperationHistory()
    yield HH

@pytest.fixture
def Cal(history_1):
    X = Calculator(history=history_1)
    yield X  


@pytest.fixture
def Cal_no_history():
    return Calculator()


# ============================================
# Fixtures for the test_mocking_advanced.py
# ============================================

@pytest.fixture
def mock_history(mocker):
    mock = mocker.Mock()
    return mock

@pytest.fixture
def calculator_with_mock(mock_history):
    CC = Calculator(history=mock_history)
    return CC



# ============================================
# Fixtures for the test_parametrized.py
# ============================================

@pytest.fixture(params=[1,2,3,4])
def param_fixture(request):
    return request.param

