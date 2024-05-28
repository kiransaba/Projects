#Xpaths & Element Ids are correct according to DOM structure/ Selecting Dynamic Xapths are not the right approach they mostly make the situation complex
#I am Providing Data Inputs on the Run time that is required for data Input testing testing.
import traceback
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from setting_constant import wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_MEDIUM
def click_tax_rate_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-card-body'])[18]"))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Tax_rates Tab is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Tax_rates Tab : {e}")
        traceback.print_exc()
        raise

def click_tab_back(wait):
    try:
        click_tab = wait_for_element(wait, (By.XPATH, "(//a)[13]"))
        click_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Tax_rates back button is clicked ")
    except Exception as e:
        print(f"An error occurred on clicking Tax_rates back button: {e}")
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

def click_checkbox_btn(wait):
    try:
        click_checkbox = wait_for_element(wait, (By.XPATH, "(//input[@type='checkbox'])[3]"))
        sleep(WAIT_TIME_SHORT)
        click_checkbox.click()
        sleep(WAIT_TIME_SHORT)
        print("Checkbox button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking checkbox button: {e}")
        traceback.print_exc()
        raise

#######################  ADD_Methods
def enter_tax_name(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Tax Name']")))
        sleep(WAIT_TIME_SHORT)
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Tax Name is added")
    except Exception as e:
        print(f"Error in entering the Tax name in the textfield: {e}")
        traceback.print_exc()
        raise
def enter_tax_rate(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Tax Rate']")))
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Tax rate  is added")
    except Exception as e:
        print(f"Error in entering the tax rate in the textfield: {e}")
        traceback.print_exc()
        raise
def click_default_btn(wait):
    try:
        click_default_btn = wait_for_element(wait, (By.XPATH, "//div[@class='ui-checkbox']//span//label"))
        click_default_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Default button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Default  button: {e}")
        traceback.print_exc()
        raise
def select_type(wait):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-select-selector'])[2]"))
        sleep(WAIT_TIME_SHORT)
        click_dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("Type Drop-down button is clicked")
    except Exception as e:
        print(f"Error occurred on clicking the Type-dropdown: {e}")
        traceback.print_exc()
        raise
def type_dropdown(wait,title):
    try:
        option = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        option.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"Type {title} is selected")
    except Exception as e:
        print(f"An error occurred on selecting the Type option: {e}")
        traceback.print_exc()
        raise
def select_geo_zone(wait):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-select-selector'])[3]"))
        sleep(WAIT_TIME_SHORT)
        click_dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("Geo Zone Drop-down button is clicked")
    except Exception as e:
        print(f"Error occurred on clicking the Geo Zone-dropdown: {e}")
        traceback.print_exc()
        raise
def zone_dropdown(wait,title):
    try:
        zone = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        zone.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"Geo Zone {title} is selected")
    except Exception as e:
        print(f"An error occurred on selecting Geo Zone option: {e}")
        traceback.print_exc()
        raise
#######################Edit Stock
def click_edit_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//span[contains(text(),'Edit')])[2]"))
        click_edit.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Edit button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Edit button: {e}")
        traceback.print_exc()
        raise
def edit_tax_name(wait, value):
    try:
        edit_name = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Tax Name']")))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(Keys.BACKSPACE * len(edit_name.get_attribute('value')))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Tax Name is edited")
    except Exception as e:
        print(f"Error in editing the Tax name in the textfield: {e}")
        traceback.print_exc()
        raise
def edit_tax_rate(wait, value):
    try:
        edit_rate = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Tax Rate']")))
        sleep(WAIT_TIME_SHORT)
        edit_rate.send_keys(Keys.BACKSPACE * len(edit_rate.get_attribute('value')))
        sleep(WAIT_TIME_SHORT)
        edit_rate.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Tax rate  is edited")
    except Exception as e:
        print(f"Error in editing the tax rate in the textfield: {e}")
        traceback.print_exc()
        raise