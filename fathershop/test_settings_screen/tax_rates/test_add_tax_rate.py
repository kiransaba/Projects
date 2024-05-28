import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_addnew_btn
from tax_helper import click_tax_rate_tab,enter_tax_name,enter_tax_rate,click_default_btn,select_type,type_dropdown,select_geo_zone,zone_dropdown
class Add_Tax_Rate:
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
 def click_tax_rate_tab(self):
     try:
         click_tax_rate_tab(self.wait)
         self.results["Tax Rate Page is opened"] = "Passed"
     except Exception as e:
         self.results["Tax Rate tab is not clicked"] = f"Failed: {e}"

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
 def enter_tax_name(self,value):
    try:
        enter_tax_name(self.wait,value)
        self.results["Tax name is added"] = "Passed"
    except Exception as e:
         self.results["Tax name is not added"] = f"Failed: {e}"
 def enter_tax_rate(self, value):
     try:
         enter_tax_rate(self.wait, value)
         self.results["Tax Rate is added "] = "Passed"
     except Exception as e:
         self.results["Tax Rate is not added "] = f"Failed: {e}"
 def click_default_btn(self):
     try:
         click_default_btn(self.wait)
         self.results["Default button is clicked"] = "Passed"
     except Exception as e:
         self.results["Default button is not clicked"] = f"Failed: {e}"
 def select_type(self):
     try:
         select_type(self.wait)
         self.results["Select Type drop-down button is clicked"] = "Passed"
     except Exception as e:
         self.results["Select Type drop-down button is not clicked"] = f"Failed: {e}"
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
     write_to_excel(self.results, "excel_results","add_tax_rate_results")


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
        #add_rate.login()                      #Commented part is required in future
        #add_rate.write_to_excel()
        #add_rate.navigate_to_settings()
        #add_rate.write_to_excel()
        add_rate = Add_Tax_Rate(driver)
        add_rate.click_tax_rate_tab()
        add_rate.write_to_excel()
        add_rate.click_addnew_btn()
        add_rate.write_to_excel()
        add_rate.enter_tax_name("Test 10%")
        add_rate.write_to_excel()
        add_rate.enter_tax_rate("2500")
        add_rate.write_to_excel()
        add_rate.click_default_btn()
        add_rate.write_to_excel()
        add_rate.select_type()
        add_rate.type_dropdown("Percentage")
        add_rate.select_geo_zone()
        add_rate.zone_dropdown("UK Shipping")
        add_rate.click_save_btn()
        add_rate.write_to_excel()







