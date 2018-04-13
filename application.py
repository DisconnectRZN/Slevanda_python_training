from selenium import webdriver

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def logout(self):
        # logout
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        # return to groups page
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def create_group(self, group):
        driver = self.driver
        self.open_group_page()
        # init group creation
        driver.find_element_by_name("new").click()
        # fill gtoup form
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_group_page(self):
        # open group page
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def login(self, username, password):
        # login
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath('//*[@id="LoginForm"]/input[3]').click()

    def open_home_page(self):
        # open home page
        driver = self.driver
        driver.get("http://localhost/addressbook/group.php")

    def  destroy(self):
        self.driver.quit()


