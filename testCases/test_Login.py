from selenium import webdriver
import pytest
from PageObjectModel.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
import time
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("**************Test_001_Login*******************")
        self.logger.info("***********Verifying Home page title*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********Home page title is passed************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*****************Home page title is failed*************")
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_UserName(self.username)
        self.lp.set_Password(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
