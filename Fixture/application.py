from selenium import webdriver
from Slevanda_python_training.Fixture.session import SessionHelper
from Slevanda_python_training.Fixture.group import GroupHelper
from Slevanda_python_training.Fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_home_page(self):
        # open home page
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()


