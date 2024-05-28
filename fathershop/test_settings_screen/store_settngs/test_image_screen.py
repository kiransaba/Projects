import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login,click_save_btn, Driver_path,write_to_excel
from store_setting_helper import click_store_settings_tab, click_image_tab,image_image,image_icon,image_placeholder
class Image_Tab:
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
    def click_image_tab(self):
        try:
            click_image_tab(self.wait)
            self.results["Image Tab is clicked"] = "Passed"
        except Exception as e:
            self.results["Image Tab is not clicked"] = f"Failed: {e}"
    def image_image(self):
        try:
            image_image(self.wait)
            self.results["Image is uploaded"] = "Passed"
        except Exception as e:
            self.results["Image is not uploaded"] = f"Failed: {e}"
    def image_icon(self):
        try:
            image_icon(self.wait)
            self.results["Image Icon is uploaded"] = "Passed"
        except Exception as e:
            self.results["Image Icon is not uploaded"] = f"Failed: {e}"
    def image_placeholder(self):
        try:
            image_placeholder(self.wait)
            self.results["Image placeholder Icon is uploaded"] = "Passed"
        except Exception as e:
            self.results["Image placeholder Icon is not uploaded"] = f"Failed: {e}"

    def click_save_btn(self):
        try:
            click_save_btn(self.wait)
            self.results["All the data on Store Tab is stored"] = "Passed"
        except Exception as e:
            self.results["All the data on the Store Tab is not stored"] = f"Failed: {e}"

    def write_to_excel(self, folder_name="excel_results", file_name="image_tab_result.xlsx"):
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
        image = Image_Tab(driver)
        image.click_store_settings_tab()
        image.click_image_tab()
        image.write_to_excel()
        image.image_image()
        image.write_to_excel()
        image.image_icon()
        image.write_to_excel()
        image.image_placeholder()
        image.write_to_excel()
        image.click_save_btn()
        image.write_to_excel()










