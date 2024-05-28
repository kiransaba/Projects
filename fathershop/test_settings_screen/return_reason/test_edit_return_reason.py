import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from return_helper import click_return_reason_tab,click_edit_btn,edit_return_reason_name,edit_return_reason_name1
class Edit_Return_Reason:
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
         self.results["Return Statuses Page is opened"] = "Passed"
     except Exception as e:
         self.results["Return Statuses Tab is not clicked"] = f"Failed: {e}"

 def click_edit_bth(self):
     try:
         click_edit_btn(self.wait)
         self.results["Edit New button is clicked"] = "Passed"
     except Exception as e:
         self.results["Edit New button is not clicked"] = f"Failed: {e}"

 def click_save_btn(self):
     try:
         click_save_btn(self.wait)
         self.results["Save button is clicked"] = "Passed"
     except Exception as e:
         self.results["Save button is not clicked"] = f"Failed: {e}"

 def edit_return_reason_name(self, value):
     try:
         edit_return_reason_name(self.wait, value)
         self.results["Return Status name is edited in the English language"] = "Passed"
     except Exception as e:
         self.results["Return Status name is not edited in the English language"] = f"Failed: {e}"
 def edit_return_reason_name1(self, value):
     try:
         edit_return_reason_name1(self.wait, value)
         self.results["Return Status name is edited in the Arabic language"] = "Passed"
     except Exception as e:
         self.results["Return Status name is not edited in the Arabic language"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="edit_return_reason_result.xlsx"):
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
         login(login_wait,USERNAME, PASSWORD)
         # Change URL to Base_URL after logging in
         driver.get(Base_URL)
         yield driver
         driver.quit()
     def test_user_functions(self, setup):
         driver = setup
         edit_reason = Edit_Return_Reason(driver)
         #edit_reason.login()                         #commented part is required in near future
         #edit_reason.write_to_excel()
         #edit_reason.navigate_to_settings()
         #edit_reason.write_to_excel()
         edit_reason.click_return_reason_tab()
         edit_reason.write_to_excel()
         edit_reason.click_edit_bth()
         edit_reason.write_to_excel()
         edit_reason.edit_return_reason_name("Orderdone1212")
         edit_reason.write_to_excel()
         edit_reason.edit_return_reason_name1("Orderdone1212")
         edit_reason.write_to_excel()
         edit_reason.click_save_btn()
         edit_reason.write_to_excel()
