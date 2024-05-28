import pytest
from selenium import webdriver
from theme_constants import click_back_btn, edit_gradient,check_cache_btn,no_element_dropdown,create_new_btn,duplicate,delete,filter_search,gradient,camera,save,edit,color,edit_color
from setting_constant import USERNAME, PASSWORD, LOGIN_URL,Driver_path, write_to_excel,login
from selenium.webdriver.support.ui import WebDriverWait
from header_helpers import navigate_to_header_screen,additional_option2,select_icon,select_size
from classic_helper import navigat_to_classic,open_global_options,fullwidth_border,header_height,max_width1,open_homepage_override,menustyle_dropdown,\
click_tab_by_name,cont_padding,header_max_width,side_offset,new_save,header_name,padding
from button_helpers import enter_stylelabel,create_newstyle_btn,open_new_style_tabs,add_offset,enter_margin,cart_position,cart_min_height,sticky_status_btn,open_menu_trigger,open_off_canvas,\
open_general,open_main_menu2,close_main_menu2,open_desktop_menu,close_desktop_menu,open_site_overlay,menu_border,side_margin

class Classic:
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

    def navigat_to_classic(self):
        try:
            navigat_to_classic(self.wait)
            self.results["Classic Screen is opened"] = "Passed"
        except Exception as e:
            self.results["Classic Screen is not opened"] = f"Failed: {e}"

#----------------------------------------------------
    def check_cache_btn(self):
        try:
            check_cache_btn(self.wait)
            self.results["Cache button is clicked & working"] = "Passed"
        except Exception as e:
            self.results["Cache button s clicked & not working "] = f"Failed: {e}"

    def no_element_dropdown(self):
        try:
            no_element_dropdown(self.wait)
            self.results["No_of elements button clicking & list is showing"] = "Passed"
        except Exception as e:
            self.results["No_of elements button clicking & list is not showing"] = f" is Failed: {e}"

    def duplicate(self):
        try:
            duplicate(self.wait)
            self.results["Clicking on Footer duplicate button is successful"] = "Passed"
        except Exception as e:
            self.results["Footer duplicate button clicking is not successful"] = f"Failed: {e}"

    def delete(self):
        try:

            delete(self.wait)
            self.results["Clicking on Footer delete button is successful"] = "Passed"
        except Exception as e:
            self.results["Footer delete button clicking is not successful"] = f"Failed: {e}"

    def filter_search(self, search_term):
        try:
            filter_search(self.wait, search_term)
            self.results["Footer Search is showing the desired result"] = "Passed"
        except Exception as e:
            self.results["Footer Filter Search is not working"] = f"Failed: {e}"

    def edit(self):
        try:
            edit(self.wait)
            self.results["Edit button on Footer Screen is working "] = "Passed"
        except Exception as e:
            self.results["Edit button on Footer Screen is not working "] = "Passed"

    def click_back_btn(self):
        try:
            click_back_btn(self.wait)
            self.results["Back button on Footer Screen is working"] = "Passed"
        except Exception as e:
            self.results["Back button on Footer Screen is not working"] = f"Failed: {e}"

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

    def color(self):
        try:
            color(self.wait)
            self.results["The Icon Color has been selected"] = "Passed"
        except Exception as e:
            self.results["The Icon Color has not been selected"] = f"Failed: {e}"

    def edit_color(self):
        try:
            edit_color(self.wait)
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

    def write_to_excel(self, folder_name="excel_results", file_name="classic_screen_result.xlsx"):
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
    def test_header_classic_functions(self, setup):
        driver = setup
        classic= Classic(driver)
        classic.login()
        classic.navigate_to_header_screen()
        classic.navigat_to_classic()
        classic.check_cache_btn()
        classic.duplicate()
        classic.filter_search("Classic")
        classic.create_new_btn()
        classic.open_global_options()
        classic.header_name(" Test")
        classic.color()
        classic.gradient()
        classic.camera()
        classic.padding("10")
        classic.fullwidth_border("10")
        classic.open_homepage_override()
        classic.click_tab_by_name("Logo")
        classic.color()
        classic.gradient()
        classic.camera()
        classic.cont_padding("10")
        classic.add_offset("10", "10")
        classic.click_tab_by_name("Top Bar")
        classic.color()
        classic.gradient()
        classic.camera()
        classic.fullwidth_border("10")
        classic.padding("10")
        classic.click_tab_by_name("Top Menu")
        # classic.menustyle_dropdown()
        classic.click_tab_by_name("Top Menu 2")
        classic.create_newstyle_btn()
        classic.enter_stylelabel(" Test")
        # classic.open_new_style_tabs("Menu Item")
        classic.color()
        classic.gradient()
        classic.camera()
        classic.padding("10")
        classic.new_save()
        classic.click_tab_by_name("Secondary Menu")
        classic.click_tab_by_name("Language/Currency")
        classic.click_tab_by_name("Search")
        # ——————————————————————————————————————————————————————————————————————————————————————— Cart
        classic.click_tab_by_name("Cart")
        classic.cart_min_height()
        # ——————————————————————————————————————————————————————————————————————————————————————— Main Menu
        classic.click_tab_by_name("Main Menu")
        classic.open_general()
        classic.menu_border("10", "10")
        classic.open_main_menu2()
        classic.color()
        classic.side_margin("10", "20")
        classic.close_main_menu2()
        classic.open_desktop_menu()
        classic.gradient()
        classic.camera()
        classic.side_margin("10", "10")  # Fullwidthborder value
        classic.close_desktop_menu()
        classic.open_site_overlay()
        classic.max_width()
        classic.side_offset()
        # ——————————————————————————————————————————————————————————————————————————————————————— Off-Canvas
        classic.click_tab_by_name("Off Canvas Menu")
        classic.open_off_canvas()
        classic.open_menu_trigger()
        classic.color()
        classic.select_icon()
        classic.select_size("10")
        classic.gradient()
        classic.camera()
        classic.save()
        classic.edit()
        classic.open_global_options()
        classic.edit_color()
        classic.edit_gradient()
        classic.save()





#-------------------------------------------------






