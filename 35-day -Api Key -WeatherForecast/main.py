import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = '*************'
auth_token = '*************'

weather_params= {
    "lat": 42.697708,
    "lon": 23.321867,

    "exclude": "currently,daily,minutely",
    "appid": "****************"

}


data = requests.get(OWM_Endpoint, params=weather_params)
data.raise_for_status()
current_data = data.json()
data_for_twelve_hours = current_data["hourly"][:12]

will_rain = False
for day in data_for_twelve_hours:
    if day["weather"][0]["id"] < 700:
        will_rain = True
[print(f'{data_for_twelve_hours.index(day)}h.  "Bring your umbrella."') for day in data_for_twelve_hours if day["weather"][0]["id"] < 700]

# print(current_data["hourly"])

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="It's going to rain.Bring your umbrella ☂",
        from_='********',
        to='*********'
    )

    print(message.status)