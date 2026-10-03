# Final Project: Weather API Application
# Description: Connecting to the OpenWeather API Key

# Standard-library imports
import os
import requests

# Global Variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def load_weather_data(city_name):
    """Get request to openweathermap.org via your API key to get access to real-time weather"""

    params = {
        "q": city_name.lower(),
        "appid": API_KEY,
        "units": metric
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.rasie_for_status()
        return respons.json()
    except requests.RequestException as error:
        print(f"Weather request failed: {error}")
        return None