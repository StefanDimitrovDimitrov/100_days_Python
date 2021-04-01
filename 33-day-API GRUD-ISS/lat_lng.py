import requests
from datetime import datetime
import _datetime

MY_LAT = 42.697708
MY_LNG = 23.321867

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json?", params=parameters)
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour


print(sunrise)
print(sunset)
print(current_hour)