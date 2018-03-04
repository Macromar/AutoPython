import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Counter import *
from config import *


class TestUM(unittest.TestCase):
    def setUp(self):
        self.options = Options()
        self.options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome('./chromedriver.exe', options=self.options)
        self.url = "https://uk-ua.facebook.com/"

    def tearDown(self):
        self.driver.close()

    def test_counter_vs_count(self):
        login(self.driver, user, password, self.url)
        from_main_to_friends(self.driver, self.url)
        friends = count_friends(self.driver)
        friends_counter = int(self.driver.find_element_by_class_name("_gs6").text)
        self.assertEqual(friends_counter, friends)

    def test_counter_no_friends(self):
        login(self.driver, no_friends_user, no_friends_password, self.url)
        from_main_to_friends(self.driver, self.url)
        friends = count_friends(self.driver)
        self.assertTrue(friends == 0)

    def test_counter_vs_count_blocked_friends(self):
        login(self.driver, blocked_friends_user, blocked_friends_password, self.url)
        from_main_to_friends(self.driver, self.url)
        friends = count_friends(self.driver)
        friends_counter = int(self.driver.find_element_by_class_name("_gs6").text)
        self.assertNotEqual(friends_counter, friends)

if __name__ == '__main__':
    unittest.main()