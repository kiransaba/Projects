import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_addnew_btn
from classes_helper import click_tax_classes_tab, enter_class_name,enter_description,click_default_btn,select_tax_rate,rate_dropdown,select_shipping_address,address_dropdown,\
    send_priority
class Add_Tax_Class:
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
 def click_tax_classes_tab(self):
     try:
         click_tax_classes_tab(self.wait)
         self.results["Tax Classes Page is opened"] = "Passed"
     except Exception as e:
         self.results["Tax Classes tab is not clicked"] = f"Failed: {e}"
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
 def enter_class_name(self,value):
    try:
        enter_class_name(self.wait,value)
        self.results["Tax Class name is added"] = "Passed"
    except Exception as e:
         self.results["Tax Class name is not added"] = f"Failed: {e}"
 def enter_description(self, value):
     try:
         enter_description(self.wait, value)
         self.results["Tax Class Description is added "] = "Passed"
     except Exception as e:
         self.results["Tax Class Description is not added "] = f"Failed: {e}"
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

 def  send_priority(self, value):
     try:
        send_priority(self.wait, value)
        self.results["Priority value is added "] = "Passed"
     except Exception as e:
        self.results["Priority value is not added "] = f"Failed: {e}"

 def write_to_excel(self):
     write_to_excel(self.results, "excel_results","add_tax_classes_results")

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
        #add_rate.login()                       #Commented part is required in the future
        #add_rate.write_to_excel()
        #add_rate.navigate_to_settings()
        #add_rate.write_to_excel()
        add_class = Add_Tax_Class(driver)
        add_class.click_tax_classes_tab()
        add_class.write_to_excel()
        add_class.click_addnew_btn()
        add_class.write_to_excel()
        add_class.enter_class_name("Test Class")
        add_class.write_to_excel()
        add_class.enter_description("Test Products")
        add_class.write_to_excel()
        add_class.click_default_btn()
        add_class.write_to_excel()
        add_class.select_tax_rate()
        add_class.rate_dropdown("VAT 123456")
        add_class.write_to_excel()
        add_class.select_shipping_address()
        add_class.address_dropdown("Payment Address")
        add_class.write_to_excel()
        add_class.send_priority("3")
        add_class.write_to_excel()
        add_class.click_save_btn()
        add_class.write_to_excel()







