class locMainPage():
    title = '//titlle'
    name = '//input[@id="name"]'
    occupation = '//select[@id="occupation"]'
    radio_option = "//input[@type='radio' and @value='{}']"
    black_box = """//span[@class='blackbox' and 
                   contains(@style,'background:#000')]"""
    red_box = """//span[@id='redbox' and 
                 contains(@style,'background:#f00')]"""
    green_box = """//span[@id='greenbox' and 
                   contains(@style,'background:green')]"""
    orange_box = """//span[@id='orangebox' and 
                    contains(@style,'background:orange')]"""
    purple_box = "//div[@id='purplebox']"
    link1 = "//a[@id='link1']"
    link2 = "//a[@id='link2']"
    click_me = "//a[@id='clickme']"
    wait = "//a[text()='Wait']"
    click_after_wait = "//a[contains(.,'After Wait')]"
    check_results = "//input[@id='checkresults']"
    submit = "//input[@name='submit']"
    iamhere = "//*[@id='IAmHere']"
    answer1 = "//input[@id='answer1']"
    answer4 = "//input[@id='answer4']"
    answer6 = "//input[@id='answer6']"
    answer8 = "//input[@id='answer8']"
    answer9 = "//input[@id='answer9']"
    answer10 = "//input[@id='answer10']"
    answer11 = "//input[@id='answer11']"
    name_to_enter = "/html/body/ol/li[2]/b"
    occupation_to_enter = "/html/body/ol/li[3]/b"
    link_to_click = "/html/body/ol/li[5]/b"
    position_to_select = "/html/body/ol/li[7]/b"
