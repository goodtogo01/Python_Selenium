import time
from secrets import randbelow
import pytest

from pageObjects.LoginPage import Login_Functionalities as LP
from utilities.readProperties import ReadProperties
from utilities.customLogger import LogGenerations


class Test_001_Login:
    baseURL = ReadProperties.getURL()
    username = ReadProperties.getUsername()
    password = ReadProperties.getPassword()
    save_pic = "C:\\Users\zaman\\PycharmProjects\\PythonSelenium\\Screenshoot\\"
    rand = str(randbelow(50))
    logger = LogGenerations.logGen()

    @pytest.mark.sanity
    def test_Homepage_Title(self, setup):
        self.logger.info("***************** Test_001_Start_Execution **********************")
        driver = setup
        driver.get(self.baseURL)
        # self.logger.info("***************** Varify Home Page Title **********************")
        actual_Title = driver.title
        if actual_Title == "Your store. Login":
            assert True
            self.logger.info("***************** Page Title verification is Passed **********************")
            print("The Title is Expected as : ", actual_Title)

        else:
            print("The Title is not Expected as : ", driver.title)
            self.logger.error("***************** Page Title is Failed **********************")
            assert False

        driver.close()

    @pytest.mark.regression
    def test_login_with_valid_credentials(self, setup):
        self.logger.info("***************** Start Login with Valid Credentials **********************")
        self.logger.info("***************** Varify Login Page Title **********************")
        driver = setup
        loginPage = LP(driver)
        driver.get(self.baseURL)
        loginPage.setUsername(self.username)
        time.sleep(5)
        loginPage.setPassword(self.password)
        time.sleep(5)
        loginPage.clickLogin()
        actual_Title = driver.title
        if actual_Title == "Dashboard / nopCommerce administration":
            print("The Title is Expected as : ", actual_Title)
            self.logger.info("***************** Login with valid credentials is Passed **********************")
            driver.save_screenshot(self.save_pic+"test_Passed_"+self.rand+".png")
            assert True
        else:
            driver.save_screenshot(self.save_pic+"test_Failed_"+self.rand+".png")
            print("The Title is not Expected as : ", driver.title)
            self.logger.info("***************** Page Title verification is Failed **********************")
            assert False
        driver.close()


