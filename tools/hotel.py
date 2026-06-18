from langchain.tools import tool
from dotenv import load_dotenv
import requests
import os

load_dotenv()


@tool
def get_hotels(city: str) -> str:
    """
    Get hotel recommendations for a given city using Geoapify.
    """

    api_key = os.getenv("GEOAPIFY_API_KEY")

    try:

        # Step 1: Get city coordinates
        geocode_url = (
            "https://api.geoapify.com/v1/geocode/search"
            f"?text={city}"
            f"&limit=1"
            f"&apiKey={api_key}"
        )

        geo_response = requests.get(geocode_url)

        if geo_response.status_code != 200:
            return (
                f"Failed to fetch location information.\n"
                f"Status Code: {geo_response.status_code}"
            )

        geo_data = geo_response.json()

        print("GEO DATA:")
        print(geo_data)

        if not geo_data.get("features"):
            return f"Could not find location: {city}"

        coordinates = (
            geo_data["features"][0]
            ["geometry"]["coordinates"]
        )

        lon = coordinates[0]
        lat = coordinates[1]

        print(f"LAT: {lat}")
        print(f"LON: {lon}")

        # Step 2: Search nearby hotels
        hotel_url = (
            "https://api.geoapify.com/v2/places"
            f"?categories=accommodation.hotel"
            f"&filter=circle:{lon},{lat},20000"
            f"&bias=proximity:{lon},{lat}"
            f"&limit=20"
            f"&apiKey={api_key}"
        )

        print("HOTEL URL:")
        print(hotel_url)

        hotel_response = requests.get(hotel_url)

        if hotel_response.status_code != 200:
            return (
                f"Failed to fetch hotel data.\n"
                f"Status Code: {hotel_response.status_code}"
            )

        hotel_data = hotel_response.json()

        print("HOTEL DATA:")
        print(hotel_data)

        hotels = []

        for hotel in hotel_data.get("features", []):

            properties = hotel.get("properties", {})

            name = properties.get("name")

            address = properties.get("formatted", "Address unavailable")

            if name:

                hotels.append(
                    f"Hotel: {name}\n"
                    f"Address: {address}"
                )

        if not hotels:
            return f"No hotels found near {city}"

        return "\n\n".join(hotels[:10])

    except Exception as e:

        return f"Hotel Tool Error: {str(e)}"
