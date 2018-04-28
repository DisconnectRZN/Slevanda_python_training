import time
from selenium.webdriver.support.ui import Select
from Slevanda_python_training.Model.contact import Contact
import re



class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").send_keys(contact.middle)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").send_keys(contact.nick)
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").send_keys(contact.homephone)
        driver.find_element_by_name("mobile").send_keys(contact.mobilephone)
        driver.find_element_by_name("work").send_keys(contact.workphone)
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
        driver.find_element_by_name("phone2").send_keys(contact.secondaryphone)
        driver.find_element_by_name("notes").send_keys(contact.notes)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    contact_chace = None

    def get_contact_list(self):
        if self.contact_chace is None:
            driver = self.app.driver
            self.app.open_home_page()
            self.contact_chace = []
            for element in driver.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_chace.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2], secondaryphone=all_phones[3]))
                return list(self.contact_chace)

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = driver.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        text = driver.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)

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
        self.app.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))