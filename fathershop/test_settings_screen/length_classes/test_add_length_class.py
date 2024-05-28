import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_addnew_btn
from length_helper import click_length_classes_tab,enter_length_name,enter_length_arabic_name,enter_length_unit,enter_length_unit_arabic,enter_value
class Add_Length_Class:
 def __init__(self, driver):
  self.driver = driver
  self.wait = WebDriverWait(self.driver, 10)
  self.results = {}
## Screen Login
 def login(self):                       ## will be used in the future
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
 def enter_length_name(self,value):
    try:
        enter_length_name(self.wait,value)
        self.results["Length Class name is added"] = "Passed"
    except Exception as e:
         self.results["Length Class name is not added"] = f"Failed: {e}"

 def enter_length_arabic_name(self,value):
    try:
        enter_length_arabic_name(self.wait,value)
        self.results["Length Class arabic name is added"] = "Passed"
    except Exception as e:
         self.results["Length Class arabic name is not added"] = f"Failed: {e}"
 def enter_length_unit(self, value):
     try:
         enter_length_unit(self.wait, value)
         self.results["Length Class Unit  is added "] = "Passed"
     except Exception as e:
         self.results["Length Class Unit  is not added "] = f"Failed: {e}"
 def enter_length_unit_arabic(self, value):
     try:
         enter_length_unit_arabic(self.wait, value)
         self.results["Length Class Unit in arabic is added "] = "Passed"
     except Exception as e:
         self.results["Length Class Unit in arabic is not added "] = f"Failed: {e}"
 def enter_value(self, value):
     try:
         enter_value(self.wait, value)
         self.results["Length Class Value is added "] = "Passed"
     except Exception as e:
         self.results["Length Class Value  is not added "] = f"Failed: {e}"

 def write_to_excel(self):
     write_to_excel(self.results, "excel_results","add_length_classes_results")

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
        #add_rate.login()                       #this commented part is requiired in the future as for now we are direcr redirecting to settings page
        #add_rate.write_to_excel()
        #add_rate.navigate_to_settings()
        #add_rate.write_to_excel()
        add_length = Add_Length_Class(driver)
        add_length.click_length_classes_tab()
        add_length.write_to_excel()
        add_length.click_addnew_btn()
        add_length.write_to_excel()
        add_length.enter_length_name("Test Centi")
        add_length.write_to_excel()
        add_length.enter_length_arabic_name("Test Centi")
        add_length.write_to_excel()
        add_length.enter_length_unit("cm")
        add_length.write_to_excel()
        add_length.enter_length_unit_arabic("cm")
        add_length.write_to_excel()
        add_length.enter_value("12.0000")
        add_length.click_save_btn()
        add_length.write_to_excel()







