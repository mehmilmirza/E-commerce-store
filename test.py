from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class WebAppTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # TC1: Test if the title of the web app is correct
    def test_title(self):
        driver = self.driver
        driver.get("http://13.51.165.233:5000/")
        self.assertIn("E-STORE", driver.title)

    # TC2: Test if the login is successful
    def test_login(self):
        driver = self.driver
        driver.get("http://13.51.165.233:5000/login")
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.NAME, "submit")

        username.send_keys("mehmilmirza")
        password.send_keys("Mehmil@123")
        submit.click()

        time.sleep(2)  

        self.assertIn("Dashboard", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()