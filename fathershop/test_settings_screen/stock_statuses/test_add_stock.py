import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_cancel_btn,\
click_addnew_btn
from stock_helper import click_stock_tab,enter_stock_english_name,enter_stock_arabic_name
class Add_Stock_status:
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
 def  click_stock_tab(self):
     try:
         click_stock_tab(self.wait)
         self.results["Stock Statuses Page is opened"] = "Passed"
     except Exception as e:
         self.results["Stock Statuses Tab is not clicked"] = f"Failed: {e}"

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
 def enter_stock_english_name(self,value):
    try:
        enter_stock_english_name(self.wait,value)
        self.results["Stock Status name is added in the English language"] = "Passed"
    except Exception as e:
         self.results["Stock Statusname is not added in the English language"] = f"Failed: {e}"
 def enter_stock_arabic_name(self, value):
     try:
         enter_stock_arabic_name(self.wait, value)
         self.results["Stock Status name is added in the Arabic language"] = "Passed"
     except Exception as e:
         self.results["Stock Statusname is not added in the Arabic language"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="add_stock_status_result.xlsx"):
         write_to_excel(self.results, folder_name, file_name)

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
        add_stock= Add_Stock_status(driver)
        #add_stock.login()               #commented part is required
        #add_stock.write_to_excel()
        #add_stock.navigate_to_settings()
        #add_stock.write_to_excel()
        add_stock.click_stock_tab()
        add_stock.write_to_excel()
        add_stock.click_addnew_btn()
        add_stock.write_to_excel()
        add_stock.enter_stock_english_name("Test Stock")
        add_stock.write_to_excel()
        add_stock.enter_stock_arabic_name("Test Stock")
        add_stock.write_to_excel()
        add_stock.click_save_btn()
        add_stock.write_to_excel()







