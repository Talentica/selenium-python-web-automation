import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Safari()
driver.set_window_size(1350, 768)


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


# Selecting radio button
# Select male
driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td/label').click()


# Selecting check box
# Select sunday
driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[1]/td/label').click()


# Select monday
driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[2]/td/label').click()
time.sleep(3)
