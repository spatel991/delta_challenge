#Imports
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import time

# Happy flow for selecting inputs and searching for flights ATL<->PBI for a 5 day trip starting next day

#Access Chrome
driver = webdriver.Chrome()

#Get into the Delta site
driver.get("https://www.delta.com/flightsearch/book-a-flight")
time.sleep(5)

#Acknowledge the popup in order for selenium driver to have the right focus
popup = driver.find_element(By.CSS_SELECTOR,'#onetrust-accept-btn-handler')
popup.click()
time.sleep(2)

#Find the Departure/Orgin 'From' element
from_search_main = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]')
from_search_main.click()
time.sleep(2)

#Enter ATL as the test
from_search = driver.find_element(By.XPATH, '//*[@id="search_input"]')
from_search.send_keys("ATL")
time.sleep(2)
from_search.send_keys(Keys.ENTER)
time.sleep(2)

#Find the Arrival/Destination 'To' element
to_search_main = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[1]/div[1]/a[2]/span[1]')
to_search_main.click()
time.sleep(2)

#Enter PBI as the test
to_search = driver.find_element(By.XPATH, '//*[@id="search_input"]')
to_search.send_keys("PBI")
time.sleep(2)
to_search.send_keys(Keys.ENTER)
time.sleep(2)

#Dropdown for Trip Type, default is Roundtrip
trip_type = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[2]/span/span[1]')
trip_type.click()
time.sleep(2)

#Find and expand into the Calendar widget
calendar_widget = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[3]')
calendar_widget.click()
time.sleep(2)

#first attempt at finding the current clickable calendar date
#date_picker = driver.find_element(By.CSS_SELECTOR, ".dl-datepicker")
#if date_picker.switch_to.active_element != date_picker:
#        date_picker.click()

#Find the current day but dont click on it
today = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[3]/date-selection-view/div/div/div/div/div[4]/div/div[2]/div[1]/div[2]/table/tbody/tr[5]/td[7]/a')
#Select a five day range with the keyboard (cursor navigaton had errors, still buggy)
today.send_keys(Keys.RIGHT,Keys.RIGHT,Keys.ENTER,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.RIGHT,Keys.ENTER)
time.sleep(2)

#Find and click on the Done button in the calendar widget to complete
done_button = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[3]/date-selection-view/div/div/div/div/div[4]/div/div[3]/button[2]')
done_button.click()
time.sleep(2)

#Find and select the Passenger drop-down
passenger = driver.find_element(By.CSS_SELECTOR, '#passengers-val')
passenger.click()
#Select two passengers - finding a cleaner what to do this
two_passengers = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[4]/span/span[1]')
two_passengers.click()
two_passengers.send_keys(Keys.DOWN, Keys.ENTER)
time.sleep(2)

#search for flights - SFA001 messaage from Delta's site
search_for_flights = driver.find_element(By.CSS_SELECTOR, '#btnSubmit')
search_for_flights.click()
time.sleep(5)