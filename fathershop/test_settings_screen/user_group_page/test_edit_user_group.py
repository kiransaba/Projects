import pytest

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from user_group_helper import click_user_group_tab,click_edit_btn,edit_user_group_name,edit_access_permission
class Edit_User_Group:
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
 def edit_user_group_name(self,value):
    try:
        edit_user_group_name(self.wait,value)
        self.results["first_name is edited"] = "Passed"
    except Exception as e:
         self.results["first_name is not edited"] = f"Failed: {e}"
 def edit_access_permission(self,option_value):
    try:
        edit_access_permission(self.wait,option_value)
        self.results["Access Permission is edited"] = "Passed"
    except Exception as e:
         self.results["Access Permission is not edited"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="edit_user_result.xlsx"):
         write_to_excel(self.results, folder_name, file_name)

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
        edit_group= Edit_User_Group(driver)
        #edit_group.login()                      #Commented part is required in future
        #edit_group.write_to_excel()
        #edit_group.navigate_to_settings()
        #edit_group.write_to_excel()
        edit_group.click_user_group_tab()
        edit_group.write_to_excel()
        edit_group.click_edit_bth()
        edit_group.write_to_excel()
        edit_group.edit_user_group_name("Advertister")
        edit_group.write_to_excel()
        edit_group.edit_access_permission("apps/sitemap")
        edit_group.write_to_excel()
        edit_group.click_save_btn()
        edit_group.write_to_excel()


