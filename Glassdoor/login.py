import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

class Glassdoorlogintest:
    def __init__(self, email, password):
        options = uc.ChromeOptions()
        self.driver = uc.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver.maximize_window()
        self.email = email
        self.password = password
        self.glassdoor_url = 'https://www.glassdoor.co.in/profile/login_input.htm'

    def open_galssdoor(self):
        print("Opening Glassdoor")
        self.driver.get(self.glassdoor_url)
        time.sleep(5)

    def login_test(self):
        print("Finding the email && pass Auth box")
        try:
            email_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'inlineUserEmail'))
            )
            email_input.send_keys(self.email)
            email_input.send_keys(Keys.RETURN)
            time.sleep(5)  # Reduced sleep time for demonstration
            print("Email input is proceeded.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
        try:
            password_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'inlineUserPassword'))
            )
            password_input.send_keys(self.password)
            time.sleep(5)
            password_input.send_keys(Keys.RETURN)
            time.sleep(10)  # Reduced sleep time for demonstration
            # password_input.send_keys(Keys.RETURN)
            # time.sleep(20)
            print("password input is proceeded.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def login(self):
        try:
            self.open_galssdoor()
            self.login_test()
            return self.driver
        except Exception as e:
            print(f"Error during login: {e}")
            return None

if __name__ == "__main__":
    email = 'You_email'
    password = PASSWORD
    login = Glassdoorlogintest(email, password)
    login.login()
