import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL,USERNAME, PASSWORD, LOGIN_URL,login,click_close_btn,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_delete_btn,\
    click_tab_back,click_watch_btn,click_addnew_btn,click_cancel_btn
from tax_helper import click_tax_rate_tab,click_checkbox_select_all,click_checkbox_btn,click_edit_btn,click_next_btn,click_previous_btn
class Tax_rate:
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
 def click_tax_rate_tab(self):
     try:
         click_tax_rate_tab(self.wait)
         self.results["Tax Rate Page is opened"] = "Passed"
     except Exception as e:
         self.results["Tax Rate tab is not clicked"] = f"Failed: {e}"

 def click_watch_btn(self):
     try:
         click_watch_btn(self.wait)
         self.results["Watch Video button is clicked"] = "Passed"
     except Exception as e:
         self.results["Watch Video button is not clicked"] = f"Failed: {e}"

 def click_video_btn(self):
     try:
         #click_video_btn(self.wait)
         self.results["Geo_zones: Watch Video button is clicked"] = "Passed"
     except Exception as e:
         self.results["Geo_zones: Watch Video button is not clicked"] = f"Failed: {e}"

 def click_close_btn(self):
     try:
         click_close_btn(self.wait)
         self.results["Watch Video button is clicked"] = "Passed"
     except Exception as e:
         self.results["Watch Video button is not clicked"] = f"Failed: {e}"

 def click_checkbox_select_all(self):
     try:
         click_checkbox_select_all(self.wait)
         self.results["Select all Checkbox button is clicked"] = "Passed"
     except Exception as e:
         self.results["Select all Checkbox button is not clicked"] = f"Failed: {e}"

 def click_checkbox_btn(self):
     try:
         click_checkbox_btn(self.wait)
         self.results["Checkbox button is clicked"] = "Passed"
     except Exception as e:
         self.results["Checkbox button is not clicked"] = f"Failed: {e}"

 def click_delete_btn(self):
     try:
         click_delete_btn(self.wait)
         self.results["Add New button is clicked"] = "Passed"
     except Exception as e:
         self.results["Add New button is not clicked"] = f"Failed: {e}"

 def click_addnew_btn(self):
     try:
         click_addnew_btn(self.wait)
         self.results["Add New button is clicked"] = "Passed"
     except Exception as e:
         self.results["Add New button is not clicked"] = f"Failed: {e}"

 def click_edit_btn(self):
     try:
         click_edit_btn(self.wait)
         self.results["Edit button is clicked"] = "Passed"
     except Exception as e:
         self.results["Edit button is not clicked"] = f"Failed: {e}"

 def click_tab_back(self):
     try:
         click_tab_back(self.wait)
         self.results["Stock Status Back button is clicked"] = "Passed"
     except Exception as e:
         self.results["Stock Status Back button is not clicked"] = f"Failed: {e}"

 def click_save_btn(self):
     try:
         click_save_btn(self.wait)
         self.results["Save button is clicked"] = "Passed"
     except Exception as e:
         self.results["Save button is not clicked"] = f"Failed: {e}"

 def click_cancel_btn(self):
     try:
         click_cancel_btn(self.wait)
         self.results["Cancel button is clicked"] = "Passed"
     except Exception as e:
         self.results["Cancel is not clicked"] = f"Failed: {e}"

 def click_next_btn(self):
     try:
         click_next_btn(self.wait)
         self.results["Next Page button is clicked"] = "Passed"
     except Exception as e:
         self.results["Next Page button is not clicked"] = f"Failed: {e}"

 def click_previous_btn(self):
     try:
         click_previous_btn(self.wait)
         self.results["Previous Page button is clicked"] = "Passed"
     except Exception as e:
         self.results["Previous Page button is not clicked"] = f"Failed: {e}"

 def write_to_excel(self):
     write_to_excel(self.results, "excel_results","tax_rate_results")

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
        rate= Tax_rate(driver)
        #rate.login()                       #Commented part is required in future
        #rate.write_to_excel()
        #rate.navigate_to_settings()
        #rate.write_to_excel()
        rate.click_tax_rate_tab()
        rate.write_to_excel()
        rate.click_addnew_btn()
        rate.write_to_excel()
        rate.click_tab_back()
        rate.write_to_excel()
        rate.click_addnew_btn()
        rate.write_to_excel()
        rate.click_cancel_btn()
        rate.write_to_excel()
        rate.click_edit_btn()
        rate.write_to_excel()
        rate.click_tab_back()
        rate.write_to_excel()
        rate.click_edit_btn()
        rate.write_to_excel()
        rate.click_cancel_btn()
        rate.write_to_excel()
        rate.click_checkbox_select_all()
        rate.write_to_excel()
        rate.click_next_btn()
        rate.write_to_excel()
        rate.click_checkbox_btn()
        rate.write_to_excel()
        #rate.click_delete_btn()    #uncomment t for checkng the delete funcyonalty
        #rate.write_to_excel()



