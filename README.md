## Test Automation Project - Pytest Framework


#### INFO:
This repo contains 3 test automation projects [API, GUI, Unit] written in Python using `Pytest`.
Every project has `conftest.py` file, which in charge of the `TestClasses` setups for each project - search for `_test_class_setup` @fixtures for constructors.


#### Projects:
| Project  | Dir | Tested Service | Library used | Design
| ------------- | ------------- | ------------- | ------------- |------------- |
| API  | ```/api_tests```| https://petstore.swagger.io | requests |API endpoints to classes  |
| WEB GUI  | ```/gui_test``` | https://www.saucedemo.com | selenium, webdriver-manager |Page Object Pattern |
| Unit | ```/unit_test``` | Demo functions | pytest-mock | Test file in module level


#### Installation
All 3 projects has been tested and verified with `Python 3.7` on `MacOS` & `Windows 10`.
Since webdriver-manager usage, to run GUI tests you might need to update your Chrome/Edge/Firefox browsers.


To install project's requirements, in terminal navigate to main dir:

```
cd Pytest-Automation-Project/
pip install -r requirements.txt
```

#### Commands

You can run "pytest" command from a single project dir or repo's root.

* Default env value is production for all projects.
* Please don't run constantly to avoid rate-limit.

| Command  | Info | Inputs Examples
| ------------- | ------------- | ------------- |
| ```pytest -m api```  | Run tests by marker, pytestmark global variable | ```-m api```, ```-m gui```, ```-m unit```  |
| ```pytest -m api --api_env=petstore``` | *Run inside **/api_tests** to enable this terminal option | ```-m api --api_env=qa```  |
| ```pytest -m gui --gui_env=www``` | *Run inside **/gui_tests** to enable this terminal option | ```-m gui --gui_env=qa-petstore```  |
| ```pytest -m gui --browser=chrome```  | *Run inside **/gui_tests** - Choose browser to initiate| ```--browser=firefox```, ```--browser=edge```, ```--browser=chrome```  |
| ```pytest -n 2```  | Run tests in parallel | ```-n 2```, ```-n 3```  |


#### Reports

##### pytest-html
pytest-html is a plugin that generate test report HTML file with a single command,
add this to your Pytest run command:


```
pytest --html=reports/my_report.html
pytest --html=reports/my_report.html --self-contained-html
```

![pytest-html](https://i.imgur.com/IL93Zgq.png)