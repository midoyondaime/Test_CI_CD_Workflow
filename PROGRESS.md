# Simple Calculator - Progress Log

## Week 2: Testing Fundamentals + First Project ✅ COMPLETE

**Session:** 2026-04-28 (One Day)

### What Was Done:

#### 1. **Learn Phase - Testing Fundamentals**
- Studied unit, integration, acceptance tests
- Learned test structure (Arrange-Act-Assert)
- Understood assertions and test metrics
- Documented in `notes/testing-fundamentals.md`

#### 2. **Apply Phase - Calculator Core**
- Implemented 4 core functions:
  - `add(a, b)` - addition
  - `subtract(a, b)` - subtraction
  - `multiply(a, b)` - multiplication
  - `divide(a, b)` - division with error handling
- Built professional project structure: `src/calculator/`, `tests/unit/`

#### 3. **Apply Phase - Comprehensive Tests**
- **11 tests passing** ✅
- **Parametrized tests:** `test_add()` (4 cases), `test_multiply()` (4 cases)
- **Fixture-based tests:** `test_substract()`, `test_devide()` with reusable data
- **Exception testing:** `test_divide_by_zero()` using `pytest.raises()`
- **Float handling:** Used `pytest.approx()` with custom tolerance

#### 4. **Understand Phase - Documentation**
- Created `notes/testing-fundamentals.md` - Core concepts
- Created `notes/deep-dive-fundamentals.md` - Trade-offs and decisions
- Documented when to test and when to skip
- Explained benefits of testing and design choices

#### 5. **Git Workflow**
```bash
$ git log --oneline
2e8e8f0 Added the test_devide functions
da765af Added a new fixture for the divide test
685740b Changed the divide function using raise not return
52515f1 Added the substract test using a fixture
d57ff04 Fixed a typo in conftest.py
a4eb486 Fixed some importation problem in the file
19e85a8 Updated pytest.ini
5263f51 Added pytest.ini to the root project
09d71c9 Adding .gitignore file
1ae1a54 Added a fixture in conftest.py to use them later
74ab30e Added the test_add function using parametrization
d945f82 initialisation of tests directory
299307f Created the calculator app with all operations + __init__ file
```
**Total: 13 clean, intentional commits**

### Test Results:
```bash
$ pytest tests/unit/test_core.py -v
11 passed in 0.02s ✅
```

### Project Structure:
```
simple-calculator/
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── core.py (4 functions, all tested)
├── tests/
│   └── unit/
│       ├── __init__.py
│       ├── conftest.py (fixtures)
│       └── test_core.py (11 tests)
├── pytest.ini
├── .gitignore
└── .git/ (13 commits)
```

### Learning Outcomes:

**Concepts Mastered:**
- ✅ Parametrized testing (test multiple cases efficiently)
- ✅ Fixtures (organize and reuse test data)
- ✅ Exception assertions (`pytest.raises()`)
- ✅ Float comparison (`pytest.approx()`)
- ✅ Test-Driven Development mindset
- ✅ When to test, when to skip

**Professional Practices:**
- ✅ Clean git history with meaningful commits
- ✅ Professional project structure
- ✅ Proper separation: `src/` (code) vs `tests/` (tests)
- ✅ Configuration files (pytest.ini, .gitignore)
- ✅ Documentation of design decisions

### Next Week (Week 3):
- Advanced Fixtures & Mocking
- Complex fixture dependency chains
- Mocking external services
- Refactor tests for maintainability

---

**Status:** Week 2 Complete ✅  
**Tests Passing:** 11/11 ✅  
**Commits:** 13 ✅  
**Ready for Week 3:** Yes ✅

---

**Last Updated:** 2026-04-28
