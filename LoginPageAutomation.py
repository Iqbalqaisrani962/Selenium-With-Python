from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium package, sub package webdriver, sub package chrome and then service module contains Service class
import time
from selenium.webdriver.common.by import By
s = Service('/home/dell/iqbalFolder/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(5)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
# time.sleep(10)
act_title = driver.title
exp_title = 'OrangeHRM'
if act_title == exp_title:
    print("Login Case Succeeded")
else:
    print("Login Case Failed")
driver.close()