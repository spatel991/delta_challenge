#Imports
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import time

#Test A004 - Delta User login validation

#Access Chrome
driver = webdriver.Chrome()

#Get into the Delta "Book a Flight" site
driver.get("https://www.delta.com/flightsearch/book-a-flight")
time.sleep(1)

#Find and click the login button
login_button = driver.find_element(By.CSS_SELECTOR, '#login-modal-button')
login_button.click()
time.sleep(1)

#Find the Username/SKymiles input box
user_name = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[1]/idp-login-modal-wrapper/div/idp-login-modal/div/div[2]/div[3]/idp-login-authentication-screen/div/form/div/div[1]/idp-input/div/div/input')
#Send the valid input of the test user
user_name.send_keys("jRyan1239")
time.sleep(1)

#Last Name input box displays after Username is entered, find it
last_name = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[1]/idp-login-modal-wrapper/div/idp-login-modal/div/div[2]/div[3]/idp-login-authentication-screen/div/form/div/div[2]/idp-input/div/div/input')
#Enter the valid test Last Name
last_name.send_keys("Ryan")
time.sleep(1)

#Find the Password input box
pwd = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[1]/idp-login-modal-wrapper/div/idp-login-modal/div/div[2]/div[3]/idp-login-authentication-screen/div/form/div/div[3]/idp-input/div/div/input')
pwd.send_keys("!uJp8wPkSfw")
time.sleep(1)

#Last step to validate - Click the Login Button
login_button2 = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[1]/idp-login-modal-wrapper/div/idp-login-modal/div/div[2]/div[3]/idp-login-authentication-screen/div/form/div/div[3]')
driver.implicitly_wait(2)

#Grab the name label - This is buggy
name_label = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[1]/ngc-global-nav/header/div/nav/div/div[2]/ngc-login/div')
#If the name label is present, the login was valid
if name_label.is_displayed(): print("SUCCESS") 
else: print("FAILED")
driver.implicitly_wait(2)