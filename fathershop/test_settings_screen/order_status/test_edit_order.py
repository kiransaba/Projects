import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from order_helper import click_oder_tab,click_edit_btn,edit_order_english_name,edit_order_arabic_name
class Edit_Order_status:

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

##Clicking Setting button
 def navigate_to_settings(self):
      try:
        navigate_to_settings(self)
        self.results["Navigate to Settings Screen"] = "Passed"
      except Exception as e:
        self.results["Navigate to Settings Screen"] = f"Failed: {e}"

 def click_order_tab(self):
     try:
         click_oder_tab(self.wait)
         self.results["Order Statuses Page is opened"] = "Passed"
     except Exception as e:
         self.results["Order Statuses Page  is not closed"] = f"Failed: {e}"

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
 def edit_order_english_name(self,input_value,value):
    try:
        edit_order_english_name(self.wait,input_value,value)
        self.results["Order Status name is edited in the English language"] = "Passed"
    except Exception as e:
         self.results["Order Status name is not edited in the English language"] = f"Failed: {e}"
 def edit_order_arabic_name(self,input_value,value):
     try:
         edit_order_arabic_name(self.wait,input_value,value)
         self.results["Order Status name is edited in the Arabic language"] = "Passed"
     except Exception as e:
         self.results["Order Status name is not edited in the Arabic language"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="edit_order_status_result.xlsx"):
         write_to_excel(self.results, folder_name, file_name)

class TestSettingPage:
    @pytest.fixture(scope='class')
    def setup(self):
        chrome_driver_path = Driver_path
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        # Logging in
        login_wait = WebDriverWait(driver, 10)
        login(login_wait, driver, USERNAME, PASSWORD)
        # Change URL to Base_URL after logging in
        driver.get(Base_URL)
        yield driver
        driver.quit()

    def test_user_functions(self, setup):
        driver = setup
        edit_order= Edit_Order_status(driver)
        #edit_order.login()                                       #commented part is required in near future
        #edit_order.write_to_excel()
        #edit_order.navigate_to_settings()
        #edit_order.write_to_excel()
        edit_order.click_order_tab()
        edit_order.write_to_excel()
        edit_order.click_edit_btn()
        edit_order.write_to_excel()
        edit_order.edit_order_english_name("Cancelled","Test Cancel")      #Here Input Value is the field name stored
        edit_order.write_to_excel()                                                         #Change the input value when once the code is run
        edit_order.edit_order_arabic_name("Cancelled","Test Cancel")   #Change the input value when once the code is run
        edit_order.write_to_excel()
        edit_order.click_save_btn()
        edit_order.write_to_excel()







