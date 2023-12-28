import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    '''
            elm = driver.execute_script("return document.getElementsByTagName('a')[4]")
            driver.execute_script("arguments[0].click()", elm)

    '''
    # locators
    link_Customer_main_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]"
    # document.getElementsByTagName('a')[24]
    link_Customer_menu_item_xpath = "//a[@href='/Admin/Customer/List']"
    # document.getElementsByTagName('a')[25]

    btn_AddNew_xpath = "//a[@class='btn btn-primary']"
    txt_email_xpath = "//input[@id='Email']"
    txt_pass_xpath = "//input[@id='Password']"
    txt_firstName_xpath = "//input[@id='FirstName']"
    txt_lastName_xpath = "//input[@id='LastName']"
    rdo_Femail_id = "Gender_Male"
    rdo_mail_id = "Gender_Female"
    txt_DOB_xpath = "//input[@id='DateOfBirth']"
    txt_companyName_xpath = "//input[@id='Company']"
    select_txt_extampt_xpath = "//input[@id='IsTaxExempt']"
    txt_customer_role_xpath = "//div[@class='input-group-append input-group-required']"
    list_customerRole_adm_xpath = "//li[contains(text(), 'Administrators')]"
    list_customerRole_reg_xpath = "//li[contains(text(), 'Registered')]"
    list_customerRole_guest_xpath = "//li[contains(text(), 'Guests')]"
    list_customerRole_vendor_xpath = "//li[contains(text(), 'Vendors')]"
    drpdwn_mng_vendor_xpath = "//select[@id='VendorId']"
    select_Active_xpath = "//input[@id='Active']"
    input_admin_cmt_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    # Driver initialization
    def __init__(self, driver):
        self.driver = driver

    def clicCustomerMainManu(self):

        self.driver.find_element(By.XPATH, self.link_Customer_main_menu_xpath).click()

    def clickCustomerManu(self):
        self.driver.find_element(By.XPATH, self.link_Customer_menu_item_xpath).click()

    def clickAddNewButton(self):
        self.driver.find_element(By.XPATH, self.btn_AddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_pass_xpath).send_keys(password)

    def setFirstName(self, fName):
        self.driver.find_element(By.XPATH, self.txt_firstName_xpath).send_keys(fName)

    def setLastName(self, lName):
        self.driver.find_element(By.XPATH, self.txt_lastName_xpath).send_keys(lName)

    def setCustomersRole(self, role):
        self.driver.find_element(By.XPATH, self.txt_customer_role_xpath).click()
        time.sleep(5)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRole_reg_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRole_adm_xpath)
        elif role == "Guests":
            # Here user can be registered or Guest, Either one
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            time.sleep(5)
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRole_guest_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRole_reg_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRole_vendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRole_guest_xpath)
            time.sleep(3)
        self.driver.execute_script("arguments[0].click()", self.listitem)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdo_mail_id).click()
        elif gender == "Femail":
            self.driver.find_element(By.ID, self.rdo_Femail_id).click()
        else:
            self.driver.find_element(By.ID, self.rdo_mail_id).click()

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpdwn_mng_vendor_xpath))
        drp.select_by_visible_text(value)

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txt_DOB_xpath).send_keys(dob)

    def setCompanyName(self, companyName):
        self.driver.find_element(By.XPATH, self.txt_companyName_xpath).send_keys(companyName)

    def adminComments(self, comments):
        self.driver.find_element(By.XPATH, self.input_admin_cmt_xpath).send_keys(comments)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def checkOnTax(self):
        self.driver.find_element(By.XPATH, self.select_txt_extampt_xpath).click()

    def checkOnActive(self):
        self.driver.find_element(By.XPATH, self.select_Active_xpath).click()