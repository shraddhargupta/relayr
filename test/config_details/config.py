#This file contains config related data for this project.

import os

current_directory=os.getcwd().replace('\\','/')
app_URL='https://google.de'
testcase_csv = (current_directory+ "/testdata/Driver.csv")
driver_path=(current_directory+"/drivers/chromedriver.exe")
html_report=current_directory+"/reports"