import pytest


@pytest.fixture(scope="function")
def fixture_substract():
    data = [[1,4,-3],
            [-5,-1,-4],
            [0,7,-7],
            [1.5,1.3,0.2]]

    yield data


@pytest.fixture(scope="function")
def fixture_devide():
    data = [[2,4,0.5],
            [-5,-1,5],
            [0,7,-0],
            [1.5,2.1,0.7]]

    yield data


# NEW: Module scope — reused across all tests in this file
@pytest.fixture(scope="module")
def operation_log():
    """Simulates a history log that tracks all operations.
    Module scope = created ONCE per test file, reused for all tests.
    """
    log = []
    print("\n[SETUP] Creating operation_log (runs once per file)")
    yield log
    print(f"\n[TEARDOWN] operation_log has {len(log)} entries")


# NEW: Function scope — fresh for each test (default)
@pytest.fixture(scope="function")
def fresh_log():
    """Fresh log for each test. Better for isolation."""
    log = []
    print("\n[SETUP] Creating fresh_log (runs for each test)")
    yield log
    print(f"\n[TEARDOWN] fresh_log has {len(log)} entries")


# NEW: Fixture dependencies
from src.calculator.history import OperationHistory

@pytest.fixture(scope="function")
def history():
    """Fixture: Create a real OperationHistory for testing."""
    return OperationHistory()


@pytest.fixture(scope="function")
def calculator(history):
    """Fixture: Create a Calculator with the history fixture injected.

    This demonstrates fixture DEPENDENCIES:
    - history fixture is created first
    - calculator uses it
    - Execution order: history → calculator → test
    """
    from src.calculator.core import Calculator
    return Calculator(history=history)


@pytest.fixture(scope="function")
def calculator_no_history():
    """Fixture: Calculator without history (faster, isolated)."""
    from src.calculator.core import Calculator
    return Calculator(history=None)


# NEW: Mocking
from unittest.mock import Mock

@pytest.fixture(scope="function")
def mock_history():
    """Fixture: MOCK the history service.

    Instead of a real OperationHistory, we use a Mock object.
    This is useful when history might:
    - Log to a database (slow)
    - Log to an API (network dependency)
    - Log to a file (creates artifacts)

    The mock responds instantly and tracks calls.
    """
    return Mock()


@pytest.fixture(scope="function")
def calculator_with_mock(mock_history):
    """Fixture: Calculator using a MOCKED history service."""
    from src.calculator.core import Calculator
    return Calculator(history=mock_history)