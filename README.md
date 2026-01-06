# Python Test Automation Portfolio

A comprehensive test automation suite demonstrating modern Python testing practices across unit, API, and GUI testing domains.

## 📁 Projects

### 🔬 [Unit Tests](./unit_tests/README.md)
Python unit testing with pytest, mocking, and test-driven development patterns.
- **Framework:** pytest
- **Focus:** Unit testing, mocking Google APIs, string/integer utilities

### 🌐 [API Tests](./api_tests/README.md)
RESTful API testing framework with schema validation and retry logic.
- **Framework:** pytest + requests
- **Target:** Petstore Swagger API
- **Features:** JSON schema validation, automatic retry, session management

### 🖥️ [GUI Tests](./gui_tests/README.md)
Modern Selenium 4 web automation framework with smart authentication and component patterns.
- **Framework:** pytest + Selenium 4
- **Target:** SauceDemo
- **Features:** Cookie-based auth caching, Page Object Model, parallel execution

## 🚀 Quick Start

### Prerequisites
- Python 3.14 (or Python 3.11+ recommended)
- pip (Python package manager)
- Git

### Installation
```bash
# Clone repository
git clone <repository-url>
cd <project-root>

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install project-specific dependencies
cd api_tests && pip install -r requirements.txt && cd ..
cd gui_tests && pip install -r requirements.txt && cd ..
cd unit_tests && pip install -r requirements.txt && cd ..
```

### Run Tests
```bash
# API Tests
cd api_tests && pytest tests/ -v

# GUI Tests  
cd gui_tests && pytest tests/ -v

# Unit Tests
cd unit_tests && pytest tests/ -v
```

## 📊 Tech Stack

| Technology | Version | Used In |
|------------|---------|---------|
| Python | 3.14 | All projects |
| pytest | 9.0+ | All projects |
| Selenium | 4.x | GUI tests |
| requests | 2.32+ | API tests |



### Reports

##### pytest-html
pytest-html is a plugin that generate test report HTML file with a single command,
add this to your Pytest run command:


```
pytest --html=reports/my_report.html
pytest --html=reports/my_report.html --self-contained-html
```

![pytest-html](https://i.imgur.com/IL93Zgq.png)

## 📖 Documentation

Each project contains comprehensive documentation:
- Architecture diagrams
- Design patterns explained
- Best practices demonstrated
- Code examples and usage guides

## 🎯 Skills Demonstrated

✅ Clean architecture & separation of concerns  
✅ Modern Python patterns (factories, fixtures, type hints)  
✅ Test isolation & independence  
✅ CI/CD ready infrastructure  
✅ Performance optimization (caching, parallel execution)  
✅ Professional logging & reporting  
✅ Security best practices (environment variables, no hardcoded secrets)  
