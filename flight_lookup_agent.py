import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPID_API_KEY")


def get_flight_details(
    flight_number,
    flight_date
):

    url = (
        f"https://aerodatabox.p.rapidapi.com/"
        f"flights/number/{flight_number}/{flight_date}"
    )

    querystring = {
        "withAircraftImage": "false",
        "withLocation": "false",
        "withFlightPlan": "false",
        "dateLocalRole": "Both"
    }

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    if response.status_code != 200:
       print("========== API ERROR ==========")
       print("Status Code:", response.status_code)
       print("Response:", response.text)
       print("===============================")
       return None

    print("Status Code:", response.status_code)
    print("Response Text:", response.text[:500])

    try:
       data = response.json()
    except Exception as e:
       print("JSON Error:", e)
       print("Raw Response:", response.text[:1000])
       return None

    print("\n===== AERODATABOX =====")
    print(data)

    if not data:
        return None

    flight = data[0]

    return {

        "airline":
        flight["airline"]["name"],

        "origin":
        flight["departure"]["airport"]["iata"],

        "destination":
        flight["arrival"]["airport"]["iata"],

        "origin_airport":
        flight["departure"]["airport"]["name"],

        "destination_airport":
        flight["arrival"]["airport"]["name"],

        "departure_time":
        flight["departure"]["scheduledTime"]["local"].split(" ")[1],

        "travel_date":
        flight_date,
        

        "flight_status":
        flight["status"]
    }