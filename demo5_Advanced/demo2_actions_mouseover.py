import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://nasscom.in/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT,"Membership").click()

# Hover on Membership
action = webdriver.ActionChains(driver)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Membership")).perform()

# hover on "become a member"
action.move_to_element(driver.find_element(By.LINK_TEXT, "Become a Member")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Membership Benefits")).perform()
driver.find_element(By.LINK_TEXT, "Membership Benefits").click()

time.sleep(10)
driver.quit()
