# api_tests Automation Project


## Test Automation Project - Pytest Framework
#############################################################################
I have used this lovely API to write some tests in Pytest framework.
https://official-joke-api.appspot.com/random_joke
Please support them.
########### #################################################################

You can run the tests by marker (Search for: pytestmark global variable)

### How to:
inside /Pytest-Automation-Project

pip install -r requirements.txt

##### Run tests by markers:
pytest -m gui 

pytest -m api

pytest -m unit

##### Run by marker and create HTML report:

pytest -m gui --html=ui_tests/reports/my_report.html --self-contained-html

pytest -m api --html=api_tests/reports/my_report.html --self-contained-html


#### INFO:
* Every project has conftest.py file, which in charge of the TestClasses setups for each project.
* Default env value is production
* Please don't run constantly to avoid blocking from the API.