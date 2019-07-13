class locMainPage():
    title = '//h2[@id="tophead"]'
    name = '//input[@id="name"]'
    occupation = '//select[@id="occupation"]'
    radio_options = "//input[@type='radio']"
    black_box = """//span[@class='blackbox' and 
                   contains(@style,'background:#000')]"""
    red_box = """//span[@id='redbox' and 
                 contains(@style,'background:#f00')]"""
    green_box = """//span[@id='greenbox' and 
                   contains(@style,'background:green')]"""
    orange_box = """//span[@id='orangebox' and 
                    contains(@style,'background:orange')]"""
    click_me = "//a[@id='clickme']"
    wait = "//a[contains(text(),'Wait')]"
    check_results = "//input[@id='checkresults']"
    submit = "//input[@name='submit']"
