from pageObjects.CustomerPage import AddCustomer
from pageObjects.LoginPage import Login
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readConfigFile import ReadConfig
import pytest


class Test_004_SearchCustomer:
    baseUrl=ReadConfig.getAppUrl()
    username=ReadConfig.getUsername()
    password= ReadConfig.getPwd()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
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
        sc.emailsearch("steve_gates@nopCommerce.com")
        sc.clickSearchButton()
        boolResult = sc.searchCustomerByEmail("steve_gates@nopCommerce.com")
        assert boolResult==True
        print("search customer by email is passed")
        self.driver.close()