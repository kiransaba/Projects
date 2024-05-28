import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL,USERNAME, PASSWORD, LOGIN_URL,login,click_watch_btn,click_close_btn,click_save_btn,navigate_to_settings,Driver_path,write_to_excel
from store_setting_helper import click_store_settings_tab,click_local_tab,click_country_dropdown,click_region_dropdown,click_time_dropdown,click_currency_dropdown,click_language_dropdown,click_length_dropdown,\
    click_weight_dropdown,click_admin_language_dropdown
class Local_Tab:
 def __init__(self, driver):
  self.driver = driver
  self.wait = WebDriverWait(self.driver, 10)
  self.results = {}

 def click_store_settings_tab(self):
     try:
         click_store_settings_tab(self.wait)
         self.results["Store Settings Screen is opened"] = "Passed"
     except Exception as e:
         self.results["Store Settings Screen is not opened"] = f"Failed: {e}"
 def click_local_tab(self):
     try:
         click_local_tab(self.wait)
         self.results["Local Tab is clicked"] = "Passed"
     except Exception as e:
         self.results["Local Tab is not clicked"] = f"Failed: {e}"


 def click_country_dropdown(self,title):
     try:
         click_country_dropdown(self.wait,title)
         self.results["Country is selected"] = "Passed"
     except Exception as e:
         self.results["Country is not selected"] = f"Failed: {e}"

 def click_region_dropdown(self,title):
     try:
         click_region_dropdown(self.wait,title)
         self.results["Region is selected"] = "Passed"
     except Exception as e:
         self.results["Region is not selected"] = f"Failed: {e}"


 def click_time_dropdown(self,title):
     try:
         click_time_dropdown(self.wait,title)
         self.results["Time zone is selected"] = "Passed"
     except Exception as e:
         self.results["Time zone is not selected"] = f"Failed: {e}"


 def click_language_dropdown(self,title):
     try:
         click_language_dropdown(self.wait,title)
         self.results["Language is selected"] = "Passed"
     except Exception as e:
         self.results["Language is not selected"] = f"Failed: {e}"


 def click_admin_language_dropdown(self,title):
     try:
         click_admin_language_dropdown(self.wait,title)
         self.results["Administration Language is selected"] = "Passed"
     except Exception as e:
         self.results["Administration Language is not selected"] = f"Failed: {e}"


 def click_currency_dropdown(self,title):
     try:
         click_currency_dropdown(self.wait,title)
         self.results["Currency is selected"] = "Passed"
     except Exception as e:
         self.results["Currency is not selected"] = f"Failed: {e}"

 def click_length_dropdown(self,title):
     try:
         click_length_dropdown(self.wait,title)
         self.results["Length Class is selected"] = "Passed"
     except Exception as e:
         self.results["Length Class is not selected"] = f"Failed: {e}"

 def click_weight_dropdown(self,title):
     try:
         click_weight_dropdown(self.wait,title)
         self.results["Weight Class is selected"] = "Passed"
     except Exception as e:
         self.results["Weight Class is not selected"] = f"Failed: {e}"

 def click_save_btn(self):
     try:
         click_save_btn(self.wait)
         self.results["All the data on Store Tab is stored"] = "Passed"
     except Exception as e:
         self.results["All the data on the Store Tab is not stored"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="local_tab_result.xlsx"):
     write_to_excel(self.results, folder_name, file_name)

class TestSettingPage:
     @pytest.fixture(scope='class')
     def setup(self):
         chrome_driver_path = Driver_path
         driver = webdriver.Chrome()
         driver.get(LOGIN_URL)
         driver.maximize_window()
         login_wait = WebDriverWait(driver, 20)
         login(login_wait, USERNAME, PASSWORD)
         driver.get(Base_URL)
         yield driver
         driver.quit()

     def test_store_functions(self, setup):

             driver = setup
             local = Local_Tab(driver)
             local.click_store_settings_tab()
             local.click_local_tab()
             local.write_to_excel()
             local.click_country_dropdown("Rwanda")
             local.write_to_excel()
             local.click_region_dropdown("Al Madinah")
             local.write_to_excel()
             local.click_time_dropdown("Asia/Phnom_Penh (+07:00)")
             local.write_to_excel()
             local.click_language_dropdown("عربي")
             local.write_to_excel()
             local.click_length_dropdown("Inch")
             local.write_to_excel()
             local.click_weight_dropdown("Kilogram")
             local.write_to_excel()
             local.click_currency_dropdown("US Dollar")
             local.write_to_excel()
             local.click_save_btn()
             local.write_to_excel()


