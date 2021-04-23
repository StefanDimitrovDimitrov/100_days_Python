from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Forest\GoogleDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Stefan")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Dimitrov")
email = driver.find_element_by_name("email")
email.send_keys("email@mail.com")
# submit = driver.find_element_by_tag_name('button')
submit = driver.find_element_by_class_name('btn')
submit.click()