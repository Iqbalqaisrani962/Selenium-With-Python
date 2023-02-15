# forward() command is used to the next page
# back() command is used to the previous page
# refresh() command is used to refresh the current page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s_obj = Service("C:/Users/iqbal/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.get('https://hearo.live/')
driver.back()
time.sleep(4)
driver.forward()
time.sleep(4)
driver.back()
time.sleep(4)
driver.refresh()
# print(element.text)  # this method is used to find the text of an element