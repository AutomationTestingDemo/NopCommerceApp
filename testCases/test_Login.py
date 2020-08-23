from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readConfigFile import ReadConfig
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from utilities.costumLogger import LogGen

class Test_001_Login:
    baseUrl=ReadConfig.getAppUrl()
    username=ReadConfig.getUsername()
    password =ReadConfig.getPwd()
    logger = LogGen.loggen()
    @pytest.mark.regresion
    def test_homePageTitle(self,setup):
        self.logger.info("***********************Test_001_Login*************************")
        self.logger.info("***********************Verify HomePage Title*************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        actTitle = self.driver.title
        if actTitle=="Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("***********************Verify HomePage Title Passed*************************")
        else:
            self.driver.save_screenshot("..\\screenshots"+"\\test_homePageTitle.png")
            self.driver.close()
            self.logger.info("***********************Verify HomePage Title failed*************************")
            assert False
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***********************Test_001_Login*************************")
        self.logger.info("***********************Verify Login Test*************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        lp = Login(self.driver)
        lp.enterUserName(self.username)
        lp.enterPassword(self.password)
        lp.clickLoginButton()
        actTitle = self.driver.title
        if actTitle=='Dashboard / nopCommerce administration':
            self.driver.close()
            assert True
            self.logger.info("***********************Verify LoginTest Passed*************************")
        else:
            self.driver.save_screenshot("..\\screenshots"+"\\test_login.png")
            self.driver.close()
            assert False
            self.logger.info("***********************Verify LoginTest failed*************************")