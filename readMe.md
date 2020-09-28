
#GitHub :https://github.com/shraddhargupta/relayr.git
#git commands :
     git clone https://github.com/shraddhargupta/relayr.git

# pip installation :

 pandas:pip3 install pandas --no-build-isolation
 html-testRunner:pip install html-testRunner
 selenium:pip install selenium
 requests :pip install requests


#This Project requires below python libraries
python version :Python 3.8.5

| library Name  |  Version |
|---------------|----------|
| pandas        | 1.1.2    |
| requests      | 2.24.0   |
| selenium      | 3.141.0  |
|html-testRunner| 3.141.0  |



chromedriver.exe

#Starting execution :
 run driver_script.py as python file .

#Basic Framework structure :

 This framework is designed using Selenium webdriver , python unittest , python pandas
 and HtmlTestRunner for reporting.

1. folder name: test  file name : driver_script.py
2. reports:This folder will store all html results generated .
3. testdata: This folder contains file Driver.csv .This serve as input for all testcases.
4.drivers: This folder contains webdriver for browsers
5.config_details : config.py file stores all configuration related data
6.screenshots : This folder will store screenshots if any


#I would like to propose below improvements

1.Reporting : As a temporary solution I have tried to customise report in code itself.
              More advance reporting can be implemented by providing customize HTML report or by using advanced reporting mechanism.
2.Exception Handling:Currently project has very limited exception handling in place.
3.Objects/Web elements related to a single page can be stored in separate file and not hardcoded in main script.
