# Selenium Python Automation Framework

A scalable and maintainable **Selenium Web Automation Framework** built with **Python**, **PyTest**, **Unittest**, and the **Page Object Model (POM)**.

The framework demonstrates practical automation framework concepts including reusable page objects, configuration management, CSV-based test data, explicit waits, logging, automatic screenshots on failure, PyTest HTML reporting, and Allure reporting.

## Project Overview

This project is a portfolio-level Selenium automation framework for testing the **TutorialsNinja Demo Store**.

The framework follows a modular architecture where:

- Selenium handles browser automation.
- PyTest is used as the primary test runner.
- Unittest is also supported.
- Page Object Model separates test logic from UI locators and actions.
- CSV files provide external test data.
- Configuration is maintained separately from test code.
- Explicit waits improve synchronization.
- Logging helps with debugging and execution tracking.
- Screenshots are automatically captured when tests fail.
- PyTest HTML generates execution reports.
- Allure generates interactive test reports.

Application under test:

**TutorialsNinja Demo Store**

`https://tutorialsninja.com/demo/`

## Key Features

- Selenium WebDriver automation
- Python-based framework
- PyTest test execution
- Unittest support
- Page Object Model (POM)
- Reusable Base Page
- Driver Factory
- Chrome and Firefox support
- Configuration management using `config.ini`
- CSV-based data-driven testing
- Explicit waits
- Failure screenshot capture
- Automatic screenshot attachment to Allure
- Logging
- PyTest HTML reporting
- Allure reporting
- Centralized WebDriver setup
- Reusable utility classes
- Clean separation of tests, pages, data, configuration, and utilities

## Project Structure

```text
Selenium_Python_Automation_Framework/

├── config/
│   └── config.ini
│
├── data/
│   └── test_data.csv
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── search_page.py
│
├── tests/
│   ├── test_home_unittest.py
│   ├── test_login.py
│   └── test_product_search.py
│
├── utilities/
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── driver_factory.py
│   ├── logger.py
│   └── screenshot.py
│
├── screenshots/
├── logs/
│
├── reports/
│   └── html/
│
├── allure-results/
├── allure-report/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Framework Components
### Page Object Model

The framework follows the Page Object Model (POM) design pattern.

Each important web page has a dedicated Python class containing:

- Web element locators
- Page-specific actions
- Page-specific verification methods

Example:
pages/
├── base_page.py
├── home_page.py
├── login_page.py
└── search_page.py

This prevents test cases from becoming tightly coupled to Selenium locators.

For example:

```python
login_page.login(email, password)
```

is used in the test instead of placing all Selenium interactions directly inside the test.

Benefits:

- Better maintainability
- Reusable page actions
- Cleaner test cases
- Easier locator maintenance
- Separation of test logic and UI implementation

### Base Page

base_page.py contains common Selenium operations used by multiple page objects.

Examples include:

- Opening URLs
- Finding elements
- Clicking elements
- Entering text
- Reading element text
- Getting page title
- Getting current URL
- Explicit wait handling

Example:

```python
def click(self, locator):
    self.wait.until(
        EC.element_to_be_clickable(locator)
    ).click()
```

Page-specific classes inherit from BasePage.

BasePage
   │
   ├── HomePage
   ├── LoginPage
   └── SearchPage

### Driver Factory

utilities/driver_factory.py is responsible for creating WebDriver instances.

The framework currently supports:

- Chrome
- Firefox

Browser configuration is controlled through:

```config/config.ini```

Example:

```text
[DEFAULT]
browser = chrome
base_url = https://tutorialsninja.com/demo/
headless = false
implicit_wait = 5
explicit_wait = 20
```

This avoids hardcoding browser settings inside individual tests.

### Configuration Management

Configuration is separated from the test code.

The framework uses:

```config/config.ini```

and:

```utilities/config_reader.py```

The ConfigReader provides methods for reading:

- String values
- Integer values
- Boolean values

Example:

```python
config = ConfigReader()
base_url = config.get("base_url")
```

This allows configuration changes without modifying test cases.

### CSV Data-Driven Testing

Test data is stored externally in:

```data/test_data.csv```

Example structure:

```text
username,password,product
your_email@example.com,your_password,MacBook
```

The framework uses:

```utilities/csv_reader.py```

to read the CSV file.

Example:

```python
data = CSVReader.read_data()[0]

email = data["username"]
password = data["password"]
product = data["product"]
```

Benefits:

- Separates test data from test logic
- Makes data changes easier
- Supports reusable test scenarios
- Demonstrates data-driven testing

Do not commit real passwords or sensitive credentials to a public repository.

### Synchronization and Explicit Waits

The framework uses Selenium's WebDriverWait with Expected Conditions.

Example:

```python
self.wait.until(
    EC.visibility_of_element_located(locator)
)
```

For clickable elements:

```python
self.wait.until(
    EC.element_to_be_clickable(locator)
).click()
```

The explicit wait timeout is controlled through:

```python
explicit_wait = 10
```

This improves synchronization with dynamically loaded web elements.

## Testing Frameworks
### PyTest

PyTest is the primary test framework used by the project.

Current PyTest tests include:

```
tests/test_login.py
tests/test_product_search.py
```

Run all tests:

```pytest -v```

Example final execution:

collected 3 items

tests/test_home_unittest.py::TestHomePage::test_home_page_displayed PASSED
tests/test_login.py::test_valid_login PASSED
tests/test_product_search.py::test_product_search PASSED

3 passed

### Unittest Support

The framework also demonstrates Python's built-in unittest framework.

Example:

```tests/test_home_unittest.py```

The test uses:

```python
class TestHomePage(unittest.TestCase):
```

and:

```python
def setUp(self):
```

and:

```python
def tearDown(self):
```

The test can also be executed through PyTest.

This demonstrates compatibility with both:

- PyTest
- Unittest

## Automatic Screenshots on Failure

The framework automatically captures screenshots when a test fails.

Screenshots are stored under:

```screenshots/```

The screenshot filename contains:

- Test name
- Timestamp

Example:

```test_product_search_20260920_163251.png```

The screenshot is also attached to the Allure test result.

Failure flow:

Test Failure
     │
     ↓
PyTest Hook
     │
     ↓
Screenshot Captured
     │
     ├──────────────→ screenshots/
     │
     └──────────────→ Allure Attachment

This makes debugging failed UI tests much easier.

## Logging

The framework uses Python's built-in logging module.

Logging is implemented through:

```utilities/logger.py```

Log files are stored under:

```logs/```

Example log output:

2026-09-25 15:28:04 | INFO | DriverFactory | Creating browser: chrome
2026-09-25 15:28:05 | INFO | DriverFactory | chrome browser started successfully
2026-09-25 15:28:05 | INFO | HomePage | Opening home page
2026-09-25 15:30:33 | INFO | LoginPage | Starting login process
2026-09-25 15:30:33 | INFO | LoginPage | Opening login page

Sensitive values such as passwords are not written to the logs.

## PyTest HTML Reporting

The framework supports HTML test reporting using pytest-html.

Generate an HTML report:

```pytest -v --html=reports/html/report.html --self-contained-html```

The report is generated at:

```reports/html/report.html```

The HTML report provides information such as:

- Test results
- Passed/failed tests
- Execution duration
- Environment information
- Test metadata

### Allure Reporting

The framework supports interactive Allure reporting.

First execute the tests and generate Allure result files:

```pytest -v --alluredir=allure-results```

Generate the Allure report:

```allure generate allure-results -o allure-report --clean```

Open the report:

```allure open allure-report```

The Allure report provides:

- Test execution results
- Passed/failed status
- Test duration
- Test details
- Logs
- Failure information
- Failure screenshots

## Test Scenarios
### Valid Login

File:

```tests/test_login.py```

Flow:

Open TutorialsNinja
        ↓
Click My Account
        ↓
Click Login
        ↓
Read credentials from CSV
        ↓
Enter email
        ↓
Enter password
        ↓
Click Login
        ↓
Verify successful login

### Product Search

File:

```tests/test_product_search.py```

Flow:

Open TutorialsNinja
        ↓
Verify Home Page
        ↓
Read product from CSV
        ↓
Enter product in Search
        ↓
Click Search
        ↓
Verify Search Results
        ↓
Verify requested product appears

### Home Page Smoke Test

File:

```tests/test_home_unittest.py```

Flow:

Create WebDriver
       ↓
Read base URL from configuration
       ↓
Open TutorialsNinja
       ↓
Create HomePage object
       ↓
Verify Home Page
       ↓
Close browser

This test demonstrates the use of unittest.TestCase.

## Installation

Prerequisites

Install the following:

- Python 3.x
- Google Chrome or Mozilla Firefox
- Java Runtime Environment / JDK for Allure CLI
- Allure Commandline

Verify Python:

```python --version```

Verify Java:

```java -version```

Verify Allure:

```allure --version```

## Setup

Clone or download the project.

Navigate to the project directory:

```cd Selenium_Python_Automation_Framework```

Create a virtual environment:

```python -m venv .venv```

Activate it on Windows:

```.venv\Scripts\Activate.ps1```

Install dependencies:

```pip install -r requirements.txt```

## Configuration

Open:

```config/config.ini```

Example:

```text
[DEFAULT]

browser = chrome
base_url = https://tutorialsninja.com/demo/
headless = false
implicit_wait = 5
explicit_wait = 20
```

Change browser:
For Chrome:

```browser = chrome```

For Firefox:

```browser = firefox```

Run headless
```headless = true```

Run with visible browser
```headless = false```

## Running Tests

Run the complete test suite
```pytest -v```

Run login test
```pytest tests/test_login.py -v```

Run product search test
```pytest tests/test_product_search.py -v```

Run Unittest-based test through PyTest
```pytest tests/test_home_unittest.py -v```

## Generate HTML Report

```pytest -v --html=reports/html/report.html --self-contained-html```

## Generate Allure Report

Run tests:

```pytest -v --alluredir=allure-results```

Generate report:

```allure generate allure-results -o allure-report --clean```

Open report:

```allure open allure-report```

## Generate Both Reports

````pytest -v --html=reports/html/report.html --self-contained-html --alluredir=allure-results```

Then:

```allure generate allure-results -o allure-report --clean```

Open:

```allure open allure-report```

## Technologies Used

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| Python             | Programming language      |
| Selenium WebDriver | Browser automation        |
| PyTest             | Test execution            |
| Unittest           | Additional test framework |
| Page Object Model  | Test architecture         |
| CSV                | External test data        |
| ConfigParser       | Configuration management  |
| WebDriverWait      | Explicit synchronization  |
| Python Logging     | Execution logs            |
| pytest-html        | HTML reporting            |
| Allure             | Interactive reporting     |
| webdriver-manager  | WebDriver management      |

## Security Considerations

The project uses external test data for login testing.

Do not store real credentials in a public repository.

For a production implementation, sensitive values should be supplied through secure environment variables or a secrets-management system rather than committed to:

```data/test_data.csv```

## Generated Files

The following directories contain generated execution artifacts:

screenshots/
logs/
reports/
allure-results/
allure-report/

These are excluded through .gitignore.

They can be regenerated whenever the tests are executed.

## Current Test Coverage

The current framework demonstrates:

Test	Framework	Purpose
test_login.py	PyTest	Valid login
test_product_search.py	PyTest	Product search
test_home_unittest.py	Unittest	Home page smoke test

Current verified execution:

3 passed

## Framework Design Principles

The framework follows these principles:

Separation of concerns:
Test cases, page objects, utilities, configuration, and test data are separated.

Reusability:
Common Selenium operations are implemented in BasePage.

Maintainability:
Locators and page-specific actions are centralized in Page Object classes.

Configurability:
Browser, URL, wait times, and execution settings are maintained in config.ini.

Debuggability:
Logs and failure screenshots help investigate failed tests.

Reporting:
Both PyTest HTML and Allure reports provide test execution visibility.

## Future Enhancements

Potential future improvements include:

- Parallel test execution
- More test scenarios
- Parameterized testing
- Environment-specific configuration
- API + UI integration testing
- Database validation
- Advanced Allure metadata
- Cross-browser test matrix
- Dockerized test execution

## Author

Arpan Mukherjee

B.Tech Computer Science Engineering (IOT, CS, BT)

This project was developed as a practical demonstration of Python-based Selenium automation and test framework design.

## Project Highlights

This framework demonstrates practical knowledge of:

```text
Python
   ↓
Selenium
   ↓
PyTest + Unittest
   ↓
Page Object Model
   ↓
Driver Factory
   ↓
Configuration Management
   ↓
CSV Data-Driven Testing
   ↓
Explicit Waits
   ↓
Logging
   ↓
Failure Screenshots
   ↓
HTML Reporting
   ↓
Allure Reporting
```

The framework is designed to be reusable, maintainable, configurable, and suitable for demonstrating Selenium automation skills in a software-testing portfolio.
