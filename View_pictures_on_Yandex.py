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
        wd.get("https://www.google.ru/")
        wd.find_element_by_id("sb_ifc0").click()
        wd.find_element_by_id("lst-ib").click()
        wd.find_element_by_id("lst-ib").clear()
        wd.find_element_by_id("lst-ib").send_keys("rfhnbyrb")
        wd.find_element_by_id("lst-ib").click()
        wd.find_element_by_id("lst-ib").clear()
        wd.find_element_by_id("lst-ib").send_keys("картинки")
        wd.find_element_by_css_selector("input.lsb").click()
        wd.find_element_by_link_text("Картинки по запросу картинки").click()
        wd.find_element_by_name("cSxKcymuOCYr1M:").click()
        wd.find_element_by_xpath("//a[@id='irc_ra']/div").click()
        ActionChains(wd).double_click(wd.find_element_by_id("irc_ra")).perform()
        ActionChains(wd).double_click(wd.find_element_by_id("irc_ra")).perform()
        wd.find_element_by_id("irc_cb").click()
        wd.find_element_by_xpath("//a[@id='logo']/img").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
