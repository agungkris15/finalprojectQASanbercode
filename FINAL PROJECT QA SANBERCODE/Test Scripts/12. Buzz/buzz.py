import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Verify the Update Status tab
class Test1VerifyTheUpdateStatusTab(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # Post without input characters
    def test_tc_input_data_blank_buzz(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running TESTING
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # 2. Click "Buzz" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[11]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Status text box
        browser.find_element(By.ID,"createPost_content").click() 
        time.sleep(1)
        # 2. Click "Post" button
        browser.find_element(By.ID,"postSubmitBtn").click() 
        time.sleep(1)

        # validation
        post = browser.find_element(By.ID,"buzz").text

        # Cannot post
        self.assertIn('2021', post)

    # Post with input characters
    def test_tc_input_post_buzz(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running TESTING
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # 2. Click "Buzz" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[11]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Status text box and input characters
        browser.find_element(By.ID,"createPost_content").send_keys("Hello Testing") 
        time.sleep(1)
        # 2. Click "Post" button
        browser.find_element(By.ID,"postSubmitBtn").click() 
        time.sleep(3)

        # validation
        post = browser.find_element(By.ID,"buzz").text
        
        # Successfully posted
        self.assertIn('Hello Testing', post)

    def tearDown(self): 
        self.browser.close()

# Test Scenario: Verify the Upload Images tab
class Test2VerifyTheUploadImagesTab(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:
    # Input characters without upload an image
    def test_tc_024(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running TESTING
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # 2. Click "Buzz" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[11]/a/b").click()
        time.sleep(1)
        # 3. Click "Upload Images" tab
        browser.find_element(By.ID,"tabLink2").click()
        time.sleep(1)
        # Test Steps
        # 1. Click text box and input characters
        browser.find_element(By.ID,"phototext").send_keys("Bon Appetit") 
        time.sleep(1)
        # 2. Click "Post" button
        browser.find_element(By.ID,"imageUploadBtn").click() 
        time.sleep(1)

        # validation
        post = browser.find_element(By.ID,"buzz").text

        # Cannot post
        self.assertIn('Hello Testing', post)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()