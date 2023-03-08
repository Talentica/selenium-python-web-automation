import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Safari()
driver.set_window_size(1350, 768)

driver.get(
    "https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html"
)
time.sleep(2)

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium.chrome").click()
driver.switch_to.default_content()
time.sleep(2)

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "ChromeOptions").click()
driver.switch_to.default_content()
time.sleep(2)

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[5]/a").click()
time.sleep(4)
