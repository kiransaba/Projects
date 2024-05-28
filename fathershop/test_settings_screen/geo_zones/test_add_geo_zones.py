import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel,click_cancel_btn,\
click_addnew_btn
from geo_helper import   click_geo_zones_tab,enter_geo_zones_name,enter_description,click_add_zones_btn,select_country_name,click_country_dropdown
class Add_Geo_Zones:
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

 def click_geo_zones_tab(self):
     try:
         click_geo_zones_tab(self.wait)
         self.results["Geo Zones screen is opened"] = "Passed"
     except Exception as e:
         self.results["Geo Zones screen  is not closed"] = f"Failed: {e}"

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

 def enter_geo_zones_name(self,value):
    try:
        enter_geo_zones_name(self.wait,value)
        self.results["Geo Zones name name is added in the English language"] = "Passed"
    except Exception as e:
         self.results["Geo Zones name is not added in the English language"] = f"Failed: {e}"

 def enter_description(self, value):
     try:
         enter_description(self.wait, value)
         self.results[" Geo Zones descripton is added in the Arabic language"] = "Passed"
     except Exception as e:
         self.results["Geo Zones descripton is not added in the Arabic language"] = f"Failed: {e}"
 def click_add_zones_btn(self):
     try:
         click_add_zones_btn(self.wait)
         self.results["Add Country Zones button is clicked"] = "Passed"
     except Exception as e:
         self.results["Add Country Zones button is not clicked"] = f"Failed: {e}"
 def click_country_dropdown(self):
     try:
         click_country_dropdown(self.wait)
         self.results["Country drop-down button is clicked"] = "Passed"
     except Exception as e:
         self.results["Country drop-down button is not clicked"] = f"Failed: {e}"
 def select_country_name(self,country_name):
     try:
         select_country_name(self.wait,country_name)
         self.results["Country is selected"] = "Passed"
     except Exception as e:
         self.results["Country is not selected"] = f"Failed: {e}"

 def write_to_excel(self):
     write_to_excel(self.results, "excel_results","add_geo_zones_results")


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
        #add_zones.login()               #this commented part is requiired in the future as for now we are direcr redirecting to settings page
        #add_zones.write_to_excel()
        #add_zones.navigate_to_settings()
        #add_zones.write_to_excel()
        add_zones = Add_Geo_Zones(driver)
        add_zones.click_geo_zones_tab()
        add_zones.write_to_excel()
        add_zones.click_addnew_btn()
        add_zones.write_to_excel()
        add_zones.enter_geo_zones_name("Test Geo")
        add_zones.write_to_excel()
        add_zones.enter_description("Testing zones")
        add_zones.write_to_excel()
        add_zones.click_add_zones_btn()
        add_zones.write_to_excel()
        add_zones.click_country_dropdown()
        add_zones.select_country_name("Andorra")
        add_zones.click_save_btn()
        add_zones.write_to_excel()







