#Xpaths & Element Ids are correct according to DOM structure/ Selecting Dynamic Xapths are not the right approach they mostly make the situation complex
#I am Providing Data Inputs on the Run time that is required for data Input testing testing.
from time import sleep
import traceback
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from setting_constant import wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_MEDIUM
##################Click Button Methods###############
def click_stock_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-card-body'])[15]"))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Stock Status Tab is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Stock Status Tab : {e}")
        traceback.print_exc()
        raise

def click_delete_btn(wait):
    try:
        delete_btn =wait_for_element(wait,(By.XPATH, "//div[2]//button[2]//span[2]"))
        delete_btn.click()
        sleep(WAIT_TIME_SHORT)
        #alert = wait.until(EC.alert_is_present())
        #alert.accept()
        confirm_btn = wait_for_element(wait, (By.XPATH, "(//button[@class='ant-btn css-1cjitus ant-btn-default btn !rounded-md btnRoundedFull btnDanger btnInvert'])[1]"))
        confirm_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Selected Stock Status is deleted")
    except Exception as e:
        print(f"An error occurred on clicking the Delete  button: {e}")
        traceback.print_exc()
        raise

def click_tab_back(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Stock Statuses']"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Stock Statuses back button is clicked ")
    except Exception as e:
        print(f"An error occurred on clicking Stock Statuses back button: {e}")
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
        click_checkbox = wait_for_element(wait, (By.XPATH, "(//input[@type='checkbox'])[7]"))
        sleep(WAIT_TIME_SHORT)
        click_checkbox.click()
        sleep(WAIT_TIME_SHORT)
        print("Checkbox button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking checkbox button: {e}")
        traceback.print_exc()
        raise

def click_video_btn(wait):
    try:
        watch_btn = wait_for_element(wait, (By.XPATH, "//span[@class='ant-btn-icon']//parent::button[@type='button']"))
        watch_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Stock Status: Watch video button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking watch video button in the Stock Status screen: {e}")
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

#######################  ADD_Currency
def enter_stock_english_name(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[1]")))
        sleep(WAIT_TIME_SHORT)
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("English Stock name is added")
    except Exception as e:
        print(f"Error in entering the English stock name in the textfield: {e}")
        traceback.print_exc()
        raise

def enter_stock_arabic_name(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "(//input[@class='w-full'])[2]")))
        sleep(WAIT_TIME_SHORT)
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Arabic Stock name is added")
    except Exception as e:
        print(f"Error in entering the Arabic stock name in the textfield: {e}")
        traceback.print_exc()
        raise
#######################Edit Method
def edit_stock_english_name(wait,input_value, value):
    try:
        xpath = f"//input[@value='{input_value}']"  # Corrected XPath string
        edit_name = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        sleep(WAIT_TIME_SHORT)
        edit_name.clear()
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("English Stock name is edited")
    except Exception as e:
        print(f"Error in editing the English stock name in the textfield: {e}")
        traceback.print_exc()
        raise

def edit_stock_arabic_name(wait,input_value,value):
    try:
        xpath = f"//input[@value='{input_value}']"  # Corrected XPath string
        edit_name = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Arabic Stock name is edited")
    except Exception as e:
        print(f"Error in edit the Arabic stock name in the textfield: {e}")
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

