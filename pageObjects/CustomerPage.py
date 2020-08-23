from selenium.webdriver.support.select import Select

class AddCustomer:
    customers_MainLink_xpath ="//a[@href='#']//span[text()='Customers']"
    customersMenuItem_xpath="//span[@class='menu-item-title'][text()='Customers']"
    AddNewCustomer_Button_xpath="//a[@class='btn bg-blue']"
    emailTextBox_id="Email"
    passwordTextBox_id = "Password"
    firstNameTextBox_id ='FirstName'
    lastNameTextBox_id ='LastName'
    genderFemaleRadio_id='Gender_Female'
    genderMaleRadio_id = 'Gender_Male'
    dateOfBirthTextbox_id='DateOfBirth'
    companyNameTextBox_id='Company'
    taxExemptCheckbox_id ='IsTaxExempt'
    # NewsLetter_multiselect_xpath
    multiselectList_xpath="//div[@class='k-multiselect-wrap k-floatwrap']"
    listItemStoreName_xpath = "//li[text()='Your store name']"
    listItemStoreName2_xpath = "//li[text()='Test store 2']"
    # customerRoles_multiselect_xpath = "//div[@class='k-multiselect-wrap k-floatwrap'][2]"
    listItemAdministrator_xpath="//li[text()='Administrators']"
    listItemForumModerators_xpath = "//li[text()='Forum Moderators']"
    listItemGuests_xpath = "//li[text()='Guests']"
    listItemRegistered_xpath = "//li[text()='Registered']"
    listItemVendors_xpath = "//li[text()='Vendors']"
    vendorDropdown_id="VendorId"
    AdminCommentTextbox_id="AdminComment"
    saveButton_name='save'
    activeCheckbox_id ="Active"

    def __init__(self,driver):
        self.driver= driver
    def clickOnCustomerLink(self):
        self.driver.find_element_by_xpath(self.customers_MainLink_xpath).click()
    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.customersMenuItem_xpath).click()
    def clickAddNewCustomer(self):
        self.driver.find_element_by_xpath(self.AddNewCustomer_Button_xpath).click()

    def enterEmail(self,email):
        self.driver.find_element_by_id(self.emailTextBox_id).send_keys(email)
    def enterPassword(self,password):
        self.driver.find_element_by_id(self.passwordTextBox_id).send_keys(password)
    def enterFirstName(self,firstname):
        self.driver.find_element_by_id(self.firstNameTextBox_id).send_keys(firstname)
    def enterLastName(self,lastname):
        self.driver.find_element_by_id(self.lastNameTextBox_id).send_keys(lastname)
    def selectGender(self,gender):
        if gender=="female":
            self.driver.find_element_by_id(self.genderFemaleRadio_id).click()
        else:
            self.driver.find_element_by_id(self.genderMaleRadio_id).click()

    def enterDob(self,dob):
        self.driver.find_element_by_id(self.dateOfBirthTextbox_id).send_keys(dob)

    def enterCompanyName(self,companyName):
        self.driver.find_element_by_id(self.companyNameTextBox_id).send_keys(companyName)

    def isTaxExempt(self,yesORno):
        if yesORno=="yes":
            self.driver.find_element_by_id(self.taxExemptCheckbox_id).click()
        else:
            pass

    def enterAdminComments(self,comments):
        self.driver.find_element_by_id(self.AdminCommentTextbox_id).send_keys(comments)

    def clickSaveButton(self):
        self.driver.find_element_by_name(self.saveButton_name).click()

    def selectVendorID(self,vendorID):
        selectVendor = Select(self.driver.find_element_by_id(self.vendorDropdown_id))
        selectVendor.select_by_visible_text(vendorID)

    def selectNewsLetterRoles(self,storeName):
        l1= self.driver.find_elements_by_xpath(self.multiselectList_xpath)
        l1[0].click()
        if storeName=="Your store name":
            self.driver.find_element_by_xpath(self.listItemStoreName_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.listItemStoreName2_xpath).click()

    def selectCustomerRoles(self, role):
        l1 = self.driver.find_elements_by_xpath(self.multiselectList_xpath)
        l1[1].click()
        if role == "Administrators":
            self.listItem = self.driver.find_element_by_xpath(self.listItemAdministrator_xpath)
        elif role == "Forum Moderators":
            self.listItem =self.driver.find_element_by_xpath(self.listItemForumModerators_xpath)
        elif role == "Vendors":
            self.listItem =self.driver.find_element_by_xpath(self.listItemVendors_xpath)
        elif role == "Guests":
            status = self.driver.find_element_by_xpath(self.listItemRegistered_xpath).is_displayed()
            print(status)
            if status:
                self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            else:
                pass
            self.listItem =self.driver.find_element_by_xpath(self.listItemGuests_xpath)
        elif role == "Registered":
            status = self.driver.find_element_by_xpath(self.listItemGuests_xpath).is_displayed()
            if status:
                self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            else:
                pass
            self.listItem =self.driver.find_element_by_xpath(self.listItemRegistered_xpath)
        else:
            self.listItem =self.driver.find_element_by_xpath(self.listItemGuests_xpath)
        self.driver.execute_script("arguments[0].click();",self.listItem)
    def checkActiveCheckbox(self,bool):
        if bool:
            self.driver.find_element_by_id(self.activeCheckbox_id).click()
        else:
            pass
