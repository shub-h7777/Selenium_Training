import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://www.royalcaribbean.com")
driver.implicitly_wait(30)
driver.maximize_window()

wait = WebDriverWait(driver, 30)
# wait.until(expected_conditions)

random_num=random.randint(1,1000)
email="shubham"+str(random_num)+"@gmail.com"


# click on sign in --> Create new account --> Enter the details
driver.find_element(By.XPATH, "//span[contains(text(),'Sign In')]").click()
driver.find_element(By.LINK_TEXT, "Create an account").click()
driver.find_element(By.XPATH, "//input[@data-placeholder='First name/Given name']").send_keys("dennis")
driver.find_element(By.XPATH, "//input[@data-placeholder='Last name/Surname']").send_keys("rich")
driver.find_element(By.XPATH, "//div/span[contains(text(),'Month')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'April')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'Day')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'4')]").click()
driver.find_element(By.XPATH, "//input[@data-placeholder='Year']").send_keys(1990)
driver.find_element(By.XPATH, "//span[contains(text(),'Country/Region of residence')]").click()
driver.find_element(By.XPATH, "(//span[contains(text(),'India')]) [2]").click()

#adding time.sleep() because it is not taking the email without wait.
time.sleep(1)

driver.find_element(By.XPATH, "//input[@data-placeholder='Email address']").send_keys(email)
driver.find_element(By.XPATH, "//input[@data-placeholder='Create new password']").send_keys("Shubham@123")
driver.find_element(By.XPATH, "//span[contains(text(),'Select one security question')]").click()
# driver.find_element(By.XPATH,"//span[normalize-space()='What was your first car's make or model?']").click()
driver.find_element(By.XPATH,"(//span[@class='mat-option-text'])[7]").click()
driver.find_element(By.XPATH, "//input[@data-placeholder='Answer']").send_keys("Toyota-Supra")
# driver.find_element(By.XPATH, "//input[@aria-labelledby='agreements']").click()
driver.find_element(By.XPATH,"(//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin'])[2]").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Done']").click()


time.sleep(5)
print("TC is passed.")
driver.quit()