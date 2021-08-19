from selenium import webdriver
import pytest
from PageObjectModel.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
import time
from Utilities.customLogger import LogGen
from Utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getURL()
    path = ".//TestData/Login.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        print("No: of rows in a excel",self.rows)

        lst_status= []  #Empty list variable
        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.set_UserName(self.user)
            self.lp.set_Password(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("************TC Passed****************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

                elif self.exp == "Fail":
                    self.logger.info("********TC Failed*********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("********TC Failed***********")
                    lst_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info("*******TC Passed*********")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False

