#Xpaths & Element Ids are correct according to DOM structure/ Selecting Dynamic Xapths are not the right approach they mostly make the situation complex
#I am Providing Data Inputs on the Run time that is required for data Input testing testing.
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from setting_constant import wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_LONG,WAIT_TIME_MEDIUM

##################Click Button Methods###############
def click_return_action_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-card-body'])[10]"))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Return Action Tab is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Return Action Tab : {e}")
        raise

def click_edit_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//span[contains(text(),'Edit')])[1]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Edit button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking edit button: {e}")
        raise

def click_tab_back(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//a[normalize-space()='Return Actions'])[1]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("from  back button is clicked ")
    except Exception as e:
        print(f"An error occurred on clicking back button: {e}")
        raise

def click_checkbox_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//input[@type='checkbox'])[7]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Checkbox button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking checkbox button: {e}")
        raise
#######################Input Data
def enter_return_action_name(wait,value):
    try:
         add_action_name= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='w-full'])[1]")))
         add_action_name.clear()
         add_action_name.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Return Action name is added in the English")
    except Exception as e:
        print(f"Error in entering the Return Action name in English Language: {e}")
        raise

def enter_return_action_name1(wait,value):
    try:
         add_action_name= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='w-full'])[2]")))
         sleep(WAIT_TIME_SHORT)
         add_action_name.send_keys(Keys.BACKSPACE * len(value))
         sleep(WAIT_TIME_SHORT)
         add_action_name.send_keys(value)
         print("Return Action name is added in the Arabic")
    except Exception as e:
        print(f"Error in entering the Return Action name in Arabic Language: {e}")
        raise

###########################  Edit User_group Screen Methods #############################
def edit_return_action_name(wait,value):
    try:
         add_return_name= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='w-full'])[1]")))
         sleep(WAIT_TIME_SHORT)
         add_return_name.send_keys(Keys.BACKSPACE * len(value))
         sleep(WAIT_TIME_SHORT)
         add_return_name.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Return Action name is edited in the English")
    except Exception as e:
        print(f"Error occurred on editing the Return Action name in English Language: {e}")
        raise
def edit_return_action_name1(wait,value):
    try:
         add_action_name= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='w-full'])[2]")))
         sleep(WAIT_TIME_SHORT)
         add_action_name.send_keys(Keys.BACKSPACE * len(value))
         sleep(WAIT_TIME_SHORT)
         add_action_name.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Return Action name is added in the Arabic")
    except Exception as e:
        print(f"Error occurred on editing the Return Action name in Arabic Language: {e}")
        raise
