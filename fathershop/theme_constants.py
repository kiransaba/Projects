#This File for Journal theme pages public functions don't relate it with setting pages

from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from setting_constant import WAIT_TIME_SHORT,WAIT_TIME_MEDIUM,WAIT_TIME_LONG,wait_for_element

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def check_cache_btn(wait):
    try:
        cache = wait_for_element(wait, (By.CSS_SELECTOR, ".icon.icon-restore"))
        cache.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Cache is clicked & saved")

    except StaleElementReferenceException:
        print("Element is stale, trying to locate again...")
        wait.check_cache_btn()
    except Exception as e:
        print(f"Error clicking on clicking cache button: {e}")
        raise
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def no_element_dropdown(wait):
    try:
        no_of_element = wait_for_element(wait, (By.CSS_SELECTOR, "span[title='10']"))
        no_of_element.click()
        sleep(WAIT_TIME_MEDIUM)
        print("No.Of_Elements drop_down list is clicked & showing")

        list = wait_for_element(wait, (By.XPATH, "//div[@title='20']"))
        list.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Selected No.Of_Elements Result is showing")
    except Exception as e:
        print(f"Error in No.of_Elements method: {e}")
        raise
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def filter_search(wait, search_term):
    try:
        # Find the filter input field and enter the search term
        filter_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Filter...']")))
        filter_input.send_keys(search_term)
        # Wait for the search results to appear
        search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='variable-name']")))
        print("Desired Search result is found")
        sleep(WAIT_TIME_MEDIUM)
    except TimeoutException as te:
        print(f"TimeoutException in filter_search method: {te}")
        raise
    except Exception as e:
        print(f"Error in filter_search method: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def duplicate(wait):
    try:
        duplicate_btn = wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='list-icon'])[2]")))
        duplicate_btn.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Duplicate button is clicked")
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        sleep(WAIT_TIME_MEDIUM)
        print("Selected Style is duplicated")
    except Exception as e:
        print(f"Error occurred on clicking the duplicate button: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def delete(wait):
    try:
        delete_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='module-items']//div[1]//div[1]//a[3]//*[name()='svg']")))
        delete_btn.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Delete button is clicked")

        # Switch to the alert dialog
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        sleep(WAIT_TIME_MEDIUM)
        print("Selected Style is deleted")
    except Exception as e:
        print(f"Error occurred on clicking the delete button: {e}")
        raise


#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def create_new_btn(wait):
    try:
        create_new = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='icon icon-add']")))
        create_new.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Create New button is clicked")
        #assert create_new.is_enabled(), "Create New Footer button is not enabled after clicking"
    except Exception as e:
        print(f"Error occured on clicking the create_new button: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def edit(wait):
    try:
        edit_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "list-icon")))
        edit_btn.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Edit button is clicked")
        #assert edit_btn.is_enabled(), "Edit button is not enabled after clicking"
    except TimeoutException:
        print("Timed out waiting for the Edit button to be clickable.")
    except Exception as e:
        print(f"Error in Edit method: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def color(wait):
    try:
        select_color = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-color-picker-color-block-inner")))
        select_color.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Color menu is opened")

        color = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-color-picker-color-block-inner' and contains(@style, 'background: rgb(245, 34, 45);')]")))
        color.click()  # Added parentheses to actually call the click method
        sleep(WAIT_TIME_SHORT)
        print("Color is selected")

        close_color = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-color-picker-color-block-inner")))
        close_color.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Color is closed")
    except Exception as e:
        print(f"Error occurred in color method: {e}")
        raise
#—————————————————————————————————————————————————————————————————————————————
def edit_color(self):
    try:
        color_picker = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-color-picker-color-block-inner")))
        color_picker.click()
        sleep(WAIT_TIME_MEDIUM)

        color_option = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='ant-color-picker-color-block-inner' and contains(@style, 'background: rgb(19, 168, 168);')]")))
        color_option.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Color is edited")
    except Exception as e:
        print(f"Error occurred in color edit method: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def gradient(wait):
    try:

        gradient = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".gradient-preview")))
        gradient.click()
        sleep(WAIT_TIME_MEDIUM)
        preview = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='gradient-preview'])[5]")))
        preview.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Gradient preview screen is opened")
        gra = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "gradient-preview")))
        gra.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Gradient is de-selected")
    except Exception as e:
        print(f"Error occurred in gradient method: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def camera(wait):
    try:
        select_color = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".bg-image")))
        select_color.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Camera Icon is clicked")

        select_image = wait.until(EC.element_to_be_clickable((By.XPATH,"//img[@alt='administrator-6']"  )))
        select_image.click()
        sleep(WAIT_TIME_SHORT)
        print("Image is selected")

    except Exception as e:
        print(f"An error occurred on clicking the camera: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def image_options(wait):
    try:
        image_options = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@type='primary']")))
        image_options.click()
        sleep(WAIT_TIME_SHORT)
        print("Image Options menu is opened")
    except Exception as e:
        print(f"An error occurred on clicking Image Option: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def save(wait):
    try:
        save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span)[34]")))
        save_btn.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Save button is clicked & data is saved")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def add_breakpoint_btn(wait):
    try:
        add_breakpoint = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@type='primary'])[3]")))
        add_breakpoint.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Add breakpoint button is clicked")
    except Exception as e:
        print(f"Error in breakpoint method: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

def click_back_btn(wait):
    try:
        back_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='icon icon-arrow_back'])[1]")))
        back_btn.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Back button is clicked")
    except Exception as e:
        print(f"Error occurred in Clicking Back button method: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————
def reset_btn(self):
    try:
        reset = self.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon.icon-close.reset-field")))
        ActionChains(self.driver).move_to_element(reset).perform()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Mouse hovered over reset button")
        reset.click()
        sleep(WAIT_TIME_SHORT)
        print("Reset button is clicked successfully")
    except Exception as e:
        print(f"An error occurred on clicking Reset button: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def edit_gradient(wait):
    try:
        gradient_edit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".gradient-preview")))
        gradient_edit.click()
        sleep(3)
        preview_edit = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='gradient-preview'])[7]")))
        preview_edit.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Gradient preview screen is opened")
        gra = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "gradient-preview")))
        gra.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Gradient is de-selected")
    except Exception as e:
        print(f"Error occurred in edit gradient method: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def edit_camera(wait):
    try:
        camera = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bg-image")))
        camera.click()
        sleep(WAIT_TIME_MEDIUM)
        preview = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='istockphoto-139']")))
        preview.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image is selected")
    except Exception as e:
        print(f"An error occurred on the camera edit: {e}")
        raise
#—————————————————————————————————————————————————————————————————————————————————
def click_hovertab(wait):
    try:
        hover_tab = wait.until(EC.element_to_be_clickable((By.XPATH,"(//li[contains(text(),'Hover')])[1]")))
        hover_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Hover Tab is clicked")
    except Exception as e:
        print(f"An error occurred on clicking Hover Tab: {e}")
        raise
#############################################################################

