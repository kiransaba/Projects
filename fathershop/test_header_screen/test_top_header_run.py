import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import USERNAME, PASSWORD, LOGIN_URL,Driver_path, write_to_excel,login
from theme_constants import check_cache_btn,no_element_dropdown,create_new_btn,duplicate,delete,filter_search,edit,\
click_back_btn,reset_btn,image_options,save
from header_helpers import navigate_to_header_screen,top_menu_edit,Topmenu_modulename,Top_menu_addNewItem,topmenu_name,topmenu_addstatus,select_icon,select_size,click_hovertab,\
additional_option1,additional_option2,additional_option3,header_color,edit_select_icon,edit_header_color
class Header:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.results = {}
    def login(self):
        try:
            login(self.wait,USERNAME, PASSWORD)
            self.results["Login"] = "Passed"
        except Exception as e:
            self.results["Login"] = f"Failed: {e}"
    def navigate_to_header_screen(self):
      try:
          navigate_to_header_screen(self)
          self.results["Navigation to header Screen"] = "Passed"
      except Exception as e:
          self.results["Navigation to headerer Screen"] = f"Failed: {e}"

    def check_cache_btn(self):
      try:
        check_cache_btn(self.wait)
        self.results["Cache button s clicked"] = "Passed"
      except Exception as e:
         self.results["Cache button s clicked"] = f"Failed: {e}"

    def no_element_dropdown(self):
      try:
        no_element_dropdown(self.wait)
        self.results["No_of elements button clicking & list"] = "Passed"
      except Exception as e:
          self.results["No_of elements button clicking & list"] = f"Failed: {e}"

    def duplicate(self):
      try:
        duplicate(self.wait)
        self.results["Clicking on Top menu  duplicate button is successful"] = "Passed"
      except Exception as e:
       self.results["Top menu  duplicate button clicking is not successful"] = f"Failed: {e}"

    def delete(self):
      try:

        delete(self.wait)
        self.results["Clicking on Top menu  delete button is successful"] = "Passed"
      except Exception as e:
       self.results["Clicking on Top menu  delete button is successful"] = f"Failed: {e}"

    def filter_search(self, search_term):
        try:
            filter_search(self.wait, search_term)
            self.results["Top menu  Search is showing the desired result"] = "Passed"
        except Exception as e:
            self.results["Top menu  Filter Search is not working"] = f"Failed: {e}"

    def edit(self):
        try:
            edit(self.wait)
            self.results["Edit button on Top menu  Screen is working "] = "Passed"
        except Exception as e:
            self.results["Edit button on Top menu  Screen is not working "] = "Passed"


    def top_menu_edit(self):
        try:
            top_menu_edit(self.wait)
            self.results["Top menu data is Edited"] = "Passed"
        except Exception as e:
            self.results["Top menu data is not Edited"] = f"Failed: {e}"

    def click_back_btn(self):
        try:
            click_back_btn(self.wait)
            self.results["Back button on Header Screen is working"] = "Passed"
        except Exception as e:
            self.results["Back button on Header Screen is not working"] = f"Failed: {e}"

    def create_new_btn(self):
        try:
            create_new_btn(self.wait)
            self.results["Create New Button is clicked "] = "Passed"
        except Exception as e:
            self.results["Create New Button is not clicked "] = f"Failed: {e}"

    def Topmenu_modulename(self, variable_name):
        try:
            Topmenu_modulename(self.wait, variable_name)
            self.results["Module name is entered"] = "Passed"
        except Exception as e:
            self.results["Module name is not entered"] = f"Failed: {e}"

    def Top_menu_addNewItem(self):
        try:
            Top_menu_addNewItem(self.wait)
            self.results["New Item button is clicked"] = "Passed"
        except Exception as e:
            self.results["New item button is not clicked"] = f"Failed: {e}"

    def topmenu_name(self, variable_name1,variable_name2):
        try:
            topmenu_name(self.wait, variable_name1,variable_name2)  # pass self.wait instead of self
            self.results["Item Name & Menu Title are entered"] = "Passed"
        except Exception as e:
            self.results["Item Name & Menu Title are not entered"] = f"Failed: {e}"

    def topmenu_addstatus(self):
        try:
            topmenu_addstatus(self.wait,)  # pass self.wait instead of self
            self.results["Navigating on Status Tabs"] = "Passed"
        except Exception as e:
            self.results["Navigation on Status Tabs are not successful"] = f"Failed: {e}"

    def select_icon(self):
        try:
            select_icon(self.wait)
            self.results["Icon image is uploaded"] = "Passed"
        except Exception as e:
            self.results["Icon image is not uploaded"] = f"Failed: {e}"

    def edit_select_icon(self):
        try:
            edit_select_icon(self.wait)
            self.results["Icon image is edited"] = "Passed"
        except Exception as e:
            self.results["Icon image is not edited"] = f"Failed: {e}"

    def select_size(self,size):
        try:
            select_size(self.wait,size)
            self.results["Icon Size is added"] = "Passed"
        except Exception as e:
            self.results["Icon Size is not added"] = f"Failed: {e}"

    def click_hovertab(self):
        try:
            click_hovertab(self.wait)
            self.results["Icon Hover tab is clicked"] = "Passed"
        except Exception as e:
            self.results["Icon Hover tab is not clicked"] = f"Failed: {e}"

    def additional_option1(self, X,Y):
        try:
            additional_option1(self.wait,X,Y)  # pass self.wait instead of self
            self.results["additional_option1 values are entered"] = "Passed"
        except Exception as e:
            self.results["additional_option1 values are not entered"] = f"Failed: {e}"

    def additional_option2(self, x,y,z):
        try:
            additional_option2(self.wait,x,y,z)  # pass self.wait instead of self
            self.results["additional_option2 values are entered"] = "Passed"
        except Exception as e:
            self.results["additional_option2 values are not entered"] = f"Failed: {e}"


    def additional_option3(self):
        try:
            additional_option3(self.wait)  # pass self.wait instead of self
            self.results["additional_option3 values are entered"] = "Passed"
        except Exception as e:
            self.results["additional_option3 values are not entered"] = f"Failed: {e}"

    def header_color(self):
        try:
            header_color(self.wait)
            self.results["The Icon Color has been selected"] = "Passed"
        except Exception as e:
            self.results["The Icon Color has not been selected"] = f"Failed: {e}"

    def edit_header_color(self):
        try:
            edit_header_color(self.wait)
            self.results["The Icon Color has been edited"] = "Passed"
        except Exception as e:
            self.results["The Icon Color is not edited"] = f"Failed: {e}"

    def image_options(self):
        try:
            image_options(self.wait)
            self.results["In Background Image Options has been selected"] = "Passed"
        except Exception as e:
            self.results["In Background Image Options has not been selected"] = f"Failed: {e}"

    def reset_btn(self):
        reset_btn(self.wait)

    def save(self):
        try:
            save(self.wait)
            self.results["All the Changes made in the Top menu Screen has been Saved"] = "Passed"
        except Exception as e:
            self.results["All the Changes made in the Top menu Screen are not Saved"] = f"Failed: {e}"

    def write_to_excel(self, folder_name="excel_results", file_name="top_header_result.xlsx"):
        write_to_excel(self.results, folder_name, file_name)

class TestFathershopTheme:
    @pytest.fixture(scope='class')
    def setup(self):
        chrome_driver_path = Driver_path
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_header_functions(self, setup):
        driver = setup
        header= Header(driver)
        header.login()
        header.navigate_to_header_screen()
        header.write_to_excel()
        header.check_cache_btn()
        header.write_to_excel()
        header.duplicate()
        header.write_to_excel()
        header.filter_search("Top")
        header.write_to_excel()
        header.create_new_btn()
        header.Topmenu_modulename(" Test12") #Change the Moduule name before excecuting the code
        header.write_to_excel()
        header.Top_menu_addNewItem()
        header.write_to_excel()
        header.topmenu_name(" Accounts", " Test Accounts")
        header.write_to_excel()
        header.topmenu_addstatus()
        header.write_to_excel()
        header.select_icon()
        header.write_to_excel()
        header.header_color()
        header.select_size("20")
        header.write_to_excel()
        header.additional_option1("10", "10")
        header.write_to_excel()
        header.additional_option2("5", "5", "2")
        header.write_to_excel()
        header.click_hovertab()
        header.write_to_excel()
        header.header_color()
        header.write_to_excel()
        header.save()
        header.write_to_excel()
        #header.click_back_btn()
        #header.delete()
        #header.reset_btn()




