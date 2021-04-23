from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Forest\GoogleDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

number = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(number.text)

all_portals = driver.find_elements_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
