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
| Docker | - | All projects |
| GitHub Actions | - | CI/CD |

## 🐳 Docker

All three projects run inside a single Docker image. Selenium Manager (4.11+) auto-downloads browser binaries at runtime — no manual Chrome or Firefox installation in the image.
```bash
# Build
docker build -t pytest-automation .

# Run all tests
docker run --rm pytest-automation

# Run by project marker
docker run --rm pytest-automation pytest -m api
docker run --rm pytest-automation pytest -m gui --browser=chrome --headless
docker run --rm pytest-automation pytest -m unit

# Run specific marker within a project
docker run --rm pytest-automation pytest -m "gui and login" --browser=firefox --headless -n 2

# Mount reports to host
docker run --rm \
  -v $(pwd)/reports:/app/reports \
  pytest-automation pytest -m api
```

**Key decisions:**
- Selenium Manager downloads "Chrome for Testing" at runtime instead of baking browser binaries into the image. Keeps the image ~500MB vs ~800MB with pre-installed browsers. First run inside a fresh container is ~30s slower; subsequent runs use the cached binary.
- `--headless` is required for all GUI tests inside Docker — no display available.
- `.env` files are committed alongside the code. All targets are public mock APIs (PetStore, SauceDemo) — no real credentials at risk.

### Reports

pytest-html generates a self-contained HTML report automatically via `addopts` in `pytest.ini`. When running in Docker, mount the `reports/` directory to get the file on your host:
```bash
docker run --rm -v $(pwd)/reports:/app/reports pytest-automation pytest -m gui --browser=chrome --headless
# Report at: ./reports/report.html
```

![pytest-html](https://i.imgur.com/IL93Zgq.png)

## 🔄 CI/CD Pipeline

Each project has its own workflow triggered manually from the GitHub Actions tab. Shared build and deploy logic lives in a single reusable workflow (`_test_logic.yml`) — the three caller workflows just pass inputs.

### Workflows

| Workflow | Trigger | Inputs |
|----------|---------|--------|
| `unit_tests.yml` | Manual | Workers |
| `api_tests.yml` | Manual | Marker, Workers |
| `gui_tests.yml` | Manual | Marker, Browser, Workers |

### How it works

1. Caller workflow (`api_tests.yml`, `gui_tests.yml`, or `unit_tests.yml`) is triggered manually with the desired inputs.
2. It calls `_test_logic.yml`, passing the marker expression, browser (GUI only), and worker count.
3. The reusable workflow builds the Docker image with layer caching, runs pytest inside the container, and deploys the HTML report to GitHub Pages.
4. A link to the live report is posted in the workflow summary.

### Live Report

The report is automatically deployed to GitHub Pages after each run and linked in the workflow summary.

> Note: all three workflows currently deploy to the same Pages URL. The last workflow to run is the report you'll see. Each run's report is also available as a download from the workflow summary.

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
