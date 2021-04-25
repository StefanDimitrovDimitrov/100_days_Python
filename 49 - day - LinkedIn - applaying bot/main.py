from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os

USER = os.getenv('USER')
PASS = os.getenv('PASS')

chrome_driver_path = "C:\Forest\GoogleDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

email = driver.find_element_by_name('session_key')
email.send_keys(USER)

password = driver.find_element_by_name('session_password')
password.send_keys(PASS)

submit = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
submit.send_keys(Keys.ENTER)
time.sleep(2)

remember_me = driver.find_element_by_css_selector('#remember-me-prompt__form-primary button')
remember_me.click()
time.sleep(6)


#
# element = driver.find_element_by_link_text("Stefan Dimitrov")
#
# # create action chain object
# action = ActionChains(driver)
#
# # perform the operation
# action.move_to_element(element).click().perform()
# time.sleep(5)

element_2 = driver.find_element_by_xpath('/html/body/div[8]/header/div[2]/nav/ul/li[3]/a')
element_2.click()
time.sleep(6)


search = driver.find_element_by_css_selector('.ember-view input')
print(search.text)
search.send_keys('Python')
time.sleep(2)
location = driver.find_element_by_css_selector('.jobs-search-box__input--location input')
location.send_keys('Sofia')
time.sleep(1)
search_btn = driver.find_element_by_css_selector('.jobs-search-box__container button')
search_btn.click()