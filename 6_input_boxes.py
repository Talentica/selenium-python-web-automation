# importing the modules
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# using chrome driver
driver = webdriver.Safari()
driver.set_window_size(1350, 768)

# web page url
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# select class name where is input box are present
input_elements = driver.find_elements(By.CLASS_NAME, "text_field")

# find number of input box
print("input_elements: ", input_elements)

# fill value in input box
driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-1"]').send_keys("Vishal")
driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-2"]').send_keys("Palasgaonkar")
driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-3"]').send_keys("99999999")
time.sleep(1)

# check status
is_result_displayed = driver.find_element(
    By.XPATH, '//*[@id="RESULT_TextField-1"]'
).is_displayed()
print("is_result_displayed: ", is_result_displayed)
driver.close()
