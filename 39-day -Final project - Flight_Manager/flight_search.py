import requests
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
query = "locations/query"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")


class FlightSearch:

    def get_destination_code(self, city_name):

        apikey = {
            "apikey": TEQUILA_API_KEY
        }

        params = {
            "term": city_name
        }

        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/{query}",
                                params=params,
                                headers=apikey)

        data = response.json()
        IATA_code = data["locations"][0]["code"]
        print(IATA_code)
        return IATA_code