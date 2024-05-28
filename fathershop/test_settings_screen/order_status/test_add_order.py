import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_addnew_btn
from order_helper import click_oder_tab,enter_order_english_name,enter_order_arabic_name
class Add_Order_Status:
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
 def click_order_tab(self):
     try:
         click_oder_tab(self.wait)
         self.results["Order Statuses Page is opened"] = "Passed"
     except Exception as e:
         self.results["Order Statuses Page  is not closed"] = f"Failed: {e}"

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
 def enter_order_english_name(self,value):
    try:
        enter_order_english_name(self.wait,value)
        self.results["Order Status name is added in the English language"] = "Passed"
    except Exception as e:
         self.results["Order Statusname is not added in the English language"] = f"Failed: {e}"
 def enter_order_arabic_name(self, value):
     try:
         enter_order_arabic_name(self.wait, value)
         self.results["Order Status name is added in the Arabic language"] = "Passed"
     except Exception as e:
         self.results["Order Statusname is not added in the Arabic language"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="add_order_status_result.xlsx"):
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
        login(login_wait, USERNAME, PASSWORD)
        # Change URL to Base_URL after logging in
        driver.get(Base_URL)
        yield driver
        driver.quit()
    def test_user_functions(self, setup):
        driver = setup
        add_order= Add_Order_Status(driver)
        #add_order.login()                       #omment part will be used in the future
        #add_order.write_to_excel()
        #add_order.navigate_to_settings()
        #add_order.write_to_excel()
        add_order.click_order_tab()
        add_order.write_to_excel()
        add_order.click_addnew_btn()
        add_order.write_to_excel()
        add_order.enter_order_english_name("Test Order")
        add_order.write_to_excel()
        add_order.enter_order_arabic_name("Test Order")
        add_order.write_to_excel()
        add_order.click_save_btn()
        add_order.write_to_excel()







