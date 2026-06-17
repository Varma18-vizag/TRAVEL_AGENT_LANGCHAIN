from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

@tool
def get_weather(city: str) -> str:
    """Fetch the current weather data of a city"""

    api_key = os.getenv("WEATHERSTACK_API_KEY")

    url = (
        f"http://api.weatherstack.com/current"
        f"?access_key={api_key}"
        f"&query={city}"
    )

    response = requests.get(url)

    try:

        data = response.json()

        if "current" not in data:
            return (
                f"Weather data unavailable "
                f"for {city}"
            )

        current = data["current"]

        return (
            f"Temperature: {current['temperature']}°C\n"
            f"Weather: {current['weather_descriptions'][0]}"
        )

    except Exception as e:

        return f"Weather Tool Error: {str(e)}"