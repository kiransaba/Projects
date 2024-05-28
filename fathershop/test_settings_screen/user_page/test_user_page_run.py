import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL,USERNAME, PASSWORD, LOGIN_URL,login,click_guide_btn,click_close_btn,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_delete_btn,\
    click_tab_back,click_watch_btn,click_addnew_btn,click_cancel_btn
from user_helper import click_user_tab,click_checkbox_btn,click_edit_btn
class User_Page:
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
 def click_user_tab(self):
     try:
         click_user_tab(self.wait)
         self.results["User Page is opened"] = "Passed"
     except Exception as e:
         self.results["User Page  is not closed"] = f"Failed: {e}"

 def click_watch_btn(self):
     try:
         click_watch_btn(self.wait)
         self.results["User Screen:Watch Video button is clicked"] = "Passed"
     except Exception as e:
         self.results["User Screen:Watch Video button is not clicked"] = f"Failed: {e}"
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
         self.results["User(back) button is clicked"] = "Passed"
     except Exception as e:
         self.results["User(back) button is not clicked"] = f"Failed: {e}"

 def click_save_btn(self):
     try:
         click_save_btn(self.wait)
         self.results["Save button is clicked"] = "Passed"
     except Exception as e:
         self.results["Save button is not clicked"] = f"Failed: {e}"

 def click_cancel_btn(self):
     try:
         click_cancel_btn(self.wait)
         self.results["Cancel button is clicked"] = "Passed"
     except Exception as e:
         self.results["Cancel is not clicked"] = f"Failed: {e}"

 def write_to_excel(self):
     write_to_excel(self.results, "excel_user_results","user_screen_results")


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
        user= User_Page(driver)
        #user.login()                               #Commented part is required in future
        #user.write_to_excel()
        #user.navigate_to_settings()
        #user.write_to_excel()
        user.click_watch_btn()
        user.write_to_excel()
        user.click_guide_btn()
        user.write_to_excel()
        user.click_close_btn()
        user.write_to_excel()
        user.click_user_tab()
        user.write_to_excel()
        user.click_addnew_btn()
        user.write_to_excel()
        user.click_tab_back()
        user.write_to_excel()
        user.click_addnew_btn()
        user.write_to_excel()
        user.click_cancel_btn()
        user.write_to_excel()
        user.click_edit_btn()
        user.write_to_excel()
        user.click_tab_back()
        user.write_to_excel()
        user.click_edit_btn()
        user.write_to_excel()
        user.click_cancel_btn()
        user.write_to_excel()
        user.click_checkbox_btn()
        user.write_to_excel()
        user.click_delete_btn()
        user.write_to_excel()



