import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import  Base_URL, USERNAME, PASSWORD, LOGIN_URL,login, Driver_path,write_to_excel
from store_setting_helper import click_store_settings_tab,upload_image
from store_setting_helper import click_option_tab,enter_admin_items,enter_max_login,enter_voucher_min,enter_voucher_max,enter_invoice_prefix,processing_order_status,complete_order_status,fraud_order_status,\
api_user
class Option_Tab:
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
    def click_option_tab(self):
        try:
            click_option_tab(self.wait)
            self.results["Option Tab is clicked"] = "Passed"
        except Exception as e:
            self.results["Option Tab is not clicked"] = f"Failed: {e}"
    def enter_admin_items(self, value):
        try:
            enter_admin_items(self.wait, value)
            self.results["Admin Items Count is added in the text_field area"] = "Passed"
        except Exception as e:
            self.results["Admin Items Count is not added"] = f"Failed: {e}"

    def enter_voucher_min(self, value):
        try:
            enter_voucher_min(self.wait, value)
            self.results["Voucher Min is added in the text_field area"] = "Passed"
        except Exception as e:
            self.results["Voucher Min is not added"] = f"Failed: {e}"

    def enter_voucher_max(self, value):
        try:
            enter_voucher_max(self.wait, value)
            self.results["Voucher Max is added in the text_field area"] = "Passed"
        except Exception as e:
            self.results["Voucher Max is not added"] = f"Failed: {e}"


    def enter_max_login(self, value):
        try:
            enter_max_login(self.wait, value)
            self.results["Max Login Attempts is added in the text_field area"] = "Passed"
        except Exception as e:
            self.results["Max Login Attempts is not added"] = f"Failed: {e}"

    def enter_invoice_prefix(self, value):
        try:
            enter_invoice_prefix(self.wait, value)
            self.results["Invoice Prefix is added in the text_field area"] = "Passed"
        except Exception as e:
            self.results["Invoice Prefix is not added"] = f"Failed: {e}"

    def processing_order_status(self, status):
        try:
            processing_order_status(self.wait, status)
            self.results["Processing Order Status is added"] = "Passed"
        except Exception as e:
            self.results["Processing Order Status is not added"] = f"Failed: {e}"

    def fraud_order_status(self, status):
        try:
            fraud_order_status(self.wait, status)
            self.results["Fraud Order Status is added"] = "Passed"
        except Exception as e:
            self.results["Fraud Order Status is not added"] = f"Failed: {e}"

    def complete_order_status(self, status):
        try:
            complete_order_status(self, status)
            self.results["Fraud Order Status is added"] = "Passed"
        except Exception as e:
            self.results["Fraud Order Status is not added"] = f"Failed: {e}"


    def api_user(self, status):
        try:
            api_user(self, status)
            self.results["API User is added"] = "Passed"
        except Exception as e:
            self.results["API User is not added"] = f"Failed: {e}"

    def write_to_excel(self, folder_name="excel_results", file_name="option_tab_result.xlsx"):
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
        option = Option_Tab(driver)
        option.click_store_settings_tab()
        option.click_option_tab()
        option.write_to_excel()
        option.enter_admin_items("25")
        option.write_to_excel()
        option.enter_voucher_min("100")
        option.write_to_excel()
        option.enter_voucher_max("500")
        option.write_to_excel()
        option.processing_order_status("Denied")
        option.write_to_excel()
        option.enter_invoice_prefix("INV-2021-11")
        option.write_to_excel()
        option.complete_order_status("Chargeback")
        option.write_to_excel()
        option.fraud_order_status("Pending")
        option.write_to_excel()
