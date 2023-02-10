# XPath is the address of an element
# XPath is used to find the location of an element on a webpage using HTML DOM structure
# XPath is defined as XML Path
# XPath is a syntax or language for finding any element on the web page using XML path expression
# DOM is an API interface provided by Browser
# When a web page is loaded, the browser creates a Document Object Model of the page
# There re two types of XPath 1) Relative/Partial XPath(Starts with \\) 2) Absolute/Full XPath(Starts with \)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
ser_obj = Service('/home/dell/iqbalFolder/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=ser_obj)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(3)

# Absolute Path
driver.maximize_window()
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]').send_keys('abc')
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]').send_keys('asd')


# Relative Path
# driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('abc')
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('asd')
# time.sleep(3)

# 'OR' & 'AND' with XPath
# driver.find_element(By.XPATH, "//input[@placeholder='Username' or @name='username1']").send_keys('abc')
# driver.find_element(By.XPATH, "//input[@placeholder='Username' and @name='username']").send_keys('abc')
# Code written in below code must generate an error because both options must be correct in and condition
# driver.find_element(By.XPATH, "//input[@placeholder='Username' and @name='username1']").send_keys('abc')

# contains(), startswith(), and text() methods
driver.find_element(By.XPATH, "//input[contains(@name, 'user')]").send_keys('Admin')
driver.find_element(By.XPATH, "//input[starts-with(@type, 'pa')]").send_keys('admin123')
driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
time.sleep(3)