import unittest
from src.steps.steps import test_steps
from settings.settings import url


class challenge_test(unittest.TestCase, test_steps):
    def setUp(self):
        self.openChrome(url)

    def tearDown(self):
        self.close_browser()
        

    def test_main(self):
        self.test()

if __name__ == '__main__':
    unittest.main()