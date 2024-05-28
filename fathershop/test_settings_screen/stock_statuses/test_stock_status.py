import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL,USERNAME, PASSWORD, LOGIN_URL,login,click_close_btn,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_delete_btn,\
    click_tab_back,click_watch_btn,click_addnew_btn,click_cancel_btn
from stock_helper import click_stock_tab,click_checkbox_select_all,click_checkbox_btn,click_video_btn,click_edit_btn
class Stock_Status:
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
 def click_stock_tab(self):
     try:
         click_stock_tab(self.wait)
         self.results["Stock Status Page is opened"] = "Passed"
     except Exception as e:
         self.results["User Page  is not closed"] = f"Failed: {e}"

 def click_watch_btn(self):
     try:
         click_watch_btn(self.wait)
         self.results["Watch Video button is clicked"] = "Passed"
     except Exception as e:
         self.results["Watch Video button is not clicked"] = f"Failed: {e}"

 def click_video_btn(self):
     try:
         click_video_btn(self.wait)
         self.results["Stock Status: Watch Video button is clicked"] = "Passed"
     except Exception as e:
         self.results["Stock Status: Watch Video button is not clicked"] = f"Failed: {e}"

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

 def write_to_excel(self):
     write_to_excel(self.results, "excel_user_results","stock_status_results")

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
        stock = Stock_Status(driver)
        #stock.login()                       #Commented part is required in future
        #stock.write_to_excel()
        #stock.navigate_to_settings()
        #stockr.write_to_excel()
        stock.click_watch_btn()
        stock.write_to_excel()
        stock.click_close_btn()
        stock.write_to_excel()
        stock.click_stock_tab()
        stock.write_to_excel()
        stock.click_addnew_btn()
        stock.write_to_excel()
        stock.click_tab_back()
        stock.write_to_excel()
        stock.click_addnew_btn()
        stock.write_to_excel()
        stock.click_cancel_btn()
        stock.write_to_excel()
        stock.click_edit_btn()
        stock.write_to_excel()
        stock.click_tab_back()
        stock.write_to_excel()
        stock.click_edit_btn()
        stock.write_to_excel()
        stock.click_cancel_btn()
        stock.write_to_excel()
        stock.click_checkbox_select_all()
        stock.write_to_excel()
        stock.click_checkbox_btn()
        stock.write_to_excel()
        #stock.click_delete_btn()    #uncomment it for checkng the delete funcyonalty
        #stock.write_to_excel()




