import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")

driver.find_element(By.NAME, "UserFirstName").send_keys("Shubham")
driver.find_element(By.NAME, "UserLastName").send_keys("Patel")
driver.find_element(By.NAME, "UserEmail").send_keys("Shubham@gmail.com")
Select(driver.find_element(By.NAME, "UserTitle")).select_by_value("IT_Manager_AP")
driver.find_element(By.NAME, "CompanyName").send_keys("SalesForce")
Select(driver.find_element(By.NAME, "CompanyEmployees")).select_by_value("250")
driver.find_element(By.NAME, "UserPhone").send_keys("1")
Select(driver.find_element(By.NAME, "CompanyCountry")).select_by_visible_text("India")
phone_Validation_Message = driver.find_element(By.XPATH, "//span[contains(@id,'UserPhone')]").text
print(phone_Validation_Message)
driver.find_element(By.CLASS_NAME, "checkbox-ui").click()
driver.find_element(By.NAME, "start my free trial").click()

time.sleep(10)
driver.quit()
