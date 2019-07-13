import unittest
from src.pages.mainPage import mainPage
from settings.settings import url


class challenge_test(unittest.TestCase, mainPage):
    def setUp(self):
        self.openChrome(url)

    def tearDown(self):
        self.close_browser()

    def test_main(self):
        print (self.get_title())
        self.write_name('Lucas D\'Hers')
        self.select_occupation('Project Manager')

if __name__ == '__main__':
    unittest.main()