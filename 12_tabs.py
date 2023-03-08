import time

from selenium import webdriver

driver = webdriver.Safari()
driver.set_window_size(1350, 768)

url = "https://www.google.co.in/"
new_url = "https://www.google.com/doodles"

driver.get(url)

driver.execute_script("window.open('');")
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)
time.sleep(2)
