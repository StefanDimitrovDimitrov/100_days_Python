import requests
from bs4 import BeautifulSoup
import datetime as dt
import smtplib
import os

url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

headers = {
    "Accept-Language": "en-US,en;q=0.9,en-GB;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
}

response = requests.get(url=url, headers=headers)

data = response.text

soup = BeautifulSoup(data, "html.parser")

item_price = float(soup.find(name="span",id="priceblock_ourprice").getText().split("$")[1])
item_name = soup.find(name="span",id="productTitle").getText().split(", ")[0].strip()



MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

if item_price <= 100:

        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()  # secure the connection
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="dimitrov22@yahoo.com",
                msg=f"Subject:Buy_now\n\nItem Title: {item_name}\nPrice: {item_price}\nLink: {url} .")