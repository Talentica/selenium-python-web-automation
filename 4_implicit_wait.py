from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.set_window_size(1350, 768)


driver.get("https://www.google.com/doodles")
driver.implicitly_wait(10)

print("driver.title: ", driver.title)
assert "Google Doodles" in driver.title

search_element = driver.find_element(By.NAME, "q")
search_element.send_keys("cricket")
search_subnmit_element = driver.find_element(By.XPATH, '//*[@id="searchbtn"]').click()

driver.quit()
