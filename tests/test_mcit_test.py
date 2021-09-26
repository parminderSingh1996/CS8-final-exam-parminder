import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_mcit(self):
        driver = self.driver
        driver.get("https://montrealcollege.omnivox.ca/Login/Account/Login?L=ANG")
        self.assertIn("Omnivox - Montreal College of Information Technology",driver.title)
        college_name = driver.find_element_by_css_selector(".subtitle > a")
        self.assertIn("Montreal College of Information Technology",college_name.text)

    def tearDown(self):
        print("Triggered teardown")
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
