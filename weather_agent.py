import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(lat, lon):

    url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?lat={lat}"
    f"&lon={lon}"
    f"&appid={API_KEY}"
    f"&units=metric"
)

    response = requests.get(url)


    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "wind_speed": data["wind"]["speed"],
        "humidity": data["main"]["humidity"],
        "visibility": data.get("visibility", 10000) / 1000,
        "condition": data["weather"][0]["description"]
    }