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
class Glassdoorposttest():
    def __init__(self):    
        email = 'Your_email'
        password = PASSWORD
        self.login_instance = Glassdoorlogintest(email, password)
        self.driver = self.login_instance.login()
        
    def test_posting(self):
        driver = self.driver
        try:
            #clicking the post button
            post = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="Button-special-standard"]'))
            )
            post.click()
            print("Clicked the post button successfully")
            time.sleep(5)
        except:
            print("Post button not Clickable")
        try:
            select = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[text()="Select a relevant bowl for your post"]'))
            )
            select.click()
            time.sleep(10)
            print("Clicked the Select a relevant bowl for your post link")
            community = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@data-test="BowlSwitchAccordion-panel-options-0-text-wrapper" and .//span[text()="Career Advice for Students in India"]]'))
            )
            community.click()
            print("Clicked the Career Advice for Students in India")
            time.sleep(3)
        except Exception as e:
            print(f"Was not able to  click: {e}")
        try:
            # To write input to the post
            input_area = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[data-test="CreatePost-Modal-Editor"]'))
            )
            input_area.click()
            input_area.send_keys("What are some best resources that I can use for aptitude preparation?")
            time.sleep(3)
            print("Entered the input for the post")
        except Exception as e:
            print(f"Search input field not found: {e}")
        
        try:
            # To submit the post
            post_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="CreatePost-Modal-submit-button"]'))
            )
            post_button.click()
            print("Submitted the post")
            time.sleep(20)
            self.driver.back()
        except Exception as e:
            print(f"Was not able to  post: {e}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    Post_c = Glassdoorposttest()
    Post_c.test_posting()
