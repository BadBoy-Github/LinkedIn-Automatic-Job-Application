
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
linkedin_url = os.getenv("LINKEDIN_URL")
linkedin_email = os.getenv("LINKEDIN_EMAIL")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")

# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Website
driver.get(linkedin_url)
sleep(5)

print("🔘 Sign In ....")
signin_button = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
signin_button.click()
sleep(3)

email = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
email.send_keys(linkedin_email)
print("✅ Email")
sleep(1)
password = driver.find_element(By.ID, value="base-sign-in-modal_session_password")
password.send_keys(linkedin_password)
print("✅ Password")
sleep(1)

sign_in_button = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
sign_in_button.click()
print("✅ Logged in")
sleep(10)

easy_apply_button = driver.find_element(By.CLASS_NAME, value='jobs-apply-button--top-card')
easy_apply_button.click()
print("✅ Easy Apply")
sleep(3)

print("⚠️ Please Check the Details!")
sleep(10)

next = driver.find_element(By.ID, value='ember310')
next.click()
print("✅ Next")

print("⚠️ Please Check the Details!")
sleep(10)
review = driver.find_element(By.ID, value='ember314')
review.click()
print("✅ Review")
sleep(3)

print("⚠️ Please Check the Details Finally!")

submit = driver.find_element(By.ID, value='ember324')
submit.click()
print("✅ Submit")
print("✅ ALL Done")
sleep(10)

# Close the browser
driver.quit()


