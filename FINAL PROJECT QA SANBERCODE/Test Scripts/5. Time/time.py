import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Verify the Employee Timesheets sub-menu
class TestVerifyTheEmployeeTimesheetsSubMenu(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # No input Employee Name
    def test_tc_addEmployeeNameTime(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # 2. Click "Time" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[4]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Employee Name text box
        browser.find_element(By.ID,"employee").click() 
        time.sleep(1)
        # 2. Click "View" button
        browser.find_element(By.ID,"btnView").click() 
        time.sleep(1)

        # validation
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/span").text

        # Cannot view
        self.assertIn('Required', response_message)


    def test_tc_unlistedEmployeeName(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # 2. Click "Time" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[4]/a/b").click()
        time.sleep(1)
        # Test Steps
        browser.find_element(By.ID,"employee").click()
        time.sleep(1)
        # 1. Click Employee Name text box and input a Name
        browser.find_element(By.ID,"employee").send_keys("Paijo") 
        time.sleep(1)
        # 2. Click "View" button
        browser.find_element(By.ID,"btnView").click() 
        time.sleep(3)

        # validation
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/span").text
    
        # Cannot view
        self.assertIn('Invalid', response_message)

    # Input a listed Employee Name
    def test_tc_listEmployeeName(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running 
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # 2. Click "Time" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[4]/a/b").click()
        time.sleep(1)
        # Test Steps
        browser.find_element(By.ID,"employee").click()
        time.sleep(1)
        # 1. Click Employee Name text box, input a Name, and click the available option
        browser.find_element(By.ID,"employee").send_keys("Charlie Carter") 
        time.sleep(1)
        # 2. Click "View" button
        browser.find_element(By.ID,"btnView").click() 
        time.sleep(3)

        # validation
        validation = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/div[1]/h3").text
        
        # Response Timesheet for name search
        self.assertIn('Charlie Carter', validation)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()