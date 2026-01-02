# API Test Automation Framework

A robust, scalable API testing framework built with Python and pytest, demonstrating professional test automation practices and design patterns.

## 📋 Table of Contents

- [Overview](##Overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Architecture & Design](#architecture--design)
- [Adding New Tests](#adding-new-tests)
- [Reporting](#reporting)
- [Additional Resources](##Additional Resources)

---

## 🎯 Overview

This framework tests the [Petstore Swagger API](https://petstore.swagger.io/) and demonstrates:

- ✅ **Clean Architecture** - Separation of concerns (models, support, tests)
- ✅ **Reusable Client** - Single HTTP client with session management
- ✅ **Smart Test Setup** - One client instance per test class with session reset
- ✅ **Schema Validation** - JSON Schema validation for API contracts
- ✅ **Retry Mechanism** - Automatic retry for transient failures
- ✅ **Security Best Practices** - Environment variables for credentials
- ✅ **Professional Reporting** - HTML test reports with pytest-html

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.14 | Programming language |
| **pytest** | 7.4+ | Test framework |
| **requests** | 2.32.5 | HTTP client library |
| **jsonschema** | 4.25.1 | JSON Schema validation |
| **python-dotenv** | 1.0+ | Environment variable management |
| **pytest-html** | 4.0+ | HTML test reporting |

**Tested on:** macOS Sequoia (15.2)

---

## 📁 Project Structure

```
api_tests/
├── __init__.py
├── conftest.py              # Pytest configuration & fixtures
├── pytest.ini               # Pytest settings
├── requirements.txt         # Project-specific dependencies
│
├── api_models/              # API endpoint models (one class per endpoint)
│   ├── __init__.py
│   ├── pet.py              # Pet endpoints (/pet, /pet/{id})
│   ├── store.py            # Store endpoints (/store/*)
│   └── user.py             # User endpoints (/user/*)
│
├── support/                 # Infrastructure & utilities
│   ├── __init__.py
│   ├── client.py           # HTTP client with retry logic
│   ├── environment.py      # Environment configuration
│   └── users.py            # User credentials management
│
├── tests/                   # Test files (test_*.py)
│   ├── __init__.py
│   ├── test_pet.py
│   ├── test_store.py
│   └── test_user.py
│
└── utils/                   # Helper utilities (if needed)
```

**Design Pattern:**
- `api_models/` - API endpoint definitions (what requests to make)
- `support/` - Utils and supporting functions (how to make requests)
- `tests/` - Test scenarios (what to assert)

---

## ✅ Prerequisites

- **Python 3.14** (or Python 3.11+ recommended for stability)
- **pip** (Python package manager)
- **Git** (for version control)
- **macOS, Linux, or Windows** (tested on macOS Sequoia)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-root>
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### 3. Install Dependencies

The project uses a two-tier requirements structure:

```bash
# Install API test requirements
# Note it will also install base-requirements.txt
cd api_tests
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
pytest --version
# Should show pytest version 7.4+
```

---

## ⚙️ Configuration

### Environment Variables & Security

The framework uses **environment variables** for sensitive data (passwords, API keys) following security best practices.
However, for simplicity, I used `.env` file to run the project out of the box.
For best practices, store both your environments URL and user credentials as environment variables in your CI/CD pipeline.


#### Security Best Practices Demonstrated

✅ **No hardcoded secrets** - All credentials from environment  
✅ **.env in .gitignore** - Prevents accidental commits  
✅ **Fail-fast validation** - Catches missing credentials early  
✅ **CI/CD ready** - Use environment variables in pipelines  
✅ **.env.example** - Template for required variables  

---

## 🚀 Running Tests

### Run All Tests

```bash
cd api_tests
pytest tests/ -v
```

### Run Specific Test File

```bash
pytest tests/test_pet.py -v
```

### Run Specific Test Class

```bash
pytest tests/test_pet.py::TestPet -v
```

### Run Specific Test Method

```bash
pytest tests/test_pet.py::TestPet::test_new_pet_creation -v
```

### Run Tests by Marker

```bash
# Run only API tests
pytest -m api -v
```

### Run Tests with HTML Report

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### Run Tests for Different Environment

```bash
# Test Production environment
pytest tests/ --api_env=petstore -v

# Test QA environment(qa-petstore is dummy environment!)
pytest tests/ --api_env=qa-petstore -v
```

---

## 🏗️ Architecture & Design

### Client Architecture

#### The Client Class (`support/client.py`)

**Purpose:** Central HTTP client with session management and built-in retry logic.

**Key Features:**

1. **Session Reuse**
   ```python
   self.session = requests.Session()
   # Reuses TCP connections = faster tests
   ```

2. **Automatic Retry Mechanism**
   ```python
   retry_strategy = Retry(
       total=3,              # 3 retries
       backoff_factor=1,     # 1s, 2s, 4s between retries
       status_forcelist=[502, 503, 504, 520, 524]  # Retry these codes
   )
   ```
   
   **Why?** Handles transient failures (network hiccups, server restarts) automatically.

3. **Session Reset**
   ```python
   def reset_session(self):
       """Clears cookies and resets headers after each test"""
       self.session.headers = self._default_headers.copy()
       self.session.cookies.clear()
   ```
   
   **Why?** Ensures test isolation - no state leaks between tests.

4. **All HTTP Methods Supported**
   - `get_request(path, params)`
   - `post_request(path, json, data)`
   - `put_request(path, json)`
   - `delete_request(path)`

**Inheritance Chain:**
```
Client (base) → Pet/Store/User (API models) → Tests use these models
```

### API Models Pattern

Each API endpoint gets its own class that inherits from `Client`:

```python
# api_models/pet.py
class Pet(Client):
    PATH = "/pet"
    
    def create_pet(self, data):
        return self.post_request(self.PATH, json=data)
    
    def get_pet(self, pet_id):
        return self.get_request(f"{self.PATH}/{pet_id}")
```

**Benefits:**
- ✅ **Encapsulation** - All pet-related logic in one place
- ✅ **Reusability** - Same methods used by all tests
- ✅ **Maintainability** - API changes = update one file
- ✅ **Readability** - `client.create_pet()` vs raw HTTP calls

### Single Client Per Test Class Pattern

**The Problem:** Creating a new client for every test is slow and wasteful.

**The Solution:** Create client once per test class, reset session after each test.

```python
class TestPet:
    client: Pet  # Type hint for IDE support
    
    def setup_method(self):
        """Runs before EACH test"""
        if not hasattr(self.__class__, 'client'):
            self.__class__.client = Pet(self.env)  # Create only once!
    
    def teardown_method(self):
        """Runs after EACH test"""
        self.client.reset_session()  # Clear state
```

**How it works:**
1. First test runs → `setup_method` creates client (stored as class attribute)
2. Test finishes → `teardown_method` resets session
3. Second test runs → `setup_method` sees client exists, reuses it
4. Test finishes → `teardown_method` resets session
5. Repeat for all tests in class

**Benefits:**
- ✅ **Performance** - faster test execution
- ✅ **Isolation** - Session reset ensures clean state
- ✅ **Clean code** - No client instantiation in test methods
- ✅ **Resource efficient** - One session per class, not per test

### Schema Validation

**Purpose:** Validate API responses match expected structure.

```python
# In api_models/pet.py
@staticmethod
def validate_pet_creation_schema(response_data):
    pet_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "status": {
                "type": "string",
                "enum": ["available", "pending", "sold"]
            }
        },
        "required": ["id", "name", "status"]
    }
    validate(instance=response_data, schema=pet_schema)
```

**Usage in tests:**
```python
def test_new_pet_creation(self):
    response = self.client.create_pet(data)
    assert response.status_code == 200
    self.client.validate_pet_creation_schema(response.json())  # ← Schema validation
```

**Why schema validation?**
- ✅ Catches API contract violations
- ✅ Validates data types (int, string, etc.)
- ✅ Checks required fields
- ✅ Validates enums/constraints

---

## ➕ Adding New Tests

### Step 1: Create API Model (if needed)

```python
# api_models/new_endpoint.py
from api_tests.support.client import Client

class NewEndpoint(Client):
    PATH = "/new-endpoint"
    
    def get_data(self):
        return self.get_request(self.PATH)
    
    def create_data(self, payload):
        return self.post_request(self.PATH, json=payload)
```

### Step 2: Create Test File

```python
# tests/test_new_endpoint.py
from pytest import mark
from api_tests.api_models.new_endpoint import NewEndpoint

pytestmark = mark.api

@mark.usefixtures("api_test_class_setup")
class TestNewEndpoint:
    client: NewEndpoint
    
    def setup_method(self):
        if not hasattr(self.__class__, 'client'):
            self.__class__.client = NewEndpoint(self.env)
    
    def teardown_method(self):
        self.client.reset_session()
    
    def test_get_data_success(self):
        response = self.client.get_data()
        assert response.status_code == 200
        assert "data" in response.json()
```

### Step 3: Run Your New Test

```bash
pytest tests/test_new_endpoint.py -v
```

### Adding Schema Validation (Optional)

```python
# In your API model class
@staticmethod
def validate_response_schema(response_data):
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        },
        "required": ["id"]
    }
    validate(instance=response_data, schema=schema)

# In your test
def test_with_schema_validation(self):
    response = self.client.get_data()
    self.client.validate_response_schema(response.json())
```

---

## 📊 Reporting

### HTML Reports with pytest-html

Generate beautiful HTML test reports:

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

**Report includes:**
- ✅ Test results (pass/fail)
- ✅ Execution time per test
- ✅ Error messages and tracebacks
- ✅ Test markers and metadata
- ✅ Environment information

**View report:**
```bash
open reports/report.html
# or
firefox reports/report.html
```

### Console Output

The framework is configured for verbose console logging:

```ini
# pytest.ini
log_cli = true
log_cli_level = DEBUG
```

**You'll see:**
- HTTP requests being made
- Response status codes
- Retry attempts
- Detailed error messages

---


## 📚 Additional Resources

- **Pytest Documentation:** https://docs.pytest.org/
- **Requests Library:** https://requests.readthedocs.io/
- **JSON Schema Validation:** https://json-schema.org/
- **Petstore Swagger API:** https://petstore.swagger.io/
- **Python dotenv:** https://github.com/theskumar/python-dotenv

---
