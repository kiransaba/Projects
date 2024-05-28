import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_cancel_btn,\
click_addnew_btn
from return_status_helper import click_return_statuses_tab,enter_return_status_name,enter_return_status_name1
class Add_Return_Status:
 def __init__(self, driver):
  self.driver = driver
  self.wait = WebDriverWait(self.driver, 10)
  self.results = {}
 def login(self):
    try:
      login(self.wait,USERNAME, PASSWORD)
      self.results["Login"] = "Passed"
    except Exception as e:
      self.results["Login"] = f"Failed: {e}"

 def navigate_to_settings(self):
      try:
        navigate_to_settings(self)
        self.results["Navigate to Settings Screen"] = "Passed"
      except Exception as e:
        self.results["Navigate to Settings Screen"] = f"Failed: {e}"
 def click_return_statuses_tab(self):
     try:
         click_return_statuses_tab(self.wait)
         self.results["Return Statuses Page is opened"] = "Passed"
     except Exception as e:
         self.results["Return Statuses Tab is not clicked"] = f"Failed: {e}"

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

 def enter_return_status_name(self,value):
    try:
        enter_return_status_name(self.wait,value)
        self.results["Return Status name is added in the English language"] = "Passed"
    except Exception as e:
         self.results["Return Status name is not added in the English language"] = f"Failed: {e}"

 def enter_return_status_name1(self, value):
     try:
         enter_return_status_name1(self.wait, value)
         self.results["Return Status name is added in the Arabic language"] = "Passed"
     except Exception as e:
         self.results["Return Status name is not added in the Arabic language"] = f"Failed: {e}"

class TestSettingPage:
    @pytest.fixture(scope='class')
    def setup(self):
        chrome_driver_path = Driver_path
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        login_wait = WebDriverWait(driver, 10)
        login(login_wait, USERNAME, PASSWORD)
        driver.get(Base_URL)
        yield driver
        driver.quit()
    def test_user_functions(self, setup):
        driver = setup
        add_status= Add_Return_Status(driver)
        #add_status.login()                                  #Commented part is required in the near future
        #add_status.write_to_excel()
        #add_status.navigate_to_settings()
        #add_status.write_to_excel()
        add_status.click_return_statuses_tab()
        add_status.click_addnew_btn()
        add_status.click_save_btn()







