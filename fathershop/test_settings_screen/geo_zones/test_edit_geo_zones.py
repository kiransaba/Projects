import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,navigate_to_settings,click_save_btn,Driver_path,write_to_excel
from geo_helper import   click_geo_zones_tab,edit_geo_zones_name,edit_description,click_add_zones_btn,click_edit_btn,click_country_dropdown,select_country_name
class Edit_Geo_Zones:
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

 def click_geo_zones_tab(self):
     try:
         click_geo_zones_tab(self.wait)
         self.results["Geo Zones screen is opened"] = "Passed"
     except Exception as e:
         self.results["Geo Zones screen  is not closed"] = f"Failed: {e}"

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

 def edit_geo_zones_name(self,value):
    try:
        edit_geo_zones_name(self.wait,value)
        self.results["Geo Zones name  is edited in the English language"] = "Passed"
    except Exception as e:
         self.results["Geo Zones name is not edited in the English language"] = f"Failed: {e}"

 def edit_description(self,value):
     try:
         edit_description(self.wait, value)
         self.results[" Geo Zones descripton is edited in the Arabic language"] = "Passed"
     except Exception as e:
         self.results["Geo Zones descripton is not edited in the Arabic language"] = f"Failed: {e}"

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
         self.results["Country name is changed"] = "Passed"
     except Exception as e:
         self.results["Country name is not changed"] = f"Failed: {e}"


 def write_to_excel(self):
     write_to_excel(self.results, "excel_results","edit_geo_zones_results")

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
        #edit_zones.login()                        #this commented part is requiired in the future as for now we are direcr redirecting to settings page
        #edit_zones.write_to_excel()
        #edit_zones.navigate_to_settings()
        #edit_zones.write_to_excel()
        edit_zones = Edit_Geo_Zones(driver)
        edit_zones.click_geo_zones_tab()
        edit_zones.write_to_excel()
        edit_zones.click_edit_btn()
        edit_zones.write_to_excel()
        edit_zones.edit_geo_zones_name("Test Geo Zones")
        edit_zones.write_to_excel()
        edit_zones.edit_description("Testing Purpose")
        edit_zones.write_to_excel()
        edit_zones.click_country_dropdown()
        edit_zones.select_country_name("Albania")
        edit_zones.click_save_btn()
        edit_zones.write_to_excel()







