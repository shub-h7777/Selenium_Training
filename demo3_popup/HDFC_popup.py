import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")
driver.maximize_window()

#click on go
driver.find_element(By.XPATH, "//img[contains(@alt,'Go')]").click()

# to get text
alert_text = driver.switch_to.alert.text
print(alert_text)

driver.switch_to.alert.accept()


time.sleep(5)
driver.quit()
