import pytest
from selenium import webdriver
from openpyxl import Workbook
from openpyxl.styles import Alignment
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL,USERNAME, PASSWORD, LOGIN_URL, login,navigate_to_settings,click_save_btn,Driver_path,click_addnew_btn
from user_helper import click_user_tab, enter_first_name, enter_last_name, \
    enter_email, upload_image, enter_password, enter_confirm_password
#This Test is to check if the required fields are not entered, email is not valid
# password & confirm password do not match then on clicking save does it show error messages on the screen
class Add_User:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.results = {}

    def login(self):
        try:
            login(self.wait, USERNAME, PASSWORD)
            self.results["Login"] = "Passed"
        except Exception as e:
            self.results["Login"] = f"Failed: {e}"

    def navigate_to_settings(self):
        try:
            navigate_to_settings(self)
            self.results["Navigate to Settings Screen"] = "Passed"
        except Exception as e:
            self.results["Navigate to Settings Screen"] = f"Failed: {e}"
    def click_user_tab(self):
        try:
            click_user_tab(self.wait)
            self.results["User Page is opened"] = "Passed"
        except Exception as e:
            self.results["User Page  is not closed"] = f"Failed: {e}"

    def click_addnew_btn(self):
        try:
            click_addnew_btn(self.wait)
            self.results["Add New button is clicked"] = "Passed"
        except Exception as e:
            self.results["Add New button is not clicked"] = f"Failed: {e}"

    def click_save_btn(self):
        try:
            click_save_btn(self.wait)
            self.results["Save button is clicked"] = "Passed"
        except Exception as e:
            self.results["Save button is not clicked"] = f"Failed: {e}"

    def enter_first_name(self, value):
        try:
            enter_first_name(self.wait, value)
            self.results["first_name is added in the text_field area"] = "Passed"
        except Exception as e:
            self.results["first_name has not been added"] = f"Failed: {e}"

    def enter_last_name(self, value):
        try:
            enter_last_name(self.wait, value)
            self.results["last_name is added in the text_field area"] = "Passed"
        except Exception as e:
            self.results["last_name has not been added"] = f"Failed: {e}"

    def enter_email(self, value):
        try:
            enter_email(self.wait, value)
            self.results["email is added in the text_field area"] = "Passed"
        except Exception as e:
            self.results["email has not been added"] = f"Failed: {e}"

    def upload_image(self):
        try:
            upload_image(self.wait)
            self.results["Image is uploaded"] = "Passed"
        except Exception as e:
            self.results["Image is not uploaded"] = f"Failed: {e}"

    def enter_password(self, value):
        try:
            enter_password(self.wait, value)
            self.results["password is added in the text_field area"] = "Passed"
        except Exception as e:
            self.results["password has not been added"] = f"Failed: {e}"
    def enter_confirm_password(self, value):
        try:
            enter_confirm_password(self.wait, value)
            self.results["confirm_password is added in the text_field area"] = "Passed"
        except Exception as e:
            self.results["confirm_password has not been added"] = f"Failed: {e}"

class TestSettingPage:
    @pytest.fixture(scope='class')
    def setup(self):
        chrome_driver_path = Driver_path
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        login_wait = WebDriverWait(driver, 10)
        login(login_wait,USERNAME, PASSWORD)
        driver.get(Base_URL)
        yield driver
        driver.quit()

    def test_user_functions(self, setup):
        driver = setup
        add = Add_User(driver)
        add.click_user_tab()
        add.click_addnew_btn()
        add.enter_email("ola1/123 xyz@gmailcom")
        add.enter_password("1212")
        add.enter_confirm_password("121212")
        add.click_save_btn()






