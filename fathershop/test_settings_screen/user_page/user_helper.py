#Xpaths & Element Ids are correct according to DOM structure/ Selecting Dynamic Xapths are not the right approach they mostly make the situation complex
#I am Providing Data Inputs on the Run time that is required for data Input testing testing.
import traceback
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from setting_constant import wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_MEDIUM
##################Click Button Methods###############
def click_user_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-card-body'])[6]"))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("User Screen is opened successfully")
    except Exception as e:
        print(f"An error occurred on clicking User Tab : {e}")
        traceback.print_exc()
        raise
def click_edit_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//span[contains(text(),'Edit')])[5]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Edit button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking edit button: {e}")
        traceback.print_exc()
        raise

def click_checkbox_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//input[@type='checkbox'])[6]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Checkbox button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking checkbox button: {e}")
        traceback.print_exc()
        raise


def add_user_group(wait):
    try:
         click_dopdown= wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='input-user-group']")))
         click_dopdown.click()
         sleep(WAIT_TIME_SHORT)
         print("User group drop-down button is clicked ")

         select_group = wait.until(EC.element_to_be_clickable((By.XPATH,"//select[@id='input-user-group'], ")))
         select_group.click()
         sleep(WAIT_TIME_SHORT)
         print("User group drop-down button is clicked ")

    except Exception as e:
        print(f"Error on clicking the user_group drop=down button : {e}")
        traceback.print_exc()
        raise
######################## Enter Data Methods ###############
def enter_first_name(wait,value):
    try:
         add_first_name= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='First Name']")))
         add_first_name.clear()
         add_first_name.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("first name is added in the text_field area")
    except Exception as e:
        print(f"Error in entering the First_name in the text_field area : {e}")
        traceback.print_exc()
        raise
def enter_last_name(wait,value):
    try:
         add_last_name= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Last Name']")))
         add_last_name.clear()
         add_last_name.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("last is added in the text_field area")
    except Exception as e:
        print(f"Error in entering Last_name in the text_field area : {e}")
        traceback.print_exc()
        raise
def enter_email(wait,value):
    try:
         add_email= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='E-Mail']")))

         add_email.clear()
         add_email.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Email is added in the text_field area")
    except Exception as e:
        print(f"Error in entering the Email in the title text_field area : {e}")
        traceback.print_exc()
        raise
def enter_password(wait,value):
    try:
         add_password= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']")))
         sleep(WAIT_TIME_SHORT)
         add_password.clear()
         sleep(WAIT_TIME_SHORT)
         add_password.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Password is added in the text_field area")
    except Exception as e:
        print(f"Error in entering the Password in the title text_field area : {e}")
        traceback.print_exc()
        raise
def enter_confirm_password(wait,value):
    try:
         add_confirm= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Confirm']")))
         sleep(WAIT_TIME_SHORT)
         add_confirm.clear()
         sleep(WAIT_TIME_SHORT)
         add_confirm.send_keys(value)

         print("Password is added in the text_field area")
    except Exception as e:
        print(f"Error in entering the Password in the title text_field area : {e}")
        traceback.print_exc()
        raise
def upload_image(wait):
    try:
        click_image_icon = wait_for_element(wait, (By.XPATH, "//i[@class='icon icon-camera']"))
        click_image_icon.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image Icon is clicked")
        select_image = wait_for_element(wait, (By.XPATH, "//img[@alt='deep-data-serve']"))
        select_image.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image is selected")
    except Exception as e:
        print(f"An error occurred on clicking Image Icon : {e}")
        traceback.print_exc()
        raise
def user_group_dropdown(wait, option_value):
    try:

        dropdown_selector = wait_for_element(wait,  (By.XPATH, "(//div[@class='ant-space css-1cjitus ant-space-vertical ant-space-gap-row-small ant-space-gap-col-small'])[2]"))
        dropdown_selector.click()
        sleep(WAIT_TIME_MEDIUM)
        print("User Group dropdown button is clicked")
        # Click the desired option
        option = wait_for_element(wait, (By.CSS_SELECTOR, f".ant-select-item[title='{option_value}']"))
        option.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"User Group {option_value} is selected")
    except Exception as e:
        print(f"An error occurred on clicking the User Group dropdown : {e}")
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
###########################  Edit User Screen Methods #############################
def edit_first_name(wait,value1):
    try:
         edit_first_name= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='First Name']")))
         sleep(WAIT_TIME_SHORT)
         edit_first_name.send_keys(Keys.BACKSPACE * len(value1))
         sleep(WAIT_TIME_SHORT)
         edit_first_name.send_keys(value1)
         sleep(WAIT_TIME_MEDIUM)
         print("first name is edited")
    except Exception as e:
        print(f"Error editing the first_name : {e}")
        traceback.print_exc()
        raise
def edit_last_name(wait,value2):
    try:
         edit_last_name= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Last Name']")))
         sleep(WAIT_TIME_SHORT)
         edit_last_name.send_keys(Keys.BACKSPACE * len(value2))
         sleep(WAIT_TIME_SHORT)
         edit_last_name.send_keys(value2)
         sleep(WAIT_TIME_MEDIUM)
         print("last name is edited")
    except Exception as e:
        print(f"Error in editing the last_name : {e}")
        traceback.print_exc()
        raise
def edit_email(wait,value3):
    try:
         edit_email= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']")))
         sleep(WAIT_TIME_SHORT)
         edit_email.send_keys(Keys.BACKSPACE * len(value3))
         sleep(WAIT_TIME_SHORT)
         edit_email.send_keys(value3)
         sleep(WAIT_TIME_SHORT)
         print("Email is edited ")
    except Exception as e:
        print(f"Error in editing the Email : {e}")
        traceback.print_exc()
        raise
def edit_password(wait,value4):
    try:
         edit_password= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']")))
         sleep(WAIT_TIME_SHORT)
         edit_password.send_keys(Keys.BACKSPACE * len(value4))
         sleep(WAIT_TIME_SHORT)
         edit_password.send_keys(value4)
         sleep(WAIT_TIME_SHORT)
         print("Password is added in the text_field area")
    except Exception as e:
        print(f"Error in entering the Password in the title text_field area : {e}")
        traceback.print_exc()
        raise
def edit_confirm_password(wait,value5):
    try:
         edit_confirm= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Confirm']")))
         sleep(WAIT_TIME_SHORT)
         edit_confirm.send_keys(Keys.BACKSPACE * len(value5))
         sleep(WAIT_TIME_SHORT)
         edit_confirm.send_keys(value5)
         sleep(WAIT_TIME_SHORT)
         print("Confirm Password is edited")
    except Exception as e:
        print(f"Error on editing the confirm password : {e}")
        traceback.print_exc()
        raise
def edit_image(wait):
    try:
        click_image_icon1 = wait_for_element(wait, (By.XPATH, "//img[@alt='bg-image']"))
        click_image_icon1.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image Icon is clicked")

        edit_image = wait_for_element(wait, (By.XPATH, "//img[@alt='feedback.png']"))
        edit_image.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image is edited")
    except Exception as e:
        print(f"An error occurred on the editing Image: {e}")
        traceback.print_exc()
        raise

#-----------------
def edit_user_group(wait, option_value):
    try:
        dropdown_selector = wait_for_element(wait, (By.XPATH,  "(//div[@class='ant-space css-1cjitus ant-space-vertical ant-space-gap-row-small ant-space-gap-col-small'])[2]"))
        dropdown_selector.click()
        sleep(WAIT_TIME_MEDIUM)
        print("User Group dropdown button is clicked")
        # Click the desired option
        option = wait_for_element(wait, (By.CSS_SELECTOR, f".ant-select-item[title='{option_value}']"))
        option.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"User Group {option_value} is edited")
    except Exception as e:
        print(f"An error occurred while editing the User-Group: {e}")
        traceback.print_exc()
        raise
def edit_status(wait, status_value):
    try:
        status = wait_for_element(wait, (By.XPATH, "//div[@fieldname='status']"))
        status.click()
        sleep(WAIT_TIME_SHORT)
        print("Status drop-down button is clicked")
        option = wait_for_element(wait, (By.XPATH, f"//div[@title='{status_value}']"))
        option.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"Status {status_value} is edited")
    except Exception as e:
        print(f"An error occurred while editing the status: {e}")
        traceback.print_exc()
        raise




