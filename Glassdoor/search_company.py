import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from login import Glassdoorlogintest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
load_dotenv()
PASSWORD = os.getenv('PASSWORD')
class searchcompanytest():
    def __init__(self):    
        email = 'Your_email'
        password = PASSWORD
        self.login_instance = Glassdoorlogintest(email, password)
        self.driver = self.login_instance.login()
        
    def test_search_company(self):
        driver = self.driver
        try:
            company = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@data-test="site-header-companies"]/a'))
            )
            company.click()
            print("Clicked the company button successfully")
            
            # Wait for the URL to change to the job search page
            WebDriverWait(driver, 10).until(
                EC.url_to_be('https://www.glassdoor.co.in/Reviews/index.htm')
            )
            print("Navigated to the company search page")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        try:
            # To search for the job
            search = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='companyAutocomplete-companyDiscover-employerSearch']"))
            )
            search.click()
            search.send_keys("Accenture")
            time.sleep(3)
            print("Entered the company name")
            time.sleep(5)
        except Exception as e:
            print(f"Search input field not found: {e}")
        
        try:
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="company-search-button"]'))
            )
            search_button.click()
            print("Search button clicked successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
            
        try:
            # Find all company elements
            company_elements = driver.find_elements(By.CSS_SELECTOR, 'div.col-9.pr-0 h2 a')

            # Check if we found any companies
            if not company_elements:
                print("No companies found.")
            else: 
                # Select a random company element
                random_company_element = random.choice(company_elements)

                # Click on the selected company element
                random_company_element.click()

                # Optional: Wait for the new page to load
                time.sleep(5)
            # Optionally print the new page title or URL to confirm the click
            print(f"Navigated to: {driver.current_url}")
            self.driver.back()
        except Exception as e:
            print(f"Not chooseable: {e}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    search = searchcompanytest()
    search.test_search_company()
