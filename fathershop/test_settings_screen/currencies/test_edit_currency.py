import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from currency_helper import click_currencies_tab,click_edit_currency1,hover_help_icon,edit_currency_symbol,edit_decimal_value,edit_value,symbol_position,status_radio_btn
class Edit_Currency:
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
 def  click_currencies_tab(self):
        try:
            click_currencies_tab(self.wait)
            self.results["Currencies screen is opened"] = "Passed"
        except Exception as e:
            self.results["Currencies Tab is not clicked"] = f"Failed: {e}"
 def click_edit_currency1(self):
        try:
            click_edit_currency1(self.wait)
            self.results["Currency Edit button is clicked"] = "Passed"
        except Exception as e:
            self.results["Currency Edit button is not clicked"] = f"Failed: {e}"

 def  status_radio_btn(self):
     try:
         status_radio_btn(self.wait)
         self.results["Status option is changed"] = "Passed"
     except Exception as e:
         self.results["Status option is changed"] = f"Failed: {e}"

 def click_save_btn(self):
     try:
         click_save_btn(self.wait)
         self.results["Save Return Action button is clicked"] = "Passed"
     except Exception as e:
         self.results["Save Return Action button is not clicked"] = f"Failed: {e}"

 def symbol_position(self, position):
     try:
         symbol_position(self.wait, position)
         self.results["Symbol Position is edited"] = "Passed"
     except Exception as e:
         self.results["Symbol Position is not edited"] = f"Failed: {e}"

 def edit_currency_symbol(self, value):
     try:
         edit_currency_symbol(self.wait, value)
         self.results["Currency value is edited"] = "Passed"
     except Exception as e:
         self.results["Currency value is not edited"] = f"Failed: {e}"

 def edit_decimal_value(self, value):
     try:
         edit_decimal_value(self.wait, value)
         self.results["Decimal value is edited"] = "Passed"
     except Exception as e:
         self.results["Decimal value is not edited"] = f"Failed: {e}"
 def hover_help_icon(self):
     try:
         hover_help_icon(self)
         self.results["Hovering over Value question mark icon"] = "Passed"
     except Exception as e:
         self.results["Hovering over Value question mark icon is not successful"] = f"Failed: {e}"

 def edit_value(self, value):
     try:
         edit_value(self.wait, value)
         self.results["Value is edited"] = "Passed"
     except Exception as e:
         self.results["Value is not edited"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="edit_currency_result.xlsx"):
     write_to_excel(self.results, folder_name, file_name)

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
         edit_currency = Edit_Currency(driver)
         #edit_currency.login()                       #this commented part is requiired in the future as for now we are direcr redirecting to settings page
         #edit_currency.write_to_excel()
         #edit_currency.navigate_to_settings()
         #edit_currency.write_to_excel()
         edit_currency.click_currencies_tab()
         edit_currency.write_to_excel()
         edit_currency.click_edit_currency1()
         edit_currency.write_to_excel()
         edit_currency.edit_currency_symbol("$")
         edit_currency.write_to_excel()
         edit_currency.symbol_position("Left")
         edit_currency.edit_decimal_value("0.1")
         edit_currency.write_to_excel()
         edit_currency.hover_help_icon()
         edit_currency.write_to_excel()
         edit_currency.edit_value("009")
         edit_currency.write_to_excel()
         edit_currency.click_save_btn()
         edit_currency.write_to_excel()







