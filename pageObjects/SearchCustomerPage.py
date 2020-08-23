class SearchCustomer:
    searchEmailTextbox_id="SearchEmail"
    searchFirstNameTextbox_id="SearchFirstName"
    searchLastNameTextbox_id="SearchLastName"
    searchButton_id="search-customers"
    resultsTable_xpath="//table[@id='customers-grid']"
    totalRows_xpath="//*[@id='customers-grid']/tbody/tr"
    totalCols_xpath="//*[@id='customers-grid']/tbody/tr[1]/td"

    def __init__(self,driver):
        self.driver=driver
    def emailsearch(self,email):
        self.driver.find_element_by_id(self.searchEmailTextbox_id).send_keys(email)
    def firstNameSearch(self,firstName):
        self.driver.find_element_by_id(self.searchFirstNameTextbox_id).send_keys(firstName)
    def lastNameSearch(self,lastName):
        self.driver.find_element_by_id(self.searchLastNameTextbox_id).send_keys(lastName)
    def clickSearchButton(self):
        self.driver.find_element_by_id(self.searchButton_id).click()
    def totalRows(self):
        tRows= len(self.driver.find_elements_by_xpath(self.totalRows_xpath))
        return tRows
    def totalCols(self):
        tcols=  len(self.driver.find_elements_by_xpath(self.totalCols_xpath))
        return tcols
    def searchCustomerByEmail(self,email):
        flag = False
        trows = self.totalRows()
        table=self.driver.find_element_by_xpath(self.resultsTable_xpath)
        for r in range(1,trows+1):
            resultEmail=table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if resultEmail==email:
                flag=True
                break
        return flag

    def searchCustomerByName(self,name):
        flag = False
        trows = self.totalRows()
        table=self.driver.find_element_by_xpath(self.resultsTable_xpath)
        for r in range(1,trows+1):
            resultName=table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name in resultName:
                flag=True
                break
        return flag