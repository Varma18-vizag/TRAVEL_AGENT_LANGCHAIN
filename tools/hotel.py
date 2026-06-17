from langchain.tools import tool
from dotenv import load_dotenv
import requests
import os

load_dotenv()


@tool
def get_hotels(city: str) -> str:
    """
    Get hotels for a given city using Geoapify.
    """

    api_key = os.getenv("GEOAPIFY_API_KEY")

    try:
       

        geocode_url = (
            "https://api.geoapify.com/v1/geocode/search"
            f"?text={city}"
            f"&limit=1"
            f"&apiKey={api_key}"
        )

        geo_response = requests.get(geocode_url)

        if geo_response.status_code != 200:
            return "Failed to fetch location information."

        geo_data = geo_response.json()

        if not geo_data["features"]:
            return f"Could not find location: {city}"

        coordinates = geo_data["features"][0]["geometry"]["coordinates"]

        lon = coordinates[0]
        lat = coordinates[1]

      

        hotel_url = (
            "https://api.geoapify.com/v2/places"
            f"?categories=accommodation.hotel"
            f"&filter=circle:{lon},{lat},10000"
            f"&limit=10"
            f"&apiKey={api_key}"
        )

        hotel_response = requests.get(hotel_url)

        if hotel_response.status_code != 200:
            return "Failed to fetch hotel data."

        hotel_data = hotel_response.json()

        hotels = []

        for hotel in hotel_data.get("features", []):

            properties = hotel.get("properties", {})

            name = properties.get("name")

            address = properties.get("formatted")

            if name:
                hotels.append(
                    f"Hotel: {name}\n"
                    f"Address: {address}"
                )

        if not hotels:
            return f"No hotels found near {city}"

        return "\n\n".join(hotels)

    except Exception as e:
        return f"Error: {str(e)}"