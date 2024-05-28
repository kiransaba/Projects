import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from tax_helper import click_tax_rate_tab,click_edit_btn,edit_tax_name,edit_tax_rate,click_default_btn,select_type,type_dropdown,select_geo_zone,zone_dropdown
class Edit_Tax_Rate:
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
 def click_tax_rate_tab(self):
     try:
         click_tax_rate_tab(self.wait)
         self.results["Tax Rate Page is opened"] = "Passed"
     except Exception as e:
         self.results["Tax Rate tab is not clicked"] = f"Failed: {e}"

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

 def edit_tax_name(self, value):
     try:
         edit_tax_name(self.wait, value)
         self.results["Tax name is edited"] = "Passed"
     except Exception as e:
         self.results["Tax name is not edited"] = f"Failed: {e}"

 def edit_tax_rate(self, value):
     try:
         edit_tax_rate(self.wait, value)
         self.results["Tax Rate is edited "] = "Passed"
     except Exception as e:
         self.results["Tax Rate is not edited "] = f"Failed: {e}"
 def click_default_btn(self):
     try:
         click_default_btn(self.wait)
         self.results["Default button is clicked"] = "Passed"
     except Exception as e:
         self.results["Default button is not clicked"] = f"Failed: {e}"
 def select_type(self):
     try:
         select_type(self.wait)
         self.results["Select drop-down button is clicked"] = "Passed"
     except Exception as e:
         self.results["Select drop-down button is not clicked"] = f"Failed: {e}"
 def type_dropdown(self, title):
     try:
         type_dropdown(self.wait, title)
         self.results["Type is selected "] = "Passed"
     except Exception as e:
         self.results["Type is not selected "] = f"Failed: {e}"
 def select_geo_zone(self):
     try:
         select_geo_zone(self.wait)
         self.results["Select Geo Zone drop-down button is clicked"] = "Passed"
     except Exception as e:
         self.results["Select Geo Zone drop-down button is not clicked"] = f"Failed: {e}"
 def zone_dropdown(self, title):
     try:
         zone_dropdown(self.wait, title)
         self.results["Zone is selected "] = "Passed"
     except Exception as e:
         self.results["Zone is not selected "] = f"Failed: {e}"

 def write_to_excel(self):
     write_to_excel(self.results, "excel_results","edit_tax_rate_results")

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
        #edit_rate.login()                      #Commented part is required in future
        #edit_rate.write_to_excel()
        #edit_rate.navigate_to_settings()
        #edit_rate.write_to_excel()
        edit_rate = Edit_Tax_Rate(driver)
        edit_rate.click_tax_rate_tab()
        edit_rate.write_to_excel()
        edit_rate.click_edit_btn()
        edit_rate.write_to_excel()
        edit_rate.edit_tax_name("Test12 VAT")
        edit_rate.write_to_excel()
        edit_rate.edit_tax_rate("120000")
        edit_rate.write_to_excel()
        edit_rate.click_default_btn()
        edit_rate.write_to_excel()
        edit_rate.select_type()
        edit_rate.write_to_excel()
        edit_rate.type_dropdown("Fixed Amount")
        edit_rate.write_to_excel()
        edit_rate.select_geo_zone()
        edit_rate.write_to_excel()
        edit_rate.zone_dropdown("KSA Zone")
        edit_rate.write_to_excel()
        edit_rate.click_save_btn()
        edit_rate.write_to_excel()







