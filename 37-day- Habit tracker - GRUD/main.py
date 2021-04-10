import requests
from datetime import date
import os

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.environ["TOKEN"]
USERNAME = "stefan22"
GRAPH_ID = "graph1"
today = date.today()
f_today = today.strftime("%Y%m%d")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{f_today}"
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{f_today}"
graph_config = {
    "id": GRAPH_ID,
    "name": "crunches",
    "unit": "cr",
    "type": "int",
    "color": "ajisai"
}
create_pixel = {
    "date": f_today,
    "quantity": input("How many crunches did you make today? "),
}
update_graph = {
    "quantity": "200",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

### CREATE
response = requests.post(url=post_endpoint, json=create_pixel, headers=headers)
print(response.text)

### UPDATE
# response = requests.put(url=put_endpoint, json=update_graph, headers=headers)
# print(response.text)

#### DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
