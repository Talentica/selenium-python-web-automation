import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Safari()
driver.set_window_size(1350, 768)

driver.get("https://ide.geeksforgeeks.org/tryit.php/WXYeMD9tD4")

alert = Alert(driver)
print(alert.text)
alert.accept()
time.sleep(2)
