import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Safari()
driver.set_window_size(1350, 768)

driver.get("https://www.google.com/doodles")
time.sleep(2)

links = driver.find_elements(By.TAG_NAME, "a")
# print("links: ", links)
# for link in links:
#     print(link.text)

driver.find_element(By.LINK_TEXT, "About").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Archi").click()
time.sleep(2)
