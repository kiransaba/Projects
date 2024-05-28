#Xpaths & Element Ids are correct according to DOM structure/ Selecting Dynamic Xapths are not the right approach they mostly make the situation complex
#I am Providing Data Inputs on the Run time that is required for data Input testing testing.
import traceback
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from setting_constant import wait_for_element,WAIT_TIME_SHORT,WAIT_TIME_MEDIUM
##################Click Button Methods###############
def click_currencies_tab(wait):
    try:
        tab = wait_for_element(wait, (By.XPATH, "(//div[@class='ant-card-body'])[14]")) # xpath is right csn't make it dynamic
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Currencies Tab is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Currencies Tab : {e}")
        traceback.print_exc()
        raise

def click_tab_back(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//a[normalize-space()='Currencies'])[1]"))
        click_edit.click()
        sleep(WAIT_TIME_SHORT)
        print("Currencies back button is clicked ")
    except Exception as e:
        print(f"An error occurred on clicking Currencies back button: {e}")
        traceback.print_exc()
        raise

def click_delete_btn(wait):
    try:
        delete_btn = wait_for_element(wait, (By.XPATH, "//div[2]//button[2]//span[2]"))
        delete_btn.click()
        sleep(WAIT_TIME_SHORT)
        confirm_btn = wait_for_element(wait, (By.XPATH, "(//button[@class='ant-btn css-1cjitus ant-btn-default btn !rounded-md btnRoundedFull btnDanger btnInvert'])[1]"))
        confirm_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Selected Currency is deleted")
    except Exception as e:
        print(f"An error occurred on clicking Delete Currency button: {e}")
        traceback.print_exc()
        raise


def currency_set_default_btn(self, country_name):
    try:
        # Locate the element containing the country name
        default_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(),'{country_name}')]")))

        # Hover over the located element
        ActionChains(self.driver).move_to_element(default_btn).perform()
        print(f"{country_name} is hovered")
        sleep(WAIT_TIME_MEDIUM)

        # Locate the default button after hovering
        click_default_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@class='ant-table-cell ant-table-cell-row-hover']//span[@class='ml-2']")) )

        # Click the default button
        click_default_btn.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"{country_name} Set Default button is clicked")
    except Exception as e:
        print(f"Error occurred while clicking on {country_name} Set Default Button: {e}")
        traceback.print_exc()
        raise


def click_status_toggle(wait, status):
    try:
        # Find all switch elements based on their class name
        switch_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ant-switch")))

        for switch_element in switch_elements:
            # Get the current status of the switch
            current_status = switch_element.get_attribute("aria-checked")
            # Check if the current status matches the desired status
            if (current_status == "true" and status == "enabled") or (
                    current_status == "false" and status == "disabled"):
                print(f"Switch is already {status}. No action needed.")
                continue
            # Click the switch to change its status
            switch_element.click()
            # Optionally, add a short sleep to allow for the UI to update
            sleep(WAIT_TIME_SHORT)
            # Verify if the status has been changed successfully
            new_status = switch_element.get_attribute("aria-checked")
            new_status = "enabled" if new_status == "true" else "disabled"
            print(f"Switch status changed to {new_status}.")
    except Exception as e:
        print(f"An error occurred while toggling the switch status: {e}")
        traceback.print_exc()
        raise

#######################  ADD_Currency
def select_currency_checkbox(wait,checkbox_id):
    try:
        click_currency = wait_for_element(wait, (By.XPATH, f"//input[@name='{checkbox_id}']"))
        click_currency.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Currency checkbox is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking on currency checkbox: {e}")
        traceback.print_exc()
        raise


def click_add_currency(wait, row_key):
    try:
        # Find the row by data-row-key attribute
        row = wait.until(
            EC.presence_of_element_located((By.XPATH, f"//tr[@data-row-key='{row_key}']"))
        )
        print(f"Currency={row_key} found")

        # Find the Add button within the row
        add_button = row.find_element(By.XPATH, ".//button[contains(@class, 'ant-btn') and contains(@class, 'btnPrimary')]")

        # Click the Add button
        add_button.click()
        sleep(WAIT_TIME_MEDIUM)  # Use time.sleep correctly
        print("New Currency is added successfully")
    except Exception as e:
        print(f"An error occurred while clicking the Add button for row key {row_key}: {e}")
        traceback.print_exc()
        raise

def click_cross_btn(wait):
    try:
        click_cancel = wait_for_element(wait, (By.XPATH, "//span[@aria-label='close']"))
        click_cancel.click()
        sleep(WAIT_TIME_SHORT)
        print("Add currency scrren  is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Cross button : {e}")
        traceback.print_exc()
        raise
def click_currency_cancel(wait):
    try:
        click_cancel = wait_for_element(wait, (By.XPATH, "(//span[@class='ant-btn-icon'])[18]"))
        click_cancel.click()
        sleep(WAIT_TIME_SHORT)
        print("Add Currency:Cancel button is clicked  successfully")
    except Exception as e:
        print(f"An error occurred on clicking Cancel button(Add Currency Screen): {e}")
        traceback.print_exc()
        raise

#######################Edit Currency
def click_edit_btn(wait):
    try:
        click_edit = wait_for_element(wait, (By.XPATH, "(//a[@target='_self'])[2]"))
        click_edit.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Edit button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Edit button: {e}")
        traceback.print_exc()
        raise
def edit_currency_symbol(wait, value):
    try:
        edit_symbol = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Currency Symbol']")))
        sleep(WAIT_TIME_SHORT)
        edit_symbol.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_symbol.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Currency Symbol is edited")
    except Exception as e:
        print(f"Error in editing the Currency Symbol in the textfield: {e}")
        traceback.print_exc()
        raise

def edit_decimal_value(wait, value):
    try:
        edit_decimal = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Decimal Places']")))
        sleep(WAIT_TIME_SHORT)
        edit_decimal.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_decimal.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Decimal places value is edited")
    except Exception as e:
        print(f"Error in editing the Decimal places value in the textfield: {e}")
        traceback.print_exc()
        raise

def hover_help_icon(self):
    try:
         hover_icon= self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon.icon-question.info-field.mx-1.hint-info")))
         ActionChains(self.driver).move_to_element(hover_icon).perform()
         sleep(WAIT_TIME_SHORT)
         hover_icon.click()
         sleep(WAIT_TIME_SHORT)
         print("Currency_value Help Icon name is hovered")
    except Exception as e:
        print(f"Error occurred on hovering over Currency_value help Icon: {e}")
        traceback.print_exc()
        raise

def edit_value(wait, value):
    try:
        edit_value = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Value']")))
        sleep(WAIT_TIME_SHORT)
        edit_value.send_keys(Keys.BACKSPACE * len(value))
        sleep(WAIT_TIME_SHORT)
        edit_value.send_keys(value)
        sleep(WAIT_TIME_SHORT)
        print("Currency value is edited")
    except Exception as e:
        print(f"Error in editing the Currency value in the textfield: {e}")
        traceback.print_exc()
        raise

def symbol_position(wait, position):
    try:
        click_dropdown = wait_for_element(wait, (By.XPATH, "//div[@fieldname='position']"))
        click_dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("Symbol Position drop-down button is clicked")
        option = wait_for_element(wait, (By.XPATH, f"//div[@title='{position}']"))
        option.click()
        sleep(WAIT_TIME_MEDIUM)
        print(f"Symbol Position {position} is selected")
    except Exception as e:
        print(f"An error occurred on clicking the Position Symbol dropdown : {e}")
        traceback.print_exc()
        raise

def status_radio_btn(wait):
    try:

        click_radio = wait_for_element(wait, (By.XPATH, "//label[@class='is-checked']"))
        click_radio.click()
        sleep(WAIT_TIME_SHORT)
        print(f"Status radio button is clicked")
    except Exception as e:
        print(f"An error occurred on clicking the Status Radio button : {e}")
        traceback.print_exc()
        raise