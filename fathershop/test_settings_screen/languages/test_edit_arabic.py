import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from language_helper import click_store_language_tab,click_edit_english,click_edit_arabic,status_dropdown,hover_help_icon,enter_sort_order

class Edit_Language:
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
 def click_store_language_tab(self):
     try:
         click_store_language_tab(self.wait)
         self.results["Store Language screen is opened"] = "Passed"
     except Exception as e:
         self.results["Store Language Tab is not clicked"] = f"Failed: {e}"
 def click_edit_arabic(self):
     try:
         click_edit_arabic(self.wait)
         self.results["Arabic Language Edit button is clicked"] = "Passed"
     except Exception as e:
         self.results["Arabic  Language Edit button is not clicked"] = f"Failed: {e}"

 def status_dropdown(self,status_value):
     try:
         status_dropdown(self.wait, status_value)
         self.results["Status dropdown menu is opened and status is selected"] = "Passed"
     except Exception as e:
         self.results["Status dropdown menu is not opened and status  not selected"] = f"Failed: {e}"
 def hover_help_icon(self):
     try:
         hover_help_icon(self)
         self.results["Hovering over status question mark icon"] = "Passed"
     except Exception as e:
         self.results["Hovering over status question mark icon is not successful"] = f"Failed: {e}"

 def click_save_btn(self):
     try:
         click_save_btn(self.wait)
         self.results["Save Return Action button is clicked"] = "Passed"
     except Exception as e:
         self.results["Save Return Action button is not clicked"] = f"Failed: {e}"
 def enter_sort_order(self, value):
     try:
         enter_sort_order(self.wait, value)
         self.results["Sort Order value is added"] = "Passed"
     except Exception as e:
         self.results["Sort order value is not added"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="edit_language_result.xlsx"):
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
         edit_language = Edit_Language(driver)
         #edit_language.login()
         #edit_language.write_to_excel()
         #edit_language.navigate_to_settings()
         #edit_language.write_to_excel()
         edit_language.click_store_language_tab()
         edit_language.click_edit_arabic()
         edit_language.write_to_excel()
         edit_language.status_dropdown("Disabled")
         edit_language.write_to_excel()
         edit_language.enter_sort_order("2")
         edit_language.write_to_excel()
         edit_language.hover_help_icon()
         edit_language.write_to_excel()
         edit_language.click_save_btn()
         edit_language.write_to_excel()

