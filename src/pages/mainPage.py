from src.selenium_driver import selenium_driver
from src.pageLoc.locMainPage import locMainPage as MP

class mainPage(selenium_driver):
    def get_title(self):
        return self.get_element_text(MP.title)

    def write_name(self, name):
        self.write(MP.name, name, 10)

    def select_occupation(self, occupation):
        self.select_by_text(MP.occupation, occupation)

    def count_black_boxes(self):
        return len(self.search_elements(MP.black_box))

    def mark_radio(self, option):
        options = self.search_elements(MP.radio_options)
        options[option].click()

    def click_me(self):
        self.click_elem(MP.click_me)
    
    def get_class_from_red(self):
        return self.get_attribute(MP.red_box, 'class')

    def get_text_from_red(self):
        return self.get_element_text(MP.red_box)
