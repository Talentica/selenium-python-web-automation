import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Safari()
driver.set_window_size(1350, 768)


driver.get("https://www.expedia.co.in")
time.sleep(2)

# Go to flights tab
driver.find_element(
    By.XPATH, '//*[@id="wizardMainRegionV2"]/div/div/div/div/ul/li[2]/a/span'
).click()

# Add journey details
time.sleep(2)
origin_element = driver.find_element(By.ID, "location-field-leg1-origin-menu")
origin_element.click()
time.sleep(2)
origin_element.send_keys("BOM")
time.sleep(2)
origin_element.send_keys(Keys.RETURN)

time.sleep(2)
destination_element = driver.find_element(By.ID, "location-field-leg1-destination-menu")
destination_element.click()
time.sleep(2)
destination_element.send_keys("DEL")
time.sleep(2)
origin_element.send_keys(Keys.RETURN)

time.sleep(2)

driver.find_element(
    By.XPATH, '//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button'
).click()
time.sleep(5)

direct_element = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.ID, "NUM_OF_STOPS-0-w1t"))
)
direct_element.click()

driver.quit()
