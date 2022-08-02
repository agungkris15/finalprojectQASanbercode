import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Verify the login
class TestVerifyTheLogin(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:
    # Input invalid Username and invalid Password
    def test_negative_login(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # 1. Click Username text box and input Username
        browser.find_element(By.ID,"txtUsername").send_keys("HR") 
        time.sleep(1)
        # 2. Click Password text box and input Password
        browser.find_element(By.ID,"txtPassword").send_keys("orangexyz") 
        time.sleep(1)
        # 3. Click "LOGIN" button
        browser.find_element(By.ID,"btnLogin").click() 
        time.sleep(1)
        
        # validation
        response_message = browser.find_element(By.ID,"spanMessage").text

        # response login falied
        self.assertIn('Invalid', response_message)


    # Input valid data
    def test_positive_login(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # 1. Click Username text box and input Username
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        # 2. Click Password text box and input Password
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        # 3. Click "LOGIN" button
        browser.find_element(By.ID,"btnLogin").click() 
        time.sleep(1)
        
        # validation
        response_message = browser.find_element(By.ID,"welcome").text

        # Successful login
        self.assertIn('Welcome', response_message)

    def tearDown(self): 
        self.browser.close()
 
if __name__ == "__main__": 
    unittest.main()