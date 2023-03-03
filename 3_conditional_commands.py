import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.set_window_size(1350, 768)

driver.get("https://www.google.com/doodles")
search_element = driver.find_element(By.NAME, "q")
print("search element displayed?: ", search_element.is_displayed())
print("search element enabled?: ", search_element.is_enabled())

search_element.send_keys("cricket")
search_subnmit_element = driver.find_element(By.XPATH, '//*[@id="searchbtn"]').click()
time.sleep(3)

world_cup_element = driver.find_element(
    By.XPATH, '//*[@id="archive-list"]/li[1]/div[1]/div[2]/div[2]/a'
)
print("world_cup element displayed?: ", world_cup_element.is_displayed())
print("world_cup element enabled?: ", world_cup_element.is_enabled())

world_cup_element.click()
time.sleep(3)

driver.quit()
