import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_cancel_btn,\
click_addnew_btn
from return_action_helper import click_return_action_tab,enter_return_action_name,enter_return_action_name1
class Add_Return_Action:

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
 def click_return_action_tab(self):
     try:
         click_return_action_tab(self.wait)
         self.results["Return Action Page is opened"] = "Passed"
     except Exception as e:
         self.results["Return Action Tab is not clicked"] = f"Failed: {e}"

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

 def enter_return_action_name(self,value):
    try:
        enter_return_action_name(self.wait,value)
        self.results["Return Action name is added in the English language"] = "Passed"
    except Exception as e:
         self.results["Return Ation name is not added in the English language"] = f"Failed: {e}"
 def enter_return_action_name1(self, value):
     try:
         enter_return_action_name1(self.wait, value)
         self.results["Return Action name is added in the Arabic language"] = "Passed"
     except Exception as e:
         self.results["Return Action name is not added in the Arabic language"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="add_return_action_result.xlsx"):
         write_to_excel(self.results, folder_name, file_name)

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
        add_action= Add_Return_Action(driver)
        #add_status.login()                      ##commented part is required in near future
        #add_status.write_to_excel()
        #add_status.navigate_to_settings()
        #add_status.write_to_excel()
        add_action.click_return_action_tab()
        add_action.write_to_excel()
        add_action.click_addnew_btn()
        add_action.write_to_excel()
        add_action.enter_return_action_name("Test")
        add_action.write_to_excel()
        add_action.enter_return_action_name1("Test")
        add_action.write_to_excel()
        add_action.click_save_btn()
        add_action.write_to_excel()






