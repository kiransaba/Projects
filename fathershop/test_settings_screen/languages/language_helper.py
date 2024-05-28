from time import sleep
import traceback
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from setting_constant import click_element,wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_LONG,WAIT_TIME_MEDIUM

##################Click Button Methods###############
def click_store_language_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-card-body'])[13]"))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Store Language Tab is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Store Language Tab : {e}")
        traceback.print_exc()
        raise

def click_edit_english(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//a[@target='_self'])[1]"))
        sleep(WAIT_TIME_SHORT)
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("English Language Edit button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking the English Language edit button: {e}")
        traceback.print_exc()
        raise

def click_edit_arabic(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//a[@target='_self'])[2]"))
        sleep(WAIT_TIME_SHORT)
        click_edit.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Arabic Language Edit button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking the Arabic edit button: {e}")
        traceback.print_exc()
        raise


def click_status_english(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-switch-handle'])[1]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("English language status button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking English language status button: {e}")
        traceback.print_exc()
        raise

def click_status_arabic(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-switch-handle'])[2]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Arabic language status button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Arabic language status button: {e}")
        traceback.print_exc()
        raise

def click_tab_back(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//a)[13]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Language back button is clicked ")
    except Exception as e:
        print(f"An error occurred on clicking Language back button: {e}")
        traceback.print_exc()
        raise

def click_language_cancel(wait):
    try:
        click_cancel = wait_for_element(wait, (By.XPATH, "(//span[@class='ant-btn-icon'])[9]"))
        click_cancel.click()
        sleep(WAIT_TIME_SHORT)
        print("Cancel button is clicked on langauge preview screen successfully")
    except Exception as e:
        print(f"An error occurred on clicking Cancel button on the langauge preview screen: {e}")
        traceback.print_exc()
        raise

def click_cross_btn(wait):
    try:
        click_cancel = wait_for_element(wait, (By.XPATH, "//span[@aria-label='close']"))
        click_cancel.click()
        sleep(WAIT_TIME_SHORT)
        print("Close Icon is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Close Icon: {e}")
        traceback.print_exc()
        raise

def click_checkbox_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//input[@type='checkbox'])[3]"))
        click_edit.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Checkbox button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking checkbox button: {e}")
        traceback.print_exc()
        raise

#######################Input Data


def enter_sort_order(wait, value):
    try:
        add_sort_order = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Sort Order']")))
        sleep(WAIT_TIME_SHORT)
        add_sort_order.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)

        add_sort_order1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Sort Order']")))
        add_sort_order1.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Sort Order value is added")
    except Exception as e:
        print(f"Error in entering the Sort order value in the textfield: {e}")
        traceback.print_exc()
        raise

def hover_help_icon(self):
    try:
         hover_icon= self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='icon icon-question info-field mx-1 hint-info'])[2]")))
         ActionChains(self.driver).move_to_element(hover_icon).perform()
         sleep(WAIT_TIME_SHORT)
         hover_icon.click()
         sleep(WAIT_TIME_SHORT)
         print("Status Help Icon name is hovered")
    except Exception as e:
        print(f"Error occurred on hovering over Status help Icon: {e}")
        traceback.print_exc()
        raise



def english_set_default_btn(self):
    try:

         default_btn= self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'English')]")))
         ActionChains(self.driver).move_to_element(default_btn).perform()
         print("English Set Default button is hovered")
         sleep(WAIT_TIME_MEDIUM)


         click_default_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span)[52]")))
         click_default_btn.click()
         sleep(WAIT_TIME_SHORT)
         print("English Set Default button is clicked")
    except Exception as e:

         print(f"Error occurred on hovering over Set Default Button: {e}")
         traceback.print_exc()
         raise

def arabic_set_default_btn(self):
    try:

         default_btn= self.wait.until(EC.element_to_be_clickable((By.XPATH, " // span[contains(text(), 'عربي')]")))
         ActionChains(self.driver).move_to_element(default_btn).perform()
         print("Arabic Set Default button is hovered")
         sleep(WAIT_TIME_MEDIUM)


         click_default_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span)[63]")))
         click_default_btn.click()
         sleep(WAIT_TIME_SHORT)
         print("Arabic Set Default button is clicked")
    except Exception as e:

         print(f"Error occurred on hovering over Set Default Button: {e}")
         traceback.print_exc()
         raise

def status_dropdown(wait, status_value):
    try:
        status = wait_for_element(wait, (By.XPATH, "//div[@fieldname='status']"))
        status.click()
        sleep(WAIT_TIME_SHORT)
        print("Status drop-down button is clicked")

        option = wait_for_element(wait, (By.XPATH, f"//div[@title='{status_value}']"))

        option.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"Status {status_value} is selected")

    except Exception as e:
        print(f"An error occurred on clicking the status dropdown : {e}")
        traceback.print_exc()
        raise
