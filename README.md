Getting Started:
* We'll need to install the Selenium package. 
* We can use pip to install with following command "pip install -U selenium". 
* More information can be found here https://pypi.org/project/selenium/
* Next we'll need the drivers to interface with the specific browsers we want to run our tests on. 
* The browsers section of https://www.selenium.dev/downloads/ has more details and you can also get them from https://pypi.org/project/selenium/ 
under drivers section.

Other packages used:
* Webdriver manager - manages binary drivers that interface with different browsers for us - pip install webdriver-manager
* Openpyxl - Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files - pip install openpyxl
* Faker - generates fake data - pip install Faker
* Pytest - Testing framework that scales to support complex functional testing for applications and libraries - pip install pytest
* Softest - Supports the soft assert style of testing - pip install softest
* Ddt - A library to multiply test cases - pip install ddt


Note: It is better to use dynamic waits than to use time.sleep, time.sleep here is to mainly show the results of the automation
