import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from theme_constants import check_cache_btn, create_new_btn, duplicate, delete, filter_search, edit, save, no_element_dropdown
from setting_constant import  USERNAME, PASSWORD, LOGIN_URL,Driver_path,write_to_excel,login,
from variable_helper import navigate_to_variable_screen,new_breakpoint, select_Colours, new_colors,edit_colors, selectFontFamily, new_font, edit_font,select_size ,enter_fontsize_label,\
select_spacing,new_spacing,edit_spacing,select_radius , new_radius,select_gradient,new_gradient,select_shadow,new_shadow,edit_shadow, select_items, new_items,click_up_btn,add_gradient
class Variables:

    def __init__(self, driver):  # def __init__(self, driver, excel_path):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.results = {}

    def login(self):
        try:
            login(self.wait, USERNAME, PASSWORD)
            self.results["Fathersshop Login"] = " Passed"
        except Exception as e:
            self.results["Fathersshop Login"] = f" Failed: {e}"
    def navigate_to_variable_screen(self):
        try:
         navigate_to_variable_screen(self)
         self.results ["Navigated to Variable screen successfully"] = " Passed"
        except Exception as e:
         self.results["Navigated to Variable screen is not successful"] = f" Failed: {e}"

    def no_element_dropdown(self):
       try:
        no_element_dropdown(self.wait)
        self.results["No.of element dropdown is clicked & showing the result"] = "Passed"
       except Exception as e:
        self.results["An error occurred on clicking no.of element drop-down button"] = f"Failed: {e}"


    def check_cache_btn(self):
        try:
            check_cache_btn(self.wait)
            self.results["Cache button is clicked & working"] = "Passed"
        except Exception as e:
            self.results["Cache button s clicked & not working "] = f"Failed: {e}"

    def filter_search(self, search_term):
        try:
            filter_search(self.wait, search_term)
            self.results["Variable Search is showing the desired result"] = "Passed"
        except Exception as e:
            self.results["Variable Filter Search is not working"] = f"Failed: {e}"

    def duplicate(self):
      try:
        duplicate(self.wait)
        self.results["Clicking on Variable duplicate button is successful"] = "Passed"
      except Exception as e:
       self.results["Variable duplicate button clicking is not successful"] = f"Failed: {e}"

    def delete(self):
      try:

        delete(self.wait)
        self.results["Clicking on Variable delete button is successful"] = "Passed"
      except Exception as e:
       self.results["Variable delete button clicking is not successful"] = f"Failed: {e}"

    def save(self):
        try:
            save(self.wait)
            self.results["Changes made in the Variable Screen has been Saved"] = "Passed"
        except Exception as e:
            self.results["Changes made in the Variable Screen are not Saved"] = f"Failed: {e}"

    def create_new_btn(self):
        try:
            create_new_btn(self.wait)
            self.results["Variable Create New Button is working"] = "Passed"
        except Exception as e:
            self.results["Variable Create New Button is not working"] = f"Failed: {e}"

    def edit(self):
        try:
            edit(self.wait)
            self.results["Edit button on Variable Screen is clicked "] = "Passed"
        except Exception as e:
            self.results["Edit button on Variable Screen is not working "] = "Passed"

    def click_up_btn(self):
        try:
            click_up_btn(self.wait)
            self.results["Increase button is clicked & value is updated"] = "Passed"
        except Exception as e:
            self.results["Increase button is not clicked"] = f"Failed: {e}"

###################BreakPoint Methods
    def new_breakpoint(self, variable_name):
        try:
         new_breakpoint(self.wait, variable_name)
         self.results["Breakpoints label is added"] = "Passed"
        except Exception as e:
         self.results["Breakpoint label is not added"] = f"Failed: {e}"

######### Color Screen Methods

    def select_Colours(self):
      try:
        select_Colours(self.wait)
        self.results["Color tab is clicked & color variable screen is opened"] = "Passed"
      except Exception as e:
        self.results["An error occurred on clicking Colors tab"] = f"Failed: {e}"

    def new_colors(self, variable_name):
       try:
        new_colors(self.wait, variable_name)
        self.results["Color label & value is added"] = "Passed"
       except Exception as e:
        self.results["Error occured label in adding color label & value method"] = f"Failed: {e}"
    def edit_colors(self):
      try:
        edit_colors(self.wait)
        self.results["Color value is edited"] = "Passed"
      except Exception as e:
        self.results["Color value is not edited"] = f"Failed: {e}"

######### Font_Family Methods

    def selectFontFamily(self):
        try:
            selectFontFamily(self.wait)
            self.results["Font Family Tab is clikced and opened"] = "Passed"
        except Exception as e:
            self.results["Error occurred on clicking Font Family tab"] = f"Failed: {e}"

    def new_font(self, variable_name):
        try:
            new_font(self.wait, variable_name)
            self.results["Font Family label/Type & Family is added"] = "Passed"
        except Exception as e:
            self.results["Error occurred on adding Font Family details"] = f"Failed: {e}"

    def edit_font(self):
        try:
            edit_font(self.wait)
            self.results["Font Family label/type & family fields are edited"] = "Passed"
        except Exception as e:
            self.results["Error occurred in editing Font Family details"] = f"Failed: {e}"

######Font Size Methods

    def select_size(self):
        try:
            select_size(self.wait)
            self.results["Font Size tab is clicked"] = "Passed"
        except Exception as e:
            self.results["Error occurred on clicking the Font Size Tab"] = f"Failed: {e}"

    def enter_fontsize_label(self, variable_name):

        try:
            enter_fontsize_label(self.wait, variable_name)
            self.results["Font Size label is added"] = "Passed"
        except Exception as e:
            self.results["Error occurred on adding Font Size label"] = f"Failed: {e}"

 ###Spacing Methods

    def select_spacing(self):
        try:
            select_spacing(self.wait)
            self.results["Spacing tab is clicked"] = "Passed"
        except Exception as e:
            self.results["Error occurred on clicking the Spacing tab"] = f"Failed: {e}"

    def new_spacing(self, variable_name):
        try:
            new_spacing(self.wait, variable_name)
            self.results["Spacing label is added"] = "Passed"
        except Exception as e:
            self.results["Error occurred on adding Space label"] = f"Failed: {e}"

###Radius Methods
    def select_radius(self):

        try:
            select_radius(self.wait)
            self.results["Radius tab is clicked"] = "Passed"
        except Exception as e:
            self.results["Error occurred on clicking  the Radius Tab"] = f"Failed: {e}"
    def new_radius(self, variable_name):

        try:
            new_radius(self.wait, variable_name)
            self.results["Radius label is added"] = "Passed"
        except Exception as e:
            self.results["Error occurred on adding Radius label"] = f"Failed: {e}"

### Gradient_Methods
    def select_gradient(self):
        try:
            select_gradient(self.wait)
            self.results["Gradient tab is clicked"] = "Passed"
        except Exception as e:
            self.results["Error occurred on clicking  the Gradient Tab"] = f"Failed: {e}"

    def new_gradient(self, variable_name):
        try:
            new_gradient(self.wait, variable_name)
            self.results["Gradient label is added"] = "Passed"
        except Exception as e:
            self.results["Error occurred on adding Gradient label"] = f"Failed: {e}"

    def add_gradient(self, variable_name):
        try:
            add_gradient(self.wait, variable_name)
            self.results["New Gradient is added"] = "Passed"
        except Exception as e:
            self.results["Error occurred on adding New Gradient"] = f"Failed: {e}"

########### Shadow_Tab Methods
    def select_shadow(self):
        try:
            select_shadow(self.wait)
            self.results["Shadow tab is clicked"] = "Passed"
        except Exception as e:
            self.results["Error occurred on clicking  the Shadow Tab"] = f"Failed: {e}"

    def new_shadow(self, variable_name, variable_value):
        try:
            new_shadow(self.wait, variable_name, variable_value)
            self.results["Shadow: label/value/blur/color are added"] = "Passed"
        except Exception as e:
            self.results["Error occurred on adding Shadow details"] = f"Failed: {e}"


    def edit_shadow(self,value1):

        try:
            new_shadow(self.wait,value1)
            self.results["Shadow: color & blurr values are edited"] = "Passed"
        except Exception as e:
            self.results["Error occurred in Shadow Shadow details"] = f"Failed: {e}"



    def select_items(self):
        try:
            select_items(self.wait)
            self.results["Items Per Row tab is clicked"] = "Passed"
        except Exception as e:
            self.results["Error occurred on clicking the Items Per Row Tab"] = f"Failed: {e}"


    def new_items(self, variable_name):

        try:
            new_items(self.wait, variable_name)
            self.results["Items Per Row tab variable name & No.of cols are added"] = "Passed"
        except Exception as e:
            self.results["Error occurred on adding the details on Items Per Row screen "] = f"Failed: {e}"

    def write_to_excel(self, folder_name="excel_results", file_name="variable_result.xlsx"):
        write_to_excel(self.results, folder_name, file_name)

class TestFathershopTheme:
    @pytest.fixture
    def setup(self):
        chrome_driver_path = Driver_path
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_styles_functions(self, setup):
        driver = setup
        variable = Variables(driver)
        variable.login()
        variable.write_to_excel()
        variable.navigate_to_variable_screen()
        variable.write_to_excel()

        variable.check_cache_btn()
        variable.filter_search("Test")
        variable.duplicate()
        variable.write_to_excel()
        variable.delete()
        variable.write_to_excel()
        # ———————————————————————————-
        variable.create_new_btn()
        variable.write_to_excel()

        variable.new_breakpoint(" Test breakpoint")
        variable.write_to_excel()

        variable.click_up_btn()
        variable.write_to_excel()

        variable.save()
        variable.write_to_excel()

        variable.edit()
        variable.write_to_excel()

        variable.click_up_btn()
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()

        # ———————————————————————————-
        variable.select_Colours()
        variable.write_to_excel()
        variable.no_element_dropdown()
        variable.write_to_excel()
        variable.create_new_btn()
        variable.write_to_excel()
        variable.new_colors("New Colors")
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()
        variable.edit()
        variable.edit_colors()
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()
        # ———————————————————————————-
        variable.selectFontFamily()
        variable.write_to_excel()
        variable.create_new_btn()
        variable.new_font("Test Font")
        variable.write_to_excel()
        variable.click_up_btn()
        variable.save()
        variable.write_to_excel()
        variable.edit()
        variable.edit_font()
        variable.write_to_excel()
        variable.click_up_btn()
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()
        # ———————————————————————————-
        variable.select_size()
        variable.write_to_excel()
        variable.create_new_btn()
        variable.enter_fontsize_label("Test Size")
        variable.write_to_excel()
        variable.click_up_btn()
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()
        variable.edit()
        variable.write_to_excel()
        variable.click_up_btn()
        variable.write_to_excel()
        variable.save()
        # ———————————————————————————-
        variable.select_spacing()
        variable.write_to_excel()
        variable.create_new_btn()
        variable.write_to_excel()
        variable.new_spacing("Test Spacing")
        variable.write_to_excel()
        variable.click_up_btn()
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()
        variable.edit()
        variable.write_to_excel()
        variable.click_up_btn()
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()
        # ———————————————————————————
        variable.select_radius()
        variable.write_to_excel()
        variable.create_new_btn()
        variable.write_to_excel()
        variable.new_radius("Test Radius")
        variable.write_to_excel()
        variable.click_up_btn()
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()
        variable.edit()
        variable.write_to_excel()
        variable.click_up_btn()
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()

        # ———————————————————————————
        variable.select_gradient()
        variable.write_to_excel()
        variable.create_new_btn()
        variable.write_to_excel()
        variable.new_gradient("New Gradient")
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()
        # ———————————————————————————
        variable.select_shadow()
        variable.write_to_excel()
        variable.create_new_btn()
        variable.write_to_excel()
        variable.new_shadow("New Shadow", "10")
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()
        variable.edit()
        variable.write_to_excel()
        variable.edit_shadow("20")
        variable.write_to_excel()
        variable.save()
        variable.write_to_excel()

    # ———————————————————————————
        variable.select_items()
        variable.create_new_btn()
        variable.new_items("New Items")
        variable.save()
        variable.edit()
        variable.click_up_btn()
        variable.save()


