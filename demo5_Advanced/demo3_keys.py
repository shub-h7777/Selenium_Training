import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://google.com/")
driver.maximize_window()

action=webdriver.ActionChains(driver)
action.key_down(webdriver.Keys.SHIFT).send_keys("pyhton").key_up(webdriver.Keys.SHIFT).pause(1)\
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(1)\
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(1)\
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(1).click().perform()
    # .send_keys(webdriver.Keys.ENTER)


# driver.refresh()
# driver.back()
# driver.forward()

time.sleep(5)
driver.quit()