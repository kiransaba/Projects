import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL,USERNAME,PASSWORD,LOGIN_URL,login,navigate_to_settings,click_save_btn,write_to_excel, Driver_path, click_cancel_btn,click_addnew_btn
from language_helper import click_store_language_tab,click_checkbox_btn,click_tab_back,click_cross_btn,click_language_cancel,click_status_arabic,click_status_english,click_edit_english,click_edit_arabic,\
    arabic_set_default_btn,english_set_default_btn
class Test_Language:
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

    def click_store_language_tab(self):
        try:
            click_store_language_tab(self.wait)
            self.results["Store Language screen is opened"] = "Passed"
        except Exception as e:
            self.results["Store Language Tab is not clicked"] = f"Failed: {e}"

    def click_cross_btn(self):
        try:
            click_cross_btn(self.wait)
            self.results["Cross button is clicked on language Preview screen"] = "Passed"
        except Exception as e:
            self.results["Cross button is not clicked language Preview screen"] = f"Failed: {e}"

    def click_language_cancel(self):
        try:
            click_language_cancel(self.wait)
            self.results["language_cancel button is clicked on language Preview screen"] = "Passed"
        except Exception as e:
            self.results["language_cancel button is not clicked on language Preview screen"] = f"Failed: {e}"

    def click_status_english(self):
        try:
            click_status_english(self.wait)
            self.results["English Language Status toggle button is clicked"] = "Passed"
        except Exception as e:
            self.results[" English LanguageStatus toggle button is not clicked"] = f"Failed: {e}"

    def click_status_arabic(self):
        try:
            click_status_arabic(self.wait)
            self.results["Arabic Language Status toggle button is clicked"] = "Passed"
        except Exception as e:
            self.results[" Arabic LanguageStatus toggle button is not clicked"] = f"Failed: {e}"

    def click_checkbox_btn(self):
        try:
            click_checkbox_btn(self.wait)
            self.results["Checkbox button is clicked"] = "Passed"
        except Exception as e:
            self.results["Checkbox button is not clicked"] = f"Failed: {e}"
    def english_set_default_btn(self):
        try:
            english_set_default_btn(self)
            self.results["English Set default button is hovered & clicked"] = "Passed"
        except Exception as e:
            self.results["English Set default button is not hovered & clicked"] = f"Failed: {e}"
    def arabic_set_default_btn(self):
        try:
            arabic_set_default_btn(self)
            self.results["Arabic Set default button is hovered & clicked"] = "Passed"
        except Exception as e:
            self.results["Arabiic Set default button is not hovered & clicked"] = f"Failed: {e}"

    def click_addnew_btn(self):
        try:
            click_addnew_btn(self.wait)
            self.results["Add New button is clicked"] = "Passed"
        except Exception as e:
            self.results["Add New button is not clicked"] = f"Failed: {e}"
    def click_edit_english(self):
        try:
            click_edit_english(self.wait)
            self.results["English Language Edit button is clicked"] = "Passed"
        except Exception as e:
            self.results["English Language Edit button is not clicked"] = f"Failed: {e}"
    def click_edit_arabic(self):
        try:
            click_edit_arabic(self.wait)
            self.results["Arabic Language Edit button is clicked"] = "Passed"
        except Exception as e:
            self.results["Arabic  Language Edit button is not clicked"] = f"Failed: {e}"

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

    def write_to_excel(self, folder_name="excel_results", file_name="test_language_results.xlsx"):
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
        login(login_wait, USERNAME, PASSWORD)
        # Change URL to Base_URL after logging in
        driver.get(Base_URL)
        yield driver
        driver.quit()

    def test_user_functions(self, setup):
        driver = setup

        language = Test_Language(driver)
        # language.login()
        # language.write_to_excel()
        # language.navigate_to_settings()
        # language.write_to_excel()
        language.click_store_language_tab()
        language.write_to_excel()
        language.arabic_set_default_btn()
        language.write_to_excel()
        language.english_set_default_btn()
        language.write_to_excel()
        language.click_addnew_btn()
        language.write_to_excel()
        language.click_language_cancel()
        language.write_to_excel()
        language.click_addnew_btn()
        language.write_to_excel()
        language.click_cross_btn()
        language.write_to_excel()
        language.click_edit_english()
        language.write_to_excel()
        language.click_tab_back()
        language.write_to_excel()
        language.click_edit_arabic()
        language.write_to_excel()
        language.click_cancel_btn()
        language.write_to_excel()
        language.click_status_arabic()
        language.click_checkbox_btn()
        language.write_to_excel()






