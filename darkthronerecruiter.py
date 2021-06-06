import time
# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
# Here Chrome  will be used
driver = webdriver.Chrome()
 
# URL of website
url = "http://darkthrone.com/recruiter/"
 
# Opening the website
driver.get(url)

time.sleep(3)
email = driver.find_element_by_id("email_address")
passwd = driver.find_element_by_name("user[password]")
login = driver.find_element_by_class_name("submitbtn")
email.send_keys('username')
passwd.send_keys('password')
login.click()

while True:
    button = driver.find_element_by_id("recruit_link")
    button.click()
    time.sleep(2.5)
    print("Still going")
