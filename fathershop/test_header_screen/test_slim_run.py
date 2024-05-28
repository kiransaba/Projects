import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from theme_constants import edit_gradient,check_cache_btn,no_element_dropdown,create_new_btn,duplicate,delete,filter_search,gradient,camera,save,edit
from setting_constant import USERNAME, PASSWORD, LOGIN_URL,Driver_path, write_to_excel,login
from header_helpers import navigate_to_header_screen,additional_option2,header_color,select_icon,select_size,edit_header_color
from classic_helper import navigat_to_slim,open_global_options,fullwidth_border,padding,header_height,max_width1,open_homepage_override,menustyle_dropdown,\
click_tab_by_name,cont_padding,header_max_width,side_offset,new_save,header_name
from button_helpers import enter_stylelabel,create_newstyle_btn,open_new_style_tabs,add_offset,enter_margin,cart_position,cart_min_height,sticky_status_btn,open_menu_trigger,open_off_canvas,\
open_general,open_main_menu2,close_main_menu2,open_desktop_menu,close_desktop_menu,open_site_overlay,menu_border,side_margin

class Slim:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.results = {}

    def login(self):
        try:
            login(self.wait, USERNAME, PASSWORD)
            self.results["Login"] = "Passed"
        except Exception as e:
            self.results["Login"] = f"Failed: {e}"

    def navigate_to_header_screen(self):
      try:
          navigate_to_header_screen(self)
          self.results["Navigation to header Screen"] = "Passed"
      except Exception as e:
          self.results["Navigation to headerer Screen"] = f"Failed: {e}"

    def navigat_to_slim(self):
        try:
            navigat_to_slim(self.wait)
            self.results["Slim Screen is opened"] = "Passed"
        except Exception as e:
            self.results["Sliim Screen is not opened"] = f"Failed: {e}"

#----------------------------------------------------
    def check_cache_btn(self):
        check_cache_btn(self.wait)

    def no_element_dropdown(self):
        no_element_dropdown(self.wait)

    def duplicate(self):
        duplicate(self.wait)

    def delete(self):
        delete(self.wait)

    def filter_search(self, search_term):
        filter_search(self.wait, search_term)

    def edit(self):
        edit(self.wait)

    def create_new_btn(self):
        try:
            create_new_btn(self.wait)
            self.results["Create New Button is clicked "] = "Passed"
        except Exception as e:
            self.results["Create New Button is not clicked "] = f"Failed: {e}"

    def open_global_options(self):
        try:
            open_global_options(self.wait)
            self.results["Global Options dropdown menu is clicked "] = "Passed"
        except Exception as e:
            self.results["Global Options dropdown menu is not clicked "] = f"Failed: {e}"
    def header_name(self,name):
        try:
            header_name(self.wait,name)
            self.results["header name is added"] = "Passed"
        except Exception as e:
            self.results["header name is not added"] = f"Failed: {e}"

    def gradient(self):
        try:
         gradient(self.wait)
         self.results["In Item Background Gradient has been selected"] = "Passed"
        except Exception as e:
            self.results["In Item Background Gradient has not been selected"] = f"Failed: {e}"

    def edit_gradient(self):
        try:
         edit_gradient(self.wait)
         self.results["In Item Background Gradient is edted"] = "Passed"
        except Exception as e:
            self.results["In Item Background Gradient has not edited"] = f"Failed: {e}"

    def camera(self):
        try:
         camera(self.wait)
         self.results["In Background Camera Image has been selected"] = "Passed"
        except Exception as e:
            self.results["In Background Camera Image has not been selected"] = f"Failed: {e}"

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


    def save(self):
        try:
            save(self.wait)
            self.results["All the Changes made in the Classic Header  Screen has been Saved"] = "Passed"
        except Exception as e:
            self.results["All the Changes made in the Classic Header  Screen are not Saved"] = f"Failed: {e}"

    def new_save(self):
        try:
            new_save(self.wait)
            self.results["All the Changes made in Create new style  Screen has been Saved"] = "Passed"
        except Exception as e:
            self.results["All the Changes made in the Create new style  Screen are not Saved"] = f"Failed: {e}"

    def fullwidth_border(self,value):
        try:
            fullwidth_border(self.wait,value)
            self.results["fullwidth_border value is added"] = "Passed"
        except Exception as e:
            self.results["fullwidth_bordervalue is not added"] = f"Failed: {e}"

    def padding(self,value):
        try:
            padding(self.wait,value)
            self.results["header_padding value is added"] = "Passed"
        except Exception as e:
            self.results["header_padding is not added"] = f"Failed: {e}"

    def cont_padding(self,value):
        try:
            cont_padding(self.wait,value)
            self.results["container padding value is added"] = "Passed"
        except Exception as e:
            self.results["container padding is not added"] = f"Failed: {e}"

    def header_height(self):
        try:
            header_height(self.wait)
            self.results["header_heightvalue is added"] = "Passed"
        except Exception as e:
            self.results["header_height is not added"] = f"Failed: {e}"

    def header_max_width(self):
        try:
            header_max_width(self.wait)
            self.results["header_max_width is added"] = "Passed"
        except Exception as e:
            self.results["header_max_width is not added"] = f"Failed: {e}"

    def open_homepage_override(self):
        try:
            open_homepage_override(self.wait)
            self.results["header_max_width is added"] = "Passed"
        except Exception as e:
            self.results["header_max_width is not added"] = f"Failed: {e}"

    def select_icon(self):
        try:
            select_icon(self.wait)
            self.results["Icon image is uploaded"] = "Passed"
        except Exception as e:
            self.results["Icon image is not uploaded"] = f"Failed: {e}"

    def select_size(self, size):
        try:
         select_size(self.wait, size)
         self.results["Icon Size is added"] = "Passed"
        except Exception as e:
         self.results["Icon Size is not added"] = f"Failed: {e}"


    def add_offset(self,x_value, y_value):
        try:
            add_offset(self,x_value, y_value)
            self.results["Text Padding value is added"] = "Passed"
        except Exception as e:
            self.results["Text Padding value is not added"] = f"Failed: {e}"

    def cart_margin(self,x_value, y_value):
        try:
            #cart_margin(self,x_value, y_value)
            self.results["Cart Margin value is added"] = "Passed"
        except Exception as e:
            self.results["Cart Margin value is not added"] = f"Failed: {e}"

    def click_tab_by_name(self,tab_name):
        try:
            click_tab_by_name(self.wait,tab_name)
            self.results["Topbar Tab is selected"] = "Passed"
        except Exception as e:
            self.results["Topbar Tab not selected"] = f"Failed: {e}"

    def  create_newstyle_btn(self):
        try:
            create_newstyle_btn(self.wait)
            self.results["Clicking on Create New Style button is successful"] = "Passed"
        except Exception as e:
            self.results["Clicking on Create New Style button  is not successful"] = f"Failed: {e}"

    def enter_stylelabel(self, variable_name):
        try:
            enter_stylelabel(self.wait, variable_name)
            self.results["Style label is entered"] = "Passed"
        except Exception as e:
            self.results["Style label is not entered"] = f"Failed: {e}"

    def menustyle_dropdown(self):
        try:
            menustyle_dropdown(self.wait)
            self.results["menustyle_dropdown is clicked successfuly"] = "Passed"
        except Exception as e:
            self.results["menustyle_dropdownis not successful"] = f"Failed: {e}"


    def cart_position(self):
        try:
            cart_position(self.wait)
            self.results["cart_position is clicked successfuly"] = "Passed"
        except Exception as e:
            self.results["cart_position button is not successful"] = f"Failed: {e}"

    def open_new_style_tabs(self):
        try:
            open_new_style_tabs(self.wait)
            self.results["Global tab is clicked successfuly"] = "Passed"
        except Exception as e:
            self.results["Clicking on Global tab is not successfull"] = f"Failed: {e}"

    def enter_margin(self, variable_name):
        try:
            enter_margin(self.wait, variable_name)
            self.results["{tab_name} tab is clicked successfuly"] = "Passed"
        except Exception as e:
               self.results["Clicking on {tab_name} tab is not successfull"] = f"Failed: {e}"

    def additional_option2(self, x, y, z):
        try:
            additional_option2(self.wait, x, y, z)  # pass self.wait instead of self
            self.results["additional_option2 values are entered"] = "Passed"
        except Exception as e:
            self.results["additional_option2 values are not entered"] = f"Failed: {e}"


        # --------------------------------------------------------------Menu border

    def open_general(self):
        open_general(self.wait)
    def open_main_menu2(self):
        open_main_menu2(self.wait)
    def close_main_menu2(self):
        close_main_menu2(self.wait)
    def open_desktop_menu(self):
        open_desktop_menu(self.wait)
    def close_desktop_menu(self):
        close_desktop_menu(self.wait)
    def open_site_overlay(self):
        open_site_overlay(self.wait)
    def menu_border(self, t_value, r_value):
        try:
            menu_border(self.wait, t_value, r_value)
            self.results["menu bordeer values are entered"] = "Passed"
        except Exception as e:
            self.results["menu bordeer values areentered"] = f"Failed: {e}"

    def side_margin(self, x_value, y_value):
        try:
            side_margin(self.wait, x_value, y_value)
            self.results["Side Margin values are entered"] = "Passed"
        except Exception as e:
            self.results["Side Margin values areentered"] = f"Failed: {e}"

        # ———————————————————————————————————————————————————————————————————————————————————————####Cart

    def cart_min_height(self):
        try:
            cart_min_height(self.wait)
            self.results["Cart max width is added"] = "Passed"
        except Exception as e:
            self.results["Cart max wiidth is not added"] = f"Failed: {e}"

        # ———————————————————————————————————————————————————————————————————————————————————————#### stiickey header starts

    def sticky_status_btn(self):
        try:
            sticky_status_btn(self)
            self.results["rsticky_status_ Button is clicked "] = "Passed"
        except Exception as e:
            self.results["sticky_status Button is not clicked "] = f"Failed: {e}"
        # ———————————————————————————————————————————————————————————————————————————————————————#### off canvas starts

    def open_off_canvas(self):
        try:
            open_off_canvas(self.wait)
            self.results["Off Canvas Menu on Desktop dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Off Canvas Menu on Desktop dropdown is not opened"] = f"Failed: {e}"

    def open_menu_trigger(self):
        try:
            open_menu_trigger(self.wait)
            self.results["Menu Trigger dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Menu Trigger dropdown is not opened"] = f"Failed: {e}"



#____________________________________
    def max_width(self):####deleted before copying it to classic run
        try:
            max_width1(self.wait)
            self.results["header_padding value is added"] = "Passed"
        except Exception as e:
            self.results["header_padding is not added"] = f"Failed: {e}"


            self.results["header_padding is not added"] = f"Failed: {e}"


    def side_offset(self):  ####
        try:
            side_offset(self.wait)
            self.results["header_padding value is added"] = "Passed"
        except Exception as e:
            self.results["header_padding is not added"] = f"Failed: {e}"

    def write_to_excel(self, folder_name="excel_results", file_name="slim_screen_result.xlsx"):
        write_to_excel(self.results, folder_name, file_name)

class TestFathershopTheme:
    @pytest.fixture(scope='class')
    def setup(self):
        chrome_driver_path = Driver_path
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        #driver.maximize_window()
        driver.set_window_size(1380, 1200)  # Set to a reasonable size

        yield driver
        driver.quit()

    def test_header_classic_functions(self, setup):
        driver = setup
        slim= Slim(driver)
        slim.login()
        slim.navigate_to_header_screen()
        slim.navigat_to_slim()
        slim.check_cache_btn()
        slim.duplicate()
        slim.filter_search("Slim")
        slim.create_new_btn()
        slim.header_name(" Test")
        slim.open_global_options()
        slim.header_color()
        slim.gradient()
        slim.camera()
        slim.padding("10")
        slim.fullwidth_border("10")
        slim.open_homepage_override()

        slim.click_tab_by_name("Logo")
        slim.header_color()
        slim.gradient()
        slim.camera()
        slim.cont_padding("10")
        slim.add_offset("10", "10")

        slim.click_tab_by_name("Top Bar")
        slim.header_color()
        slim.gradient()
        slim.camera()
        slim.fullwidth_border("10")
        slim.padding("10")
        # won't work because dropdown buttons menu is not accessible by selenium
        slim.click_tab_by_name("Top Menu")
        # classic.menustyle_dropdown()
        slim.click_tab_by_name("Top Menu 2")
        slim.create_newstyle_btn()
        slim.enter_stylelabel(" Test")
        # classic.open_new_style_tabs("Menu Item")
        slim.header_color()
        slim.gradient()
        slim.camera()
        slim.padding("10")
        slim.new_save()
        slim.click_tab_by_name("Secondary Menu")
        slim.click_tab_by_name("Language/Currency")
        slim.click_tab_by_name(" Search ")
        # ——————————————————————————————————————————————————————————————————————————————————————— Cart
        slim.click_tab_by_name("Cart")
        slim.cart_min_height()
        # ——————————————————————————————————————————————————————————————————————————————————————— Main Menu
        slim.click_tab_by_name("Main Menu")
        slim.open_general()
        slim.menu_border("10", "10")
        slim.open_main_menu2()
        slim.header_color()
        slim.side_margin("10", "20")

        slim.close_main_menu2()
        slim.open_desktop_menu()
        slim.gradient()
        slim.camera()
        slim.side_margin("10", "10")  # Fullwidthborder value
        slim.close_desktop_menu()
        slim.open_site_overlay()
        slim.max_width()
        slim.side_offset()

        # ——————————————————————————————————————————————————————————————————————————————————————— Off-Canvas
        slim.click_tab_by_name("Off Canvas Menu")
        slim.open_off_canvas()
        slim.open_menu_trigger()
        slim.header_color()
        slim.select_icon()
        slim.select_size("10")
        slim.gradient()
        slim.camera()
        slim.save()
        slim.edit()
        slim.open_global_options()
        slim.edit_header_color()
        slim.edit_gradient()
        slim.save()






