import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL,USERNAME,PASSWORD,LOGIN_URL,login,navigate_to_settings,write_to_excel, Driver_path,click_next_btn,click_addnew_btn
from currency_helper import click_currencies_tab,click_add_currency
class Add_Currency:
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
    def  click_currencies_tab(self):
        try:
            click_currencies_tab(self.wait)
            self.results["Currencies screen is opened"] = "Passed"
        except Exception as e:
            self.results["Currencies Tab is not clicked"] = f"Failed: {e}"


    def click_addnew_btn(self):
        try:
            click_addnew_btn(self.wait)
            self.results["Add New button is clicked"] = "Passed"
        except Exception as e:
            self.results["Add New button is not clicked"] = f"Failed: {e}"
    def click_add_currency(self,row_key):
        try:
            click_add_currency(self.wait,row_key)
            self.results["New currency is added"] = "Passed"
        except Exception as e:
            self.results["New cuurency is not added"] = f"Failed: {e}"

    def write_to_excel(self, folder_name="excel_results", file_name="add_currency_result.xlsx"):
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
        add_currency =  Add_Currency(driver)
        # add_currency.login()                                  #this commented part is requiired in the future as for now we are direcr redirecting to settings page
        # add_currency.write_to_excel()
        # add_currency.navigate_to_settings()
        # add_currency.write_to_excel()
        add_currency.click_currencies_tab()
        add_currency.write_to_excel()
        add_currency.click_addnew_btn()
        add_currency.write_to_excel()
        add_currency.click_add_currency("41")
        add_currency.write_to_excel()





