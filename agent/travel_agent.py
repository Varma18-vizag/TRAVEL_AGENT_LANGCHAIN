from tools.weather import get_weather
from tools.hotel import get_hotels
from tools.attractions import get_attractions
from tools.budget import estimate_budget

from agent.router import route_query
from llm import generate_response

import re


def travel_agent(city: str, days: int):

    weather_data = get_weather.invoke(city)

    hotel_data = get_hotels.invoke(city)

    attractions_data = get_attractions.invoke(city)

    budget_data = estimate_budget.invoke(
        {
            "city": city,
            "days": days
        }
    )

    prompt = f"""
You are an expert travel planner.

Create a detailed travel itinerary.

City: {city}
Duration: {days} days

Weather Information:
{weather_data}

Hotel Recommendations:
{hotel_data}

IMPORTANT:
- Use ONLY the hotels provided above.
- Do NOT invent hotel names.
- Do NOT invent hotel addresses.
- If hotel data is unavailable, mention that clearly.

Tourist Attractions:
{attractions_data}

Budget Information:
{budget_data}

Generate:

1. Trip Overview
2. Recommended Hotel
3. Day-wise itinerary
4. Estimated Budget
5. Travel Tips
"""

    return generate_response(prompt)


def extract_city(query: str):

    # Weather in Goa
    match = re.search(
        r"(?:in|at|for|to)\s+([A-Za-z\s]+)",
        query,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    words = query.split()

    return words[-1].replace("?", "")


def run_agent(query: str):

    route = route_query(query)

    print("Selected Route:", route)

    # WEATHER
    if route == "weather":

        city = extract_city(query)

        return get_weather.invoke(city)

    # HOTELS
    elif route == "hotels":

        city = extract_city(query)

        return get_hotels.invoke(city)

    # ATTRACTIONS
    elif route == "attractions":

        city = extract_city(query)

        return get_attractions.invoke(city)

    # BUDGET
    elif route == "budget":

        days_match = re.search(r"\d+", query)

        if not days_match:
            return "Please specify the number of days."

        days = int(days_match.group())

        city = extract_city(query)

        return estimate_budget.invoke(
            {
                "city": city,
                "days": days
            }
        )

    # FULL TRIP PLANNER
    elif route == "full_trip":

        days_match = re.search(r"\d+", query)

        if not days_match:
            return (
                "Please specify trip duration.\n"
                "Example: Plan a 3 day trip to Goa"
            )

        days = int(days_match.group())

        city = extract_city(query)

        return travel_agent(
            city=city,
            days=days
        )

    return "Sorry, I could not understand your request."
