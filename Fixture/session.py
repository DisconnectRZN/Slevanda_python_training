class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        # login
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath('//*[@id="LoginForm"]/input[3]').click()



    def logout(self):
        # logout
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()