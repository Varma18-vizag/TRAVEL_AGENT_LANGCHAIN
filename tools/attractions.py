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

    try:

        # STEP 1: Get coordinates
        geo_url = (
            f"https://api.opentripmap.com/0.1/en/places/geoname"
            f"?name={city}"
            f"&apikey={api_key}"
        )

        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        print("GEO DATA:")
        print(geo_data)

        if "lat" not in geo_data or "lon" not in geo_data:
            return (
                f"Could not find coordinates for {city}.\n"
                f"Response: {geo_data}"
            )

        lat = geo_data["lat"]
        lon = geo_data["lon"]

        print("PASSED LAT/LON STEP")

        # STEP 2: Get attractions
        places_url = (
            f"https://api.opentripmap.com/0.1/en/places/radius"
            f"?radius=10000"
            f"&lon={lon}"
            f"&lat={lat}"
            f"&rate=2"
            f"&limit=5"
            f"&apikey={api_key}"
        )

        print("PLACES URL:")
        print(places_url)

        places_response = requests.get(places_url)

        print("PLACES STATUS:")
        print(places_response.status_code)

        places_data = places_response.json()

        print("PLACES DATA:")
        print(places_data)

        if "features" not in places_data:
            return (
                f"No attractions data received.\n"
                f"Response: {places_data}"
            )

        attractions = []

        for place in places_data.get("features", []):

            name = (
                place.get("properties", {})
                .get("name", "")
            )

            if name:
                attractions.append(name)

        if not attractions:
            return f"No attractions found for {city}"

        return "\n".join(attractions)

    except Exception as e:

        return f"Attractions Tool Error: {str(e)}"
