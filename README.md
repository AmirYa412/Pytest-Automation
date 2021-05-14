## Test Automation Project - Pytest Framework
### This repo contains 3 projects example, all of them written using Pytest framework.


| Project  | Dir | Tested Service | Library used
| ------------- | ------------- | ------------- | ------------- |
| API  | /api_tests| https://petstore.swagger.io | requests |
| GUI  | /gui_test | https://www.saucedemo.com | selenium, webdriver-manager |
| Unit |/unit_test | My common functions | pytest-mock |

You can run "pytest" command from a single project dir or repo's root.


## Userful Commands
| Command  | Info | Inputs Examples
| ------------- | ------------- | ------------- |
| pytest -m api  | Run tests by marker, pytestmark global variable | api, gui, unit  |
| pytest --html=reports/my_report.html --self-contained-html  | Creates HTML report |   |
| pytest -m api  | Run tests by marker, pytestmark global variable | api, gui, unit  |
| pytest -m gui --browser=chrome  | Choose browser to initiate (Only Chrome works currently) | firefox, explorer, chrome  |
| pytest -n 2  | Run tests in parallel | int  |



##### Run tests by markers:
You can run the tests by marker 
(Search for: pytestmark global variable to see which module collects by which marker)


### INFO:
* Every project has conftest.py file, which in charge of the TestClasses setups for each project.
* Default env value is production.
* Please don't run constantly to avoid blocking from the API.
* Might need to update your Chrome/Edge/Firefox local browsers.
