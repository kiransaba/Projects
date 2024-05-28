#This file contains login,driver path,Password,User name and settings pages public functions
import os
import traceback
from time import sleep
from openpyxl import Workbook
from openpyxl.styles import Alignment
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME_SHORT = 2
WAIT_TIME_MEDIUM = 5
WAIT_TIME_LONG = 10

USERNAME = 'ola'
PASSWORD = '1212'

Driver_path = '/Users/zain/Downloads/chromedriver'
Base_URL = 'https://test101.fathershops-test.xyz/admin/setting'
LOGIN_URL = 'https://test101.fathershops-test.xyz/admin'

def login(wait, username, password):
    ID = wait.until(EC.presence_of_element_located((By.ID, 'input-username')))
    ID.send_keys(username)
    sleep(WAIT_TIME_SHORT)
    print('Username entered')

    Password = wait.until(EC.presence_of_element_located((By.ID, 'input-password')))
    Password.send_keys(password)
    sleep(WAIT_TIME_SHORT)
    print('Password entered')

    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()
    sleep(WAIT_TIME_SHORT)
    print('Logged in successfully')

def navigate_to_settings(self):
    try:
        click_element(self.wait, (By.CSS_SELECTOR, ".menu-icon.brio-menu.rounded"))
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Clicked on the Collapased Tab successfully.")
        btn = wait_for_element(self.wait, (By.XPATH, "//li[@id='menu-system']//span[@class='menu-name']"))
        btn.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Setting Screen is opened successfully")
    except Exception as e:
        print(f"An error occurred on clickng Setting button: {e}")
        traceback.print_exc()
        raise

def click_tab_back(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//a)[13]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("from tab back button is clicked ")
    except Exception as e:
        print(f"An error occurred on clicking tab (back) button: {e}")
        traceback.print_exc()
        raise

def click_checkbox_select_all(wait):
    try:
        click_all = wait_for_element(wait, (By.XPATH, "//input[@aria-label='Select all']"))
        click_all.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Select all checkbox is clicked successfully")
        click_all.click()
        sleep(WAIT_TIME_SHORT)
        print("select all is un-selected")

    except Exception as e:
        print(f"An error occurred on clicking select all checkbox: {e}")
        traceback.print_exc()
        raise

def click_delete_btn(wait):
    try:
        delete_btn = wait_for_element(wait, (By.XPATH, "//span[@aria-label='delete']"))
        delete_btn.click()
        sleep(WAIT_TIME_SHORT)
        confirm_btn = wait_for_element(wait, (By.XPATH, "(//button[@class='ant-btn css-1cjitus ant-btn-default btn !rounded-md btnRoundedFull btnDanger btnInvert'])[1]"))
        confirm_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Selected User is deleted")
    except Exception as e:
        print(f"An error occurred on clicking Delete User button: {e}")
        traceback.print_exc()
        raise

def click_addnew_btn(wait):
    try:
        addnew_btn = wait_for_element(wait, (By.XPATH, "//span[normalize-space()='Add New']"))
        addnew_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Add New button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Add New button: {e}")
        traceback.print_exc()
        raise
def click_next_btn(wait):
    try:
        click_next = wait_for_element(wait, (By.XPATH, "(//span[@aria-label='right'])[1]"))
        sleep(WAIT_TIME_SHORT)
        click_next.click()
        sleep(WAIT_TIME_SHORT)
        print("Next button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Next button: {e}")
        traceback.print_exc()
        raise

def click_previous_btn(wait):
    try:
        click_previous = wait_for_element(wait, (By.XPATH, "//span[@aria-label='left']"))
        click_previous.click()
        sleep(WAIT_TIME_MEDIUM)
        print("previous button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking previous button: {e}")
        traceback.print_exc()
        raise

def click_save_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "//span[normalize-space()='Save']"))
        click_edit.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Save button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking save button: {e}")
        traceback.print_exc()
        raise

def click_cancel_btn(wait):
    try:
        click_cancel = wait_for_element(wait, (By.XPATH, "//a[@target='_self']//span[1]"))
        click_cancel.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Cancel button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Cancel button: {e}")
        traceback.print_exc()

        raise

def click_watch_btn(wait):
    try:
        watch_btn = wait_for_element(wait, (By.XPATH, "(//span)[33]"))
        watch_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Watch video button is clicked sucessfully")
    except Exception as e:
        print(f"An error occurred on clicking watch video button: {e}")
        traceback.print_exc()
        raise

def click_guide_btn(wait):
    try:
        guide_btn = wait_for_element(wait, (By.XPATH, "//div[@class='ant-collapse-expand-icon']"))
        guide_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Store Setting guide button is clicked sucessfully")
    except Exception as e:
        print(f"An error occurred on clicking Store Setting guide button: {e}")
        traceback.print_exc()
        raise
def click_close_btn(wait):
    try:
        close_btn = wait_for_element(wait, (By.XPATH, "//span[@aria-label='close']"))
        close_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("video cancel button is clicked sucessfully")
    except Exception as e:
        print(f"An error occurred on clicking cancel video button: {e}")
        traceback.print_exc()
        raise

def write_to_excel(results, folder_path="excel_reports", filename="results.xlsx"):
    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create the full file path
    file_path = os.path.join(folder_path, filename)

    # Write results to Excel
    wb = Workbook()
    sheet = wb.active
    sheet.title = "Test Results"
    sheet["A1"] = "Test Step"
    sheet["B1"] = "Result"
    sheet["A1"].alignment = Alignment(horizontal='center')
    sheet["B1"].alignment = Alignment(horizontal='center')

    row_index = 2
    for test_step, result in results.items():
        sheet[f"A{row_index}"] = test_step
        sheet[f"B{row_index}"] = result
        row_index += 1

    wb.save(file_path)

def click_element(wait, locator):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

def wait_for_element(wait, locator):
    element1 = wait.until(EC.presence_of_element_located(locator))
    return element1