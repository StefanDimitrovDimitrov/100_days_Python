from selenium import webdriver
chrome_driver_path = "C:\Forest\GoogleDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

driver.get("https://www.python.org/")
search_bar= driver.find_element_by_name("q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element_by_class_name("python-logo")

documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)

python_wiki = driver.find_element_by_xpath('//*[@id="container"]/li[4]/ul/li[10]/a')
print(python_wiki.text)


# driver.close() # close the current tab
driver.quit()  # exit the website or web app