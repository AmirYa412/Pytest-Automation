## Test Automation Project - Pytest Framework
### This repo contains 3 projects example, all of them written using Pytest framework.
**API**  -  Pytest-Automation-Project/api_tests

**GUI**  -  Pytest-Automation-Project/gui_tests

**UNIT** -  Pytest-Automation-Project/unit_tests


pip install -r requirements.txt


#### Run tests commands from within projects dirs:

cd Pytest-Automation-Project/api_tests      ->  pytest

cd Pytest-Automation-Project/gui_tests      ->  pytest

cd Pytest-Automation-Project/unit_tests     ->  pytest


#### Run tests by markers:
You can run the tests by marker 
(Search for: pytestmark global variable to see which module collects by which marker)


pytest -m gui 

pytest -m api

pytest -m unit

#### Run by marker and create HTML report:

pytest -m gui --html=ui_tests/reports/my_report.html --self-contained-html

pytest -m api --html=api_tests/reports/my_report.html --self-contained-html

pytest -m unit --html=api_tests/reports/my_report.html --self-contained-html


### INFO:
* Every project has conftest.py file, which in charge of the TestClasses setups for each project.
* Default env value is production
* Please don't run constantly to avoid blocking from the API.
