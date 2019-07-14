# Automation test

This framework is in Python 3, with selenium. It's for automate web pages. In this framework, is added more method than selenium already has.


## Instalation

It use these libraries:
- Selenium
- Pillow
- Logger

These requirements is in requirements file in requirements/requirements.txt


## Settings
The file settings/settings.py is the settings file, where assign the url to automate. And define the path to save the evidence (screenshot, log file, etc), the default value is the test path.


## Test
The test file is in test/test.py

It use unnittest for run the test. The test is based in Page Object Model

## Step
The steps for the test is in the folder src/steps. 

## Pages
The Page Object is in the folder src/pages.