import random
import string
from selenium import webdriver
from utilities.costumLogger import LogGen
from utilities.readConfigFile import ReadConfig
from pageObjects.CustomerPage import AddCustomer
from pageObjects.LoginPage import Login
import pytest


class Test_003_AddCustomer:
    baseUrl=ReadConfig.getAppUrl()
    userName= ReadConfig.getUsername()
    password= ReadConfig.getPwd()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.driver=setup
        self.driver.get(self.baseUrl)
        lp=Login(self.driver)
        lp.enterUserName(self.userName)
        lp.enterPassword(self.password)
        lp.clickLoginButton()
        actTitle=self.driver.title
        if actTitle=="Dashboard / nopCommerce administration":
            assert True
            print("Login success")
        else:
            print("Login Failed")
            assert False
        addCustomer= AddCustomer(self.driver)
        addCustomer.clickOnCustomerLink()
        addCustomer.clickOnCustomerMenuItem()
        addCustomer.clickAddNewCustomer()
        # addCustomer.enterEmail("Kalyan"+str(random.randint(0,99))+"@gmail.com")
        addCustomer.enterEmail(randon_generator()+ "@gmail.com")
        addCustomer.enterPassword("password@123")
        addCustomer.enterFirstName("Kalyan")
        addCustomer.enterLastName("Mundra")
        addCustomer.selectGender("male")
        addCustomer.enterDob("8/3/1994")
        addCustomer.enterCompanyName("SAP")
        addCustomer.isTaxExempt("yes")
        addCustomer.selectNewsLetterRoles("storeName")
        addCustomer.selectCustomerRoles("Guests")
        addCustomer.selectVendorID("Vendor 1")
        addCustomer.checkActiveCheckbox(False)
        addCustomer.enterAdminComments("Good Customer")
        addCustomer.clickSaveButton()
        self.msg = self.driver.find_element_by_tag_name('body').text
        if "The new customer has been added successfully" in self.msg:
            assert True,"Add customer Test is passed"
        else:
            self.driver.save_screenshot(".\\screenshots"+"\\test_login.png")
            assert False,"Add customer Test is failed"
        self.driver.close()

def randon_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))