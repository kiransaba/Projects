import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,click_watch_btn,click_guide_btn,click_close_btn,navigate_to_settings,click_save_btn,Driver_path,\
    click_tab_back,write_to_excel
from user_group_helper import click_user_group_tab,click_checkbox_btn,click_delete_btn,click_addnew_btn,click_edit_btn,click_cancel_btn
class User_Page_Group:
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
 def click_user_group_tab(self):
     try:
         click_user_group_tab(self.wait)
         self.results["User Group  Page is opened"] = "Passed"
     except Exception as e:
         self.results["User Group Tab is not clicked"] = f"Failed: {e}"

 def click_watch_btn(self):
     try:
         click_watch_btn(self.wait)
         self.results["User Group  Page is opened"] = "Passed"
     except Exception as e:
         self.results["User Group Tab is not clicked"] = f"Failed: {e}"

 def click_guide_btn(self):
     try:
         click_guide_btn(self.wait)
         self.results["Store Setting guide button is clicked"] = "Passed"
     except Exception as e:
         self.results["Store Setting guide button is not clicked"] = f"Failed: {e}"

 def click_close_btn(self):
     try:
         click_close_btn(self.wait)
         self.results["Watch Video button is clicked"] = "Passed"
     except Exception as e:
         self.results["Watch Video button is not clicked"] = f"Failed: {e}"

 def click_cancel_btn(self):
     try:
         click_cancel_btn(self.wait)
         self.results["Cancel button is clicked"] = "Passed"
     except Exception as e:
         self.results["Cancel button is not clicked"] = f"Failed: {e}"

 def click_checkbox_btn(self):
     try:
         click_checkbox_btn(self.wait)
         self.results["Checkbox button is clicked"] = "Passed"
     except Exception as e:
         self.results["Checkbox button is not clicked"] = f"Failed: {e}"

 def click_delete_btn(self):
     try:
         click_delete_btn(self.wait)
         self.results["Add New button is clicked"] = "Passed"
     except Exception as e:
         self.results["Add New button is not clicked"] = f"Failed: {e}"

 def click_addnew_btn(self):
     try:
         click_addnew_btn(self.wait)
         self.results["Add New button is clicked"] = "Passed"
     except Exception as e:
         self.results["Add New button is not clicked"] = f"Failed: {e}"

 def click_edit_btn(self):
     try:
         click_edit_btn(self.wait)
         self.results["Edit button is clicked"] = "Passed"
     except Exception as e:
         self.results["Edit button is not clicked"] = f"Failed: {e}"

 def click_tab_back(self):
     try:
         click_tab_back(self.wait)
         self.results["Tab(back) button is clicked"] = "Passed"
     except Exception as e:
         self.results["Tab(back) button is not clicked"] = f"Failed: {e}"

 def click_save_btn(self):
     try:
         click_save_btn(self.wait)
         self.results["Save button is clicked"] = "Passed"
     except Exception as e:
         self.results["Save button is not clicked"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="user_group_tab_result.xlsx"):
         write_to_excel(self.results, folder_name, file_name)

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
        user_group1= User_Page_Group(driver)
        user_group1.click_watch_btn()
        user_group1.write_to_excel()
        user_group1.click_close_btn()
        user_group1.write_to_excel()
        user_group1.click_user_group_tab()
        user_group1.write_to_excel()
        user_group1.click_addnew_btn()
        user_group1.write_to_excel()
        user_group1.click_tab_back()
        user_group1.write_to_excel()
        user_group1.click_addnew_btn()
        user_group1.write_to_excel()
        user_group1.click_cancel_btn()
        user_group1.write_to_excel()
        user_group1.click_edit_btn()
        user_group1.write_to_excel()
        user_group1.click_tab_back()
        user_group1.write_to_excel()
        user_group1.click_edit_btn()
        user_group1.write_to_excel()
        user_group1.click_cancel_btn()
        user_group1.write_to_excel()
        user_group1.click_checkbox_btn()
        user_group1.write_to_excel()
        #user_group1.click_delete_btn()    #uncomment it if you want to delete
        #user_group1.write_to_excel()



