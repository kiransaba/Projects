import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL,USERNAME,PASSWORD,LOGIN_URL, Driver_path,login,click_close_btn,navigate_to_settings,click_save_btn,write_to_excel,click_cancel_btn,\
click_next_btn,click_previous_btn,click_addnew_btn
from currency_helper import click_currencies_tab,click_tab_back,select_currency_checkbox,currency_set_default_btn,click_status_toggle,click_cross_btn,click_currency_cancel,click_delete_btn
class Currency:
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
    def currency_set_default_btn(self,country_name):
        try:
            currency_set_default_btn(self,country_name)
            self.results[f"{country_name} set default button is clicked"] = "Passed"
        except Exception as e:
            self.results[f"{country_name} set default button button is not clicked"] = f"Failed: {e}"

    def click_status_toggle(self,status):
        try:
            click_status_toggle(self.wait,status)
            self.results["Currency Status toggle button is clicked"] = "Passed"
        except Exception as e:
            self.results["Currency Status toggle button is not clicked"] = f"Failed: {e}"

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

    def click_close_btn(self):
        try:
            click_close_btn(self.wait)
            self.results["Close Video button is clicked"] = "Passed"
        except Exception as e:
            self.results["Close Video button is not clicked"] = f"Failed: {e}"

    def select_currency_checkbox(self,currency_name):
        try:
            select_currency_checkbox(self.wait,currency_name)
            self.results["Cuurency Checkbox button is clicked"] = "Passed"
        except Exception as e:
            self.results["Currency Checkbox button is not clicked"] = f"Failed: {e}"

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

    def click_tab_back(self):
        try:
            click_tab_back(self.wait)
            self.results["Currency (back) button is clicked"] = "Passed"
        except Exception as e:
            self.results["Currency (back) button is not clicked"] = f"Failed: {e}"

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
    def click_currency_cancel(self):
        try:
            click_currency_cancel(self.wait)
            self.results["Add Currency Cancel button is clicked"] = "Passed"
        except Exception as e:
            self.results["Add Currency Cancel button is not clicked"] = f"Failed: {e}"
    def click_cross_btn(self):
        try:
            click_cross_btn(self.wait)
            self.results["Cross button is clicked"] = "Passed"
        except Exception as e:
            self.results["Cross button is not clicked"] = f"Failed: {e}"

    def write_to_excel(self, folder_name="excel_results", file_name="currency_screen_result.xlsx"):
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
        currency = Currency(driver)
        # currency.login()                                     #this commented part is requiired in the future as for now we are direcr redirecting to settings page
        # currency.write_to_excel()
        # currency.navigate_to_settings()
        # currency.write_to_excel()
        currency.click_currencies_tab()
        currency.write_to_excel()
        currency.click_addnew_btn()
        currency.write_to_excel()
        currency.click_cross_btn()
        currency.write_to_excel()
        currency.click_addnew_btn()
        currency.write_to_excel()
        currency.click_currency_cancel()
        currency.write_to_excel()
        currency.click_status_toggle("disabled")
        currency.write_to_excel()
        currency.click_status_toggle("enabled")
        currency.write_to_excel()
        currency.currency_set_default_btn("Bahraini Dinar")
        currency.write_to_excel()
        currency.click_next_btn()
        currency.write_to_excel()
        currency.click_previous_btn()
        currency.write_to_excel()
        currency.select_currency_checkbox("id_55")
        currency.click_delete_btn()
        currency.write_to_excel()







