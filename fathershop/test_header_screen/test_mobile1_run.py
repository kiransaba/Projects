import pytest
from selenium import webdriver
from theme_constants import click_back_btn, edit_gradient,check_cache_btn,no_element_dropdown,create_new_btn,duplicate,delete,filter_search,gradient,camera,save,edit
from selenium.webdriver.support.ui import WebDriverWait
from setting_constant import USERNAME, PASSWORD, LOGIN_URL,Driver_path, write_to_excel,login
from header_helpers import navigate_to_header_screen,additional_option2,header_color,select_icon,select_size,edit_header_color
from classic_helper import navigat_to_moble_1,open_global_options,fullwidth_border,padding,header_height,max_width1,open_homepage_override,menustyle_dropdown,\
click_tab_by_name,cont_padding,header_max_width,side_offset,new_save,mob_header_name
from button_helpers import enter_stylelabel,create_newstyle_btn,open_new_style_tabs,add_offset,enter_margin,cart_position,cart_min_height,sticky_status_btn,open_menu_trigger,open_off_canvas,\
open_general,close_main_menu2,open_desktop_menu,close_desktop_menu,open_site_overlay,menu_border,side_margin,open_menu_name,open_count_badge,open_menu1,name_ofset



class Mobile1:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
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

    def navigat_to_moble_1(self):
        try:
            navigat_to_moble_1(self.wait)
            self.results["Mobile_1 Screen is opened"] = "Passed"
        except Exception as e:
            self.results["Mobile_1 Screen is not opened"] = f"Failed: {e}"

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
    def mob_header_name(self,name1):#####################################
        try:
            mob_header_name(self.wait,name1)
            self.results["Mobileheader name is added"] = "Passed"
        except Exception as e:
            self.results["Mobile header name is not added"] = f"Failed: {e}"

    def enter_menu_name(self,name2):#####################################
        try:
            mob_header_name(self.wait,name2)
            self.results["Mobile Menu name is added"] = "Passed"
        except Exception as e:
            self.results["Mobile Menu header name is not added"] = f"Failed: {e}"

    def open_menu_name(self):
        try:
            open_menu_name(self.wait)
            self.results["Menu Name dropdown is clicked "] = "Passed"
        except Exception as e:
            self.results["Menu Name dropdown is not clicked "] = f"Failed: {e}"

    def open_count_badage(self):
        try:
            open_count_badge(self.wait)
            self.results["Count Badge dropdown is clicked "] = "Passed"
        except Exception as e:
            self.results["Count Badge dropdown is not clicked "] = f"Failed: {e}"


    def open_menu1(self):
        try:
            open_menu1(self.wait)
            self.results["Menu1 dropdown is clicked "] = "Passed"
        except Exception as e:
            self.results["Menu1 dropdown is not clicked "] = f"Failed: {e}"

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

    def padding(self,value):    ##############################Pading
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
        try:
            open_general(self.wait)
            self.results["General dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["General dropdown is not opened"] = f"Failed: {e}"

    def close_main_menu2(self):
     try:
        close_main_menu2(self.wait)
        self.results["Main Menu 2 dropdown  is closed"] = "Passed"
     except Exception as e:
         self.results["Main Menu 2 dropdown is not closed"] = f"Failed: {e}"

    def open_desktop_menu(self):
       try:
         open_desktop_menu(self.wait)
         self.results["Desktop Menu  dropdown  is opened"] = "Passed"
       except Exception as e:
         self.results["Desktop Menu dropdown  is opened "] = f"Failed: {e}"

    def close_desktop_menu(self):
      try:
        close_desktop_menu(self.wait)
        self.results["Desktop Menu  dropdown  is closed"] = "Passed"
      except Exception as e:
       self.results["Desktop Menu  dropdown  is not closed"] = f"Failed: {e}"

    def open_site_overlay(self):
      try:
         open_site_overlay(self.wait)
         self.results["Site Overlay  dropdown  is opened"] = "Passed"
      except Exception as e:
          self.results["Site Overlay  dropdown  is not opened"] = f"Failed: {e}"

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
            self.results["sticky_status_ Button is clicked "] = "Passed"
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
    def max_width(self):
        try:
            max_width1(self.wait)
            self.results["mobile_max width value is added"] = "Passed"
        except Exception as e:
            self.results["mobile_padding is not added"] = f"Failed: {e}"


            self.results["mobile_max width is not added"] = f"Failed: {e}"
#---------------------------------------

    def side_offset(self):  ####
        try:
            side_offset(self.wait)
            self.results["mobile_padding value is added"] = "Passed"
        except Exception as e:
            self.results["mobile_padding is not added"] = f"Failed: {e}"

    def name_ofset(self,value1, value2):  ####
        try:
            name_ofset(self.wait,value1, value2)
            self.results["Menu mane offset value is added"] = "Passed"
        except Exception as e:
            self.results["Menu mane offset is not added"] = f"Failed: {e}"

    def write_to_excel(self, folder_name="excel_results", file_name="mobile1_screen_result.xlsx"):
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

    def test_header_mobile_functions(self, setup):
        driver = setup
        mob1 = Mobile1(driver)

        mob1.login()
        mob1.write_to_excel()
        mob1.navigate_to_header_screen()
        mob1.write_to_excel()
        mob1.navigat_to_moble_1()

        mob1.write_to_excel()
        mob1.check_cache_btn()
        mob1.write_to_excel()
        mob1.duplicate()
        mob1.write_to_excel()
        mob1.filter_search("mobile")
        mob1.write_to_excel()
        mob1.write_to_excel()
        mob1.create_new_btn()
        mob1.write_to_excel()
        mob1.write_to_excel()
        mob1.mob_header_name(" Test")
        mob1.write_to_excel()
        mob1.header_color()
        mob1.write_to_excel()
        mob1.gradient()
        mob1.camera()
        mob1.click_tab_by_name("Top Bar")
        mob1.header_color()
        mob1.gradient()
        mob1.camera()
        mob1.side_offset()
        # mob1.padding("10") #not fndng the Id

        mob1.click_tab_by_name("Top Menu")
        mob1.create_newstyle_btn()
        mob1.write_to_excel()
        mob1.enter_stylelabel(" Test")
        mob1.write_to_excel()
        mob1.header_color()
        mob1.write_to_excel()
        mob1.gradient()
        mob1.write_to_excel()
        mob1.camera()
        mob1.write_to_excel()
        mob1.new_save()
        mob1.click_tab_by_name("Language/Currency")
        mob1.write_to_excel()
        mob1.click_tab_by_name("Logo")
        mob1.header_color()
        mob1.gradient()
        mob1.camera()
        mob1.name_ofset("10", "10")
        # ——————————————————————————————————————————————————————————————————————————————————————— Custom Menus Menu
        mob1.click_tab_by_name("Main Menu")
        mob1.open_general()
        mob1.select_icon()
        mob1.select_size("10")
        mob1.header_color()
        mob1.camera()
        mob1.gradient()
        mob1.open_menu_name()
        mob1.enter_menu_name("Menu Test")
        mob1.write_to_excel()
        mob1.click_tab_by_name("Search")
        mob1.open_menu_trigger()
        mob1.select_icon()
        mob1.write_to_excel()
        mob1.header_color()
        mob1.gradient()
        mob1.camera()
        #mob1.enter_menu_name("Test Menu") #not finding the element Id
        # ——————————————————————————————————————————————————————————————————————————————————————— Cart
        mob1.click_tab_by_name("Cart")
        mob1.open_general()
        mob1.write_to_excel()
        mob1.select_icon()
        mob1.select_size("10")
        mob1.header_color()
        mob1.open_menu_name()
        mob1.write_to_excel()
        #mob1.enter_menu_name(" Test Name") #not finding the element Id
        mob1.open_count_badage()
        mob1.name_ofset("10","10")
        # ——————————————————————————————————————————————————————————————————————————————————————— Sticky Header
        mob1.click_tab_by_name("Custom Menus")
        # classic.sticky_status_btn()
        mob1.open_menu1()
        mob1.write_to_excel()
        mob1.header_color()
        mob1.gradient()
        mob1.write_to_excel()
        mob1.camera()
        mob1.write_to_excel()
        mob1.open_menu_name()
        mob1.write_to_excel()
        mob1.name_ofset("10","10")
        mob1.open_count_badage()
        # ——————————————————————————————————————————————————————————————————————————————————————— Sticky Header
        mob1.click_tab_by_name("Sticky Header")
        # classic.sticky_status_btn()
        mob1.header_color()
        mob1.gradient()
        mob1.camera()
        mob1.save()














