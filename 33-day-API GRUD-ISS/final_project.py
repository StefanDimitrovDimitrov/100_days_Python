from datetime import datetime
import requests
import smtplib
import time
MY_LAT = 42.697708
MY_LNG = 23.321867

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    data = response.json()
    iss_latitude = float(data["iss_position"]['latitude'])
    iss_longitude = float(data["iss_position"]['longitude'])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True

def is_nigth():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json?", params=parameters)
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

# while True:
#     time.sleep(68)
    if is_iss_overhead() and is_nigth():
        connection = smtplip.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg = "Subject:Look Up \n\nThe ISS is above you in the sky"
        )