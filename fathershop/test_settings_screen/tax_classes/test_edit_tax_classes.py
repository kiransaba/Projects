import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from classes_helper import click_tax_classes_tab,click_edit_btn,edit_class_name,edit_description,click_default_btn,select_tax_rate,rate_dropdown,select_shipping_address,address_dropdown
class Edit_Tax_Classes:
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
 def click_tax_classes_tab(self):
     try:
         click_tax_classes_tab(self.wait)
         self.results["Tax Classes Page is opened"] = "Passed"
     except Exception as e:
         self.results["Tax Classes tab is not clicked"] = f"Failed: {e}"

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
 def edit_class_name(self, value):
     try:
         edit_class_name(self.wait, value)
         self.results["Class name is edited"] = "Passed"
     except Exception as e:
         self.results["Class name is not edited"] = f"Failed: {e}"
 def edit_description(self, value):
     try:
         edit_description(self.wait, value)
         self.results["Tax Class Description is edited "] = "Passed"
     except Exception as e:
         self.results["Tax Class Description is not edited "] = f"Failed: {e}"
 def click_default_btn(self):
     try:
         click_default_btn(self.wait)
         self.results["Default button is clicked"] = "Passed"
     except Exception as e:
         self.results["Default button is not clicked"] = f"Failed: {e}"
 def select_tax_rate(self):
     try:
         select_tax_rate(self.wait)
         self.results["Select Tax Rate drop-down button is clicked"] = "Passed"
     except Exception as e:
         self.results["Select Tax Rate drop-down button is not clicked"] = f"Failed: {e}"
 def rate_dropdown(self, title):
     try:
         rate_dropdown(self.wait, title)
         self.results["Tax Rate is selected "] = "Passed"
     except Exception as e:
         self.results["Tax Rate is not selected "] = f"Failed: {e}"
 def select_shipping_address(self):
     try:
         select_shipping_address(self.wait)
         self.results["Select Shipping Address drop-down button is clicked"] = "Passed"
     except Exception as e:
         self.results["Select Shipping Address drop-down button is not clicked"] = f"Failed: {e}"
 def address_dropdown(self,title):
     try:
         address_dropdown(self.wait,title)
         self.results["Shipping Address is selected"] = "Passed"
     except Exception as e:
         self.results["Shipping Address is not selected"] = f"Failed: {e}"

 def write_to_excel(self):
     write_to_excel(self.results, "excel_results","edit_tax_classes_results")


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
        #edit_rate.login                         #Commented part is required in the future
        #edit_rate.write_to_excel()
        #edit_rate.navigate_to_settings()
        #edit_rate.write_to_excel()
        edit_class = Edit_Tax_Classes(driver)
        edit_class.click_tax_classes_tab()
        edit_class.write_to_excel()
        edit_class.click_edit_btn()
        edit_class.write_to_excel()
        edit_class.edit_class_name("Test VAT")
        edit_class.write_to_excel()
        edit_class.edit_description("Products tested")
        edit_class.write_to_excel()
        edit_class.click_default_btn()
        edit_class.write_to_excel()
        edit_class.select_tax_rate()
        edit_class.rate_dropdown("VAT 15%")
        edit_class.write_to_excel()
        edit_class.select_shipping_address()
        edit_class.address_dropdown("Store Address")
        edit_class.write_to_excel()
        edit_class.click_save_btn()
        edit_class.write_to_excel()







