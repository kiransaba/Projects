import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from theme_constants import check_cache_btn,no_element_dropdown,\
create_new_btn,duplicate,delete,filter_search,edit,color,gradient,camera,save,click_back_btn,edit_gradient,edit_color
from setting_constant import USERNAME, PASSWORD, LOGIN_URL,Driver_path, write_to_excel,login
from styles_helpers import navigate_to_styles_screen
from typograpghy_helper import navigate_to_typograpghy,open_general,close_general,open_text_link,close_text_link,open_headings,close_headings,open_other_elements,close_other_elements,select_icon,select_size,open_blockquote,\
close_blockquote, open_drop_cap,open_ampersand,close_drop_cap,close_ampersand,open_horizontal,close_horizontal,open_font_render,close_font_render,open_table,close_table,open_responsive_video,close_responsive_video,click_icon_tab,click_container_styles,additional_option2,\
padding,margin,new_label
class Typography:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.results = {}

    def login(self):
        try:
            login(self.wait, USERNAME, PASSWORD)
            self.results["Fathersshop Login"] = " Passed"
        except Exception as e:
            self.results["Fathersshop Login"] = f" Failed: {e}"

    def navigate_to_styles_scree(self):
       try:
         navigate_to_styles_screen(self)
         self.results["Navigation to Styles Screen"] = "Passed"
       except Exception as e:
         self.results["Navigation to Styles Screen"] = f"Failed: {e}"

    def navigate_to_typograpghy(self):
      try:
          navigate_to_typograpghy(self)
          self.results["Navigation to header Screen"] = "Passed"
      except Exception as e:
          self.results["Navigation to headerer Screen"] = f"Failed: {e}"

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

    def create_new_btn(self):
        try:
            create_new_btn(self.wait)
            self.results["Create New Button is clicked "] = "Passed"
        except Exception as e:
            self.results["Create New Button is not clicked "] = f"Failed: {e}"

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

    def click_back_btn(self):
        try:
            click_back_btn(self.wait)
            self.results["Back button on Footer Screen is working"] = "Passed"
        except Exception as e:
            self.results["Back button on Footer Screen is not working"] = f"Failed: {e}"

    def click_icon_tab(self):
        try:
            click_icon_tab(self.wait)
            self.results["Horizontal:Icon Tab is working"] = "Passed"
        except Exception as e:
            self.results["Horizontal:Icon Tab on is not working"] = f"Failed: {e}"

    def save(self):
        try:
            save(self.wait)
            self.results["All the Changes made in the Classic Header  Screen has been Saved"] = "Passed"
        except Exception as e:
            self.results["All the Changes made in the Classic Header  Screen are not Saved"] = f"Failed: {e}"

    def new_save(self):
        try:
           # new_save(self.wait)
            self.results["All the Changes made in Create new style  Screen has been Saved"] = "Passed"
        except Exception as e:
            self.results["All the Changes made in the Create new style  Screen are not Saved"] = f"Failed: {e}"

    def color(self):
        try:
            color(self.wait)
            self.results["The Icon Color has been selected"] = "Passed"
        except Exception as e:
            self.results["The Icon Color has not been selected"] = f"Failed: {e}"

    def edit_color(self):
        try:
            edit_color(self)
            self.results["The Icon Color has been edited"] = "Passed"
        except Exception as e:
            self.results["The Icon Color is not edited"] = f"Failed: {e}"

    def new_label(self, variable_name):
       try:
        self.results["Style label has been added"] = "Passed"
        new_label(self.wait, variable_name)
       except Exception as e:
        self.results["Style label  is not added"] = f"Failed: {e}"

    def select_icon(self):
        try:
            select_icon(self.wait)
            self.results["Icon image is uploaded"] = "Passed"
        except Exception as e:
            self.results["Icon image is not uploaded"] = f"Failed: {e}"

    def select_size(self,size):
        try:
            select_size(self.wait,size)
            self.results["Icon Size is added"] = "Passed"
        except Exception as e:
            self.results["Icon Size is not added"] = f"Failed: {e}"


    def click_container_styles(self):
        try:
            click_container_styles(self.wait)
            self.results["Clicking on container_stylesbutton is successful"] = "Passed"
        except Exception as e:
            self.results["container_styles button clicking is not successful"] = f"Failed: {e}"


    def additional_option2(self, x,y,z):
        try:
            additional_option2(self.wait,x,y,z)  # pass self.wait instead of self
            self.results["additional_option2 values are entered"] = "Passed"
        except Exception as e:
            self.results["additional_option2 values are not entered"] = f"Failed: {e}"

    def padding(self,value):
        try:
            padding(self.wait,value)
            self.results["Padding value is added"] = "Passed"
        except Exception as e:
            self.results[" Padding value is not added"] = f"Failed: {e}"

    def margin(self,value):
       try:
             margin(self.wait,value)
             self.results["Padding value is added"] = "Passed"
       except Exception as e:
            self.results[" Padding value is not added"] = f"Failed: {e}"



################################################Dropdown Methods

    def open_general(self):
        try:
            open_general(self.wait)
            self.results["General dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["General dropdown is not opened"] = f"Failed: {e}"

    def close_general(self):
     try:
        close_general(self.wait)
        self.results["Main Menu 2 dropdown  is closed"] = "Passed"
     except Exception as e:
         self.results["Main Menu 2 dropdown is not closed"] = f"Failed: {e}"

    def open_text_link(self):
        try:
            open_text_link(self.wait)
            self.results["Text Link dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Text Link dropdown is not opened"] = f"Failed: {e}"
    def close_text_link(self):
     try:
        close_text_link(self.wait)
        self.results["Text Link dropdown  is closed"] = "Passed"
     except Exception as e:
         self.results["Text Link dropdown is not closed"] = f"Failed: {e}"

    def open_headings(self):
        try:
            open_headings(self.wait)
            self.results["Headngs dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Headings dropdown is not opened"] = f"Failed: {e}"

    def close_headings(self):
        try:
            close_headings(self.wait)
            self.results["Text Link dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Text Link dropdown is not closed"] = f"Failed: {e}"

    def open_other_elements(self):
        try:
            open_other_elements(self.wait)
            self.results["Other_elements dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Other_elements dropdown is not opened"] = f"Failed: {e}"

    def close_other_elements(self):
        try:
            close_other_elements(self.wait)
            self.results["Other_elements dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Other_elementsdropdown is not closed"] = f"Failed: {e}"

    def open_blockquote(self):
        try:
            open_blockquote(self.wait)
            self.results["Blockquote dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Blockquote dropdown is not opened"] = f"Failed: {e}"

    def close_blockquote(self):
        try:
            close_blockquote(self.wait)
            self.results["Blockquote dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Blockquote dropdown is not closed"] = f"Failed: {e}"
    def open_drop_cap(self):
        try:
            open_drop_cap(self.wait)
            self.results["Drop Cap dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Drop Cap dropdown is not opened"] = f"Failed: {e}"

    def close_drop_cap(self):
        try:
            close_drop_cap(self.wait)
            self.results["Drop Cap dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Drop Cap dropdown is not closed"] = f"Failed: {e}"

    def open_ampersand(self):
        try:
            open_ampersand(self.wait)
            self.results["Ampersanddropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Ampersand dropdown is not opened"] = f"Failed: {e}"

    def close_ampersand(self):
        try:
            close_ampersand(self.wait)
            self.results["Ampersand dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Ampersand dropdown is not closed"] = f"Failed: {e}"

    def open_horizontal(self):
        try:
            open_horizontal(self.wait)
            self.results["Horizontal Rule dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Horizontal Rule dropdown is not opened"] = f"Failed: {e}"

    def close_horizontal(self):
        try:
            close_horizontal(self.wait)
            self.results["Horizontal Rule dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Horizontal Rule dropdown is not closed"] = f"Failed: {e}"


    def open_font_render(self):
        try:
            open_font_render(self.wait)
            self.results["Font Rendering dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Font Rendering dropdown is not opened"] = f"Failed: {e}"

    def close_font_render(self):
        try:
            close_font_render(self.wait)
            self.results["Ampersand dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Ampersand dropdown is not closed"] = f"Failed: {e}"
    def open_table(self):
        try:
            open_table(self.wait)
            self.results["Table dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Table Rendering dropdown is not opened"] = f"Failed: {e}"

    def close_table(self):
        try:
            close_table(self.wait)
            self.results["Table dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Table dropdown is not closed"] = f"Failed: {e}"

    def open_responsive_video(self):
        try:
            open_responsive_video(self.wait)
            self.results["Responsive Video dropdown is opened"] = "Passed"
        except Exception as e:
            self.results["Responsive Video dropdown is not opened"] = f"Failed: {e}"

    def close_responsive_video(self):
        try:
            close_responsive_video(self.wait)
            self.results["Responsive Video dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Responsive Video dropdown is not closed"] = f"Failed: {e}"

    def write_to_excel(self, folder_name="excel_results", file_name="typography_result.xlsx"):
        write_to_excel(self.results, folder_name, file_name)
#————————————————————————————————————————————————————
class TestFathershopTheme:
    @pytest.fixture
    def setup(self):
        chrome_driver_path = Driver_path
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        yield driver
        driver.quit()

#———————————————————————————————————————————————————————
    def test_styles_functions(self, setup):
        driver = setup

        typo = Typography(driver)
        typo.login()
        typo.write_to_excel()

        typo.navigate_to_styles_scree()
        typo.write_to_excel()

        typo.navigate_to_typograpghy()
        typo.write_to_excel()

        typo.check_cache_btn()
        typo.write_to_excel()

        typo.duplicate()
        typo.write_to_excel()
        
        typo.filter_search("Def")
        typo.write_to_excel()

        typo.create_new_btn()
        typo.write_to_excel()

        typo.new_label("Test Typo")
        typo.write_to_excel()

        typo.open_general()
        typo.write_to_excel()
        typo.color()
        typo.write_to_excel()
        #typo.additional_option2("10","10","5")
        #typo.write_to_excel()

        typo.close_general()
        typo.write_to_excel()

        typo.open_text_link()
        typo.write_to_excel()
        typo.color()
        typo.write_to_excel()
        typo.close_text_link()
        typo.write_to_excel()

        typo.open_headings()
        typo.write_to_excel()
        typo.color()
        typo.write_to_excel()
        typo.gradient()
        typo.write_to_excel()
        typo.camera()
        typo.write_to_excel()
        typo.margin("20")
        typo.write_to_excel()
        typo.padding("10")
        typo.write_to_excel()
        typo.close_headings()
        typo.write_to_excel()

        typo.open_other_elements()
        typo.write_to_excel()
        typo.color()
        typo.write_to_excel()
        typo.gradient()
        typo.write_to_excel()
        typo.camera()
        typo.write_to_excel()
        typo.margin("20")
        typo.write_to_excel()
        typo.padding("10")
        typo.write_to_excel()
        typo.close_other_elements()
        typo.write_to_excel()
        driver.execute_script("window.scrollTo(0, 0);") #for scrolliing up

        typo.open_blockquote()
        typo.write_to_excel()
        typo.select_icon()
        typo.write_to_excel()
        typo.color()
        typo.write_to_excel()
        typo.select_size("10")
        typo.write_to_excel()
        #typo.click_container_styles()
        #typo.color()
        #typo.gradient()
        #typo.camera()
        #typo.margin("20")
        #typo.padding("10")
        typo.close_blockquote()
        typo.write_to_excel()
        driver.execute_script("window.scrollTo(0, 0);")

        typo.open_drop_cap()
        typo.write_to_excel()
        typo.color()
        typo.write_to_excel()
        typo.close_drop_cap()
        typo.write_to_excel()

        typo.open_ampersand()
        typo.write_to_excel()
        typo.select_icon()
        typo.write_to_excel()
        typo.color()
        typo.write_to_excel()
        typo.select_size("10")
        typo.write_to_excel()
        typo.close_ampersand()
        typo.write_to_excel()
        driver.execute_script("window.scrollTo(0, 0);")

        typo.open_horizontal()
        typo.write_to_excel()
        typo.color()
        typo.write_to_excel()
        typo.gradient()
        typo.write_to_excel()
        typo.camera()
        typo.write_to_excel()
        #typo.click_icon_tab()
        #typo.write_to_excel()
        #typo.select_icon()
        #typo.write_to_excel()
        #typo.color()
        #typo.write_to_excel()
        #typo.gradient()
        #typo.write_to_excel()
        typo.close_horizontal()
        typo.write_to_excel()
        driver.execute_script("window.scrollTo(0, 0);")

        typo.open_font_render()
        typo.write_to_excel()
        #just check
        typo.close_font_render()
        typo.write_to_excel()
        typo.open_table()
        typo.write_to_excel()
        typo.close_table()
        typo.write_to_excel()
        driver.execute_script("window.scrollTo(0, 0);")

        typo.open_responsive_video()
        typo.write_to_excel()
        typo.color()
        typo.write_to_excel()
        typo.gradient()
        typo.write_to_excel()
        typo.camera()
        typo.write_to_excel()
        typo.margin("20")
        typo.write_to_excel()
        typo.padding("10")
        typo.write_to_excel()

        typo.close_responsive_video()
        typo.write_to_excel()

        typo.save()
        typo.write_to_excel()

        typo.edit()
        typo.open_general()
        typo.edit_color()
        typo.save()
        typo.click_back_btn()


#———————————————————————————————————————————————————————


