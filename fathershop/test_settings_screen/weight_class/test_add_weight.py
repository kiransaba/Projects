import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_addnew_btn
from weight_helpers import click_weight_classes_tab,enter_weight_name,enter_weight_arabic_name,enter_weight_unit,enter_weight_unit_arabic,enter_value
class Add_Weight_Class:
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

 def click_weight_classes_tab(self):
     try:
         click_weight_classes_tab(self.wait)
         self.results["Weight Classes Page is opened"] = "Passed"
     except Exception as e:
         self.results["Weight Classes tab is not clicked"] = f"Failed: {e}"

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
 def enter_weight_name(self,value):
    try:
        enter_weight_name(self.wait,value)
        self.results["Length Class name is added"] = "Passed"
    except Exception as e:
         self.results["Length Class name is not added"] = f"Failed: {e}"

 def enter_weight_arabic_name(self,value):
    try:
        enter_weight_arabic_name(self.wait,value)
        self.results["Weight Class arabic name is added"] = "Passed"
    except Exception as e:
         self.results["Weight Class arabic name is not added"] = f"Failed: {e}"
 def enter_weight_unit(self, value):
     try:
         enter_weight_unit(self.wait, value)
         self.results["Weight Class Unit  is added "] = "Passed"
     except Exception as e:
         self.results["Weight Class Unit  is not added "] = f"Failed: {e}"
 def enter_weight_unit_arabic(self, value):
     try:
         enter_weight_unit_arabic(self.wait, value)
         self.results["Weight Class Unit in arabic is added "] = "Passed"
     except Exception as e:
         self.results["Weight Class Unit in arabic is not added "] = f"Failed: {e}"
 def enter_value(self, value):
     try:
         enter_value(self.wait, value)
         self.results["Weight Class Value is added "] = "Passed"
     except Exception as e:
         self.results["Weight Class Value  is not added "] = f"Failed: {e}"

 def write_to_excel(self):
     write_to_excel(self.results, "excel_results","add_weight_classes_results")

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
        #add_weight.login()                       #this commented part is requiired in the future as for now we are direcr redirecting to settings page
        #add_weight.write_to_excel()
        #add_weight.navigate_to_settings()
        #add_weight.write_to_excel()
        add_weight = Add_Weight_Class(driver)
        add_weight.click_weight_classes_tab()
        add_weight.write_to_excel()
        add_weight.click_addnew_btn()
        add_weight.write_to_excel()
        add_weight.enter_weight_name("Test kilo")
        add_weight.write_to_excel()
        add_weight.enter_weight_arabic_name("Test kilo")
        add_weight.write_to_excel()
        add_weight.enter_weight_unit("kgs")
        add_weight.write_to_excel()
        add_weight.enter_weight_unit_arabic("kgs")
        add_weight.write_to_excel()
        add_weight.enter_value("1.00000")
        add_weight.click_save_btn()
        add_weight.write_to_excel()







