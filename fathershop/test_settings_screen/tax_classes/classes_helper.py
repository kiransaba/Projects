#Xpaths & Element Ids are correct according to DOM structure/ Selecting Dynamic Xapths are not the right approach they mostly make the situation complex
#I am Providing Data Inputs on the Run time that is required for data Input testing testing.
import traceback
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from setting_constant import wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_MEDIUM
def click_tax_classes_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-card-body'])[19]"))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Tax_classes Tab is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Tax_classes Tab : {e}")
        traceback.print_exc()
        raise

def click_tab_back(wait):
    try:
        click_tab = wait_for_element(wait, (By.XPATH, "(//a)[13]"))
        click_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Tax_classes back button is clicked ")
    except Exception as e:
        print(f"An error occurred on clicking Tax_classes back button: {e}")
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
def enter_class_name(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Tax Class Title']")))
        sleep(WAIT_TIME_SHORT)
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Tax_ Class Name is added")
    except Exception as e:
        print(f"Error in entering the Tax_Class name in the textfield: {e}")
        traceback.print_exc()
        raise
def enter_description(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Description']")))
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Tax description  is added")
    except Exception as e:
        print(f"Error in entering the tax description in the textfield: {e}")
        traceback.print_exc()
        raise
def click_default_btn(wait):
    try:
        click_default_btn = wait_for_element(wait, (By.XPATH, "(//button[@class='ant-btn css-1cjitus ant-btn-default text-white font-bold py-2 px-4 rounded btn btn-primary fathershops-button-primary'])[1]"))
        click_default_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Default button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Default  button: {e}")
        traceback.print_exc()
        raise
def select_tax_rate(wait):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-select-selector'])[2]"))
        sleep(WAIT_TIME_SHORT)
        click_dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("Tax rate Drop-down button is clicked")
    except Exception as e:
        print(f"Error occurred on clicking the Tax rate-dropdown: {e}")
        traceback.print_exc()
        raise
def rate_dropdown(wait,title):
    try:
        option = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        option.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"Tax Rate {title} is selected")

    except Exception as e:
        print(f"An error occurred on selecting the Tax Rate option: {e}")
        traceback.print_exc()
        raise
def select_shipping_address(wait):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-col ant-col-7 css-1cjitus'])[2]"))
        sleep(WAIT_TIME_SHORT)
        click_dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("Shipping Address Drop-down button is clicked")
    except Exception as e:
        print(f"Error occurred on clicking the Shipping Address-dropdown: {e}")
        traceback.print_exc()
        raise
def address_dropdown(wait,title):
    try:
        zone = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        zone.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"Shipping Address {title} is selected")
    except Exception as e:
        print(f"An error occurred on selecting Shipping Address option: {e}")
        traceback.print_exc()
        raise
def send_priority(wait,value):
    try:
        priority = wait_for_element(wait, (By.XPATH,"//input[@type='number']"))
        priority.send_keys(value)
        sleep(WAIT_TIME_MEDIUM)
        print(f"Priority {value} is added")
    except Exception as e:
        print(f"An error occurred on adding Priority value: {e}")
        traceback.print_exc()
        raise
#######################Edit Stock
def click_edit_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//span[contains(text(),'Edit')])[5]"))
        click_edit.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Edit button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Edit button: {e}")
        traceback.print_exc()
        raise
def edit_class_name(wait, value):
    try:
        edit_name = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Tax Class Title']")))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Tax_ Class Name is edit")
    except Exception as e:
        print(f"Error in editing the Tax_Class name in the textfield: {e}")
        traceback.print_exc()
        raise
def edit_description(wait, value):
    try:
        edit_name = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Description']")))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Tax description is edited")
    except Exception as e:
        print(f"Error in editing the tax description in the textfield: {e}")
        traceback.print_exc()
        raise