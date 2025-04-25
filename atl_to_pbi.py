#Imports
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import time

# Sanity flow for selecting inputs and searching for flights ATL<->PBI

#Access Chrome
driver = webdriver.Chrome()

#Get into the Delta site
driver.get("https://www.delta.com/flightsearch/book-a-flight")
time.sleep(2)

#Find the Departure 'From' element
from_search_main = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]')
from_search_main.click()
time.sleep(2)

#Enter ATL as the test
from_search = driver.find_element(By.XPATH, '//*[@id="search_input"]')
from_search.send_keys("ATL")
time.sleep(2)
from_search.send_keys(Keys.ENTER)
time.sleep(5)

#Find the Arrival 'To' element
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

#/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[2]/ngc-search-options/fieldset/div/div[3]/input

#input_departureDate_1
###
#cal1 = driver.find_element(By.XPATH, '/html/body/idp-root/div/div[2]/idp-advance-search/div/div[1]/div[2]/idp-book-widget/div/ngc-book/div[1]/div/form/div[1]/div/div[1]/div[1]/div[3]/date-selection-view/div/div/div/div/div[4]/div/div[2]/div[1]/div[2]/table/tbody/tr[5]/td[5]/a')
#cal1.send_keys(Keys.DOWN)
#cal1.send_keys(Keys.ENTER)
#goto_cal.send_keys(Keys.DOWN)
#goto_cal.send_keys(Keys.ENTER)
### html.fresh-air.no-scroll body.ng-tns-0-1.scrollWidgetEnabled idp-root div.idp-shopping-slice div.idp-shopping-slice__body idp-advance-search.ng-star-inserted div.idp-advance-search div.adv-container.container div.adv-container__book-widget idp-book-widget.ng-star-inserted div.adv-search-book-widget ngc-book.ng-tns-c88-2.ng-star-inserted div#primaryPanel1.common-va-widget-bg.ng-tns-c88-2 div#booking.book-widget-container.container-padding-x.ng-tns-c88-2 form.ng-tns-c88-2.ng-untouched.ng-pristine.ng-invalid.ng-star-inserted div.container.booking-widget_container-mobile.ng-tns-c88-2.book-container-padding-bottom div.form-row.ng-tns-c88-2 div.col-lg-10.pl-xl-0.pl-xxl-0.p-0.pt-sm-3.safari-mob-padding.ng-tns-c88-2 div.form-row.ng-tns-c88-2 div.col-lg-3.col-sm-12.d-lg-block.offset-md-2.col-md-8.offset-lg-0.book-element.ng-tns-c88-2.d-sm-none.booking-element.ng-star-inserted date-selection-view.ng-tns-c88-2 div.travelDateSelectionView div.form-group.ng-untouched.ng-pristine.ng-invalid.ng-star-inserted div.icon-addon div.calendarMasterCont.calMedium div.calenderContainer div.dl-datepicker.dl-datepicker-multi.dl-datepicker-multi-2

#Submit Button - Search for flights, uncomment submit when calendar is working
#submit = driver.find_element(By.XPATH, '//*[@id="btnSubmit"]')
#submit.click()