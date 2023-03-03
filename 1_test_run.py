from selenium import webdriver

# driver = webdriver.Chrome()
driver = webdriver.Safari()

driver.get("https://www.google.co.in/")
print(driver.title)
print(driver.current_url)
# print(driver.page_source)
driver.close()
