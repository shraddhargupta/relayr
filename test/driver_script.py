import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import HtmlTestRunner
from config_details import config
from read_testdata import get_execution_details
from unittest import SkipTest
from selenium.common.exceptions import NoSuchElementException


# This is the starting point of framework.
# Functionalty : This file will read data from .csv file located in  and execute testcases.
# Testcase execution is controlled by RunFlag
class TestGoogleSearch(unittest.TestCase):
    # setUpClass :This function will execute basic setup required for test execution.
    # Improvement : We can use configuration to pick webbrowser dynamically .
    # This will be helpful in  cross Browser testing
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=config.driver_path)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    # test_Search_VerifyTitle :This function will verify title of webpage displayed after search.
    # Search Criteria should be part of title of web browser.
    def test_Search_VerifyTitle(self):
        search_list = get_execution_details(1)
        if search_list == 'N':
            raise SkipTest
        for search_string in search_list:
            print('<br><b>Scenario :Verify page title after searching string : ', search_string, '</b><br>')
            self.driver.get(config.app_URL)
            print('&nbsp;&nbsp;&nbsp;&nbsp;Step 1:Navigating to URL   : ', config.app_URL, '<br>')
            element = self.driver.find_element_by_xpath("//input[@title='Search']")
            element.send_keys(search_string)
            print('&nbsp;&nbsp;&nbsp;&nbsp;Step 2:Enter Search Criteria  : ', search_string, '<br>')
            element.send_keys(Keys.RETURN)
            print('&nbsp;&nbsp;&nbsp;&nbsp;Step 3: Click on Google Search button .', '<br>')
            title = self.driver.title
            print("&nbsp;&nbsp;&nbsp;&nbsp;Step 4: Retrieve title for search result : ", title, '<br>')
            self.assertEqual(title, search_string + ' - Google Search')

    # test_VerifySearchResults_displayed :This will verify if search results are displayed or not
    def test_VerifySearchResults_displayed(self):
        search_list = get_execution_details(2)
        if search_list == 'N':
            raise SkipTest
        for search_string in search_list:
            print('<br><b>Scenario :Verify search results displayed after entering : ', search_string, '</b><br>')
            self.driver.get(config.app_URL)
            print('&nbsp;&nbsp;&nbsp;&nbsp;Step 1:Navigating to URL   : ', config.app_URL, '<br>')
            element = self.driver.find_element_by_xpath("//input[@title='Search']")
            element.send_keys(search_string)
            print('&nbsp;&nbsp;&nbsp;&nbsp;Step 2:Enter Search Criteria  : ', search_string, '<br>')
            element.send_keys(Keys.RETURN)
            print('&nbsp;&nbsp;&nbsp;&nbsp;Step 3: Click on Google Search button .', '<br>')
            try:
                result_status = self.driver.find_element_by_xpath("//div[@id='result-stats']")
                result = result_status.is_displayed()
                if result:
                    print('&nbsp;&nbsp;&nbsp;&nbsp;Result: Total Number of search results displayed : ',
                          result_status.text, '<br>')

            except NoSuchElementException:
                print(
                    "&nbsp;&nbsp;&nbsp;&nbsp;Result:Please enter valid input.No search results are displayed for : " + search_string,
                    '<br>')

    # Below testcase will verify if webpage has any broken links .To verify that we are using HTTP request status code
    def test_brokeninks(self):
        search_list = get_execution_details(3)
        if search_list == 'N':
            raise SkipTest
        broken_link = False
        for search_string in search_list:
            print('<br><b>Scenario :Verify if webpage has broken links', '</b><br>')
            self.driver.get(config.app_URL)
            print('&nbsp;&nbsp;&nbsp;&nbsp;Step 1:Navigating to URL   : ', config.app_URL, '<br>')
            element = self.driver.find_element_by_xpath("//input[@title='Search']")
            element.send_keys(search_string)
            print('&nbsp;&nbsp;&nbsp;&nbsp;Step 2:Enter Search Criteria  : ', search_string, '<br>')
            element.send_keys(Keys.RETURN)
            print('&nbsp;&nbsp;&nbsp;&nbsp;Step 3: Click on Enter .', '<br>')
            links = self.driver.find_elements_by_css_selector("a")
            print('&nbsp;&nbsp;&nbsp;&nbsp;Step 4:Retrieve all links on a web page.', '<br>')

            for link in links:
                pageLink = link.get_attribute('href')
                if (pageLink is not None):
                    request = requests.head(link.get_attribute('href'))
                    if (request.status_code >= 400) and (request.status_code != 403):
                        print('&nbsp;&nbsp;&nbsp;&nbsp;Error :Web Page contains Broken Link.', pageLink,
                              'Status Code is :', request.status_code, '<br>')
                        broken_link = True
                    break

        self.assertFalse(broken_link, msg='Webpage does not contain any broken link.')

    # tearDownClass : This method will close browser after completing execution
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(verbosity=3, report_title='Google Search : GUI Automation Report',
                                                 output='../reports',
                                                 descriptions='This Report provides summary of all executed testcases.'))
