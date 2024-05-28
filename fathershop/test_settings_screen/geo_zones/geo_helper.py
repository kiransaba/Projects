#Xpaths & Element Ids are correct according to DOM structure/ Selecting Dynamic Xapths are not the right approach they mostly make the situation complex
#I am Providing Data Inputs on the Run time that is required for data Input testing.
import traceback
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from setting_constant import wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_MEDIUM
def click_geo_zones_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-card-body'])[17]"))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Geo_zones Tab is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Geo_zones Tab : {e}")
        traceback.print_exc()
        raise
def click_tab_back(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Geo Zones']"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Geo Zones back button is clicked ")
    except Exception as e:
        print(f"An error occurred on clicking Geo Zones back button: {e}")
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

def click_checkbox_btn(wait):
    try:
        click_checkbox = wait_for_element(wait, (By.XPATH, "(//input[@type='checkbox'])[5]"))
        sleep(WAIT_TIME_SHORT)
        click_checkbox.click()
        sleep(WAIT_TIME_SHORT)
        print("Checkbox button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking checkbox button: {e}")
        traceback.print_exc()
        raise
#######################  ADD_Methods
def enter_geo_zones_name(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Geo Zone Name']")))
        sleep(WAIT_TIME_SHORT)
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Geo Zones name is added")
    except Exception as e:
        print(f"Error in entering the Geo Zones name in the textfield: {e}")
        traceback.print_exc()
        raise
def enter_description(wait, value):
    try:
        add_name = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Description']")))
        add_name.clear()
        sleep(WAIT_TIME_SHORT)
        add_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Geo Zones description is added")
    except Exception as e:
        print(f"Error in entering the Geo Zones description in the textfield: {e}")
        traceback.print_exc()
        raise
def click_add_zones_btn(wait):
    try:
        click_zones_btn = wait_for_element(wait, (By.CSS_SELECTOR, "button.fathershops-button-primary svg[stroke='currentColor']"))
        sleep(WAIT_TIME_SHORT)
        click_zones_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Add Geo Zones button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking geo-zones button: {e}")
        traceback.print_exc()
        raise
def click_country_dropdown(wait):
    try:
        #click_dropdown = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-col ant-col-12 css-1cjitus'])[3]"))
        click_dropdown = wait_for_element(wait, (By.CSS_SELECTOR, "div.ant-select[fieldname='zone_to_geo_zones[0].country_id']"))

        sleep(WAIT_TIME_SHORT)
        click_dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("Country Drop-down button is clicked")
    except Exception as e:
        print(f"Error occurred on clicking the country from dropdown: {e}")
        traceback.print_exc()
        raise


def select_country_name(wait, country_name):
    try:

        css_selector = f"div.ant-select-item[title='{country_name}']"
        country_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        country_element.click()
        sleep(WAIT_TIME_SHORT)
        print(f"Country '{country_name}' is selected successfully")
    except Exception as e:
        print(f"Error occurred on selecting the country '{country_name}' from the list: {e}")
        traceback.print_exc()
        raise
#######################Edit Stock
def click_edit_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//button[@type='button'])[8]"))
        click_edit.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Edit button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Edit button: {e}")
        traceback.print_exc()
        raise
def edit_geo_zones_name(wait, value):
    try:
        edit_name = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Geo Zone Name']")))

        edit_name.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_name.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Geo Zones name is edited")
    except Exception as e:
        print(f"Error in editing the Geo Zones name in the textfield: {e}")
        traceback.print_exc()
        raise
def edit_description(wait,value):
    try:
        edit_descrip = wait_for_element(wait,((By.XPATH, "//input[@placeholder='Description']")))
        sleep(WAIT_TIME_SHORT)
        edit_descrip.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_descrip.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Geo Zones description is edited")
    except Exception as e:
        print(f"Error in editng the Geo Zones description in the textfield: {e}")
        traceback.print_exc()
        raise

