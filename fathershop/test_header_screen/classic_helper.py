from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from setting_constant import WAIT_TIME_MEDIUM, WAIT_TIME_SHORT

def navigat_to_classic(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='classic']")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Classic screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Classic Tab: {e}")
        raise
#—————————————————————————————————————————————————————————————

def navigat_to_mega(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='header_desktop_mega']")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Megua screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Mega Tab: {e}")
        raise
#—————————————————————————————————————————————————————————————

def navigat_to_compact(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='header_desktop_compact']")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Compact screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Compact Tab: {e}")
        raise
#—————————————————————————————————————————————————————————————
def navigat_to_slim(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Slim']")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Slim screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Slim Tab: {e}")
        raise
#—————————————————————————————————————————————————————————————
def navigat_to_moble_1(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='header_mobile_1']")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Mobile 1 screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Mobiile 1 Tab: {e}")
        raise
#—————————————————————————————————————————————————————————————
def navigat_to_moble_2(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='header_mobile_2']")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Mobile 2 screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Mobiile 2 Tab: {e}")
        raise

#—————————————————————————————————————————————————————————————
def navigat_to_moble_3(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='header_mobile_3']")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Mobile 3 screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Mobiile 3 Tab: {e}")
        raise
#—————————————————————————————————————————————————————————————
def open_site(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='classic']")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Classic screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Classic Tab: {e}")
        raise

#—————————————————————————————————————————————————————————————

def open_global_options(wait):
    try:
        global1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='accordion-heading id_gen'])[1]")))
        global1.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Global Options dropdown menu is opened")
    except Exception as e:
        print(f"An error occurred on clicking Global Options dropdown menu: {e}")
        raise
#—————————————————————————————————————————————————————————————

def new_save(wait):
    try:
        save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[7]")))
        save_btn.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Create new style Save button is clicked & data is saved")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
#———————————————————————————————————————————————————
def padding(wait,value):
    try:
         header_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='L'])[2]")))
         header_value.clear()
         header_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Header Padding value is added")

    except Exception as e:
        print(f"Error in adding  Padding  value method: {e}")
        raise
def fullwidth_border(wait,value):
    try:
         add_border_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='ALL'])[1]")))
         add_border_value.clear()
         add_border_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("fullwidth Border  value is added")

    except Exception as e:
        print(f"Error in adding full width Border  value method: {e}")
        raise

def add_offset(self, x_value, y_value):
    try:
        # Call the appropriate function to add offset
        add_offset(self.wait, x_value, y_value)
        self.results["Text Padding value is added"] = "Passed"
    except Exception as e:
        self.results["Text Padding value is not added"] = f"Failed: {e}"

def cont_padding(self, value):
    try:
        # Call the appropriate function to add container padding
        cont_padding(self.wait, value)
        self.results["container padding value is added"] = "Passed"
    except Exception as e:
        self.results["container padding is not added"] = f"Failed: {e}"

#———————————————————————————————————————————————————
def header_height(wait):
    try:
         header_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@aria-label='Increase Value'])[1]")))
         header_value.clear()
         header_value.click()
         sleep(WAIT_TIME_SHORT)
         print("header_height value is added")

    except Exception as e:
        print(f"Error in adding header_height  value method: {e}")
        raise
#—————————————————————————————————————————————————————————————
def max_width1(wait):
    try:
         max_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@aria-label='Increase Value'])[1]")))
         max_value.click()
         sleep(WAIT_TIME_SHORT)
         print("max width is increased")

    except Exception as e:
        print(f"Error in header max width method: {e}")
        raise
#—————————————————————————————————————————————————————————————
def header_max_width(wait,value):
    try:
         max_width= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='px'])[3]")))
         max_width.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Header max width is added")

    except Exception as e:
        print(f"Error in header max width method: {e}")
        raise

#—————————————————————————————————————————————————————————————
def open_homepage_override(wait):
    try:
        global1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_home")))
        global1.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Global Options dropdown menu is opened")
    except Exception as e:
        print(f"An error occurred on clicking Global Options dropdown menu: {e}")
        raise

#—————————————————————————————————————————————————————————————
def menustyle_dropdown(wait):
    try:
        menustyle= wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ant-select-selection-item' and @title='Top Menu Default']")))
        menustyle.click()
        sleep(WAIT_TIME_SHORT)
        print("menu style dropdown menu is opened")

        # Find the dropdown option element
        select = wait.until(EC.element_to_be_clickable((By.ID, "Main Menu")))
        select.click()
        sleep(WAIT_TIME_SHORT)
        print("Dropdown option is selected")
    except Exception as e:
        print(f"An error occurred on Shadow dropdown button: {e}")
        raise


#—————————————————————————————————————————————————————————————
def position(wait,value):
    try:
        logo = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='px']")))
        logo.send_keys(value)
        sleep(WAIT_TIME_MEDIUM)
        print("Position is value is added")
    except Exception as e:
        print(f"An error occurred on Position increase button screen tab menu: {e}")
        raise
#—————————————————————————————————————————————————————————————
def click_tab_by_name(wait, tab_name):
    try:
        # Find the tab element by its text
        tab_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//ul[@class='tab-items']/li[text()='{tab_name}']")))

        # Click on the tab element
        tab_element.click()

        print(f"{tab_name} tab is clicked")
        sleep(WAIT_TIME_MEDIUM)

    except Exception as e:
        print(f"An error occurred while clicking {tab_name} tab: {e}")
        raise
#—————————————————————————————————————————————————————————————

def radio_btn(self):
    try:

        tick_radio = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-tooltip css-djtmh8 ant-tooltip-placement-top'])[1]")))
        ActionChains(self.driver).move_to_element(tick_radio).perform()
        sleep(WAIT_TIME_SHORT)
        tick_radio.click()
        sleep(WAIT_TIME_MEDIUM)
        print("item radio button is clicked")
    except Exception as e:
        print(f"An error occurred on clicking item_btn radio btn button : {e}")
        raise

#—————————————————————————————————————————————————————————————
def side_offset(wait):
    try:
         value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@aria-label='Decrease Value'])[2]")))
         value.click()
         sleep(WAIT_TIME_SHORT)
         print("max width is increased")

    except Exception as e:
        print(f"Error in header max width method: {e}")
        raise
#_______________________Desktop Header Name
def header_name(wait,name):
    try:
         header= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='New Header']")))
         header.clear()
         header.send_keys(name)
         sleep(WAIT_TIME_SHORT)
         print("Desktop Header name is added")

    except Exception as e:
        print(f"Error on adding desktop Header name : {e}")
        raise
#____________________________________Mobile Header
def mob_header_name(wait,name1):
    try:
         heade1r= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='New Mobile Header']")))
         heade1r.clear()
         heade1r.send_keys(name1)
         sleep(WAIT_TIME_SHORT)
         print("Mobile Header name is added")

    except Exception as e:
        print(f"Error on adding Mobile Header Name value method: {e}")
        raise
def enter_menu_name(wait,name2):
    try:
         header= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='w-full'])[4]")))
         header.clear()
         header.send_keys(name2)
         sleep(WAIT_TIME_SHORT)
         print("Mobile Header name is added")

    except Exception as e:
        print(f"Error on adding Mobile Header Name value method: {e}")
        raise