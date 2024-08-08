import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from login import Glassdoorlogintest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

class Glassdoorsearchtest():
    def __init__(self):    
        email = 'Your_email'
        password = PASSWORD
        self.login_instance = Glassdoorlogintest(email, password)
        self.driver = self.login_instance.login()
        
    def test_search_jobs(self):
        driver = self.driver
        try:
            job = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@data-test="site-header-jobs"]/a'))
            )
            job.click()
            print("Clicked the job button successfully")
            
            # Wait for the URL to change to the job search page
            WebDriverWait(driver, 10).until(
                EC.url_to_be('https://www.glassdoor.co.in/Job/index.htm')
            )
            print("Navigated to the job search page")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        try:
            # To search for the job
            search = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='searchBar-jobTitle']"))
            )
            search.click()
            search.send_keys("Data Scientist")
            time.sleep(3)
            print("Entered the job title")
        except Exception as e:
            print(f"Search input field not found: {e}")
        
        try:
            # To find the location
            location = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='searchBar-location']"))
            )
            location.click()
            location.send_keys("Bengaluru")
            print("Entered the location")
            location.send_keys(Keys.RETURN)
            time.sleep(10)
            self.driver.back()
        except Exception as e:
            print(f"Location input field not found: {e}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    search = Glassdoorsearchtest()
    search.test_search_jobs()
