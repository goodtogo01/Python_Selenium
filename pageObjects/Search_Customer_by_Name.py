import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SearchCustomer:
    # Locators from search functionalities

    icon_search_xpath = "//div[@class='icon-search']"
    txt_FirstName_id = "SearchFirstName"
    txt_LastName_id = "SearchLastName"
    btn_Search_id = "search-customers"

    table_xpath = "//*[@id='customers-grid']"
    table_Row_xpath = "//*[@id='customers-grid']//tbody/tr"
    table_Col_xpath = "//*[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSearchIcon(self):
        self.driver.find_element(By.XPATH, self.icon_search_xpath).click()

    def setFirstName(self, fName):
        self.driver.find_element(By.ID, self.txt_FirstName_id).clear()
        self.driver.find_element(By.ID, self.txt_FirstName_id).send_keys(fName)

    def setLastName(self, lName):
        self.driver.find_element(By.ID, self.txt_LastName_id).clear()
        self.driver.find_element(By.ID, self.txt_LastName_id).send_keys(lName)

    def clickSearchButton(self):
        self.driver.find_element(By.ID, self.btn_Search_id).click()

    def getNumberOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Row_xpath))

    def getNumberOfCol(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Col_xpath))

    def searchCustomerByName(self, name):
        passed = False
        for rows in range(1, self.getNumberOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            customerName = table.find_element(By.XPATH,
                                              "//*[@id='customers-grid']/tbody/tr[" + str(rows) + "]/td[3]").text
            if customerName == name:
                passed = True
                break
        return passed
