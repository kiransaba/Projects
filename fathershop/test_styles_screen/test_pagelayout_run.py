import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from theme_constants import check_cache_btn,no_element_dropdown,create_new_btn,\
duplicate,delete,filter_search,edit,color,gradient,camera,image_options,save,click_back_btn,edit_color,edit_gradient,edit_camera
from setting_constant import USERNAME, PASSWORD, LOGIN_URL,Driver_path, write_to_excel,login
from styles_helpers import navigate_to_styles_screen, new_label,select_options,open_general,open_site_container,open_content_container,open_side_column,max_width_btn,add_Padding,close_general,close_site_container,close_content_container,close_side_column,open_right_column,\
close_right_column,open_boxedoption,close_boxedoption,col_btn,select_none,click_up_btn
class GlobalStyles:
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

    def navigate_to_styles_screen(self):
        try:
            navigate_to_styles_screen(self)
            self.results["Navigation to Styles Screen"] = "Passed"
        except Exception as e:
            self.results["Navigation to Styles Screen"] = f"Failed: {e}"

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
            self.results["Footer Create New Button is working"] = "Passed"
        except Exception as e:
            self.results["Footer Create New Button is not working"] = f"Failed: {e}"

    def color(self):
        try:
            color(self.wait)
            self.results["In Background Color has been selected"] = "Passed"
        except Exception as e:
            self.results["In Background Color has not been selected"] = f"Failed: {e}"

    def gradient(self):
        try:
            gradient(self.wait)
            self.results["In Background Gradient has been selected"] = "Passed"
        except Exception as e:
            self.results["In Background Gradient has not been selected"] = f"Failed: {e}"

    def edit_color(self):
        try:
            edit_color(self)
            self.results["In Background Color has been edited"] = "Passed"

        except Exception as e:
            self.results["In Background Color is not edited"] = f"Failed: {e}"

    def edit_gradient(self):
        try:
            edit_gradient(self.wait)
            self.results["In Background Gradient has been edited"] = "Passed"
        except Exception as e:
            self.results["In Background Gradient is not edited"] = f"Failed: {e}"

    def camera(self):
        try:
            camera(self.wait)
            self.results["In Background Camera Image has been selected"] = "Passed"
        except Exception as e:
            self.results["In Background Camera Image has not been selected"] = f"Failed: {e}"

    def image_options(self):
        try:
            image_options(self.wait)
            self.results["In Background Image Options has been selected"] = "Passed"
        except Exception as e:
            self.results["In Background Image Options has not been selected"] = f"Failed: {e}"

    def save(self):
        try:
            save(self.wait)
            self.results["All the Changes made in the Footer Screen has been Saved"] = "Passed"
        except Exception as e:
            self.results["All the Changes made in the Footer Screen are not Saved"] = f"Failed: {e}"

    def new_label(self, variable_name):

        try:
            new_label(self.wait, variable_name)
            self.results["Style Label is added"] = "Passed"
        except Exception as e:
            self.results["Error occurred on adding the style label in the text field"] = f"Failed: {e}"


    def  select_options(self):
         select_options(self.wait, self.driver)

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

    def open_boxedoption(self):
        try:
            open_boxedoption(self.wait)
            self.results["Boxed_Option dropdown  is opened"] = "Passed"
        except Exception as e:
            self.results["Boxed_Option dropdown is not opened"] = f"Failed: {e}"

    def close_boxedoption(self):
        try:
            close_boxedoption(self.wait)
            self.results["Boxed_Option dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Boxed_Option dropdown is not closed"] = f"Failed: {e}"
    def open_site_container(self):
        try:
            open_site_container(self.wait)
            self.results["Site Container  dropdown  is opened"] = "Passed"
        except Exception as e:
            self.results["Site Container  dropdown is not opened"] = f"Failed: {e}"
    def close_site_container(self):

        try:
            close_site_container(self.wait)
            self.results["Site Container dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Site Container  dropdown is not closed"] = f"Failed: {e}"
    def open_content_container(self):
        try:
            open_content_container(self.wait)
            self.results["Content Container dropdown  is opened"] = "Passed"
        except Exception as e:
            self.results["Content Container dropdown is not opened"] = f"Failed: {e}"

    def close_content_container(self):
        try:
            close_content_container(self.wait)
            self.results["Content Container dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Content Container dropdown is not closed"] = f"Failed: {e}"

    def open_side_column(self):
        try:
            open_side_column(self.wait)
            self.results["Side column dropdown  is opened"] = "Passed"
        except Exception as e:
            self.results["Side column dropdown is not opened"] = f"Failed: {e}"

    def close_side_column(self):
        try:
            close_side_column(self.wait)
            self.results["Side column dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Error occurred on closing the Side column dropdown"] = f"Failed: {e}"

    def open_right_column(self):
        try:
            open_right_column(self.wait)
            self.results["Right column dropdown  is opened"] = "Passed"
        except Exception as e:
            self.results["Right column dropdown is not opened"] = f"Failed: {e}"


    def close_right_column(self):
        try:
            close_right_column(self.wait)
            self.results["Right Column dropdown  is closed"] = "Passed"
        except Exception as e:
            self.results["Error occurred on closing the Right Column dropdown"] = f"Failed: {e}"

    def max_width_btn(self):

        try:
            max_width_btn(self.wait)
            self.results["Max Width value is added"] = "Passed"
        except Exception as e:
            self.results[" Max Width  value is not added"] = f"Failed: {e}"

    def click_up_btn(self):
        try:
            click_up_btn(self.wait)
            self.results["Increase button is clicked & value is updated"] = "Passed"
        except Exception as e:
            self.results["Increase button is not clicked"] = f"Failed: {e}"

    def add_Padding(self, value):
        try:
            add_Padding(self.wait, value)
            self.results["Padding value is added"] = "Passed"
        except Exception as e:
            self.results[" Padding value is not added"] = f"Failed: {e}"
    def col_btn(self):
        col_btn(self.wait)

    def select_none(self):

        try:
            select_none(self.wait)
            self.results["None button is clicked"] = "Passed"
        except Exception as e:
            self.results["Error occurred on clicking the None button"] = f"Failed: {e}"


    def edit_camera(self):
        try:
            edit_camera(self.wait)
            self.results["Camera Image is edited"] = "Passed"
        except Exception as e:
            self.results["Camera Image is not changed"] = f"Failed: {e}"

    def write_to_excel(self, folder_name="excel_results", file_name="pagelayout_result.xlsx"):
        write_to_excel(self.results, folder_name, file_name)
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class TestFathershopTheme:
    @pytest.fixture
    def setup(self):
        chrome_driver_path = Driver_path
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        yield driver
        driver.quit()
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    def test_styles_functions(self, setup):
        driver = setup
        styles = GlobalStyles(driver)
        styles.login()
        styles.write_to_excel()
        styles.navigate_to_styles_screen()
        styles.write_to_excel()
        styles.check_cache_btn()
        styles.write_to_excel()
        styles.filter_search("Def")
        styles.write_to_excel()
        styles.create_new_btn()
        styles.write_to_excel()
        styles.new_label(" Test")
        styles.write_to_excel()
        styles.open_general()
        styles.write_to_excel()
        styles.select_options()
        styles.write_to_excel()
        styles.color()
        styles.write_to_excel()
        styles.gradient()
        styles.write_to_excel()
        styles.camera()
        styles.write_to_excel()
        styles.close_general()
        styles.write_to_excel()
        # ——————————————————————————————————————
        styles.open_boxedoption()
        styles.write_to_excel()
        styles.max_width_btn()
        styles.write_to_excel()
        styles.add_Padding("10")
        styles.write_to_excel()
        styles.color()
        styles.write_to_excel()
        styles.close_boxedoption()
        styles.write_to_excel()
        #—————————————————————————————————————————————
        styles.open_site_container()
        styles.write_to_excel()
        #styles.max_width_btn()
        styles.click_up_btn()
        styles.write_to_excel()
        styles.color()
        styles.write_to_excel()
        styles.gradient()
        styles.write_to_excel()
        styles.camera()
        styles.write_to_excel()
        styles.add_Padding("10")
        styles.write_to_excel()
        styles.close_site_container()
        styles.write_to_excel()
#——————————————————————————————————————————
        styles.open_content_container()
        styles.write_to_excel()
        #styles.max_width_btn()
        styles.click_up_btn()
        styles.write_to_excel()
        styles.color()
        styles.write_to_excel()
        styles.gradient()
        styles.write_to_excel()
        styles.camera()
        styles.write_to_excel()
        styles.close_content_container()
        styles.write_to_excel()
#———————————————————————————————————
        styles.open_side_column()
        styles.write_to_excel()
        styles.col_btn()
        styles.click_up_btn()
        styles.write_to_excel()
        styles.color()
        styles.write_to_excel()
#——————————————————————————————————
        styles.open_right_column()
        styles.write_to_excel()
        styles.select_none()
        styles.write_to_excel()
        styles.save()
        styles.write_to_excel()
#———————-————————————————
        styles.edit()
        styles.write_to_excel()
        styles.open_general()
        styles.write_to_excel()
        styles.edit_color()
        styles.write_to_excel()
        styles.edit_gradient()
        styles.write_to_excel()
        styles.edit_camera()
        styles.write_to_excel()
        styles.save()
        styles.write_to_excel()


