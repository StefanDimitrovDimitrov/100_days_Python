from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
import smtplib
import schedule


USER = os.getenv('USER')
PASS = os.getenv('PASS')
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")



def send_list_with_positions():
    chrome_driver_path = "C:\Forest\GoogleDriver\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(
        "https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
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


    element_2 = driver.find_element_by_xpath('/html/body/div[8]/header/div[2]/nav/ul/li[3]/a')
    element_2.click()
    time.sleep(3)


    search = driver.find_element_by_css_selector('.ember-view input')
    print(search.text)
    search.send_keys('Python')
    time.sleep(1)
    location = driver.find_element_by_css_selector('.jobs-search-box__input--location input')
    location.send_keys('Sofia')
    time.sleep(1)
    search_btn = driver.find_element_by_css_selector('.jobs-search-box__container button')
    search_btn.click()
    time.sleep(2)
    # list_job_titles = driver.find_elements_by_css_selector('.jobs-search-results__list a')
    list_job_titles = driver.find_elements_by_css_selector('.jobs-search-results__list .job-card-list__title')
    time.sleep(1)
    dict_positions_companies = {}


    for i, title in enumerate(list_job_titles):
        dict_positions_companies[i] = {
            'position': title.text,
            'link_position': title.get_attribute('href')
        }
    list_job_company = driver.find_elements_by_css_selector('.jobs-search-results__list .job-card-container__company-name')
    time.sleep(1)
    for i, company in enumerate(list_job_company):
        dict_positions_companies[i].update({
            'company': company.text,
            'link_company': company.get_attribute('href')
        })


    python_positions_list = []

    for key, value in dict_positions_companies.items():
        if 'Python' in value['position'] and 'Senior' not in value['position']:
            python_positions_list.append(value)


    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()  # secure the connection
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:List_Positions\n\n{[[f'{k}: {v}' for k,v in l.items()] for l in python_positions_list]}")
    driver.quit()

schedule.every().day.at('09:00').do(send_list_with_positions)

while True:
    schedule.run_pending()
    time.sleep(1)

