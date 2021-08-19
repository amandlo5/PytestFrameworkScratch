import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


class AddCustomer:
    customers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    customer_menu_item_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    addnew_xpath = "//a[@class='btn btn-primary']"
    email_xpath = "//input[@id='Email']"
    password_xpath = "//input[@id='Password']"
    firstname_id = "FirstName"
    lastname_id = "LastName"
    male_gender_id = "Gender_Male"
    female_gender_id = "Gender_Female"
    dob_name = "DateOfBirth"
    company_id = "Company"
    customerroles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    administrator_xpath = "//li[contains(text(),'Administrators')]"
    ForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    Guests_xpath = "//li[contains(text(),'Guests')]"
    Registered_xpath = "//li[contains(text(),'Registered')]"
    Vendors_xpath = "//li[contains(text(),'Vendors')]"
    mgr_vendor_xpath = "//select[@id='VendorId']"
    admin_comment_id = "AdminComment"
    save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickCustomers(self):
        self.driver.find_element_by_xpath(self.customers_menu_xpath).click()

    def clickCustomer_menu(self):
        self.driver.find_element_by_xpath(self.customer_menu_item_xpath).click()

    def addNew(self):
        self.driver.find_element_by_xpath(self.addnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)

    def setPassword(self,pswd):
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(pswd)

    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.firstname_id).clear()
        self.driver.find_element_by_id(self.firstname_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_id(self.lastname_id).clear()
        self.driver.find_element_by_id(self.lastname_id).send_keys(lname)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.male_gender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.female_gender_id).click()

        else:
            self.driver.find_element_by_id(self.male_gender_id).click()

    def dob(self,dob):
        self.driver.find_element_by_name(self.dob_name).send_keys(dob)

    def setCompanyName(self,cname):
        self.driver.find_element_by_id(self.company_id).send_keys(cname)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(".//span[@title='delete']").click()
        self.driver.find_element_by_xpath(self.customerroles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.list = self.driver.find_element_by_xpath(self.Registered_xpath)

        elif role == "Administrator":
            self.list = self.driver.find_element_by_xpath(self.administrator_xpath)

        elif role == "Guests":
            self.list = self.driver.find_element_by_xpath(self.Guests_xpath)

        elif role == "Forum Moderators":
            self.list = self.driver.find_element_by_xpath(self.ForumModerators_xpath)

        elif role == "Vendors":
            self.list = self.driver.find_element_by_xpath(self.Vendors_xpath)

        else:
            self.list = self.driver.find_element_by_xpath(self.Registered_xpath)

        time.sleep(3)

        self.driver.execute_script("arguments[0].click();",self.list)

    def setManagerOfVendor(self,value):
        select = Select(self.driver.find_element_by_xpath(self.mgr_vendor_xpath))
        select.select_by_visible_text(value)

    def setAdminComment(self,comment):
        self.driver.find_element_by_id(self.admin_comment_id).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.save_xpath).click()
