import random
import string
import time
from secrets import randbelow

import pytest

from pageObjects.LoginPage import Login_Functionalities as LP
from pageObjects.AddCustomerPage import AddCustomer as AC
from pageObjects.Search_Customer_by_Name import SearchCustomer as SC
from utilities.readProperties import ReadProperties
from utilities.customLogger import LogGenerations
from selenium.webdriver.common.by import By


class Test_005_Search_Customer_By_Name:
    baseURL = ReadProperties.getURL()
    username = ReadProperties.getUsername()
    password = ReadProperties.getPassword()
    save_picture = "C:\\Users\\zaman\\PycharmProjects\\PythonSelenium\\Screenshots\\"
    rand = str(randbelow(55))
    logger = LogGenerations.logGen()

    @pytest.mark.regression
    def test_search_customerByName(self, setup):
        self.logger.info("***************** Test_005_Search_Customer_By_Name ******************\n")
        self.logger.info("***************** Start Login with Valid Credentials **********************")
        driver = setup
        loginPage = LP(driver)
        driver.get(self.baseURL)
        loginPage.setUsername(self.username)
        loginPage.setPassword(self.password)
        loginPage.clickLogin()
        self.logger.info("**************** Login Successful *******************")
        self.logger.info("******* Start processing to searching a existing customer ***********")

        # Object of required classes
        addCus = AC(driver)
        srCus = SC(driver)

        # Moving to search pages
        self.logger.info("******* Moving to the search page ***********")
        addCus.clicCustomerMainManu()
        time.sleep(3)
        addCus.clickCustomerManu()
        time.sleep(3)
        # srCus.clickOnSearchIcon()
        time.sleep(5)

        # Start search in process
        self.logger.info("******* Start searching processes with Name ***********")
        srCus.setFirstName("Victoria")
        srCus.setLastName("Terces")
        srCus.clickSearchButton()
        time.sleep(5)
        status = srCus.searchCustomerByName("Victoria Terces")
        driver.save_screenshot(self.save_picture + "SearchCustomerByName_" + self.rand + ".png")
        assert True == status
        self.logger.info("***************** Test_005_Search_Customer_By_Name is completed ******************")
        driver.close()
