class SearchCustomer:

    semail_id = "SearchEmail"
    sfirstName_id = "SearchFirstName"
    sLastName_id = "SearchLastName"
    search_id = "search-customers"
    searchresults_xpath = "//table[role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver


    def setEmail(self,email):
        self.driver.find_element_by_id(self.semail_id).clear()
        self.driver.find_element_by_id(self.semail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.sfirstName_id).clear()
        self.driver.find_element_by_id(self.sfirstName_id).send_keys(fname)

    def setFirstName(self,lname):
        self.driver.find_element_by_id(self.sLastName_id).clear()
        self.driver.find_element_by_id(self.sLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            nameid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]")
            if nameid == name:
                flag = True
                break
        return flag