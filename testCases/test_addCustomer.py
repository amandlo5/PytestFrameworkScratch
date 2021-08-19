import time
import pytest
from selenium import webdriver
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from PageObjectModel.LoginPage import LoginPage
from PageObjectModel.CustomerPage import AddCustomer
import random
import string


class Test_003_AddCustomer:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self, setup):
        self.logger.info("*********Test_003_AddCustomer*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.lp = LoginPage(self.driver)
        self.lp.set_UserName(self.username)
        self.lp.set_Password(self.password)
        self.lp.clickLogin()
        self.logger.info("*********TC_LOgin_Passed***********")

        self.logger.info("***********Starting AddCustomer_TC*************")
        self.add = AddCustomer(self.driver)
        self.add.clickCustomers()
        self.add.clickCustomer_menu()
        self.add.addNew()
        self.logger.info("******Providing Customer info********")
        self.email = random_generator() + "@gmail.com"
        self.add.setEmail(self.email)
        self.add.setPassword("test123")
        self.add.setFirstName("Amol")
        self.add.setLastName("Mandloi")
        self.add.setGender("Male")
        self.add.dob("3/15/1993")
        self.add.setCompanyName("CTS")
        self.add.setCustomerRoles("Guests")
        self.add.setManagerOfVendor("Vendor 1")
        self.add.setAdminComment("Testing")
        self.add.clickOnSave()

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if "customer has been added successfully" in self.msg:
            assert True == True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_add_customer.png")
            assert True == False

        self.driver.close()

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
