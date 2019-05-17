import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class StackOverflowSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver_mac')

    def test_search_in_stack_overflow(self):
        driver = self.driver
        driver.get('https://stackoverflow.com/')
        self.assertIn(
            'Stack Overflow - Where Developers Learn, Share, & Build Careers', driver.title)
        elem = driver.find_element_by_css_selector('#search > div > input')
        elem.send_keys('hello world')
        elem.send_keys(Keys.RETURN)
        self.assertTrue('Search Results' in driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
