#Xpaths & Element Ids are correct according to DOM structure/ Selecting Dynamic Xapths are not the right approach they mostly make the situation complex
#I am Providing Data Inputs on the Run time that is required for data Input testing testing.
import traceback
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from theme_constants import wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_MEDIUM
##################Click Button Methods###############
def click_user_group_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "//img[@src='/images/icons/usergroups.svg']"))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("User Group Tab is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking User Group Tab : {e}")
        traceback.print_exc()
        raise

def click_addnew_btn(wait):
    try:
        addnew_btn = wait_for_element(wait, (By.XPATH, "//span[@aria-label='plus']"))
        addnew_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Add New button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Add New button: {e}")
        traceback.print_exc()
        raise
def click_delete_btn(wait):
    try:
        delete_btn = wait_for_element(wait, (By.XPATH, "//span[@aria-label='delete']"))
        delete_btn.click()
        print("Delete button is clicked")
        sleep(WAIT_TIME_SHORT)
        confirm_delete = wait_for_element(wait, (By.XPATH, "//div[@class='ant-modal-content']//button[@class='ant-btn css-1cjitus ant-btn-default text-[#fff] rounded delete-btn bg-[#ED5149]']"))
        confirm_delete.click()
        sleep(WAIT_TIME_SHORT)
        print("Selected User is deleted")
    except Exception as e:
        print(f"An error occurred on clicking Delete User button: {e}")
        traceback.print_exc()
        raise

def click_edit_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//span[contains(text(),'Edit')])[3]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Edit button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking edit button: {e}")
        raise

def click_cancel_btn(wait):
    try:
        click_cancel = wait_for_element(wait, (By.XPATH, "//a[@target='_self']//span[1]"))
        click_cancel.click()
        sleep(WAIT_TIME_SHORT)
        print("Cancel button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Cancel button: {e}")
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


def click_checkbox_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//input[@type='checkbox'])[11]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Checkbox button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking checkbox button: {e}")
        traceback.print_exc()
        raise
######################## Add User Group Methods ###############
def enter_user_group_name(wait,value):
    try:
         add_user_group_name= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
         add_user_group_name.clear()
         add_user_group_name.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("User group name is added in the text_field area")
    except Exception as e:
        print(f"Error in entering the User group namein the text_field area : {e}")
        traceback.print_exc()
        raise

def add_access_permission(wait,option_value):
    try:
         click_permission_checkbox= wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@fieldname='access']")))
         click_permission_checkbox.click()
         sleep(WAIT_TIME_SHORT)
         print("Access Permision drop-down is clicked ")

         access_permission = wait_for_element(wait, (By.XPATH,  f"//div[@title='{option_value}']"))
         access_permission.click()
         sleep(WAIT_TIME_MEDIUM)
         print("Access Permision option is selected ")

         close = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@fieldname='access']")))
         close.click()
         sleep(WAIT_TIME_SHORT)
         print("Access Permision drop-down is closed ")

    except Exception as e:
        print(f"Error on clicking the Access Permision drop-down button  : {e}")
        traceback.print_exc()
        raise
def modify_permission(wait, option_value1):
    try:
         click_modify_checkbox= wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@fieldname='modify']")))
         click_modify_checkbox.click()
         sleep(WAIT_TIME_MEDIUM)
         print("Modify Permision drop-down is clicked ")
         select_permission = wait_for_element((wait, (By.XPATH,  f"//div[@title='{option_value1}']")))
         sleep(WAIT_TIME_SHORT)
         select_permission.click()
         print("Modify Permision option is selected ")

    except Exception as e:
        print(f"Error on clicking the Modify Permision drop-down button: {e}")
        traceback.print_exc()
        raise
###########################  Edit User_group Screen Methods #############################
def edit_access_permission(wait, option_value):
    try:
        click_permission_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@fieldname='access']")))
        click_permission_checkbox.click()
        sleep(WAIT_TIME_SHORT)
        print("Access Permision drop-down is clicked ")
        access_permission = wait_for_element(wait, (By.XPATH, f"//div[@title='{option_value}']"))
        access_permission.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Access Permision option is edited ")
        close = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@fieldname='access']")))
        close.click()
        sleep(WAIT_TIME_SHORT)
        print("Access Permision drop-down is closed ")
    except Exception as e:
        print(f"Error on editing the Access Permision drop-down button  : {e}")
        traceback.print_exc()
        raise
def edit_user_group_name(wait,value):
        try:
            edit_user_group_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
            sleep(WAIT_TIME_SHORT)
            edit_user_group_name.send_keys(Keys.BACKSPACE * len(value))
            edit_user_group_name.send_keys(value)
            sleep(WAIT_TIME_SHORT)
            print("User group name is edited in the text_field area")
        except Exception as e:
            print(f"Error on editing the User group name in  the text_field area : {e}")
            traceback.print_exc()
            raise


