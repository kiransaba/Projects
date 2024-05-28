import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import Base_URL, USERNAME, PASSWORD, LOGIN_URL,login, click_watch_btn, click_close_btn,click_save_btn, navigate_to_settings, Driver_path,write_to_excel
from store_setting_helper import click_store_settings_tab, click_mail_tab,enter_mail,enter_reply_to
class Mail_Tab:
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
    def click_mail_tab(self):
        try:
            click_mail_tab(self.wait)
            self.results["Mail Tab is clicked"] = "Passed"
        except Exception as e:
            self.results["Mail Tab is not clicked"] = f"Failed: {e}"
    def enter_mail(self,value):
        try:
            enter_mail(self.wait,value)
            self.results["Mail is entered"] = "Passed"
        except Exception as e:
            self.results["Mail is not entered"] = f"Failed: {e}"
    def enter_reply_to(self,value):
        try:
            enter_reply_to(self.wait,value)
            self.results["Reply to is entered"] = "Passed"
        except Exception as e:
            self.results["Reply to is not entered"] = f"Failed: {e}"

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
        mail = Mail_Tab(driver)
        mail.click_store_settings_tab()
        mail.click_mail_tab()
        mail.write_to_excel()
        mail.enter_mail("sana@gmail.com")
        mail.write_to_excel()
        mail.enter_reply_to("Thankyou")
        mail.write_to_excel()
        mail.click_save_btn()
        mail.write_to_excel()











