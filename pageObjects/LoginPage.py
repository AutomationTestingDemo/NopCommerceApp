from selenium import webdriver
class Login:
    username_textbox_id ='Email'
    password_textbox_id= 'Password'
    login_button_xpath="//input[@type='submit']"
    logout_button_xpath="//a[text()='Logout']"

    def __init__(self,driver):
        self.driver=driver
    def enterUserName(self,username):
        uName = self.driver.find_element_by_id(self.username_textbox_id)
        uName.clear()
        uName.send_keys(username)
    def enterPassword(self,password):
        pwd = self.driver.find_element_by_id(self.password_textbox_id)
        pwd.clear()
        pwd.send_keys(password)
    def clickLoginButton(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
    def clickLogoutButton(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()