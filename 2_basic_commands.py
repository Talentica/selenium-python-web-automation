import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

driver.get("https://www.google.co.in/")
print(driver.title)
print(driver.current_url)

# driver.find_element(
#     By.XPATH,
#     "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]",
# ).click()

driver.get("https://www.dell.com/en-in")
print(driver.title)
print(driver.current_url)
time.sleep(1)

driver.back()
print(driver.title)
print(driver.current_url)
time.sleep(1)

driver.forward()
print(driver.title)
print(driver.current_url)
time.sleep(1)


time.sleep(5)
driver.quit()
