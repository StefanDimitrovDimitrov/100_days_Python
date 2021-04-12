import requests
from datetime import datetime
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT")
sheet_endpoint = os.getenv("sheet_endpoint")
TOKEN_sheet = os.getenv("TOKEN_sheet")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

my_exrs = {
    "query": "ran 3 miles",
    "gender": "male",
    "weight_kg": 76,
    "height_cm": 175,
    "age": 35
}
my_exrs["query"] = input(f'What were your exercise today? ')
response = requests.post(url=ENDPOINT, json=my_exrs, headers=headers)
print(response)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {"Authorization": TOKEN_sheet}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers)

    print(sheet_response.text)
