#Imports
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import time

# Sanity flow for selecting inputs and searching for flights ATL<->PBI
#

#Access Chrome
driver = webdriver.Chrome()

#Get into the Delta site
driver.get("https://www.delta.com/flightsearch/book-a-flight")
time.sleep(2)

popup = driver.find_element(By.CSS_SELECTOR,'#onetrust-accept-btn-handler')
popup.click()
time.sleep(2)

#Find and expand into the Calendar widget
calendar_widget = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[3]')
calendar_widget.click()
time.sleep(5)

#Find the current day but dont click on it
#today = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]')
date_picker = driver.find_element(By.CSS_SELECTOR, ".dl-datepicker")
if date_picker.switch_to.active_element != date_picker:
        date_picker.click()
#Select a five day range with the keyboard (cursor navigaton had errors)
#today.send_keys(Keys.RIGHT,Keys.RIGHT,Keys.ENTER,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.ENTER)
time.sleep(5)

#Find and click on the Done button in the calendar widget to complete
done_button = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[3]/date-selection-view/div/div/div/div/div[4]/div/div[3]/button[2]')
done_button.click()
time.sleep(5)


#Find the current day but dont click on it
#today = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[3]/date-selection-view/div/div/div/div/div[4]/div/div[2]/div[1]/div[2]/table/tbody/tr[5]/td[7]/a')
#Select a five day range with the keyboard (cursor navigaton had errors)
#today.send_keys(Keys.RIGHT,Keys.RIGHT,Keys.ENTER,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.ENTER)
#time.sleep(2)

#Find and click on the Done button in the calendar widget to complete
#done_button = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[3]/date-selection-view/div/div/div/div/div[4]/div/div[3]/button[2]')
#done_button.click()
#time.sleep(2)


#
#calendar_widget = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[3]')
#calendar_widget.click()
#time.sleep(5)

#today = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[3]/date-selection-view/div/div/div/div/div[4]/div/div[2]/div[1]/div[2]/table/tbody/tr[5]/td[7]/a')
#today.click()
#select a six day range with the keyboard
#today.send_keys(Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.ENTER)
#time.sleep(5)

#done_button = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[3]/date-selection-view/div/div/div/div/div[4]/div/div[3]/button[2]')
#done_button.click()
#time.sleep(5)

#WORKING
#popup = driver.find_element(By.CSS_SELECTOR,'#onetrust-accept-btn-handler')
#popup.click()
#time.sleep(2)

#2 Passengers
#passenger = driver.find_element(By.CSS_SELECTOR, '#passengers-val')
#passenger.click()
#two_passengers = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[4]/span/span[1]')
#two_passengers.click()
#two_passengers.send_keys(Keys.DOWN, Keys.ENTER)
#time.sleep(2)

#Submit Button - Search for flights, uncomment submit when calendar is working
#submit = driver.find_element(By.XPATH, '//*[@id="btnSubmit"]')
#submit.click()
#time.sleep(5)