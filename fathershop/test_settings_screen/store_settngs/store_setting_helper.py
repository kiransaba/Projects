#Xpaths & Element Ids are correct according to DOM structure/ Selecting Dynamic Xapths are not the right approach they mostly make the situation complex
#I am Providing Data Inputs on the Run time that is required for data Input testing testing.
import traceback
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from setting_constant import wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_MEDIUM
def click_store_settings_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-card-body'])[2]"))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Store page screen is opened successfully")
    except Exception as e:
        print(f"An error occurred on clicking Store setting Tab : {e}")
        traceback.print_exc()
        raise
def click_local_tab(wait):
    try:
        tab = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-tabs-tab-btn#rc-tabs-0-tab-3"))
        tab.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Local Tab Screen is opened successfully")
    except Exception as e:
        print(f"An error occurred clicking Local Tab: {e}")
        traceback.print_exc()
        raise

def click_option_tab(wait):
    try:
        tab = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-tabs-tab-btn#rc-tabs-0-tab-4"))
        tab.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Option Tab Screen is opened successfully")
    except Exception as e:
        print(f"An error occurred clicking Option Tab: {e}")
        traceback.print_exc()
        raise
def enter_title(wait,value):
    try:
         add_title= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Meta Title']")))
         add_title.send_keys(Keys.BACKSPACE * len(add_title.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_title.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Title is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering title in the text_field area: {e}")
        raise
def enter_description(wait,value):
    try:
         add_detail= wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Meta Tag Description']")))
         add_detail.send_keys(Keys.BACKSPACE * len(add_detail.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_detail.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Description is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering Description in the text_field area : {e}")
        traceback.print_exc()
        raise
def select_tag(wait, tag):
    try:
        # Click on the dropdown to make it visible
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-selection-overflow']")))
        dropdown.click()

        # Wait for the input field to be clickable and then send the tag
        input_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-controls='rc_select_1_list']")))
        input_field.send_keys(tag)
        input_field.send_keys(Keys.ENTER)  # Assuming that pressing Enter will select the tag
        sleep(WAIT_TIME_SHORT)
        print(f"Tag keywords dropdown button is clicked and {tag}  is added in the text field area")
    except Exception as e:
        print(f"Error occurred on entering Tag Keywords in the text field area: {e}")
        traceback.print_exc()
        raise


################################# Store Tab Methods ##################################
def click_store_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "//div[@id='rc-tabs-0-tab-2']"))
        tab.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Store Tab Screen is opened successfully")
    except Exception as e:
        print(f"An error occurred clicking Store Tab: {e}")
        traceback.print_exc()
        raise
def enter_store_name(wait,value):
    try:
         add_store_name= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Store Name']")))
         add_store_name.send_keys(Keys.BACKSPACE * len(add_store_name.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_store_name.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Store name is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering the Store Name in the text_field area : {e}")
        raise
def enter_owner_name(wait,value):
    try:
         add_owner_name= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Store Owner']")))
         add_owner_name.send_keys(Keys.BACKSPACE * len(add_owner_name.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_owner_name.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Store Owner is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering Store Owner in the text_field area : {e}")
        raise
def enter_address(wait,value):
    try:
         add_address= wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Address']")))
         add_address.send_keys(Keys.BACKSPACE * len(add_address.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_address.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Address is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering the Address in the text_field area : {e}")
        raise
def enter_geocode(wait,value):
    try:
         add_geocode= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Geocode']")))
         add_geocode.send_keys(Keys.BACKSPACE * len(add_geocode.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_geocode.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Geo code is  added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering Geocode in the text_field area : {e}")
        raise
def enter_email(wait,value):
    try:
         add_email= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='E-Mail']")))
         add_email.send_keys(Keys.BACKSPACE * len(add_email.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_email.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Email is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering the Email in the title text_field area : {e}")
        raise
def enter_telephone(wait,value):
    try:
         add_telephone= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Telephone']")))
         add_telephone.send_keys(Keys.BACKSPACE * len(add_telephone.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_telephone.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("first Telephone is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering the Telephone in the text_field area : {e}")
        raise
def enter_fax(wait,value):
    try:
         add_fax= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Fax']")))
         add_fax.send_keys(Keys.BACKSPACE * len(add_fax.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_fax.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Fax is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering Fax in the text_field area : {e}")
        raise
def enter_opening_times(wait,value):
    try:
         add_times= wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Opening Times']")))
         add_times.send_keys(Keys.BACKSPACE * len(add_times.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_times.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Opening Times is added in the text_field area")
    except Exception as e:
        print(f"Error occur entering the Opening Times in the text_field area : {e}")
        raise
def enter_comment(wait,value):
    try:
         comment= wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Comment']")))
         comment.send_keys(Keys.BACKSPACE * len(comment.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         comment.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Comment is added in the text_field area")
    except Exception as e:
        print(f"Error in entering the Comment in the text_field area : {e}")
        raise
def click_mode_btn(wait,mode_value):
    try:
        click_edit = wait_for_element(wait, (By.CSS_SELECTOR, f"select#config_maintenance > input[value='{mode_value}']"))
        click_edit.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Maintenance Modebutton is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Maintenance Mode button: {e}")
        raise
def upload_image(wait):
    try:
        cross_image_icon = wait_for_element(wait, (By.XPATH, "//a[@class='ui-clear']"))
        cross_image_icon.click()
        sleep(WAIT_TIME_SHORT)
        print("Image Cross Icon is clicked")
        click_image_icon = wait_for_element(wait, (By.XPATH, "//img[@alt='bg-image']"))
        click_image_icon.click()
        sleep(WAIT_TIME_SHORT)
        print("Image Icon is clicked")
        select_image = wait_for_element(wait, (By.XPATH, "//img[@alt='stripe-650x650.']"))
        select_image.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image is selected")
    except Exception as e:
        print(f"An error occurred on clicking Image Icon : {e}")
        traceback.print_exc()
        raise

########################################## Local Tab Methods

def click_country_dropdown(wait,title):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "//div[@fieldname='config_country_id']"))
        click_dropdown.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Country drop-down button is clicked successfully")
        select_country = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        select_country.click()
        sleep(WAIT_TIME_SHORT)
        print("Country is selected")
    except Exception as e:
        print(f"An error occurred on clicking Country drop-down button: {e}")
        traceback.print_exc()
        raise

def click_region_dropdown(wait,title):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "//div[@fieldname='config_zone_id']"))
        click_dropdown.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Region drop-down button is clicked successfully")
        select_country = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        select_country.click()
        sleep(WAIT_TIME_SHORT)
        print("Region is selected")
    except Exception as e:
        print(f"An error occurred on clicking Region drop-down button: {e}")
        traceback.print_exc()
        raise

def click_time_dropdown(wait, title):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "//div[@fieldname='config_timezone']"))
        click_dropdown.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Time drop-down button is clicked successfully")
        select_country = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        select_country.click()
        sleep(WAIT_TIME_SHORT)
        print("Time is selected")
    except Exception as e:
        print(f"An error occurred on clicking Time drop-down button: {e}")
        traceback.print_exc()
        raise
def click_language_dropdown(wait, title):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "//div[@fieldname='config_language']"))
        click_dropdown.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Language drop-down button is clicked successfully")
        select_country = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        select_country.click()
        sleep(WAIT_TIME_SHORT)
        print("Language is selected")
    except Exception as e:
        print(f"An error occurred on clicking Language drop-down button: {e}")
        traceback.print_exc()
        raise

def click_admin_language_dropdown(wait, title):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "//div[@fieldname='config_admin_language']"))
        click_dropdown.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Administration Language drop-down button is clicked successfully")
        select_country = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        select_country.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Administration Language is selected")
    except Exception as e:
        print(f"An error occurred on clicking Administration Language drop-down button: {e}")
        traceback.print_exc()
        raise
def click_currency_dropdown(wait, title):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "//div[@fieldname='config_currency']"))
        click_dropdown.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Currency drop-down button is clicked successfully")
        select_country = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        select_country.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Currency is selected")
    except Exception as e:
        print(f"An error occurred on clicking Currency drop-down button: {e}")
        traceback.print_exc()
        raise

def click_length_dropdown(wait, title):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "//div[@fieldname='config_length_class_id']"))
        click_dropdown.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Length Class drop-down button is clicked successfully")
        select_country = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        select_country.click()
        sleep(WAIT_TIME_SHORT)
        print("Length Class is selected")
    except Exception as e:
        print(f"An error occurred on clicking Length Class  drop-down button: {e}")
        traceback.print_exc()
        raise

def click_weight_dropdown(wait, title):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "//div[@fieldname='config_weight_class_id']"))
        click_dropdown.click()
        sleep(WAIT_TIME_MEDIUM)
        print(" Class drop-down button is clicked successfully")
        select_country = wait_for_element(wait, (By.XPATH, f"//div[@title='{title}']"))
        select_country.click()
        sleep(WAIT_TIME_SHORT)
        print("WeightClass is selected")
    except Exception as e:
        print(f"An error occurred on clicking Weight Class  drop-down button: {e}")
        traceback.print_exc()
        raise
########################################## Option Tab Methods
def enter_admin_items(wait,value):
    try:
         add_admin_items= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Default Items Per Page (Admin)']")))
         add_admin_items.send_keys(Keys.BACKSPACE * len(add_admin_items.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_admin_items.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Admin items count is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering Admin items count in the text_field area : {e}")
        raise
def enter_voucher_min(wait,value):
    try:
         add_min_voucher= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Voucher Min']")))
         add_min_voucher.send_keys(Keys.BACKSPACE * len(add_min_voucher.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_min_voucher.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Voucher Min is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering Voucher Min in the text_field area : {e}")
        raise

def enter_voucher_max(wait,value):
    try:
         add_max_voucher= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Voucher Max']")))
         add_max_voucher.send_keys(Keys.BACKSPACE * len(add_max_voucher.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_max_voucher.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Voucher Max is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering Voucher Max in the text_field area : {e}")
        raise

def enter_max_login(wait,value):
    try:
         add_login_attempts= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Max Login Attempts']")))
         add_login_attempts.send_keys(Keys.BACKSPACE * len(add_login_attempts.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_login_attempts.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Max Login Attempts is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering Max Login Attempts in the text_field area : {e}")
        raise

def enter_invoice_prefix(wait,value):
    try:
         add_invoice_prefix= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Invoice Prefix']")))
         add_invoice_prefix.send_keys(Keys.BACKSPACE * len(add_invoice_prefix.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_invoice_prefix.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Invoice Prefix is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering Invoice Prefix in the text_field area : {e}")
        raise


def processing_order_status(wait, status):
    try:
        # Click on the dropdown to make it visible
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@fieldname='config_processing_status']")))
        dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("Processing Order Status dropdown button is clicked")
        status_list = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@title='{status}']")))
        status_list.click()
        sleep(WAIT_TIME_SHORT)
        print(f"Status {status} is added")
    except Exception as e:
        print(f"Error occurred on adding Processing Order Status: {e}")
        traceback.print_exc()
        raise

def complete_order_status(wait, status):
    try:
        # Click on the dropdown to make it visible
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Complete Order Status']")))
        dropdown.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"Complete Order Status {status} is added")
        status_list = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//div[@title='{status}')")))
        status_list.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"Status {status} is added ")
    except Exception as e:
        print(f"Complete Error occurred on adding Order Status : {e}")
        traceback.print_exc()
        raise

def fraud_order_status(wait, status):
    try:
        # Click on the dropdown to make it visible
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@fieldname='config_fraud_status_id']")))
        dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("Fraud Order Status dropdown button is clicked")
        order_list = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@title='{status}']")))
        order_list.click()
        sleep(WAIT_TIME_SHORT)
        print(f"Status {status} is added")
    except Exception as e:
        print(f"Error occurred on Fraud Order Status: {e}")
        traceback.print_exc()
        raise

def api_user(wait, status):
    try:
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@fieldname='config_api_id']")))
        dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("API User dropdown button is clicked")
        # Wait for the input field to be clickable and then select the status
        order_list = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@title='{status}']")))
        order_list.click()
        sleep(WAIT_TIME_SHORT)
        print(f"API User {status} is added")
    except Exception as e:
        print(f"Error occurred on adding API User: {e}")
        traceback.print_exc()
        raise



########################################## Image Tab Methods
def click_image_tab(wait):
    try:
        tab = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-tabs-tab-btn#rc-tabs-0-tab-5"))
        tab.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image Tab Screen is opened successfully")
    except Exception as e:
        print(f"An error occurred clicking Image Tab: {e}")
        traceback.print_exc()
        raise


def image_image(wait):
    try:
        cross_image_icon = wait_for_element(wait, (By.XPATH, "//div[@class='flex flex-col form-container']//div[1]//div[1]//div[2]//div[1]//div[1]//a[1]"))
        cross_image_icon.click()
        sleep(WAIT_TIME_SHORT)
        print("Image Cross Icon is clicked")
        click_image_icon = wait_for_element(wait, (By.XPATH, "//i[@class='icon icon-camera']"))
        click_image_icon.click()
        sleep(WAIT_TIME_SHORT)
        print("Image Icon is clicked")
        select_image = wait_for_element(wait, (By.XPATH, "//img[@alt='questions-650x6']"))
        select_image.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image is selected")
    except Exception as e:
        print(f"An error occurred on clicking Image Icon : {e}")
        traceback.print_exc()
        raise

def image_icon(wait):
    try:
        cross_icon = wait_for_element(wait, (By.XPATH, "(//a[@class='ui-clear'])[2]"))
        cross_icon.click()
        sleep(WAIT_TIME_SHORT)
        print("Cross Icon is clicked")
        click_image_icon = wait_for_element(wait, (By.XPATH, "//div[@class='ui-image max-w-full w-full']"))
        click_image_icon.click()
        sleep(WAIT_TIME_SHORT)
        print("Image Icon is clicked")
        select_image = wait_for_element(wait, (By.XPATH, "//img[@alt='file_1.png']"))
        select_image.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image is selected")
    except Exception as e:
        print(f"An error occurred on clicking Icon-Image Icon : {e}")
        traceback.print_exc()
        raise

def image_placeholder(wait):
    try:
        cross_icon = wait_for_element(wait, (By.XPATH, "(//a[@class='ui-clear'])[3]"))
        cross_icon.click()
        sleep(WAIT_TIME_SHORT)
        print("Cross Icon is clicked")
        click_image = wait_for_element(wait, (By.XPATH, "//div[3]//div[1]//div[2]//div[1]//a[1]//i[1]"))

        click_image.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image Icon is clicked")
        select_image = wait_for_element(wait, (By.XPATH, "//img[@alt='questions-650x6']"))
        select_image.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image is selected")
    except Exception as e:
        print(f"An error occurred on clicking placeholder Image Icon : {e}")
        traceback.print_exc()
        raise

########################################## Mail Tab Methods

def click_mail_tab(wait):
    try:
        tab = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-tabs-tab-btn#rc-tabs-0-tab-6"))
        tab.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Mail Tab Screen is opened successfully")
    except Exception as e:
        print(f"An error occurred clicking Mail Tab: {e}")
        traceback.print_exc()
        raise

def enter_mail(wait,value):
    try:
         add_mail_parameter= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Mail Parameters']")))
         add_mail_parameter.send_keys(Keys.BACKSPACE * len(add_mail_parameter.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_mail_parameter.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Mail_parameter is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering the Mail_parameter in the text_field area : {e}")
        raise
def enter_reply_to(wait,value):
    try:
         add_reply= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Reply To']")))
         add_reply.send_keys(Keys.BACKSPACE * len(add_reply.get_attribute('value')))
         sleep(WAIT_TIME_SHORT)
         add_reply.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Reply to is added in the text_field area")
    except Exception as e:
        print(f"Error occurred on entering Reply to in the text_field area : {e}")
        raise