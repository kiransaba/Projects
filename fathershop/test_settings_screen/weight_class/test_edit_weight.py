import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from weight_helpers import click_weight_classes_tab,click_edit_btn,edit_weight_name,edit_weight_unit,edit_value,edit_weight_unit_arabic,edit_weight_arabic_name
class Edit_Weight_Classes:
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
 def click_weight_classes_tab(self):
     try:
         click_weight_classes_tab(self.wait)
         self.results["Weight Classes Page is opened"] = "Passed"
     except Exception as e:
         self.results["Weight Classes tab is not clicked"] = f"Failed: {e}"

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

 def edit_weight_name(self,value):
    try:
        edit_weight_name(self.wait,value)
        self.results["Weight Class name is edited"] = "Passed"
    except Exception as e:
         self.results["Weight Class name is not edited"] = f"Failed: {e}"
 def edit_weight_arabic_name(self,value):
    try:
        edit_weight_arabic_name(self.wait,value)
        self.results["Weight Class arabic name is edited"] = "Passed"
    except Exception as e:
         self.results["Weight Class arabic name is not edited"] = f"Failed: {e}"
 def edit_weight_unit(self, value):
     try:
         edit_weight_unit(self.wait, value)
         self.results["Weight Class Unit  is edited "] = "Passed"
     except Exception as e:
         self.results["Weight Class Unit  is not edited "] = f"Failed: {e}"

 def edit_weight_unit_arabic(self, value):
     try:
         edit_weight_unit_arabic(self.wait, value)
         self.results["WeightClass Unit in arabic is edited "] = "Passed"
     except Exception as e:
         self.results["Weight Class Unit in arabic is not edited "] = f"Failed: {e}"
 def edit_value(self, value):
     try:
         edit_value(self.wait, value)
         self.results["WeightClass Value is edited "] = "Passed"
     except Exception as e:
         self.results["Weight Class Value  is not edited "] = f"Failed: {e}"
 def write_to_excel(self):
     write_to_excel(self.results, "excel_results","edit_weight_classes_results")

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
        #edit_weight.login()
        #edit_weight.write_to_excel()                            #this commented part is requiired in the future as for now we are direcr redirecting to settings page
        #edit_weight.navigate_to_settings()
        #edit_weight.write_to_excel()
        edit_weight = Edit_Weight_Classes(driver)
        edit_weight.click_weight_classes_tab()
        edit_weight.write_to_excel()
        edit_weight.click_edit_btn()
        edit_weight.write_to_excel()
        edit_weight.edit_weight_name("Test grams")
        edit_weight.edit_weight_arabic_name("Test grams")
        edit_weight.write_to_excel()
        edit_weight.edit_weight_unit("gram")
        edit_weight.write_to_excel()
        edit_weight.edit_weight_unit_arabic("gram")
        edit_weight.write_to_excel()
        edit_weight.edit_value("1.000000")
        edit_weight.click_save_btn()
        edit_weight.write_to_excel()







