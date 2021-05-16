## Test Automation Project - Pytest Framework
### This repo contains 3 projects examples, all of them written using Pytest framework.


| Project  | Dir | Tested Service | Library used | Design
| ------------- | ------------- | ------------- | ------------- |------------- |
| API  | ```/api_tests```| https://petstore.swagger.io | requests |API endpoints to classes  |
| WEB GUI  | ```/gui_test``` | https://www.saucedemo.com | selenium, webdriver-manager |Page Object Pattern |
| Unit | ```/unit_test``` | My common functions | pytest-mock | Test file in module level

Install req file 
```
cd Pytest-Automation-Project/
pip install -r requirements.txt
```

You can run "pytest" command from a single project dir or repo's root.


## Userful Commands
| Command  | Info | Inputs Examples
| ------------- | ------------- | ------------- |
| ```pytest -m api```  | Run tests by marker, pytestmark global variable | ```-m api```, ```-m gui```, ```-m unit```  |
| ```pytest --html=reports/my_report.html --self-contained-html```  | Creates HTML report |
| ```pytest -m api --api_env=petstore``` | *Run inside **/api_tests** to enable this terminal option | ```-m api --api_env=qa```  |
| ```pytest -m gui --gui_env=www``` | *Run inside **/gui_tests** to enable this terminal option | ```-m gui --gui_env=qa-petstore```  |
| ```pytest -m gui --browser=chrome```  | *Run inside **/gui_tests** - Choose browser to initiate| ```--browser=firefox```, ```--browser=edge```, ```--browser=chrome```  |
| ```pytest -n 2```  | Run tests in parallel | ```-n 2```, ```-n 3```  |


### INFO:
* Every project has conftest.py file, which in charge of the TestClasses setups for each project.
* Default env value is production.
* Please don't run constantly to avoid rate-limit.
* Might need to update your Chrome/Edge/Firefox local browsers.
