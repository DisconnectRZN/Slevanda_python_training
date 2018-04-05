# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_group(self):
        success = True
        wd = self.wd
        wd.get("https://www.invitro.ru/")
        wd.find_element_by_css_selector("span.drugtown.active").click()
        wd.find_element_by_css_selector("span.drugtown.active").click()
        wd.find_element_by_link_text("Москва").click()
        wd.find_element_by_css_selector("body").click()
        wd.find_element_by_link_text("Анализы и цены").click()
        wd.find_element_by_css_selector("img.addimagink").click()
        wd.find_element_by_css_selector("img.addimagink").click()
        wd.find_element_by_css_selector("input.ofz").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
