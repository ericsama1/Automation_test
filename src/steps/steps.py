from src.pages.mainPage import mainPage


class test_steps(mainPage):
    def test(self):
        self.step1()
        self.step2()
        self.step3()
        self.step4()
        self.step5()
        self.step6()
        self.step7()
        self.step8()
        self.step9()
        self.step10()
        self.step11()
        self.step12()
        self.step13()
        self.step14() 
        import ipdb; ipdb.set_trace()       
        

    def step1(self):
        title = self.get_title()
        self.write_answer1(title)

    def step2(self):
        name = self.get_name()
        self.write_name(name)

    def step3(self):
        occupation = self.get_occupation()
        self.select_occupation(occupation)

    def step4(self):
        count = self.count_black_boxes()
        self.write_answer4(count)

    def step5(self):
        link = self.get_link()
        if link == 'Link 1':
            self.link1()
        elif link == 'Link 2':
            self.link2()
        elif link == 'Click Me':
            self.click_me()
        else:
            raise ValueError('The value isn\'t an option')
    
    def step6(self):
        clas = self.get_class_from_red()
        self.write_answer6(clas)

    def step7(self):
        position = self.get_position()
        self.mark_radio(position)

    def step8(self):
        text = self.get_text_from_red()
        self.write_answer8(text)

    def step9(self):
        _, orange_y = self.get_orange_box_position()
        _, green_y = self.get_green_box_position()
        if orange_y > green_y: 
            # Orange is under green
            color = self.get_background('green')
        else:
            # Green is under
            color = self.get_background('orange')
        self.write_answer9(color)

    def step10(self):
        if self.get_iam_here() is None:
            text = 'NO'
        else:
            text = 'YES'
        self.write_answer10(text)

    def step11(self):
        if self.purple_is_visible():
            text = 'YES'
        else:
            text = 'NO'
        self.write_answer11(text)

    def step12(self):
        self.click_wait()
        self.click_after_wait()

    def step13(self):
        self.switch_alert()
        self.accept_alert()
    
    def step14(self):
        self.click_submit()