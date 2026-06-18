from langchain.tools import tool
import requests


@tool
def get_weather(city: str) -> str:
    """
    Fetch weather data for a city.
    """

    geo_url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )

    geo_data = requests.get(geo_url).json()

    if "results" not in geo_data:
        return f"City not found: {city}"

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&current_weather=true"
    )

    weather_data = requests.get(weather_url).json()

    current = weather_data["current_weather"]

    return (
        f"Temperature: {current['temperature']}°C\n"
        f"Wind Speed: {current['windspeed']} km/h"
    )
