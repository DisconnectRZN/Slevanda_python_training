import time
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact):
        driver = self.app.driver
        time.sleep(2)
        driver.find_element_by_link_text("add new").click()
        time.sleep(2)
        # fill new contact form
        driver.find_element_by_name("firstname").send_keys(contact.first)
        time.sleep(2)
        driver.find_element_by_name("middlename").send_keys(contact.middle)
        driver.find_element_by_name("lastname").send_keys(contact.last)
        driver.find_element_by_name("nickname").send_keys(contact.nick)
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").send_keys(contact.home_telephone)
        driver.find_element_by_name("mobile").send_keys(contact.mobile_telephone)
        driver.find_element_by_name("work").send_keys(contact.work_telephone)
        driver.find_element_by_name("fax").send_keys(contact.fax_telephone)
        driver.find_element_by_name("email").send_keys(contact.email_1)
        driver.find_element_by_name("email2").send_keys(contact.email_2)
        driver.find_element_by_name("email3").send_keys(contact.email_3)
        driver.find_element_by_name("homepage").send_keys(contact.home_page)
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        driver.find_element_by_name("byear").send_keys(contact.byear)
        Select(driver.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        Select(driver.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        driver.find_element_by_name("ayear").send_keys(contact.ayear)
        driver.find_element_by_name("address2").send_keys(contact.address_2)
        driver.find_element_by_name("phone2").send_keys(contact.home_address)
        driver.find_element_by_name("notes").send_keys(contact.notes)
        # submit new contact creation
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()



    def delete_first_contact(self, app):
        driver = self.app.driver
        # select first group
        app.open_home_page()
        driver.find_element_by_name("selected[]").click()
        # submit deletion
        driver.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        alert = app.driver.switch_to_alert()
        alert.accept()

    def count_contact(self, app):
        driver = self.app.driver
        app.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))