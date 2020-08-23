from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readConfigFile import ReadConfig
import pytest
from utilities.costumLogger import LogGen
from utilities import xlutilities

class Test_002_Login_ddt:
    baseUrl=ReadConfig.getAppUrl()
    path=".//testData/TestData.xlsx"
    sheetName="creds"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***********************Test_002_Login_ddt*************************")
        self.logger.info("***********************Verify Login Test*************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        lp = Login(self.driver)
        rcount = xlutilities.getRowCount(self.path,self.sheetName)
        for r in range(2,rcount+1):
            self.username = xlutilities.readData(self.path,self.sheetName,r,1)
            self.password = xlutilities.readData(self.path, self.sheetName, r, 2)
            lp.enterUserName(self.username)
            lp.enterPassword(self.password)
            lp.clickLoginButton()
            actTitle = self.driver.title
            if actTitle == 'Dashboard / nopCommerce administration':
                lp.clickLogoutButton()
                xlutilities.writeData(self.path,self.sheetName,r,3,"Pass")
            else:
                self.driver.save_screenshot(".\\screenshots" + "\\test_login.png")
                xlutilities.writeData(self.path, self.sheetName, r, 3, "Fail")
        self.driver.close()