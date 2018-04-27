class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        # login
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath('*[@id="LoginForm"]input[3]').click()



    def logout(self):
        # logout
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        driver = self.app.driver
        return self.get_logged_user() == username

    def get_logged_user(self):
        driver = self.app.driver
        return driver.find_element_by_xpath("//div[@id='top']/form/b").text[1:-1]

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)