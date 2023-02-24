from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.facebook.com/")


driver.find_element(By.LINK_TEXT, "Create new account").click()
driver.find_element(By.NAME, "firstname").send_keys("John")
driver.find_element(By.NAME, "lastname").send_keys("dina")
driver.find_element(By.ID, "password_step_input").send_keys("welcome123")
driver.find_element(By.XPATH, "//input[@value='-1']").click()
driver.find_element(By.NAME, "websubmit").click()
time.sleep(5)
driver.quit()