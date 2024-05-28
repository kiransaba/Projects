#Xpaths & Element Ids are correct according to DOM structure/ Selecting Dynamic Xapths are not the right approach they mostly make the situation complex
#I am Providing Data Inputs on the Run time that is required for data Input testing testing.
import traceback
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from setting_constant import wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_MEDIUM

def click_length_classes_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-card-body'])[20]"))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Length_classes Tab is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Length_classes Tab : {e}")
        traceback.print_exc()
        raise

def click_tab_back(wait):
    try:
        click_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Length Classes']"))
        click_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Length_classes back button is clicked ")
    except Exception as e:
        print(f"An error occurred on clicking Length_classes back button: {e}")
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
def enter_length_name(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[1]")))
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Length Title is added")
    except Exception as e:
        print(f"Error in entering the Length Title in the textfield: {e}")
        traceback.print_exc()
        raise
def enter_length_arabic_name(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[2]")))
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Length Title is added in the Arabic")
    except Exception as e:
        print(f"Error in entering the Arabic Length Title in the textfield: {e}")
        traceback.print_exc()
        raise
def enter_length_unit(wait, value):
    try:
        add_unit = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[3]")))
        add_unit.clear()
        add_unit.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Length Unit is added")
    except Exception as e:
        print(f"Error in entering the Length Unit in the textfield: {e}")
        traceback.print_exc()
        raise
def enter_length_unit_arabic(wait, value):
    try:
        add_unit = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[4]")))
        add_unit.clear()
        add_unit.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Length Unit is added in the arabic field")
    except Exception as e:
        print(f"Error in entering the Length Unit in the arabic textfield: {e}")
        traceback.print_exc()
        raise
def enter_value(wait, value):
    try:
        add_value = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Value']")))
        add_value.clear()
        add_value.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Value is added")
    except Exception as e:
        print(f"Error in entering the Value in the textfield: {e}")
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

def edit_length_name(wait, value):
    try:
        edit_name = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[1]")))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Length Title is edited")
    except Exception as e:
        print(f"Error in editing the Length Title in the textfield: {e}")
        traceback.print_exc()
        raise

def edit_length_arabic_name(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[2]")))
        sleep(WAIT_TIME_SHORT)
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Length Title is edited in the Arabic")
    except Exception as e:
        print(f"Error in editing the Arabic Length Title in the textfield: {e}")
        traceback.print_exc()
        raise
def edit_length_unit(wait, value):
    try:
        edit_unit = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[3]")))
        sleep(WAIT_TIME_SHORT)
        edit_unit.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_unit.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Length Unit is edited")
    except Exception as e:
        print(f"Error in editing the Length Unit in the textfield: {e}")
        traceback.print_exc()
        raise
def edit_length_unit_arabic(wait, value):
    try:
        edit_unit = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[4]")))
        edit_unit.clear()
        sleep(WAIT_TIME_SHORT)
        edit_unit.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Length Unit is edited in the arabic field")
    except Exception as e:
        print(f"Error in editing the Length Unit in the arabic textfield: {e}")
        traceback.print_exc()
        raise
def edit_value(wait, value):
    try:
        edit_value = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Value']")))
        sleep(WAIT_TIME_SHORT)
        edit_value.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_value.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Value is edited")
    except Exception as e:
        print(f"Error in editing the Value in the textfield: {e}")
        traceback.print_exc()
        raise