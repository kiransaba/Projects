import logging
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from setting_constant import WAIT_TIME_SHORT, WAIT_TIME_MEDIUM,wait_for_element

def navigate_to_typograpghy(self):
    try:
        typo = wait_for_element(self.wait, (By.XPATH, "//a[normalize-space()='Typography']"))
        typo.click()
        sleep(WAIT_TIME_MEDIUM)

        print("Typography screen is opened successfully")
    except Exception as e:
        print(f"An error occurred in typograpgy method: {e}")
        raise
#—————————————————————————————————————————————————————————————
def open_general(wait):
    try:
        general = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_gen")))
        general.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography:General drop-down section is opened")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
def close_general(wait):
    try:
        general = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_gen")))
        general.click()
        sleep(WAIT_TIME_MEDIUM)
        print("General drop-down section is closed")
    except Exception as e:
        logging.error(f"An error occurred on clicking general drop-down {e}")
        raise
#—————————————————————————————————————————————————————————————

def open_text_link(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_link")))
        link.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Typography:Text Link drop-down section is opened")
    except Exception as e:
        print(f"An error occurred on clicking Text Link drop-down {e}")
        raise

def close_text_link(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_link")))
        link.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Typography:Text Link drop-down section is closed")
    except Exception as e:
        print(f"An error occurred on clicking Text Link drop-down {e}")
        raise

def open_headings(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_1")))
        link.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Typography: headings drop-down section is opened")
    except Exception as e:
        print(f"An error occurred on clicking headings drop-down {e}")
        raise
def close_headings(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_1")))
        link.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Typography: headings drop-down section is closed")
    except Exception as e:
        print(f"An error occurred on clicking headings closed {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def open_other_elements(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_el")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography: Other Elements drop-down section is opened")
    except Exception as e:
        print(f"An error occurred on clicking Other Elements drop-down {e}")
        raise
def close_other_elements(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_el")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography: Other Elements drop-down section is closed")
    except Exception as e:
        print(f"An error occurred on clicking Other Elements closed {e}")
        raise
#————————————————————————————
def open_blockquote(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_bl")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography:Blockquote drop-down section is opened")
    except Exception as e:
        print(f"An error occurred on clicking Blockquote drop-down {e}")
        raise
def close_blockquote(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_bl")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography: Blockquote drop-down section is closed")
    except Exception as e:
        print(f"An error occurred on clicking Blockquote closed {e}")
        raise
#————————————————————————————
def open_drop_cap(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_dc")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography:Drop Cap drop-down section is opened")
    except Exception as e:
        print(f"An error occurred on clicking Drop Cap drop-down {e}")
        raise
def close_drop_cap(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_dc")))
        link.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Typography: Drop Cap drop-down section is closed")
    except Exception as e:
        print(f"An error occurred on clicking Drop Cap closed {e}")
        raise
#————————————————————————————

def open_ampersand(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_amp")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography:Ampersand drop-down section is opened")
    except Exception as e:
        print(f"An error occurred on clicking Ampersand drop-down {e}")
        raise
def close_ampersand(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_amp")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography: Ampersand drop-down section is closed")
    except Exception as e:
        print(f"An error occurred on clicking Ampersand dropdown  {e}")
        raise

#————————————————————————————

def open_horizontal(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_hr")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography:Horizontal Rule drop-down section is opened")
    except Exception as e:
        print(f"An error occurred on clicking Horizontal Rule drop-down {e}")
        raise
def close_horizontal(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_hr")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography: Horizontal Rule drop-down section is closed")
    except Exception as e:
        print(f"An error occurred on clicking Horizontal Rule drop-down {e}")
        raise

#————————————————————————————

def open_font_render(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_render")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography:Font Rendering drop-down section is opened")
    except Exception as e:
        print(f"An error occurred on clicking Font Rendering drop-down {e}")
        raise
def close_font_render(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_render")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography: Font Rendering drop-down section is closed")
    except Exception as e:
        print(f"An error occurred on clicking Font Rendering closed {e}")
        raise
#————————————————————————————

def open_table(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_table")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography:Table drop-down section is opened")
    except Exception as e:
        print(f"An error occurred on clicking Table drop-down {e}")
        raise
def close_table(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_table")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography: Table drop-down section is closed")
    except Exception as e:
        print(f"An error occurred on clicking Table drop-down {e}")
        raise
#————————————————————————————

def open_responsive_video(wait):
    try:
        link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_vid")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography: Responsive Video drop-down section is opened")  # Corrected print statement
    except Exception as e:
        print(f"An error occurred on clicking Responsive Video drop-down {e}")
        raise

def close_responsive_video(wait):
    try:
        link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_vid")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography: Responsive Video drop-down section is closed")  # Corrected print statement
    except Exception as e:
        print(f"An error occurred on clicking Responsive Video drop-down {e}")
        raise


#————————————————————————————
#########Other than drop downs methods
def click_container_styles(wait):
    try:
        link= wait.until(EC.element_to_be_clickable((By.XPATH, "(//li)[112]")))
        link.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography:Container Styles tab is clicked")
    except Exception as e:
        print(f"An error occurred on clicking Container Styles tab {e}")
        raise

def click_icon_tab(wait):
    try:
        icon= wait.until(EC.element_to_be_clickable((By.XPATH, "(//li)[114]")))
        icon.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography:Icon tab is clicked")
    except Exception as e:
        print(f"An error occurred on clicking Icon tab {e}")
        raise

def click_dropdown(wait):
    try:
        arrow= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".ant-select-arrow")))
        arrow.click()
        sleep(WAIT_TIME_SHORT)
        print("Typography:drop-down arrow is clicked")
    except Exception as e:
        print(f"An error occurred on clicking drop-down arrow {e}")
        raise

def create_newstyle_btn(wait):
    try:
        new_style_btn = wait_for_element(wait, (By.XPATH, "//a[@class='ui-create']"))
        new_style_btn .click()
        sleep(WAIT_TIME_SHORT)
        print("Create New Style button is clicked successfuly")
    except Exception as e:
        print(f"An error occurred on clicking Create New Style button : {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————
def new_label(wait, variable_name):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Typography']"))
        enter_name.clear()
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_MEDIUM)
        logging.info("label is added")
    except Exception as e:
        print(f"An error occurred in addng new label method: {e}")
        raise
def select_size(wait,size):
    try:
        enter_size = wait_for_element(wait, (By.XPATH, "//input[@placeholder='Size']"))
        enter_size.send_keys(size)
        sleep(WAIT_TIME_SHORT)
        print("Size Value is added successfuly")
    except Exception as e:
        print(f"An error occurred in Adding Menu Title name method: {e}")
        raise
def select_icon(wait):
    try:
        icon = wait_for_element(wait, (By.CSS_SELECTOR, ".ui-icon-preview"))
        icon.click()
        sleep(WAIT_TIME_SHORT)
        print("Icon Menu is opened successfuly")

        icon_image = wait_for_element(wait, (By.XPATH, "//i[@class='icon icon-free']"))
        icon_image.click()
        sleep(WAIT_TIME_SHORT)
        print("Icon image is selected")
    except Exception as e:
        print(f"An error occurred in selecting Icon image method: {e}")
        raise

def additional_option2(wait,x,y,z):
    try:
        option2_tab = wait.until(EC.presence_of_element_located((By.XPATH,"(//a[@type='primary'])[2]")))
        option2_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Additional Options_2 Menu Screen is opened")
        X_value = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='X']")))
        X_value.send_keys(x)
        sleep(WAIT_TIME_SHORT)
        print("Text Shadow: X value is added")
        Y_value = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Y']")))
        Y_value.send_keys(y)
        sleep(WAIT_TIME_SHORT)
        print("Text Shadow:Y value is added")
        Blur = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Blur']")))
        Blur.send_keys(z)
        sleep(WAIT_TIME_SHORT)
        print("Blurr value is added")
    except Exception as e:
        print(f"An error occurred on clicking Additional Options_2 button : {e}")
        raise

def padding(wait,value):
    try:
         text_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='T'])[2]")))
         text_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print(" Padding value is added")

    except Exception as e:
        print(f"Error in adding Paddng value method: {e}")
        raise

def margin(wait,value):
    try:
         value1= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='ALL'])[1]")))
         value1.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print(" Margin value is added")

    except Exception as e:
        print(f"Error in adding Margin value method: {e}")
        raise



