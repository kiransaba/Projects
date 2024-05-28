import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from user_helper import click_user_tab,click_edit_btn, edit_first_name,edit_last_name,edit_email,edit_password,edit_confirm_password,edit_image,\
    edit_user_group,edit_status
class Edit_User:
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
 def edit_first_name(self,value1):
    try:
        edit_first_name(self.wait,value1)
        self.results["first_name is edited"] = "Passed"
    except Exception as e:
         self.results["first_name is not edited"] = f"Failed: {e}"
 def edit_last_name(self,value2):
    try:
        edit_last_name(self.wait,value2)
        self.results["last_name is edited"] = "Passed"
    except Exception as e:
         self.results["last_name not edited"] = f"Failed: {e}"
 def edit_email(self,value3):
    try:
        edit_email(self.wait,value3)
        self.results["email is edited "] = "Passed"
    except Exception as e:
         self.results["email is not edited"] = f"Failed: {e}"

 def edit_password(self,value4):
    try:
        edit_password(self.wait,value4)
        self.results["password is edited "] = "Passed"
    except Exception as e:
         self.results["password is not edited"] = f"Failed: {e}"

 def edit_confirm_password(self,value5):
    try:
        edit_confirm_password(self.wait,value5)
        self.results["confirm password is edited "] = "Passed"
    except Exception as e:
         self.results["confirm password is not edited"] = f"Failed: {e}"
 def edit_image(self):
     try:
         edit_image(self.wait)
         self.results["Image is edited"] = "Passed"
     except Exception as e:
         self.results["Image is not edited"] = f"Failed: {e}"
 def edit_user_group(self,option_value):
     try:
         edit_user_group(self.wait, option_value)
         self.results["User Group dropdown menu is opened and User Group is edited"] = "Passed"
     except Exception as e:
         self.results["User Group dropdown menu is not opened and User Group is not edited"] = f"Failed: {e}"
 def  edit_status(self,status_value):
     try:
         edit_status(self.wait, status_value)
         self.results["Status dropdown menu is opened and status is edited"] = "Passed"
     except Exception as e:
         self.results["Status dropdown menu is not opened and status  not edited"] = f"Failed: {e}"

 def write_to_excel(self):
     write_to_excel(self.results," excel_user_results", "edit_user_results.xlsx")


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
        edit= Edit_User(driver)
        #edit.login()
        #edit.write_to_excel()                ##Commented part is required in future
        #edit.navigate_to_settings()
        #edit.write_to_excel()
        edit.click_user_tab()
        edit.write_to_excel()
        edit.click_edit_bth()
        edit.write_to_excel()
        edit.edit_user_group("Manager")
        edit.edit_first_name("Elf")
        edit.write_to_excel()
        edit.edit_last_name("Jhon")
        edit.write_to_excel()
        edit.edit_email("krnsana@gmail1.com")
        edit.write_to_excel()
        edit.edit_status("Enabled")
        edit.edit_image()
        edit.write_to_excel()
        edit.click_save_btn()
        edit.write_to_excel()






