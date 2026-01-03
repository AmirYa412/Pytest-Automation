# Unit Testing Framework - Demo Project

A professional unit testing framework demonstrating best practices for Python testing with pytest, showcasing various mocking patterns and test organization strategies.

> **Note:** This is a demonstration project with dummy classes designed for practicing test automation patterns. The API endpoints don't exist - all HTTP calls are mocked in tests.

## 📋 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Key Testing Patterns Demonstrated](#-key-testing-patterns-demonstrated)
- [Coverage](#-coverage)
- [Resources](#-resources)

---



## 📋 Overview

This framework demonstrates:

- ✅ **Multiple Mocking Strategies** - `pytest-mock`, `responses`, `MagicMock`
- ✅ **Parametrized Tests** - Data-driven testing with `@pytest.mark.parametrize`
- ✅ **Clean Test Organization** - Separation by concern (auth, photos, pagination)
- ✅ **Professional Patterns** - Fixtures, custom exceptions, type hints
- ✅ **Realistic Scenarios** - Token management, pagination, retry logic

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.14 | Programming language |
| **pytest** | Latest | Test framework |
| **pytest-mock** | 3.15.1 | Method/object mocking |
| **responses** | 0.25.8 | HTTP mocking |
| **pytest-cov** | 7.0.0 | Coverage reporting |

---

## 📁 Project Structure
```
unit_tests/
├── src/
│   ├── exceptions/
│   │   └── google_exceptions.py    # Custom exceptions
│   ├── google/
│   │   ├── google_auth.py          # Auth client with token management
│   │   └── google_photos.py        # Photos client with pagination
│   ├── integers/
│   │   └── integers.py             # Simple math operations
│   └── strings/
│       └── convert_string.py       # String manipulation
│
├── tests/
│   ├── google/
│   │   ├── test_authentication.py  # Auth & token tests (18 tests)
│   │   └── test_google_photos.py   # Photo & pagination tests (27 tests)
│   ├── integers/
│   │   └── test_integers.py        # Math tests
│   └── strings/
│       └── test_strings.py         # String tests
│
├── utils/
│   └── mocks/
│       └── google_mocks.py         # Mock data generators
│
├── conftest.py                     # Shared fixtures
├── pytest.ini                      # Pytest configuration
└── requirements.txt                # Dependencies
```

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd unit_tests
pip install -r requirements.txt
```

### 2. Run Tests
```bash
# All tests
pytest tests/ -v

# Specific file
pytest tests/google/test_authentication.py -v

# With coverage
pytest tests/ --cov=src --cov-report=html
```

---

## 🎯 Key Testing Patterns Demonstrated

### 1. **HTTP Mocking with `responses`**
```python
@responses.activate
def test_login_success(self):
    responses.add(responses.POST, url, json=mock_data, status=200)
    result = client.login()  # No real HTTP call!
```

### 2. **Method Mocking with `pytest-mock`**
```python
def test_get_photos(self, mocker):
    mocker.patch.object(client, 'fetch_data', return_value=mock_data)
    photos = client.get_user_google_photos()
```

### 3. **Parametrized Tests**
```python
@pytest.mark.parametrize("page,expected", [(1, 10), (2, 10), (3, 5)])
def test_pagination(self, mocker, page, expected):
    result = client.get_photos_paginated(page=page)
    assert len(result["photos"]) == expected
```

### 4. **Exception Testing**
```python
def test_invalid_page_raises_error(self):
    with pytest.raises(PaginationError) as exc_info:
        client.get_photos_paginated(page=-1)
    assert "Page number must be >= 1" in str(exc_info.value)
```

---

## 📈 Coverage

Generate coverage report:
```bash
pytest tests/ --cov=src --cov-report=html --cov-report=term-missing
open htmlcov/index.html
```


## 📚 Resources

- **Pytest Documentation:** https://docs.pytest.org/
- **pytest-mock:** https://pytest-mock.readthedocs.io/
- **responses Library:** https://github.com/getsentry/responses

---
