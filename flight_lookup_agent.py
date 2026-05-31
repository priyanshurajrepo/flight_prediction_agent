import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv(
    "AVIATIONSTACK_API_KEY"
)

def get_flight_details(
    flight_number
):

    flight_number = (
        flight_number
        .replace(" ", "")
        .upper()
    )

    url = (
        "http://api.aviationstack.com/v1/flights"
        f"?access_key={API_KEY}"
        f"&flight_iata={flight_number}"
    )

    response = requests.get(url)

    data = response.json()

    print("Flight Number:", flight_number)
    print("API Response Count:", len(data["data"]))
    

    if len(data["data"]) == 0:

        return None

    flight = data["data"][0]

    return {

        "airline":
        flight["airline"]["name"],

        "origin":
        flight["departure"]["iata"],

        "destination":
        flight["arrival"]["iata"],

        "departure_time":
        flight["departure"]["scheduled"]

    }