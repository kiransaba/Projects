import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,click_cancel_btn,\
click_addnew_btn
from return_helper import click_return_reason_tab,enter_return_reason_name,enter_return_reason_name1
class Add_Return_Reason:
 def __init__(self, driver):
  self.driver = driver
  self.wait = WebDriverWait(self.driver, 10)
  self.results = {}

## Screen Login
 def login(self):
    try:
      login(self.wait, USERNAME, PASSWORD)
      self.results["Login"] = "Passed"
    except Exception as e:
      self.results["Login"] = f"Failed: {e}"

##Clicking Setting button
 def navigate_to_settings(self):
      try:
        navigate_to_settings(self)
        self.results["Navigate to Settings Screen"] = "Passed"
      except Exception as e:
        self.results["Navigate to Settings Screen"] = f"Failed: {e}"
 def click_return_reason_tab(self):
     try:
         click_return_reason_tab(self.wait)
         self.results["Return Reason Page is opened"] = "Passed"
     except Exception as e:
         self.results["Return Reason Tab is not clicked"] = f"Failed: {e}"

 def click_addnew_btn(self):
     try:
         click_addnew_btn(self.wait)
         self.results["Add New button is clicked"] = "Passed"
     except Exception as e:
         self.results["Add New button is not clicked"] = f"Failed: {e}"

 def click_cancel_btn(self):
     try:
         click_cancel_btn(self.wait)
         self.results["Cancel button is clicked"] = "Passed"
     except Exception as e:
         self.results["Cancel button is not clicked"] = f"Failed: {e}"

 def click_save_btn(self):
     try:
         click_save_btn(self.wait)
         self.results["Save button is clicked"] = "Passed"
     except Exception as e:
         self.results["Save button is not clicked"] = f"Failed: {e}"

 def enter_return_reason_name(self,value):
    try:
        enter_return_reason_name(self.wait,value)
        self.results["Return Reason name is added in the English language"] = "Passed"
    except Exception as e:
         self.results["Return Reason name is not added in the English language"] = f"Failed: {e}"

 def enter_return_reason_name1(self, value):
     try:
         enter_return_reason_name1(self.wait, value)
         self.results["Return Reason name is added in the Arabic language"] = "Passed"
     except Exception as e:
         self.results["Return Reason name is not added in the Arabic language"] = f"Failed: {e}"


class TestSettingPage:
    @pytest.fixture(scope='class')
    def setup(self):
        chrome_driver_path = Driver_path
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        # Logging in
        login_wait = WebDriverWait(driver, 10)
        login(login_wait, USERNAME, PASSWORD)
        # Change URL to Base_URL after logging in
        driver.get(Base_URL)
        yield driver
        driver.quit()

    def test_user_functions(self, setup):
        driver = setup
        add_reason= Add_Return_Reason(driver)
        #add_reason.login()                                   #commented part is required in near future
        #add_reason.write_to_excel()
        #add_reason.navigate_to_settings()
        #aadd_reason.write_to_excel()
## not recodring the results in the excel, it is just to check error messages on the screen
        add_reason.click_return_reason_tab()
        add_reason.click_addnew_btn()
        add_reason.click_save_btn()







