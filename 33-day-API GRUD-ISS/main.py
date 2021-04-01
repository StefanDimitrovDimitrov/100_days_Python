import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

data = response.json()
latitude = float(data["iss_position"]['latitude'])
longitude = float(data["iss_position"]['longitude'])

iss_position = (latitude, longitude)

print(iss_position)