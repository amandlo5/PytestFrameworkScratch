import time
import pytest
from selenium import webdriver
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from PageObjectModel.LoginPage import LoginPage
from PageObjectModel.CustomerPage import AddCustomer
from PageObjectModel.SearchCustomer import SearchCustomer
import random
import string


class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchCustomerByName(self, setup):
        self.logger.info("*********Test_004_SearchCustomerByEmail*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.lp = LoginPage(self.driver)
        self.lp.set_UserName(self.username)
        self.lp.set_Password(self.password)
        self.lp.clickLogin()
        self.logger.info("*********TC_LOgin_Passed***********")

        self.logger.info("***********Starting SearchCustomerByEmail_TC*************")
        self.add = AddCustomer(self.driver)
        self.add.clickCustomers()
        self.add.clickCustomer_menu()

        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.driver.close()