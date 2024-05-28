from time import sleep
from selenium.webdriver import Keys
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from setting_constant import click_element,wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_MEDIUM

def click_oder_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-card-body'])[16]"))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Oder Status Tab is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Order Status Tab : {e}")
        traceback.print_exc()
        raise

def click_tab_back(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//a)[13]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Oder Statuses back button is clicked ")
    except Exception as e:
        print(f"An error occurred on clicking Order Statuses back button: {e}")
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
        click_checkbox = wait_for_element(wait, (By.XPATH, "(//input[@type='checkbox'])[6]"))
        sleep(WAIT_TIME_SHORT)
        click_checkbox.click()
        sleep(WAIT_TIME_SHORT)
        print("Checkbox button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking checkbox button: {e}")
        traceback.print_exc()
        raise

#######################  ADD_Methods
def enter_order_english_name(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[1]")))
        sleep(WAIT_TIME_SHORT)
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("English Order Status name is added")
    except Exception as e:
        print(f"Error in entering the English Order status name in the textfield: {e}")
        traceback.print_exc()
        raise
def enter_order_arabic_name(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[2]")))
        sleep(WAIT_TIME_SHORT)
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Arabic Order Status name is added")
    except Exception as e:
        print(f"Error in entering the Arabic Order Status name in the textfield: {e}")
        traceback.print_exc()
        raise

#######################Edit Stock

def edit_order_english_name(wait,input_value, value):
    try:
        xpath = f"//input[@value='{input_value}']"  # Corrected XPath string
        edit_name = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("English Order name is edited")
    except Exception as e:
        print(f"Error in editing the English Order name in the textfield: {e}")
        traceback.print_exc()
        raise

def edit_order_arabic_name(wait,input_value,value):
    try:
        xpath = f"//input[@value='{input_value}']"  # Corrected XPath string
        edit_name = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Arabic Order name is edited")
    except Exception as e:
        print(f"Error in edit the Arabic Order name in the textfield: {e}")
        traceback.print_exc()
        raise

def click_edit_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "//button[normalize-space()='Edit']"))
        click_edit.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Edit button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Edit button: {e}")
        traceback.print_exc()
        raise