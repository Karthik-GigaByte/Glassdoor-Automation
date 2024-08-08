import os
import time
from dotenv import set_key, load_dotenv
from selenium import webdriver
from login import Glassdoorlogintest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()
PASSWORD = os.getenv('PASSWORD')
class passwordtest():
    def __init__(self):    
        email = 'Your_enmail'
        password1 = PASSWORD
        self.login_instance = Glassdoorlogintest(email, password1)
        self.driver = self.login_instance.login()
        
    def change_password(self):
        driver = self.driver
        try:
            # clicking the profile button
            icon_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/div/div[3]/div[3]"))
            )
            # icon_button = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".styles__sharedStyles__mobileContainer .utilityNav__utilityNavStyles__button[data-test='mobile-utility-nav-profile-button']"))
            # )
            # icon_button = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="profile"]'))
            # )
            icon_button.click()
            print("Profile button clicked successfully")
            time.sleep(5)
        except Exception as e:
            print(f"Profile button not clickable: {e}")
            
        try:
            #Trying to click the setting button
            settings_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@data-test="site-header-settings"]'))
            )
            settings_link.click()
            time.sleep(5)
            print("Clicked the setting link successfully")
        except:
            print("Was not able to  click the settings")
            
        try:
            #To click the Account settings
            Account_settings = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@data-test="nav-link-account-settings"]'))
            )
            Account_settings.click()
            print("Clicked the Account Settings")
            time.sleep(10)
        except:
            print("Was not able to  click the Account_settings")
            
        try:
            #To click the password edit option
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-test="account-settings-password-field-edit-button"]'))
            )
            button.click()
            print("Clicked the password edit button")
            time.sleep(10)
        except:
            print("Not able to click the edit button")
            
            
        try:
            # Wait for the password input field to be visible
            wait = WebDriverWait(driver, 10)
            password_input = wait.until(EC.visibility_of_element_located((By.ID, 'current-password')))

            
            password_input.send_keys(PASSWORD)
            print("Password entered successfully")
        except:
            print("Password Input field not found")
        # time.sleep(2000)
        try:
            # Wait for the new password input field to be visible
            password_input = wait.until(EC.visibility_of_element_located((By.ID, 'new-password')))
            NEW_PASS = os.getenv('NEW_PASSWORD')
            # Enter text into the new password input field
            password_input.send_keys(NEW_PASS)
            print("New Password entered successfully")
        except:
            print("Password Input field not found")
            
        try:
            # Wait for the re-entry password input field to be visible
            password_input = wait.until(EC.visibility_of_element_located((By.ID, 'reentry-new-password')))
            
            # Enter text into the re-entry password input field
            password_input.send_keys(NEW_PASS)
            print("re-entry of new Password entered successfully")
        except:
            print("Password Input field not found")

        try:
            # To click save button
            save_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-test="account-settings-password-field-edit-form-save-button"]'))
            )
            save_button.click()
            print("Submitted- save button")
            time.sleep(20)
            set_key('.env', 'PASSWORD', NEW_PASS)
        except:
            print("save button not found")
        # dotenv.set_key(dotenv_file, "key", os.environ["key"])
        try:
            # To sign out
            sign_out = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@data-test="nav-bar-sign-out"]'))
            )
            sign_out.click()
            print("Signed out Successfully")
            time.sleep(10)
        except:
            print("Not Signed out some error has occurred")
            self.driver.back()
    
        finally:
            self.driver.quit()

if __name__ == "__main__":
    password = passwordtest()
    password.change_password()
