import time
from lib2to3.pgen2 import driver
from lib2to3.pgen2.driver import Driver

import pytest
import pytest

import softest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import DBConfigurations.Config_file

from selenium import webdriver

from PageObjects.Home_Page import HomePage
from PageObjects.LoginPage import LoginPage
from Utility.BaseClass import BaseClass2



class Test_database(BaseClass2, softest.TestCase):
    Excel_report =DBConfigurations.Config_file.Excel_Report_File
    Excel_sheet_name = DBConfigurations.Config_file.Sheet_Name


    def test_PowerBI(self):
        log = self.getLogger()

        loginpage = LoginPage(self.driver)
        self.driver.implicitly_wait(30)

        homepage = HomePage(self.driver)
        self.driver.implicitly_wait(30)

        #DBdata = self.dbconncetions()

        self.driver.implicitly_wait(30)
        log.info("Entering Email")
        loginpage.Enter_mail().send_keys(DBConfigurations.Config_file.PowerBi_UserName)

        self.driver.implicitly_wait(30)
        log.info("clicking on submit")
        loginpage.Enter_submit().click()

        # time.sleep(5)
        self.driver.implicitly_wait(30)
        log.info("Entering Password")
        loginpage.password().send_keys(DBConfigurations.Config_file.PowerBi_Password)

        self.driver.implicitly_wait(30)
        log.info("clicking on Signin Button")
        loginpage.MS_SigninConfButton().click()

        self.driver.implicitly_wait(30)
        log.info("clicking on stay Signin Button")




        if loginpage.staysigninpage().is_displayed():
            loginpage.staysigninpage().click()
        print(homepage.Title().text)
        assert homepage.Title().text == "Student's Performance "

        log.info("click on the dropdownn button for Institute")
        homepage.Institue().click()
        log.info("checking for the slicer for institue")
        slicer_item = homepage.slicier1()
        # Find the checkbox element within the slicer item
        checkbox = slicer_item.find_element(By.XPATH, ".//span[contains(@class, 'checkboxOutlineContrast')]")

        # Check if the checkbox is selected
        if checkbox.get_attribute("class").endswith("selected"):
            print("check box already selected")
            pass
        else:
            # If the checkbox is not selected, click on it
            print("checkbox was not selected")
            checkbox.click()

        # image is displayed or not
        log.info("checking for the Image present")
        if homepage.imageBag1().is_displayed():
            print("Image is displayed.")
        else:
            print("Image is not displayed.")

        #image is dispalyed or not

        log.info("checking for the Image present")
        if homepage.imageBag2().is_displayed():
            print("Image is displayed.")
        else:
            print("Image is not displayed.")

        #print number fro dashboard

        print(homepage.number1().text)

        #print student  from dashboard

        print(homepage.student1().text)

        #print image from dashboard

        log.info("checking for the Image present")
        if homepage.kulkarni1().is_displayed():
            print("Image is displayed.")
        else:
            print("Image is not displayed.")

        #click on next page link from dashboard
        log.info("clicking on follow link")
        homepage.nextPage1().click()

        #add new line














