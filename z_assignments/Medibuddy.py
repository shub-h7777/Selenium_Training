import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.medibuddy.in")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Login").click()

driver.find_element(By.XPATH,"//div[contains(text(),'I have a Corporate Account')]").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Login using Username & Password')]").click()

driver.find_element(By.NAME,"userName").send_keys("john")
driver.find_element(By.XPATH,"//button[contains(text(),'Proceed')]").click()
driver.find_element(By.NAME,"password").send_keys("john123")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
error_text=driver.find_element(By.XPATH,"//div[contains(text(),'incorrect password')]").text
print(error_text)

time.sleep(10)
driver.quit()
