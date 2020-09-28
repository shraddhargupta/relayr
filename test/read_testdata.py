import pandas as pd
from config_details import config
import logging

logging.basicConfig(level="INFO")


# read_csv : This function will read data from csv
def read_csv():
    filepath = config.testcase_csv
    driver_file_data = pd.read_csv(filepath, header=0)
    logging.info("Test Data file is loaded.")
    return driver_file_data


# get_execution_details : This will fetch Test Data in the form of list for given test case ID
def get_execution_details(id_test_case):
    testcase_details = read_csv()
    search_criteria_list = 'N'
    # Filter CSV Data with RunFlag to execute testcase which are marked as Y
    df_testdata = testcase_details[testcase_details['RunFlag'] == 'Y']
    if df_testdata.empty:
        logging.info('Run Flag for all testcases are marked as N ')
    else:
        testcase_data = df_testdata[df_testdata['ID'] == id_test_case]
        if not testcase_data.empty:
            testdata = testcase_data[testcase_data.ID == id_test_case].TestData.item()
            search_criteria_list = testdata.split('|')
    return search_criteria_list
