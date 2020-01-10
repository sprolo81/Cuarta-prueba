from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner


class Items(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('https://www.modelit.xyz/')
        self.driver.maximize_window()

    def test_Titulo(self):
        self.assertIn('Modelit',self.driver.title)

    def test_Links(self):
        #self.driver.find_element_by_xpath("//rs-arrow[@class='tp-leftarrow tparrows hesperiden']" ).click()
        #self.driver.find_element_by_xpath("//rs-layer[@id='slider-5-slide-59-layer-35']").click()
        self.driver.find_element_by_link_text("About Us").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Services").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Our Clients").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Careers").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Blog").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Contact Us").click()
        time.sleep(2)
        
    def test_Box(self):
        CoUs = self.driver.find_element_by_link_text("Contact Us").click()
        Box1 = self.driver.find_element_by_id("sf_first_name").send_keys("Sebastian")
        Box2 = self.driver.find_element_by_id("sf_last_name").send_keys("Prolo")
        Box3 = self.driver.find_element_by_id("sf_company").send_keys("Modelit")
        Box4 = self.driver.find_element_by_id("sf_email").send_keys("sprolo81@gmail.com")
        Box5 = self.driver.find_element_by_id("sf_phone").send_keys("09090909")
        self.driver.find_element_by_xpath("//span[contains(text(),'Submit')]").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Home").click()
        time.sleep(2)

        print("Test completo")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reportes"))