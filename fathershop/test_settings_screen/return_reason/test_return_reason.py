import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,click_guide_btn,click_close_btn,navigate_to_settings,click_save_btn,write_to_excel,Driver_path,\
    click_watch_btn,click_delete_btn,click_cancel_btn,click_addnew_btn
from return_helper import click_return_reason_tab,click_checkbox_btn,click_edit_btn,click_tab_back
class Return_Reason_Page:
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
 def click_return_reason_tab(self):
     try:
         click_return_reason_tab(self.wait)
         self.results["Return Statuses screen is opened"] = "Passed"
     except Exception as e:
         self.results["Return Statuses Tab is not clicked"] = f"Failed: {e}"

 def click_watch_btn(self):
     try:
         click_watch_btn(self.wait)
         self.results["Watch Video button is clicked"] = "Passed"
     except Exception as e:
         self.results["Watch Video button is not clicked"] = f"Failed: {e}"

 def click_guide_btn(self):
     try:
         click_guide_btn(self.wait)
         self.results["Video guide button is clicked"] = "Passed"
     except Exception as e:
         self.results["Video guide button is not clicked"] = f"Failed: {e}"

 def click_close_btn(self):
     try:
         click_close_btn(self.wait)
         self.results["Close Video button is clicked"] = "Passed"
     except Exception as e:
         self.results["Close Video button is not clicked"] = f"Failed: {e}"

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
         self.results["Tab(back) button is clicked"] = "Passed"
     except Exception as e:
         self.results["Tab(back) button is not clicked"] = f"Failed: {e}"

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
         self.results["Cancel button is not clicked"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="return_reason_result.xlsx"):
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
        login(login_wait,USERNAME, PASSWORD)
        # Change URL to Base_URL after logging in
        driver.get(Base_URL)
        yield driver
        driver.quit()

    def test_user_functions(self, setup):
        driver = setup
        return_page= Return_Reason_Page(driver)
        #return_page.login()                   #commented part is required in near future
        #return_page.write_to_excel()
        #return_page.navigate_to_settings()
        #return_page.write_to_excel()
        return_page.click_watch_btn()
        return_page.write_to_excel()
        return_page.click_close_btn()
        return_page.write_to_excel()
        return_page.click_return_reason_tab()
        return_page.write_to_excel()
        return_page.click_addnew_btn()
        return_page.write_to_excel()
        return_page.click_tab_back()
        return_page.write_to_excel()
        return_page.click_addnew_btn()
        return_page.write_to_excel()
        return_page.click_cancel_btn()
        return_page.write_to_excel()
        return_page.click_edit_btn()
        return_page.write_to_excel()
        return_page.click_tab_back()
        return_page.write_to_excel()
        return_page.click_edit_btn()
        return_page.write_to_excel()
        return_page.click_cancel_btn()
        return_page.write_to_excel()
        return_page.click_checkbox_btn()
        return_page.write_to_excel()
        #return_page.click_delete_btn()   # to check delete functionality un-comment this line
        #return_page.write_to_excel()



