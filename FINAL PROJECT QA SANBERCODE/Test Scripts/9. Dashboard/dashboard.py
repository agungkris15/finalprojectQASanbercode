import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Check the Quick Launch section
class TestVerifyThePersonalDetails(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # Check the Assign Leave button
    def test_tc_assign_leave(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running testing
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # Test Steps
        # 1. Click "Assign Leave" button 
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[1]/div").click() 
        time.sleep(1)
        
        # validation
        response = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[1]/h1").text

        # Display Assign Leave page
        self.assertIn('Assign Leave', response)

    # Check the Leave List button
    def test_tc_list_leave(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running testing
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # Test Steps
        # 1. Click "Leave List" button
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[2]/div").click() 
        time.sleep(1)
        
        # validation
        response = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[1]/h1").text

        # Display Leave List page
        self.assertIn('Leave List', response)

    # Check the Timesheets button
    def test_tc_Check_timesheets(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running testing
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # Test Steps
        # 1. Click "Timesheets" button 
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[3]/div").click() 
        time.sleep(1)
        
        # validation
        response = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[1]/h1").text

        # Display Timesheets page
        self.assertIn('Timesheets', response)

    # Check the Apply Leave button
    def test_tc_apply_leave(self):
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
        # Test Steps
        # 1. Click "Apply Leave" button
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[4]/div").click() 
        time.sleep(1)
        
        # validation
        response = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[1]/h1").text

        # Display Apply Leave page
        self.assertIn('Apply Leave', response)

    # Check the My Leave button
    def test_tc_Check_myleave(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running testing
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # Test Steps
        # 1. Click "My Leave" button
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[5]/div").click() 
        time.sleep(1)
        
        # validation
        response = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[1]/h1").text

        # Display My Leave page
        self.assertIn('My Leave', response)

    # Check the My Timesheet button
    def test_tc_check_mytimesheet(self):
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
        # Test Steps
        # 1. Click "My Timesheet" button
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[6]/div").click() 
        time.sleep(1)
        
        # validation
        response = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/div[1]/h3").text

        # Display My Timesheets page
        self.assertIn('Timesheet', response)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()