import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.db4free.net/")

#clcik on phpMyAdmin
driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin").click()

#switch to 2nd tab
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
print(driver.current_url)

#enter username, password and click on login
driver.find_element(By.ID,"input_username").send_keys("Shubham")
driver.find_element(By.ID,"input_password").send_keys("welcome@123")
driver.find_element(By.ID,"input_go").click()

time.sleep(5)

#to close 2nd tab
driver.close()

#Get title and link for 1st tab after closing 2nd
driver.switch_to.window(driver.window_handles[0])
print(driver.title)
print(driver.current_url)

time.sleep(5)
driver.quit()