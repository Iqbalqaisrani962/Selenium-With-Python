# quit command is used to close all the browsers
# close command is used to close only the parent browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s_obj = Service("C:/Users/iqbal/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)
# driver.close()
driver.quit()
time.sleep(5)