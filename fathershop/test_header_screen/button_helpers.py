from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from setting_constant import WAIT_TIME_MEDIUM, WAIT_TIME_SHORT, wait_for_element
def create_newstyle_btn(wait):
    try:
        new_style_btn = wait_for_element(wait, (By.XPATH, "//a[@class='ui-create']"))
        new_style_btn .click()
        sleep(WAIT_TIME_SHORT)
        print("Create New Style button is clicked successfuly")
    except Exception as e:
        print(f"An error occurred on clicking Create New Style button : {e}")
        raise
#—————————————————————————————————————————————————————————————
def enter_stylelabel(wait, variable_name):
    try:
        enterlabel = wait_for_element(wait, (By.XPATH, "(//input[@value='New Table'])[1]"))
        enterlabel.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        print("Style label Name is added")
    except Exception as e:
        print(f"An error occurred in Style label method: {e}")
        raise

def open_new_style_tabs(wait):
    try:
        # Find the tab element by its text
        tab_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "accordion-heading id_icon")))
        # Click on the tab element
        tab_element.click()
        print("Global tab is opened")
        sleep(WAIT_TIME_SHORT)
    except Exception as e:
        print(f"An error occurred while clicking on Global Styles tab: {e}")
        raise

def enter_margin(wait, variable_name):
    try:
        entervalue = wait_for_element(wait, (By.ID, "input-div"))
        entervalue.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        print("Margin value  is added")
    except Exception as e:
        print(f"An error occurred in Margin value method: {e}")
        raise

def add_offset(wait, x_value, y_value):
        try:
            x_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='X'])[2]")))
            x_input.send_keys(x_value)
            sleep(WAIT_TIME_SHORT)
            print("X offset value is added")
            y_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Y'])[2]")))
            y_input.send_keys(y_value)
            sleep(WAIT_TIME_SHORT)
            print("Y offset value is added")
        except TimeoutException:
            print("Timeout waiting for the element to be clickable.")
        except Exception as e:
            print(f"Error in adding offset value method: {e}")
            raise

def cart_position(wait):
    try:

        cart= wait.until(EC.element_to_be_clickable((By.XPATH, "[//div[@data-name='general.cartPosition']//input[@checked]]")))
        cart.click()
        sleep(WAIT_TIME_SHORT)
        print("Cart position is clicked")


    except Exception as e:
        print(f"An error occurred on clicking on Cart Position button : {e}")
        raise



def radio_position(wait):
    try:
        btn= wait.until(EC.element_to_be_clickable((By.XPATH, "[//label[@class='is-checked']/input[@type='radio']")))
        btn.click()
        sleep(WAIT_TIME_SHORT)
        print("radio button is clicked")

    except Exception as e:
        print(f"An error occurred on clicking on radio  button : {e}")
        raise
#_________________________________________#Addtonaloffcanvas

def open_off_canvas(wait):
    try:
        general = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_3")))
        general.click()
        sleep(WAIT_TIME_SHORT)
        print("Off Canvas Menu on Desktop drop-down section is opened")
    except Exception as e:
        print(f"An error occurred on clicking Off Canvas Menu on Desktop drop-down: {e}")
        raise

def open_menu_trigger(wait):
    try:
        general = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_trig")))
        general.click()
        sleep(WAIT_TIME_SHORT)
        print("Menu Trigger drop-down section is opened")
    except Exception as e:
        print(f"An error occurred on clicking Menu Trigger: {e}")
        raise



def click_side_paddin(wait):
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//svg[@data-icon='up']/path[@d='M890.5 755.3L537.9 269.2c-12.8-17.6-39-17.6-51.7 0L133.5 755.3A8 8 0 00140 768h75c5.1 0 9.9-2.5 12.9-6.6L512 369.8l284.1 391.6c3 4.1 7.8 6.6 12.9 6.6h75c6.5 0 10.3-7.4 6.5-12.7z']")))

        # Clicking the SVG element using JavaScript
        wait.execute_script("arguments[0].dispatchEvent(new Event('click', { 'bubbles': true, 'cancelable': true }));",
                            element)

        print("Clicked the SVG element successfully")

    except TimeoutException:
        print("Timeout waiting for the element to be clickable.")
    except Exception as e:
        print(f"Error in clicking the SVG element: {e}")
        raise

#_________________________________________#AddStckeyheader


def sticky_status_btn(wait):
    try:
        tick_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[1]//label[1])")))
        tick_radio.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Status button is clicked")
    except TimeoutException:
        print("Timeout waiting for status button to be clickable.")
    except Exception as e:
        print(f"An error occurred on clicking status btn button: {e}")
        raise

#_________________________________________ Cart helper
def cart_min_height(wait):
    try:
         max_width= wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-name='general.cartHeight']//span[@aria-label='down']//*[name()='svg']")))
         max_width.click()
         sleep(WAIT_TIME_SHORT)
         print("cart min height is added")
    except Exception as e:
        print(f"Error in cart min height method: {e}")
        raise

def cart_margin1(wait, x_value, y_value):
    try:
        left = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='L'])[1]")))
        left.send_keys(x_value)
        sleep(WAIT_TIME_MEDIUM)
        print("Cart Margin:Left value is added")
        right = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='R'])[1]")))
        right.send_keys(y_value)
        sleep(WAIT_TIME_MEDIUM)
        print("Cart Margin:Right value is added")
    except TimeoutException:
         print("Timeout waiting for the element to be clickable.")
    except Exception as e:
            print(f"Error in adding cart Margins values value method: {e}")
            raise

def cart_position1(wait): ### This Element is not accessible by selenium
    try:
        btn= wait.until(EC.element_to_be_clickable((By.XPATH, "(//label[@class='is-checked'])[1]")))
        btn.click()
        sleep(WAIT_TIME_SHORT)
        print("csrt position button is added")
    except Exception as e:
        print(f"An error occurred on clicking on cart positiom  button : {e}")
        raise
#________________________________Main Menu Helper
def open_general(wait):
    try:
        general = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_gen")))
        general.click()
        sleep(WAIT_TIME_MEDIUM)
        print("General drop-down section is opened")
    except TimeoutException:
        print("Timeout waiting for General drop-down section to be clickable.")
    except Exception as e:
        print(f"An error occurred on clicking the Open_general {e}")
        raise

def open_site_overlay(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_overlay")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Site Overlay dropdowwn screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Site Overlay dropdown: {e}")
        raise

def open_main_menu2(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_m2")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Main_menu2 dropdowwn screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Main_menu2 dropdowwn: {e}")
        raise

def close_main_menu2(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_m2")))
        menu.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Main_menu2 dropdowwn screen is closed")
    except Exception as e:
        print(f"An error occurred on clicking Main_menu2 dropdowwn: {e}")
        raise

def open_desktop_menu(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_1")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Main_menu2 dropdowwn screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Main_menu2 dropdowwn: {e}")
        raise


def close_desktop_menu(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_1")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Desktop_Menu drop-dowwn screen is closed")
    except Exception as e:
        print(f"An error occurred on closing Desktop Menu drop-dowwn: {e}")
        raise

def open_menu_name(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_mn")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Menu Name dropdown is opened")
    except Exception as e:
        print(f"An error occurred on clicking Menu dropdown : {e}")
        raise
def open_menu1(wait):
    try:
        menu1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_gen")))
        menu1.click()
        sleep(WAIT_TIME_SHORT)
        print("Menu1 dropdown is opened")
    except Exception as e:
        print(f"An error occurred on clicking Menu1 dropdown : {e}")
        raise

def open_count_badge(wait):
    try:
        badge = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_count")))
        badge.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Count badge dropdown is opened")
    except Exception as e:
        print(f"An error occurred on clicking Count badge dropdown : {e}")
        raise
#def open_menu2(wait):
   # try:
       # menu2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "..accordion-heading.id_btn")))
       # menu2.click()
       # sleep(WAIT_TIME_SHORT)
       # print("Menu2 dropdown is opened")
    #except Exception as e:
        #print(f"An error occurred on clicking Menu2 dropdown : {e}")
        #raise
def menu_border(wait, t_value, r_value):
    try:
        value1= wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='T']")))
        value1.send_keys(t_value)
        sleep(WAIT_TIME_MEDIUM)
        print("Top value is added")
        value2 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='R']")))
        value2.send_keys(r_value)
        sleep(WAIT_TIME_MEDIUM)
        print("Right value is added")
    except TimeoutException:
         print("Timeout waiting for the element to be clickable.")
    except Exception as e:
            print(f"Error in adding menu border values value method: {e}")
            raise
#______________________Mobile header Main Menu-> Menu Name-> Offset

def name_ofset(wait, value1, value2):
    try:
        value_1= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='X']")))
        value_1.send_keys(value1)
        sleep(WAIT_TIME_MEDIUM)
        print("X-offset value is added")
        value_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Y']")))
        value_2.send_keys(value2)
        sleep(WAIT_TIME_MEDIUM)
        print("Y-offset value is added")
    except TimeoutException:
         print("Timeout waiting for the element to be clickable.")
    except Exception as e:
            print(f"Error in adding name offset values method: {e}")
            raise

def side_margin(wait, x_value, y_value):
    try:
        left = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='L'])[3]")))
        left.send_keys(x_value)
        sleep(WAIT_TIME_SHORT)
        print("Left value is added")
        right = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='R'])[3]")))
        right.send_keys(y_value)
        sleep(WAIT_TIME_SHORT)
        print("Right value is added")
    except TimeoutException:
         print("Timeout waiting for the element to be clickable.")
    except Exception as e:
            print(f"Error in adding menu border values value method: {e}")
            raise

def module_dropdown(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-select-arrow'])[1]")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Main Menu Module dropdown is opened")
    except Exception as e:
        print(f"An error occurred on clicking Main Menu Module dropdown : {e}")
        raise