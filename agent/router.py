from llm import generate_response


def route_query(query: str):

    query = query.lower()

    if "weather" in query:
        return "weather"

    elif "hotel" in query:
        return "hotels"

    elif "attraction" in query:
        return "attractions"

    elif "budget" in query:
        return "budget"

    else:
        return "full_trip"