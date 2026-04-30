# Week 3 Apply Phase: Advanced Fixtures & Mocking

## Your Task

Write test files that demonstrate:
1. **Fixture scope** (function vs module)
2. **Fixture dependencies** (fixtures using other fixtures)
3. **Mocking external services** (using pytest-mock)
4. **Parameterized fixtures** (running same test with multiple inputs)

---

## Deliverables

### File 1: `test_fixture_scope.py`

**Goal:** Demonstrate the difference between function and module scope.

**Requirements:**
- Create 2 fixtures: one with `scope="function"`, one with `scope="module"`
- Write tests that show:
  - Function scope = fresh instance per test
  - Module scope = reused across all tests in the file
- Include print statements to show when setup/teardown runs
- Run with `-s` flag to see the output

**Expected behavior:**
- Function scope tests should each start fresh
- Module scope tests should accumulate state

---

### File 2: `test_fixture_dependencies.py`

**Goal:** Demonstrate fixtures that depend on other fixtures.

**Requirements:**
- Create a `history` fixture that returns a real `OperationHistory`
- Create a `calculator` fixture that depends on `history`
- Create a `calculator_no_history` fixture (independent)
- Write test classes:
  - `TestCalculatorWithHistory` — tests using the calculator with history dependency
  - `TestCalculatorWithoutHistory` — tests without history
- Verify that the calculator correctly logs operations to history

**Expected behavior:**
- `calculator` fixture injects `history` automatically
- Each test gets a fresh calculator (function scope)
- Operations are logged and can be verified

---

### File 3: `test_mocking_advanced.py`

**Goal:** Mock external services using pytest-mock.

**Requirements:**
- Create a `mock_history` fixture using `mocker.Mock()`
- Create a `calculator_with_mock` fixture that uses the mock
- Write tests that verify:
  - Calculator calls `history.log()` with correct arguments
  - Track multiple calls to history
  - Verify when history is NOT called (error cases)
  - Simulate history failures (side effects)
- Use `assert_called_once_with()` and `assert_called()` patterns

**Expected behavior:**
- Mocks should respond instantly (no real OperationHistory)
- Tests should verify the calculator *calls* history correctly
- Can test error scenarios without real database

---

### File 4: `test_parameterized.py`

**Goal:** Use parameterized fixtures to run tests multiple times.

**Requirements:**
- Create a parameterized fixture with multiple test values
- Write tests that use this fixture
- At least one fixture with `params=[...]` that provides multiple values
- At least 2 different test functions using different parameterized fixtures

**Expected behavior:**
- Each test runs multiple times (once per param value)
- Each iteration gets a fresh calculator

---

## Structure

```
tests/unit/apply_phase/
├── SPEC.md (this file)
├── test_fixture_scope.py
├── test_fixture_dependencies.py
├── test_mocking_advanced.py
└── test_parameterized.py
```

---

## Acceptance Criteria

- ✅ All tests pass
- ✅ At least 20 tests total across all files
- ✅ Clear docstrings explaining what each test demonstrates
- ✅ Proper use of fixtures (scope, dependencies, mocking)
- ✅ pytest-mock used for all mocking (not unittest.mock)
- ✅ Can run with `pytest tests/unit/apply_phase/ -v`

---

## Tips

1. **Reuse fixtures from conftest.py** — `calculator`, `history`, `calculator_no_history` are already defined
2. **Add new fixtures locally** — specific fixtures for parameterization can go in each test file
3. **Reference notes** — check `notes/fixtures-mocking.md` for syntax and patterns
4. **Run and verify** — test often, commit after each file is done
5. **Use `-s` flag** — `pytest -v -s` to see print output for debugging

---

## Next Step

Start with `test_fixture_scope.py` — show when fixtures are created/destroyed.

Good luck! 🎯
