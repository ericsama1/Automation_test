from src.selenium_driver import selenium_driver
from src.pageLoc.locMainPage import locMainPage as MP

class mainPage(selenium_driver):
    def get_title(self):
        title = self.driver.find_element_by_tag_name('title')
        return title.get_attribute('text')

    def write_name(self, name):
        self.write(MP.name, name, 10)

    def select_occupation(self, occupation):
        self.select_by_text(MP.occupation, occupation)

    def count_black_boxes(self):
        timeout = 5
        return len(self.search_elements(MP.black_box, timeout))

    def mark_radio(self, option):
        self.click_elem(MP.radio_option.format(option))

    def click_me(self):
        self.click_elem(MP.click_me)

    def link1(self):
        self.click_elem(MP.link1)
    
    def link2(self):
        self.click_elem(MP.link2)

    def get_class_from_red(self):
        return self.get_attribute(MP.red_box, 'class')

    def get_text_from_red(self):
        return self.get_element_text(MP.red_box)

    def get_orange_box_position(self):
        return self.get_location(MP.orange_box)

    def get_green_box_position(self):
        return self.get_location(MP.green_box)
    
    def purple_is_visible(self):
        return self.visibility_element(MP.purple_box)

    def write_answer1(self, text):
        timeout = 5
        self.write(MP.answer1, text, timeout)

    def write_answer4(self, text):
        timeout = 5
        self.write(MP.answer4, text, timeout)

    def write_answer6(self, text):
        timeout = 5
        self.write(MP.answer6, text, timeout)

    def write_answer8(self, text):
        timeout = 5
        self.write(MP.answer8, text, timeout)

    def write_answer9(self, text):
        timeout = 5
        self.write(MP.answer9, text, timeout)

    def write_answer10(self, text):
        timeout = 5
        self.write(MP.answer10, text, timeout)

    def write_answer11(self, text):
        timeout = 5
        self.write(MP.answer11, text, timeout)

    def get_name(self):
        return self.get_element_text(MP.name_to_enter)

    def get_occupation(self):
        return self.get_element_text(MP.occupation_to_enter)

    def get_link(self):
        return self.get_element_text(MP.link_to_click)

    def get_position(self):
        return self.get_element_text(MP.position_to_select)

    def get_background(self, type):
        if type == 'orange':
            style = self.get_attribute(MP.orange_box, 'style')
        elif type == 'green':
            style = self.get_attribute(MP.green_box, 'style')
        style = style.split(';')
        color = style[0]
        index = color.index(':')
        return color[index+2:]
            
    def get_iam_here(self):
        return self.search_element_by_xpath(MP.iamhere)

    def click_wait(self):
        self.click_elem(MP.wait)

    def click_after_wait(self):
        self.go_to_xpath(MP.click_after_wait)
        self.wait(.05)
        self.click_elem(MP.click_after_wait)

    def click_submit(self):
        self.click_elem(MP.submit)