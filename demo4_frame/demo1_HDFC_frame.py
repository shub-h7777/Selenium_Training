import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.implicitly_wait(10)
driver.maximize_window()

#enter the frame
driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='login_page']"))

# enter the CustID and click on continue
driver.find_element(By.NAME, "fldLoginUserId").send_keys("test123")
driver.find_element(By.XPATH, "//a[contains(text(),'CONTINUE')]").click()

#switch to main HTML
driver.switch_to.default_content()



time.sleep(10)
driver.quit()
