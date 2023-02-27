import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.ilovepdf.com/pdf_to_word")
driver.maximize_window()


# xpath should be" //input[@type='file']  " and send keys " enter the path "
driver.find_element(By.XPATH,"//input[@type='file']").send_keys(r"C:\Users\150286\Python BootCamp\sample.pdf")


time.sleep(10)
driver.quit()