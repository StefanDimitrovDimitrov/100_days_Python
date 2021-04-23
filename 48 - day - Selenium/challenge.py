from selenium import webdriver

chrome_driver_path = "C:\Forest\GoogleDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

lis = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

dict_result = {}

for i,li in enumerate(lis):
    time = li.find_element_by_tag_name('time').get_attribute('datetime').split("T")[0]
    name = li.find_element_by_tag_name('a').text
    dict_result[i] = {
        "time": time,
        "name": name
    }

print(dict_result)
