from time import sleep
from src.browser import browser
from src.error_management import errors
from src.image import image
from src.js import js
from src.keyboard import keyboard
from src.log import log
from src.mouse import mouse
from src.search import search
from src.select_elem import select
from src.webelement import webelement

class selenium_driver(browser, keyboard, mouse, search, select, js, 
          image, webelement, log, errors):
    def wait(self, seconds):
        """Method to wait few seconds"""
        sleep(seconds)
    
