from selenium import webdriver
class LoginPage:

    email_id = "Email"
    password_id = "Password"
    login_xpath = "//button[@type='submit']"
    logout_partial_link = "Logout"

    def __init__(self,driver):
        self.driver = driver


    def set_UserName(self,username):
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(username)

    def set_Password(self,password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_partial_link_text(self.logout_partial_link).click()

