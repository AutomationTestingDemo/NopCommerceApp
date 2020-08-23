import pytest

from pageObjects.CustomerPage import AddCustomer
from pageObjects.LoginPage import Login
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readConfigFile import ReadConfig


class Test_005_SearchCustomer:
    baseUrl=ReadConfig.getAppUrl()
    username=ReadConfig.getUsername()
    password= ReadConfig.getPwd()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.driver=setup
        self.driver.get(self.baseUrl)
        lp= Login(self.driver)
        lp.enterUserName(self.username)
        lp.enterPassword(self.password)
        lp.clickLoginButton()
        actTitle = self.driver.title
        if actTitle == "Dashboard / nopCommerce administration":
            assert True
            print("Login success")
        else:
            print("Login Failed")
            assert False
        addCustomer=AddCustomer(self.driver)
        addCustomer.clickOnCustomerLink()
        addCustomer.clickOnCustomerMenuItem()
        sc=SearchCustomer(self.driver)
        sc.lastNameSearch("Holmes")
        sc.clickSearchButton()
        boolResult = sc.searchCustomerByName("Holmes")
        assert boolResult==True
        print("search customer by name is passed")
        self.driver.close()
