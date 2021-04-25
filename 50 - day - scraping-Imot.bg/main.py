from selenium import webdriver
import os
import time


USER = os.getenv('USER')
PASS = os.getenv('PASS')


chrome_driver_path = "C:\Forest\GoogleDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.imot.bg/")
time.sleep(2)
button_start = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
button_start.click()
time.sleep(2)

rent = driver.find_element_by_class_name('mapBtnNaemi')
rent.click()

sofia_btn = driver.find_element_by_id('BG-23')
sofia_btn.click()
time.sleep(1)
durvenitsa = driver.find_element_by_xpath('//*[@id="ri"]/optgroup[6]/option[7]')
durvenitsa.click()

choice_btn = driver.find_element_by_xpath('/html/body/div[1]/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td[2]/img[1]')
choice_btn.click()
time.sleep(1)
musagenitsa = driver.find_element_by_xpath('//*[@id="ri"]/optgroup[12]/option[11]')
musagenitsa.click()

choice_btn = driver.find_element_by_xpath('/html/body/div[1]/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td[2]/img[1]')
choice_btn.click()
time.sleep(1)

mladost_1 = driver.find_element_by_xpath('//*[@id="ri"]/optgroup[12]/option[5]')
mladost_1.click()

choice_btn = driver.find_element_by_xpath('/html/body/div[1]/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td[2]/img[1]')
choice_btn.click()
time.sleep(1)

a_room = driver.find_element_by_xpath('//*[@id="vi2"]')
a_room.click()
time.sleep(1)
two_rooms = driver.find_element_by_xpath('//*[@id="vi3"]')
two_rooms.click()
time.sleep(1)
money = driver.find_element_by_xpath('/html/body/div[1]/form/table[1]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[3]/input')
money.send_keys('550')
time.sleep(1)

currency= driver.find_element_by_xpath('/html/body/div[1]/form/table[1]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[9]/select/option[2]')
currency.click()


search = driver.find_element_by_xpath('/html/body/div[1]/form/table[1]/tbody/tr[1]/td[2]/table[2]/tbody/tr[3]/td[3]/input')
search.click()