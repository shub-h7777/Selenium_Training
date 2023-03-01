import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.openemr.io/b/openemr")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#authUser").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys("pass")

select_lang = Select(driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
select_lang.select_by_visible_text("English (Indian)")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.XPATH, "//div[text()='Patient']").click()
driver.find_element(By.XPATH, "//div[text()='New/Search']").click()

# enter the frame and enter the data
driver.switch_to.frame(driver.find_element(By.NAME, "pat"))
time.sleep(3)
driver.find_element(By.ID, "form_fname").send_keys("Shubham")
driver.find_element(By.ID, "form_lname").send_keys("Patel")
driver.find_element(By.ID, "form_DOB").send_keys("2023-03-01")

select_gender = Select(driver.find_element(By.ID, "form_sex"))
select_gender.select_by_visible_text("Male")
driver.find_element(By.ID, "create").click()

driver.switch_to.default_content()

# switch to next frame and click
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()

# wait for alert
wait = WebDriverWait(driver, 30)
wait.until(expected_conditions.alert_is_present())

alert_text = driver.switch_to.alert.text
print(alert_text)

driver.switch_to.alert.accept()

# close the birthday popup
driver.find_element(By.XPATH, "//div[@data-dismiss='modal']").click()

# get the name and print in the console.
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@name='pat']"))
patient_name = driver.find_element(By.XPATH, "//h2[contains(text(),'Medical')]").text
print(patient_name)

time.sleep(5)
driver.quit()
