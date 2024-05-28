import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL,USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from user_group_helper import click_user_group_tab,click_addnew_btn,enter_user_group_name,add_access_permission,modify_permission
class Add_User_Group:
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

 def enter_user_group_name(self,value):
    try:
        enter_user_group_name(self.wait,value)
        self.results["User group name is added"] = "Passed"
    except Exception as e:
         self.results["User group name is not added"] = f"Failed: {e}"

 def add_access_permission(self,option_value):
    try:
        add_access_permission(self.wait,option_value)
        self.results["Access Permission is added"] = "Passed"
    except Exception as e:
         self.results["Access Permission is not added"] = f"Failed: {e}"

 def modify_permission(self, option_value1):
     try:
         modify_permission(self.wait, option_value1)
         self.results["Modify Permission is added"] = "Passed"
     except Exception as e:
         self.results["Modify Permission is not added"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="add_user_group_result.xlsx"):
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
        add_group= Add_User_Group(driver)
        #add_group.login()                  #Commented part is required in the future
        #add_group.write_to_excel()
        #add_group.navigate_to_settings()
        #add_group.write_to_excel()
        add_group.click_user_group_tab()
        add_group.write_to_excel()
        add_group.click_addnew_btn()
        add_group.enter_user_group_name("Test Master")    #Enter any Name
        add_group.write_to_excel()
        add_group.add_access_permission("apps/marketplace")
        add_group.write_to_excel()
        add_group.modify_permission("catalog/filter")
        add_group.write_to_excel()
        add_group.click_save_btn()
        add_group.write_to_excel()






