import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Safari()
driver.set_window_size(2560, 1600)


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# find id of option
x = driver.find_element(By.ID, "RESULT_RadioButton-9")
drop = Select(x)

# select by visible text
drop.select_by_visible_text("Afternoon")
time.sleep(4)
driver.close()
