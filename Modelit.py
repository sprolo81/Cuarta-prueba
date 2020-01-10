from selenium import webdriver
import unittest
import time
import HtmlTestRunner

class TestModelit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('https://www.modelit.xyz')
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reporte HTML'))

