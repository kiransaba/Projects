# variable_helpers.py
import logging
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from setting_constant import WAIT_TIME_MEDIUM, WAIT_TIME_SHORT,wait_for_element,click_element
def navigate_to_variable_screen(self):
    try:
        logging.info("Navigating to the Variable screen...")
        click_element(self.wait, (By.CSS_SELECTOR, ".menu-icon.brio-menu.rounded"))
        sleep(WAIT_TIME_MEDIUM)  # Using imported constant
        logging.info("Clicked on the Variable screen Tab successfully.")

        # Directly mouse hover over the "Theme" tab using a relative CSS selector
        theme_tab = wait_for_element(self.wait, (By.XPATH, "//li[@id='journal3-theme']//span[@class='menu-name']"))

        # Mouse hover over the "Theme" tab
        ActionChains(self.driver).move_to_element(theme_tab).perform()
        sleep(WAIT_TIME_MEDIUM)  # Using imported constant
        logging.info("Mouse hovered over the 'Theme' tab")

        # Click on the "Theme" tab
        theme_tab.click()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        logging.info("Theme tab clicked successfully")

        # Hover over the "styles_tab" element
        variables_tab = wait_for_element(self.wait, (By.XPATH, "//li[@id='journal3-theme']//li[2]//a[1]"))
        ActionChains(self.driver).move_to_element(variables_tab).perform()
        sleep(WAIT_TIME_MEDIUM)  # Using imported constant
        logging.info("Mouse hovered over 'Variables_tab'")

        # Click on the "styles_tab"
        variables_tab.click()
        sleep(WAIT_TIME_MEDIUM)  # Using imported constant
        logging.info("Variables_tab clicked successfully")

    except Exception as e:
        # Catch any other exceptions that may occur
        print(f"An error occurred on  navgatng to Varable screen: {e}")
        raise
#-----------------------------------------------------------------------------------------------------------------------
def new_breakpoint(wait, variable_name ):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Breakpoint']"))
        enter_name.clear()
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_MEDIUM)
        print("Breakpoints label is added")

    except Exception as e:
        print(f"An error occurred on addng new breakpoint method: {e}")
        raise

def click_up_btn(wait):
    try:

        up = wait_for_element(wait, (By.XPATH, "//span[@aria-label='up']"))
        up.click()
        sleep(WAIT_TIME_MEDIUM)
        print("value is increased")
    except Exception as e:
        print(f"An error occurred on clicking increase Up button : {e}")
        raise

#---------------------------Colors Methods----------------------------------------------------------------------------
def select_Colours(wait):
    try:
        colour_tab = wait_for_element(wait, (By.XPATH, "(//a[normalize-space()='Colors'])[1]"))
        sleep(WAIT_TIME_SHORT)
        colour_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Colours tab is clicked & is opened")
    except Exception as e:
        print(f"An error occurred on clicking Colors tab: {e}")
        raise

def new_colors(wait, variable_name):
    try:
        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Color']"))
        enter_name.clear()
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_MEDIUM)
        print("Colors label is added")

        value = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-color-picker-color-block-inner"))
        value.click()
        sleep(WAIT_TIME_SHORT)
        print("Colors Menu is opened")

        color = wait_for_element(wait, (By.XPATH, "(//div)[162]"))
        color.click()
        sleep(WAIT_TIME_SHORT)
        print("Color is selected")
    except Exception as e:
        print(f"An error occurred on adding new colors method: {e}")
        raise

def edit_colors(wait):
    try:
        value = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-color-picker-color-block-inner"))
        value.click()
        sleep(WAIT_TIME_SHORT)
        print("Colors Menu is opened")

        color = wait_for_element(wait, (By.XPATH, "//div[28]//div[1]"))
        color.click()
        sleep(WAIT_TIME_SHORT)
        print("Color is selected")
    except Exception as e:
        print(f"An error occurred on clicking edit_color method: {e}")
        raise
#-------------------------------Font Family Methods----------------------------------------------------------------------------------------
def selectFontFamily(wait):
    try:
        Font_Family_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Font Family']"))
        Font_Family_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Font Family tab is clicked")
    except Exception as e:
        print(f"An error occurred on clicking Font Family Tab: {e}")
        raise
def new_font(wait, variable_name):
    try:
        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Font']"))
        enter_name.clear()
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        print("New Font Family label is added")

        FontType = wait_for_element(wait, (By.XPATH, "//span[1]//label[1]"))
        FontType.click()
        sleep(WAIT_TIME_SHORT)
        print("System Font type is selected")

        FontFamily = wait_for_element(wait, (By.XPATH, "(//span[@class='ant-select-selection-item'])[1]"))
        FontFamily.click()
        sleep(WAIT_TIME_SHORT)
        print("Font Family drop-down menu is opened")

        Dropdown = wait_for_element(wait, (By.XPATH, "//div[@title='Times, serif']//div[@class='ant-select-item-option-content']"))
        Dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("Times Font Family is selected")
    except Exception as e:
        print(f"An error occurred on adding new font method: {e}")
        raise

def edit_font(wait):
    try:
        FontType = wait_for_element(wait, (By.XPATH, "//span[1]//label[1]"))
        FontType.click()
        sleep(WAIT_TIME_SHORT)
        print("System Font type is selected")

        FontFamily = wait_for_element(wait, (By.XPATH, "(//span[@class='ant-select-selection-item'])[1]"))
        FontFamily.click()
        sleep(WAIT_TIME_SHORT)
        print("Font Family drop-down menu is opened")

        Dropdown = wait_for_element(wait, (By.XPATH, "//div[@title='Georgia, serif']//div[@class='ant-select-item-option-content']"))
        Dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("Font Family is Edited successfully")
    except Exception as e:
        print(f"An error occurred:on edt font method {e}")
        raise
#-----------------------------------------------------------------------------------------------------------------------
def select_size(wait):
    try:
        FontSze_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Font Size']"))
        sleep(WAIT_TIME_SHORT)
        FontSze_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Font Size Tab is clicked")
    except Exception as e:
        print(f"An error occurred:on clicking the Font Size Tab  {e}")
        raise

def enter_fontsize_label(wait, variable_name):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Font Size']"))
        enter_name.clear()
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        print("Font Size label is added")

    except Exception as e:
        print(f"An error occurred on adding new font size: {e}")
        raise

#-----------------------------------------------------------------------------------------------------------------------
def select_spacing(wait):
    try:
        FontSze_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Spacing']"))
        sleep(WAIT_TIME_SHORT)
        FontSze_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Spacing screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Spacing tab: {e}")
        raise

def new_spacing(wait, variable_name):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Spacing']"))
        enter_name.clear()
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        print("Spacing label is added")
    except Exception as e:
        print(f"An error occurred on adding spacing label: {e}")
        raise

def edit_spacing(wait, variable_value):
    try:

        value = wait_for_element(wait, (By.XPATH, "//input[@role='spinbutton']"))
        value.send_keys(variable_value)
        sleep(WAIT_TIME_SHORT)
        print("Spacing Value is edited")
    except Exception as e:
        print(f"An error occurred on editing spacing method {e}")
        raise

#----------------------------------------------------------------------------------------------------------
def select_radius(wait):
      try:
        FontSze_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Radius']"))
        sleep(WAIT_TIME_SHORT)
        FontSze_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Radius' screen is opened")
      except Exception as e:
          print(f"An error occurred on clicking Radius Tab {e}")
          raise
def new_radius(wait, variable_name):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Value']"))
        enter_name.clear()
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        logging.info("Radius label is added")
    except Exception as e:
        print(f"An error occurred on adding new radius label {e}")
        raise

#=------------------------------------------------------------------------------------------------------
def select_gradient(wait):
    try:
        grad_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Gradient']"))
        grad_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Gradient screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Gradient Tab {e}")
        raise


def new_gradient(wait, variable_name):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Gradient']"))
        enter_name.clear()
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        print("Gradient label is added")
    except Exception as e:
        print(f"An error occurred on new gradient method {e}")
        raise

def add_gradient(wait, variable_name):
    try:

        grad_box = wait_for_element(wait, (By.CSS_SELECTOR, ".gradient-preview"))
        grad_box.click()
        sleep(WAIT_TIME_SHORT)
        print("Gradient Icon is selected")

        gradient = wait_for_element(wait, (By.XPATH, "//textarea[@spellcheck='false']"))
        gradient.click()
        sleep(WAIT_TIME_SHORT)
        gradient.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        print("Gradient Name is added")



    except Exception as e:
        print(f"An error occurred on new gradient method {e}")
        raise

#------------------------------------------------------------------------------------------------------
def select_shadow(wait):
    try:
        shadow_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Shadow']"))
        shadow_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Gradient screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Shadow Tab: {e}")
        raise
def new_shadow(wait, variable_name, variable_value):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Shadow']"))
        enter_name.clear()
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        print("Shadow label is added")

        spread = wait_for_element(wait, (By.XPATH, "//input[@placeholder='Spr']"))
        spread.send_keys(variable_value)
        sleep(WAIT_TIME_SHORT)
        print("Spread Value is added")

        color = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-color-picker-color-block-inner"))
        color.click()
        sleep(WAIT_TIME_SHORT)
        print("Colors Menu is opened")

        blur = wait_for_element(wait, (By.XPATH, "//input[@placeholder='Blur']"))
        blur.send_keys("2")
        sleep(WAIT_TIME_SHORT)
        print("Blurr value is added")

        color = wait_for_element(wait, (By.XPATH, "(//div)[162]"))
        color.click()
        sleep(WAIT_TIME_SHORT)
        print("Color is selected")
    except Exception as e:
        print(f"An error occurred on new shadow method: {e}")
        raise
def edit_shadow(wait,value1):
    try:
        value_box = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-color-picker-color-block-inner"))
        value_box.click()
        sleep(WAIT_TIME_SHORT)
        print("Colors Menu is opened")

        color = wait_for_element(wait, (By.XPATH, "(//div)[228]"))
        color.click()
        sleep(WAIT_TIME_SHORT)
        print("Color is edited")

        blur = wait_for_element(wait, (By.XPATH, "//input[@placeholder='Blur']"))
        blur.clear()
        blur.send_keys(value1)
        sleep(WAIT_TIME_SHORT)
        print("Blurr value is edited")
    except Exception as e:
        print(f"An error occurred on editing shadow details method: {e}")
        raise

#-----------------------------------------------------------------------------------------------------------------------

def select_items(wait):
    try:
        items_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Items per Row']"))
        sleep(WAIT_TIME_SHORT)
        items_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Items Per Row screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Items Per Row Tab: {e}")
        raise

def new_items(wait, variable_name):
    try:
        enter_name = wait_for_element(wait, (By.XPATH, "(//input[@value='New Items per Row'])[1]"))
        enter_name.clear()
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        print("Items label is added")

        noofcols = wait_for_element(wait, (By.XPATH, "(//span[@aria-label='Increase Value'])[1]"))
        noofcols.click()
        sleep(WAIT_TIME_SHORT)
        print("No. of columns Value is increased")

        col = wait_for_element(wait, (By.XPATH, "(//span[@aria-label='Increase Value'])[2]"))
        col.click()
        sleep(WAIT_TIME_SHORT)
        print("One column Value is increased")
    except Exception as e:
        print(f"An error occurred on new items method {e}")
        raise

