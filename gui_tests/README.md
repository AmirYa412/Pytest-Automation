# GUI Test Automation Framework

A modern, high-performance Selenium 4 web automation framework demonstrating professional test automation practices, smart authentication caching, and component-based architecture.

## 📋 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running Tests](#-running-tests)
- [Architecture & Design](#-architecture--design)
- [Adding New Tests](#-adding-new-tests)
- [Reporting](#-reporting)
- [Additional Resources](#-additional-resources)

---

## 🎯 Overview

This framework automates testing for [SauceDemo](https://www.saucedemo.com) and demonstrates:

- ✅ **Smart Authentication** - Cookie-based auth caching (4s login → instant)
- ✅ **Component Architecture** - Reusable UI components (Header, Sidebar)
- ✅ **Page Object Model** - Clean separation with co-located locators
- ✅ **Factory Pattern** - Lazy-loaded page objects and browser instances
- ✅ **Modern Selenium 4** - Built-in driver manager, no external downloads
- ✅ **Parallel Execution** - pytest-xdist with separate logs per worker
- ✅ **Multi-Browser Support** - Chrome, Firefox, Edge, Safari
- ✅ **Environment-Aware** - Different timeouts for local vs CI
- ✅ **Professional Logging** - Structured logs with automatic test tracking

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.14 | Programming language |
| **pytest** | 9.0+ | Test framework |
| **Selenium** | 4.x | Web automation library |
| **pytest-xdist** | 3.5+ | Parallel test execution |
| **pytest-html** | 4.1+ | HTML test reporting |
| **python-dotenv** | 1.0+ | Environment variable management |

**Tested on:** macOS Sequoia (15.2)

---

## 📂 Project Structure
```
gui_tests/
├── __init__.py
├── conftest.py              # Pytest configuration & fixtures
├── logger.py                # Logging infrastructure
├── requirements.txt         # Project dependencies
│
├── components/              # Reusable UI components
│   ├── header/
│   │   ├── header.py       # Header component class
│   │   └── locators.py     # Header locators
│   └── sidebar_menu/
│       ├── sidebar_menu.py
│       └── locators.py
│
├── factories/               # Factory classes for object creation
│   ├── browser.py          # BrowserFactory (Chrome, Firefox, etc.)
│   └── pages.py            # PageFactory (lazy-load pages)
│
├── hardcoded_data/          # Test data per environment
│   ├── production.json
│   └── ci.json
│
├── logs/                    # Test execution logs
│   ├── gui-test-run-master.log
│   ├── gui-test-run-gw0.log  # Parallel worker logs
│   └── ...
│
├── pages/                   # Page Object classes
│   ├── base_page.py        # BasePage with common methods
│   ├── inventory/
│   │   ├── inventory_page.py
│   │   └── locators.py
│   ├── login/
│   │   ├── login_page.py
│   │   └── locators.py
│   └── shopping_cart/
│       ├── shopping_cart_page.py
│       └── locators.py
│
├── support/                 # Infrastructure & utilities
│   ├── environment.py      # Environment configuration
│   └── ...
│
├── tests/                   # Test files
│   ├── inventory_page/
│   │   └── test_inventory.py
│   ├── login_page/
│   │   └── test_login.py
│   └── shopping_cart_page/
│       └── test_shopping_cart.py
│
├── users/                   # User credentials management
│   └── users.py
│
└── utilities/               # Helper utilities
    ├── auth_helper.py      # Smart authentication with cookies
    └── locator_helper.py   # Locator builder utilities
```

**Design Pattern:**
- `pages/` - Page objects with co-located locators
- `components/` - Reusable UI components (Header, Sidebar)
- `factories/` - Object creation (BrowserFactory, PageFactory)
- `support/` - Infrastructure (Environment, configuration)
- `utilities/` - Helpers (AuthHelper, LocatorHelper)
- `tests/` - Test scenarios organized by page

---

## ✅ Prerequisites

- **Python 3.14** (or Python 3.11+ recommended)
- **pip** (Python package manager)
- **Git** (for version control)
- **Chrome/Firefox/Edge** (browser of choice)
- **Safari** (macOS only - enable "Allow Remote Automation" in Develop menu)

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
```bash
# Install GUI test requirements
cd gui_tests
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
pytest --version  # Should show pytest 9.0+
python -c "import selenium; print(selenium.__version__)"  # Should show 4.x
```

---

## ⚙️ Configuration

### Environment Variables & Security

The framework uses **environment variables** for sensitive data following security best practices.
==NOTE: For simplicity, .env commited to the project, but in real life scenarios, you store sensitive data in a more secured approach.==

#### Create `.env` file:
```bash
# In project root
touch .env
```

#### Add credentials:
```bash
# .env
PROD_SAUCEDEMO_USER_PASSWORD=secret_sauce
CI_SAUCEDEMO_USER_PASSWORD=qa_password_here
```

#### Security Best Practices Demonstrated

✅ **No hardcoded secrets** - All credentials from environment  
✅ **.env in .gitignore** - Prevents accidental commits  
✅ **Fail-fast validation** - Catches missing credentials early  
✅ **CI/CD ready** - Use environment variables in pipelines  

### Environment Configuration

The framework supports multiple environments via `Environment` class:
```python
# Production (default)
env = Environment("www")  # https://www.saucedemo.com

# CI environments
env = Environment("qa")   # https://qa.saucedemo.com
env = Environment("dev")  # https://dev.saucedemo.com
```

**Environment-aware features:**
- Different timeouts (CI: 10s, Local: 5s)
- Different user credentials
- Different test data (hardcoded_data/)

### Browser Configuration

Supported browsers via `BrowserFactory`:
- Chrome (default)
- Firefox
- Edge
- Safari (macOS only)

Options:
- `--headless` - Run without GUI
- `--maximize` - Maximize browser window

---

## 🚀 Running Tests

### Run All Tests
```bash
cd gui_tests
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/inventory_page/test_inventory.py -v
```

### Run Specific Test Class
```bash
pytest tests/inventory_page/test_inventory.py::TestInventoryPage -v
```

### Run Specific Test Method
```bash
pytest tests/inventory_page/test_inventory.py::TestInventoryPage::test_sort_inventory_items_by_highest_price -v
```

### Run Tests by Marker
```bash
# Run only GUI tests
pytest -m gui -v
```

### Run Tests with Different Browser
```bash
# Chrome (default)
pytest tests/ --browser=chrome -v

# Firefox
pytest tests/ --browser=firefox -v

# Edge
pytest tests/ --browser=edge -v

# Safari (macOS only)
pytest tests/ --browser=safari -v
```

### Run Tests in Headless Mode
```bash
pytest tests/ --browser=chrome --headless -v
```

### Run Tests with HTML Report
```bash
pytest tests/ --html=../reports/gui_report.html --self-contained-html -v
```

### Run Tests for Different Environment
```bash
# Production (default)
pytest tests/ --gui_env=www -v

# QA environment
pytest tests/ --gui_env=qa -v

# Dev environment
pytest tests/ --gui_env=dev -v
```

### Run Tests in Parallel
```bash
# Run with 4 workers
pytest tests/ -n 4 -v

# Auto-detect CPU cores
pytest tests/ -n auto -v
```

**Note:** Each worker gets its own log file (`gui-test-run-gw0.log`, `gui-test-run-gw1.log`, etc.)

---

## 🗃️ Architecture & Design

### Smart Authentication with Cookie Caching

**The Problem:** UI login takes ~4 seconds per test, slowing execution.

**The Solution:** Cookie-based authentication with session-scoped caching.

#### AuthHelper Class (`utilities/auth_helper.py`)
```python
class AuthHelper:
    @staticmethod
    def auth_with_cookie(driver, env, user_key, cookies_cache):
        """Inject authentication cookie, bypassing UI login."""
        
        # Navigate to domain (required for cookie injection)
        driver.get(env.base_url)
        
        # Reuse cached cookie if available
        if user_key in cookies_cache:
            for cookie in cookies_cache[user_key]:
                driver.add_cookie(cookie)
        else:
            # Create and cache new authentication cookie
            cookie = {
                'name': 'session-username',
                'value': user_data['username'],
                'domain': env.domain,
                'expiry': int((datetime.now() + timedelta(days=1)).timestamp())
            }
            driver.add_cookie(cookie)
            cookies_cache[user_key] = [cookie]
```

**Performance Impact:**
- First test: ~4s (create cookie + cache)
- Subsequent tests: ~0.1s (reuse cached cookie)
- 40x performance improvement for auth

**Usage in tests:**
```python
def test_inventory_page_navigate_for_logged_in_user(self, pages):
    pages.authenticate(user="standard_user")  # ← Instant auth
    pages.inventory.navigate()
    assert pages.inventory.are_items_titles_displayed()
```

**Why navigation is required:**
Browsers block cross-site cookie injection for security. Must navigate to domain before injecting cookies. This is a Selenium/browser limitation, not a framework design flaw.

### Page Object Model with Components

#### BasePage Pattern (`pages/base_page.py`)

All page classes inherit from `BasePage`, providing:

1. **Common Infrastructure**
```python
   class BasePage:
       PATH = "/"    # Override in subclass
       TITLE = None  # Override if page has title
       
       def __init__(self, driver, env):
           self.driver = driver
           self.env = env
           self.timeout = env.timeout
           self.logger = logging.getLogger(f"gui.{self.__class__.__name__}")
```

2. **Navigation & Verification**
```python
   def navigate(self, path=None, verify_on_page=True):
       """Navigate to page with automatic validation."""
       target = path if path is not None else self.PATH
       self.driver.get(f"{self.env.base_url}{target}")
       if verify_on_page:
           self.verify_on_page()
           self.verify_page_title()
```

3. **Explicit Waits** (No `time.sleep()` anti-pattern)
```python
   def explicit_wait_element_visibility(self, locator, timeout=None):
       """Wait for element to be visible."""
       timeout = timeout or self.timeout
       return WebDriverWait(self.driver, timeout).until(
           EC.visibility_of_element_located(locator)
       )
```

4. **Element Interactions**
```python
   def click_element(self, locator):
       element = self.explicit_wait_element_clickable(locator)
       element.click()
   
   def send_text_to_element(self, locator, text):
       element = self.explicit_wait_element_visibility(locator)
       element.clear()
       element.send_keys(text)
```

#### Page Class Example (`pages/inventory/inventory_page.py`)
```python
class InventoryPage(BasePage):
    PATH = "/inventory.html"
    TITLE = "Products"
    
    def __init__(self, driver, env):
        super().__init__(driver, env)
        self.header = Header(self)      # ← Component composition
        self.sidebar = SidebarMenu(self)
    
    def add_item_to_cart(self, item_name: str):
        """Add item using dynamic locator."""
        normalized_name = item_name.lower().replace(' ', '-')
        data_test_value = f"add-to-cart-{normalized_name}"
        locator = LocatorHelper.by_data_test(data_test_value)
        self.click_element(locator)
```

**Co-located Locators:**
```python
# pages/inventory/locators.py
class InventoryPageLocators:
    INVENTORY_ITEM_TITLE = LocatorHelper.by_class("inventory_item_name")
    SORT_DROPDOWN = LocatorHelper.by_data_test("product-sort-container")
    INVENTORY_ITEM_PRICE = LocatorHelper.by_class("inventory_item_price")
```

### Component Pattern

**Purpose:** Extract reusable UI components that appear on multiple pages.

#### Component Example (`components/header/header.py`)
```python
class Header:
    """Header component - appears on all authenticated pages."""
    
    def __init__(self, base_page: BasePage):
        """Accept BasePage to access driver and common methods."""
        self.page = base_page
    
    def is_logo_displayed(self) -> bool:
        return self.page.is_element_displayed(HeaderLocators.APP_LOGO)
    
    def click_shopping_cart(self):
        self.page.click_element(HeaderLocators.SHOPPING_CART_BUTTON)
    
    def get_cart_item_count(self) -> int:
        badge_text = self.page.get_element_text(HeaderLocators.SHOPPING_CART_BADGE)
        return int(badge_text)
```

**Usage in Page Objects:**
```python
class InventoryPage(BasePage):
    def __init__(self, driver, env):
        super().__init__(driver, env)
        self.header = Header(self)  # ← Compose component
    
    # Access component methods
    def verify_cart_count(self):
        return self.header.get_cart_item_count()
```

**Benefits:**
- ✅ Single source of truth for Header logic
- ✅ Reusable across all pages
- ✅ Easy to maintain (change once, works everywhere)
- ✅ Testable in isolation

### Factory Pattern

#### PageFactory (`factories/pages.py`)

**Purpose:** Lazy-load page objects on demand, manage authentication.
```python
class PageFactory:
    """Factory for lazy-loading page objects."""
    
    def __init__(self, driver, env, auth_cookies_cache):
        self._driver = driver
        self._env = env
        self._pages_cache = {}  # Cache page instances
        self._auth_cookies_cache = auth_cookies_cache
        self.auth_helper = AuthHelper
    
    def authenticate(self, user: str):
        """Authenticate user via cookies."""
        self.auth_helper.auth_with_cookie(
            self._driver, self._env, user, self._auth_cookies_cache
        )
    
    @property
    def inventory(self) -> InventoryPage:
        """Get or create InventoryPage instance."""
        if 'inventory' not in self._pages_cache:
            self._pages_cache['inventory'] = InventoryPage(self._driver, self._env)
        return self._pages_cache['inventory']
```

**Usage in Tests:**
```python
def test_inventory_page(self, pages):  # ← PageFactory injected
    pages.authenticate(user="standard_user")
    pages.inventory.navigate()  # ← Lazy-loaded on first access
    assert pages.inventory.are_items_titles_displayed()
```

**Benefits:**
- ✅ Clean test syntax: `pages.inventory.method()`
- ✅ Lazy loading: Only creates pages you use
- ✅ Caching: Reuses page instances
- ✅ Centralized authentication

#### BrowserFactory (`factories/browser.py`)

**Purpose:** Abstract browser creation, support multiple browsers.
```python
class BrowserFactory:
    """Modern Selenium 4 driver manager."""
    
    def __init__(self, browser: str, headless: bool, maximize_window: bool):
        self.browser = browser.lower()
        self.headless = headless
        self.maximize_window = maximize_window
    
    def create(self) -> WebDriver:
        """Get driver for specified browser."""
        if self.browser == "chrome":
            return self._chrome()
        elif self.browser == "firefox":
            return self._firefox()
        # ... etc
    
    def _chrome(self) -> WebDriver:
        options = ChromeOptions()
        if self.headless:
            options.add_argument("--headless=new")
        # ... more configuration
        return webdriver.Chrome(options=options)
```

**Key Features:**
- ✅ No external driver downloads (Selenium 4 handles it)
- ✅ Anti-detection measures (disable automation flags)
- ✅ Password manager disabled (prevents UI interference)
- ✅ Docker/CI compatible options

### Logging Infrastructure

#### LoggerFactory (`logger.py`)

**Purpose:** Structured logging with parallel execution support.
```python
class LoggerFactory:
    def __init__(self, project: str = "test"):
        """
        Args:
            project: 'gui', 'api', 'unit'
                   Logger name: 'gui', 'api', 'unit'
                   Log file: 'gui-test-run-*.log'
        """
        self.logger = self._setup_logger()
    
    def _create_file_handler(self):
        """Separate log file per pytest worker."""
        worker_id = os.environ.get('PYTEST_XDIST_WORKER', 'master')
        log_file = log_dir / f"{self.project}-test-run-{worker_id}.log"
        # ... create handler
```

**Automatic Test Logging:**
```python
# conftest.py
@fixture(scope="function", autouse=True)
def log_test_execution(request, logger):
    """Log test start/end automatically."""
    test_name = request.node.name
    logger.info(f"*** TEST {test_name} STARTING")
    yield
    logger.info(f"*** TEST {test_name} ENDED")
```

**Page-Level Logging:**
```python
class BasePage:
    def __init__(self, driver, env):
        # ...
        self.logger = logging.getLogger(f"gui.{self.__class__.__name__}")
    
    def navigate(self, path=None):
        self.logger.info(f"navigating to {target}")
        # ...
```

**Log Output:**
```
2025-01-06 10:15:23 | INFO | *** TEST test_inventory_page_navigate STARTING
2025-01-06 10:15:23 | INFO | navigating to /inventory.html
2025-01-06 10:15:24 | INFO | verifying on correct path=/inventory.html by URL
2025-01-06 10:15:24 | INFO | *** TEST test_inventory_page_navigate ENDED
```

### LocatorHelper Utility

**Purpose:** Build robust, maintainable locators.
```python
class LocatorHelper:
    """Helper for building robust locators."""
    
    @staticmethod
    def by_data_test(value: str) -> tuple[str, str]:
        """Locator using data-test attribute."""
        return By.CSS_SELECTOR, f'[data-test="{value}"]'
    
    @staticmethod
    def by_partial_data_test(partial_value: str) -> tuple[str, str]:
        """Partial match on data-test."""
        return By.CSS_SELECTOR, f'[data-test*="{partial_value}"]'
    
    @staticmethod
    def by_id(element_id: str) -> tuple[str, str]:
        return By.ID, element_id
```

**Usage:**
```python
# Instead of:
LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')

# Use:
LOGIN_BUTTON = LocatorHelper.by_data_test("login-button")

# Dynamic locators:
add_button = LocatorHelper.by_data_test(f"add-to-cart-{item_name}")
```

**Benefits:**
- ✅ Consistent locator format
- ✅ Easier to maintain
- ✅ Supports dynamic locators
- ✅ Type hints for IDE support

---

## ➕ Adding New Tests

### Step 1: Create Page Object (if needed)
```python
# pages/new_page/new_page.py
from gui_tests.pages.base_page import BasePage
from gui_tests.pages.new_page.locators import NewPageLocators

class NewPage(BasePage):
    PATH = "/new-page.html"
    TITLE = "New Page Title"
    
    def __init__(self, driver, env):
        super().__init__(driver, env)
    
    def click_submit_button(self):
        self.click_element(NewPageLocators.SUBMIT_BUTTON)
    
    def is_success_message_displayed(self) -> bool:
        return self.is_element_displayed(NewPageLocators.SUCCESS_MESSAGE)
```
```python
# pages/new_page/locators.py
from gui_tests.utilities.locator_helper import LocatorHelper

class NewPageLocators:
    SUBMIT_BUTTON = LocatorHelper.by_data_test("submit-btn")
    SUCCESS_MESSAGE = LocatorHelper.by_class("success-msg")
```

### Step 2: Add Page to PageFactory
```python
# factories/pages.py
from gui_tests.pages.new_page.new_page import NewPage

class PageFactory:
    # ...
    
    @property
    def new_page(self) -> NewPage:
        """Get or create NewPage instance."""
        if 'new_page' not in self._pages_cache:
            self._pages_cache['new_page'] = NewPage(self._driver, self._env)
        return self._pages_cache['new_page']
```

### Step 3: Create Test File
```python
# tests/new_page/test_new_page.py
from pytest import mark

pytestmark = mark.gui

@mark.usefixtures("gui_test_class_setup")
class TestNewPage:
    
    def test_submit_form_success(self, pages):
        # Arrange: Authenticate
        pages.authenticate(user="standard_user")
        
        # Act: Navigate and submit
        pages.new_page.navigate()
        pages.new_page.click_submit_button()
        
        # Assert: Verify success
        assert pages.new_page.is_success_message_displayed()
```

### Step 4: Run Your New Test
```bash
pytest tests/new_page/test_new_page.py -v
```

### Adding New Component (if reusable)
```python
# components/footer/footer.py
from gui_tests.pages.base_page import BasePage
from gui_tests.components.footer.locators import FooterLocators

class Footer:
    """Footer component."""
    
    def __init__(self, base_page: BasePage):
        self.page = base_page
    
    def click_privacy_link(self):
        self.page.click_element(FooterLocators.PRIVACY_LINK)
```

**Use in Page Objects:**
```python
class NewPage(BasePage):
    def __init__(self, driver, env):
        super().__init__(driver, env)
        self.footer = Footer(self)  # ← Add component
```

---

## 📊 Reporting

### HTML Reports with pytest-html

Generate beautiful HTML test reports with screenshots on failure:
```bash
pytest tests/ --html=../reports/gui_report.html --self-contained-html -v
```

**Report includes:**
- ✅ Test results (pass/fail)
- ✅ Execution time per test
- ✅ Screenshots on failure (auto-captured)
- ✅ Error messages and tracebacks
- ✅ Test markers and metadata
- ✅ Environment information

**View report:**
```bash
open ../reports/gui_report.html
# or
firefox ../reports/gui_report.html
```

### Screenshot on Failure

Automatically configured in `conftest.py`:
```python
@mark.hookwrapper
def pytest_runtest_makereport(item):
    """Auto-capture screenshot on test failure."""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == 'call' and report.failed:
        if 'driver' in item.fixturenames:
            driver = item.funcargs['driver']
            screenshot = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot))
```

### Log Files

Logs are automatically generated per pytest worker:
```bash
gui_tests/logs/
├── gui-test-run-master.log  # Main process
├── gui-test-run-gw0.log     # Worker 0
├── gui-test-run-gw1.log     # Worker 1
└── ...
```

**Log content:**
```
2025-01-06 10:15:23 | INFO | *** TEST test_inventory_page_navigate STARTING
2025-01-06 10:15:23 | INFO | navigating to /inventory.html
2025-01-06 10:15:24 | INFO | verifying on correct path
2025-01-06 10:15:24 | INFO | *** TEST test_inventory_page_navigate ENDED
```

---

## 📚 Additional Resources

- **Pytest Documentation:** https://docs.pytest.org/
- **Selenium Documentation:** https://www.selenium.dev/documentation/
- **SauceDemo Application:** https://www.saucedemo.com
- **Selenium Python Bindings:** https://selenium-python.readthedocs.io/
- **pytest-xdist (Parallel):** https://github.com/pytest-dev/pytest-xdist
- **Page Object Pattern:** https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/

---

## 🎯 Key Takeaways

This framework demonstrates:

1. **Performance Optimization**
   - Cookie-based auth caching (40x faster)
   - Parallel execution support
   - Lazy-loaded page objects

2. **Clean Architecture**
   - Page Object Model with co-located locators
   - Component pattern for reusable UI elements
   - Factory pattern for object creation
   - Explicit waits (no `time.sleep()`)

3. **Professional Practices**
   - Comprehensive logging infrastructure
   - Environment-aware configuration
   - Security best practices (no hardcoded secrets)
   - Type hints for IDE support

4. **Modern Selenium 4**
   - Built-in driver manager (no manual downloads)
   - Multiple browser support
   - Docker/CI compatible

5. **Scalability**
   - Easy to add new pages/components
   - Maintainable locator strategy
   - Parallel execution ready
   - Clear separation of concerns

---

**Note:** For Safari testing on macOS, enable "Allow Remote Automation" in Safari → Develop menu.
