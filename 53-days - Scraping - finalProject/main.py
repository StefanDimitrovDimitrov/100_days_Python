import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

chrome_driver_path = "C:\Forest\GoogleDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)




headers = {
    "Accept-Language": "en-US,en;q=0.9,en-GB;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
}

url_form = 'https://docs.google.com/forms/d/e/1FAIpQLSfNkv0JJLJ84ZY-r-zeyb9wTfebHuD3R3SjjpKMU5XElNkHTA/viewform?usp=sf_link'

url_sf = 'https://www.zillow.com/homes/for_rent/'
response = requests.get(url=url_sf,headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")


addresses = [address.getText() for address in soup.find_all(name="address", class_="list-card-addr")]
prises = [prises.getText() for prises in soup.find_all(name="div", class_="list-card-price")]
links_double = [link.get("href") if "http" in link.get("href") else 'https://www.zillow.com' + link.get("href")for link in soup.find_all(name="a", class_="list-card-link")]
links = [links_double[i] for i in range(len(links_double)) if i % 2 == 0]

# for n in range(len(addresses)):
#     driver.get("https://docs.google.com/forms/d/15CEbaioQOajJnkHqTd_8qP9cDKGFLsRvfmTqitCjcC4/edit")
#     time.sleep(2)
#
#     address_field, prises_field, links_field = driver.find_elements_by_css_selector(
#         '.freebirdFormviewerViewItemList input')
#     submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
#
#     address_field.send_keys(addresses[n])
#     prises_field.send_keys(prises[n])
#     links_field.send_keys(links[n])
#     submit_button.click()


table = driver.get('https://docs.google.com/forms/d/15CEbaioQOajJnkHqTd_8qP9cDKGFLsRvfmTqitCjcC4/edit#responses')

answers = driver.find_element_by_class_name('freebirdFormeditorViewTabResponsesViewTabContent')
answers.click()

excel_Btn = driver.find_element_by_xpath('//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div/div/span/span')
excel_Btn.click()