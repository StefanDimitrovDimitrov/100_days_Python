from selenium import webdriver
chrome_driver_path = "C:\Forest\GoogleDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")

driver.close() # close the current tab
driver.quit()  # exit the website or web app