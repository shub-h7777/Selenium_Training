import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.oracle.com/in/database/")
driver.maximize_window()

driver.find_element(By.ID, "acctBtnLabel").click()
driver.find_element(By.LINK_TEXT, "Sign-In").click()


sign_in_title = driver.title
print(sign_in_title)
current_url = driver.current_url
print(current_url)

oracle_header=driver.find_element(By.XPATH,"//h2[contains(text(),'Oracle account sign in')]").text
print(oracle_header)

driver.find_element(By.ID,"sso_username").send_keys("john")
driver.find_element(By.ID,"ssopassword").send_keys("john123")
driver.find_element(By.ID,"signin_button").click()
error_text=driver.find_element(By.XPATH,"//div[contains(text(),'Invalid')]").text
print(error_text)

time.sleep(10)
driver.quit()
