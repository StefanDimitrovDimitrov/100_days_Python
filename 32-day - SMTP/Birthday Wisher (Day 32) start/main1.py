import smtplib
import datetime as dt
import random
import smtplib
import os

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
print(MY_EMAIL)
print(PASSWORD)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()  # secure the connection
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="dimitrov22@yahoo.com",
            msg=f"Subject:Hello\n\n{quote}.")
