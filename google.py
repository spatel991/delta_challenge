import time
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore


driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(5)


search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search.send_keys("Weather")
search.send_keys(Keys.ENTER)
time.sleep(10)
