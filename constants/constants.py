import locale as __locale

if 'es' in __locale.getdefaultlocale()[0]:
    from constants.spanish_messages import *
    #from english_message import *
else:
    from constants.english_message import *
    
# BROWSERS
CHROME = 'chrome'
CHROME_P = 'chrome_p'
FIREFOX = 'firefox'
FIREFOX_P = 'firefox_p'
    
# CHROME PROPERTIES
IGNORE_CERTIFICATE = '--ignore-certificate-errors'

    
# JS
SCROLL = "arguments[0].scrollIntoView();"
SET_ATTRIBUTE = "arguments[0].setAttribute('style', arguments[1])"
CLICK = "arguments[0].click();"
NEW_TAB = 'window.open("{}")'
BACK = 'window.history.go(-1)'

BORDER = "border: 4px solid red"
STYLE = 'style'

# WEBELEMENT ATTRIBUTE
ARIA_OWNS = 'aria-owns'
TAG_LI = 'li'

# PATH
PNG = 'PNG'
LOG_PATH = '{}\{}.log'
PNG_FILE = '{}.png'
