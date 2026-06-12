import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(lat, lon, flight_date):

    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?lat={lat}"
        f"&lon={lon}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print("Weather API Error")

        return {
            "temperature": 0,
            "wind_speed": 0,
            "humidity": 0,
            "visibility": 10,
            "condition": "Unknown"
        }

    data = response.json()

    forecasts = data["list"]

    target = None

    for item in forecasts:

        forecast_date = item["dt_txt"].split(" ")[0]

        if forecast_date == flight_date:
            target = item
            break

    if target is None:
        target = forecasts[0]

    print("\n===== WEATHER =====")
    print(target)

    return {
        "temperature": target["main"]["temp"],
        "wind_speed": target["wind"]["speed"],
        "humidity": target["main"]["humidity"],
        "visibility": target.get("visibility", 10000) / 1000,
        "condition": target["weather"][0]["description"]
    }