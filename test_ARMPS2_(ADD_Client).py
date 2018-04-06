# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
import unittest, time, re


class TestARMPS2ADDClient(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_a_r_m_p_s2_a_d_d_client(self):
        driver = self.driver
        driver.get("http://localhost:8095/armps/login.html")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("slevanda")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("Rt63cxz12")
        driver.find_element_by_name("login").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='applicationContent']/div/table/tbody/tr[2]/td/div/div/div/div[2]/div/div/div[2]/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
        time.sleep(2)
        driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys(u"Тестовый")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='applicationContent']/div/table/tbody/tr[2]/td/div/div/div/table/tbody/tr/td[4]/div").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
