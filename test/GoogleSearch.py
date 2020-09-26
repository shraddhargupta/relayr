import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import HtmlTestRunner
from config import config


class TestGoogleSearch(unittest.TestCase):
    @classmethod
    def test_basic(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(config.app_URL)


    # def test_second(self):
    #
    #     self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
    #     self.driver.find_element_by_name("btnK").click()
    #     title=self.driver.title
    #     print("Second test ",title

    def test_brokeninks(self):
        element=self.driver.find_element_by_xpath("//input[@title='Search']")
        element.send_keys('Hello')
        element.send_keys(Keys.RETURN)
        links = self.driver.find_elements_by_css_selector("a")


        for link in links:

            #verify if links are not none
            pageLink=link.get_attribute('href')
            if (pageLink is not None):

                r = requests.head(link.get_attribute('href'))
                # print(pageLink, r.status_code)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')

if __name__ == '__main__':

   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
