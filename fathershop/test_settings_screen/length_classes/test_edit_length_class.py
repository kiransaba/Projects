import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from length_helper import click_length_classes_tab,click_edit_btn,edit_length_name,edit_length_unit,edit_value,edit_length_unit_arabic,edit_length_arabic_name
class Edit_Length_Classes:
 def __init__(self, driver):

  self.driver = driver
  self.wait = WebDriverWait(self.driver, 10)
  self.results = {}

## Screen Login
 def login(self):
    try:
      login(self.wait,USERNAME, PASSWORD)
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

 def click_length_classes_tab(self):
     try:
         click_length_classes_tab(self.wait)
         self.results["LengthClasses Page is opened"] = "Passed"
     except Exception as e:
         self.results["Length Classes tab is not clicked"] = f"Failed: {e}"

 def click_edit_btn(self):
     try:
         click_edit_btn(self.wait)
         self.results["Edit button is clicked"] = "Passed"
     except Exception as e:
         self.results["Edit button is not clicked"] = f"Failed: {e}"

 def click_save_btn(self):
     try:
         click_save_btn(self.wait)
         self.results["Save button is clicked"] = "Passed"
     except Exception as e:
         self.results["Save button is not clicked"] = f"Failed: {e}"

 def edit_length_name(self,value):
    try:
        edit_length_name(self.wait,value)
        self.results["Length Class name is edited"] = "Passed"
    except Exception as e:
         self.results["Length Class name is not edited"] = f"Failed: {e}"
 def edit_length_arabic_name(self,value):
    try:
        edit_length_arabic_name(self.wait,value)
        self.results["Length Class arabic name is edited"] = "Passed"
    except Exception as e:
         self.results["Length Class arabic name is not edited"] = f"Failed: {e}"
 def edit_length_unit(self, value):
     try:
         edit_length_unit(self.wait, value)
         self.results["Length Class Unit  is edited "] = "Passed"
     except Exception as e:
         self.results["Length Class Unit  is not edited "] = f"Failed: {e}"
 def edit_length_unit_arabic(self, value):
     try:
         edit_length_unit_arabic(self.wait, value)
         self.results["Length Class Unit in arabic is edited "] = "Passed"
     except Exception as e:
         self.results["Length Class Unit in arabic is not edited "] = f"Failed: {e}"
 def edit_value(self, value):
     try:
         edit_value(self.wait, value)
         self.results["Length Class Value is edited "] = "Passed"
     except Exception as e:
         self.results["Length Class Value  is not edited "] = f"Failed: {e}"
 def write_to_excel(self):
     write_to_excel(self.results, "excel_results","edit_length_classes_results")

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
        #edit_rate.login()
        #edit_rate.write_to_excel()                            #this commented part is requiired in the future as for now we are direcr redirecting to settings page
        #edit_rate.navigate_to_settings()
        #edit_rate.write_to_excel()
        edit_length = Edit_Length_Classes(driver)
        edit_length.click_length_classes_tab()
        edit_length.write_to_excel()
        edit_length.click_edit_btn()
        edit_length.write_to_excel()
        edit_length.edit_length_name("Testing")
        edit_length.edit_length_arabic_name("Testing")
        edit_length.write_to_excel()
        edit_length.edit_length_unit("cms")
        edit_length.write_to_excel()
        edit_length.edit_length_unit_arabic("cms")
        edit_length.write_to_excel()
        edit_length.edit_value("10.000000")
        edit_length.click_save_btn()
        edit_length.write_to_excel()







