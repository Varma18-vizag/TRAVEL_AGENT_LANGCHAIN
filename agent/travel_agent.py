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

    print("\n===== TOOL OUTPUTS =====")

    print("\nWEATHER:")
    print(weather_data)

    print("\nHOTELS:")
    print(hotel_data)

    print("\nATTRACTIONS:")
    print(attractions_data)

    print("\nBUDGET:")
    print(budget_data)

    print("\n========================\n")

    prompt = f"""
You are a professional travel planning assistant.

Your job is to create a travel itinerary ONLY from the information provided below.

IMPORTANT RULES:

1. Use ONLY the information provided in the tool outputs.
2. NEVER invent hotels.
3. NEVER invent hotel addresses.
4. NEVER invent tourist attractions.
5. NEVER invent weather information.
6. NEVER invent prices or budget values.
7. If any information is unavailable, clearly mention:
   "Information not available."
8. Do not mention places outside the destination city.
9. Do not create fictional locations.
10. If hotel recommendations are empty, state that hotel information could not be retrieved.
11. If attraction information is empty, state that attraction information could not be retrieved.
12. Do not make assumptions.
13. Use the exact hotel names returned by the hotel tool.
14. Use the exact attraction names returned by the attractions tool.

Destination City:
{city}

Trip Duration:
{days} days

=========================
WEATHER INFORMATION
=========================
{weather_data}

=========================
HOTEL RECOMMENDATIONS
=========================
{hotel_data}

=========================
TOURIST ATTRACTIONS
=========================
{attractions_data}

=========================
BUDGET INFORMATION
=========================
{budget_data}

Create the response in the following format:

# Trip Overview

Provide a short introduction to the destination using only available information.

# Recommended Hotel

List ONLY hotels from the provided hotel data.

# Day-wise Itinerary

Create a day-wise plan using ONLY the attractions provided.

# Estimated Budget

Summarize the budget information.

# Travel Tips

Provide general travel tips relevant to the destination.

Remember:
If information is missing, say it is unavailable rather than creating information.
"""

    return generate_response(prompt)


def extract_city(query: str):

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
