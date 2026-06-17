from langchain.tools import tool
from dotenv import load_dotenv
import requests
import os

load_dotenv()


@tool
def get_attractions(city: str) -> str:
    """
    Get popular attractions for a city.
    """

    api_key = os.getenv("OPENTRIPMAP_API_KEY")

    geo_url = (
        f"https://api.opentripmap.com/0.1/en/places/geoname"
        f"?name={city}"
        f"&apikey={api_key}"
    )

    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()

    lat = geo_data["lat"]
    lon = geo_data["lon"]

    places_url = (
        f"https://api.opentripmap.com/0.1/en/places/radius"
        f"?radius=10000"
        f"&lon={lon}"
        f"&lat={lat}"
        f"&rate=2"
        f"&limit=5"
        f"&apikey={api_key}"
    )

    places_response = requests.get(places_url)
    places_data = places_response.json()

    attractions = []

    for place in places_data["features"]:
        name = place["properties"]["name"]

        if name:
            attractions.append(name)

    return "\n".join(attractions)