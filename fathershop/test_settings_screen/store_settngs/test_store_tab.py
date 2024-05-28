import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from  setting_constant import Base_URL,WAIT_TIME_SHORT,USERNAME, PASSWORD, LOGIN_URL,login, Driver_path,click_save_btn,navigate_to_settings,write_to_excel
from store_setting_helper import click_store_tab,enter_store_name,enter_owner_name,enter_email,upload_image,enter_address,enter_geocode,enter_telephone,enter_fax,\
    enter_comment,enter_opening_times,click_mode_btn,click_store_settings_tab
class Store_Page:
 def __init__(self, driver):
  self.driver = driver
  self.wait = WebDriverWait(self.driver, 10)
  self.results = {}


 def click_store_settings_tab(self):
     try:
         click_store_settings_tab(self.wait)
         self.results["Store Settngs Screen is opened"] = "Passed"
     except Exception as e:
         self.results["Store Settngs Screen is not opened"] = f"Failed: {e}"

 def click_store_tab(self):
     try:
         click_store_tab(self.wait)
         self.results["Store Tab is clicked"] = "Passed"
     except Exception as e:
         self.results["Store Tab is not clicked"] = f"Failed: {e}"

 def enter_store_name(self,value):
    try:
        enter_store_name(self.wait,value)
        self.results["Store_name is added in the text_field area"] = "Passed"
    except Exception as e:
         self.results["Store_name has not been added"] = f"Failed: {e}"
 def enter_owner_name(self,value):
    try:
        enter_owner_name(self.wait,value)
        self.results["Store_owner name is added in the text_field area"] = "Passed"
    except Exception as e:
         self.results["Store_ownwer name has not been added"] = f"Failed: {e}"
 def enter_address(self,value):
    try:
        enter_address(self.wait,value)
        self.results["Address is added in the text_field area"] = "Passed"
    except Exception as e:
         self.results["Address has not been added"] = f"Failed: {e}"
 def enter_geocode(self,value):
    try:
        enter_geocode(self.wait,value)
        self.results["Geo_code is added in the text_field area"] = "Passed"
    except Exception as e:
         self.results["Geo_code has not been added"] = f"Failed: {e}"
 def enter_opening_times(self,value):
    try:
        enter_opening_times(self.wait,value)
        self.results["Opening Times is added in the text_field area"] = "Passed"
    except Exception as e:
         self.results["Opening Times has not been added"] = f"Failed: {e}"

 def enter_comment(self,value):
    try:
        enter_comment(self.wait,value)
        self.results["comment is added in the text_field area"] = "Passed"
    except Exception as e:
         self.results["comment has not been added"] = f"Failed: {e}"

 def enter_telephone(self,value):
    try:
        enter_telephone(self.wait,value)
        self.results["telephone is added in the text_field area"] = "Passed"
    except Exception as e:
         self.results["telephone has not been added"] = f"Failed: {e}"

 def enter_fax(self,value):
    try:
        enter_fax(self.wait,value)
        self.results["fax is added in the text_field area"] = "Passed"
    except Exception as e:
         self.results["fax has not been added"] = f"Failed: {e}"

 def enter_email(self,value):
    try:
        enter_email(self.wait,value)
        self.results["email is added in the text_field area"] = "Passed"
    except Exception as e:
         self.results["email has not been added"] = f"Failed: {e}"
 def upload_image(self):
     try:
         upload_image(self.wait)
         self.results["Image is uploaded"] = "Passed"
     except Exception as e:
         self.results["Image is not uploaded"] = f"Failed: {e}"

 def click_mode_btn(self,option_value):
     try:
         click_mode_btn(self.wait, option_value)
         self.results["Maintenance Mode selected/ '0'= No & '1' = Yes"] = "Passed"
     except Exception as e:
         self.results["Maintenance Mode not selected"] = f"Failed: {e}"

 def click_save_btn(self):
     try:
         click_save_btn(self.wait)
         self.results["All the data on Store Tab is stored"] = "Passed"
     except Exception as e:
         self.results["All the data on the Store Tab is not stored"] = f"Failed: {e}"

 def write_to_excel(self, folder_name="excel_results", file_name="store_tab_result.xlsx"):
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

    def test_store_functions(self, setup):
        driver = setup
        store= Store_Page(driver)
        store.click_store_settings_tab()
        store.write_to_excel()
        store.click_store_tab()
        store.write_to_excel()
        store.enter_comment("High Quality Products")
        store.enter_opening_times("2:00 pm - 7: 00 pm Mon - Friday")
        store.upload_image()
        store.write_to_excel()
        store.enter_fax("1223FF5")
        store.write_to_excel()
        store.enter_telephone("1234567899866")
        store.write_to_excel()
        store.enter_email("Testuser_1@gmail.com")
        store.write_to_excel()
        store.enter_geocode("456123")
        store.write_to_excel()
        store.enter_address("Test house 98, stree 150")
        store.write_to_excel()
        store.enter_owner_name("Test User_01")
        store.write_to_excel()
        store.enter_store_name("Shopping Centre")
        store.write_to_excel()
        store.click_save_btn()
        store.write_to_excel()












        # store.click_save_btn()
        # store.write_to_excel()

        # store.scroll_up()

        #driver.execute_script("window.scrollTo(1000, 1500 );")
        #driver.execute_script("window.scrollTo(1500, 500 );")





