import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL,USERNAME, PASSWORD, LOGIN_URL,login,click_watch_btn,click_close_btn,click_save_btn,navigate_to_settings,Driver_path,write_to_excel
from store_setting_helper import click_store_tab,enter_title,enter_description,click_store_settings_tab,select_tag
class General_Tab:
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
 def click_store_settings_tab(self):
     try:
         click_store_settings_tab(self.wait)
         self.results["Store Settngs Screen is opened"] = "Passed"
     except Exception as e:
         self.results["Store Settngs Screen is not opened"] = f"Failed: {e}"

 def click_watch_btn(self):
     try:
         click_watch_btn(self.wait)
         self.results["Watch Video button is clicked"] = "Passed"
     except Exception as e:
         self.results["Watch Video button is not clicked"] = f"Failed: {e}"

 def click_close_btn(self):
     try:
         click_close_btn(self.wait)
         self.results["Watch Video button is clicked"] = "Passed"
     except Exception as e:
         self.results["Watch Video button is not clicked"] = f"Failed: {e}"

 def click_store_tab(self):
     try:
         click_store_tab(self.wait)
         self.results["Setting Store Page is opened"] = "Passed"
     except Exception as e:
         self.results["Setting Store Page  is not closed"] = f"Failed: {e}"
 def enter_title(self,value):
    try:
        enter_title(self.wait,value)
        self.results["Title is added in the text_field area"] = "Passed"
    except Exception as e:
         self.results["Title has not been added"] = f"Failed: {e}"
 def enter_description(self,value):
    try:
        enter_description(self.wait,value)
        self.results["Description is added in the text_field area"] = "Passed"
    except Exception as e:
         self.results["Description has not been added"] = f"Failed: {e}"
 def select_tag(self,tag):
    try:
        select_tag(self.wait,tag)
        self.results["Tag is added"] = "Passed"
    except Exception as e:
         self.results["Tag is not been added"] = f"Failed: {e}"

 def click_save_btn(self):
     try:
         click_save_btn(self.wait)
         self.results["All the data on General Tab is stored"] = "Passed"
     except Exception as e:
         self.results["All the data on the General Tab is not stored"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="user_group_tab_result.xlsx"):
         write_to_excel(self.results, folder_name, file_name)

class TestSettingPage:
    @pytest.fixture(scope='class')
    def setup(self):
        chrome_driver_path = Driver_path
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        login_wait = WebDriverWait(driver, 20)
        login(login_wait, USERNAME, PASSWORD)
        driver.get(Base_URL)
        yield driver
        driver.quit()

    def test_store_functions(self, setup):
        driver = setup
        general= General_Tab(driver)
        general.click_watch_btn()
        general.write_to_excel()
        general.click_close_btn()
        general.click_store_settings_tab()
        general.write_to_excel()
        general.enter_title("Test Screen")
        general.write_to_excel()
        general.enter_description("Testing Purpose")
        general.write_to_excel()
        general.select_tag("Fashion")
        general.write_to_excel()
        general.click_save_btn()
        general.write_to_excel()




