from langchain.tools import tool


@tool
def estimate_budget(city : str ,days: int) -> str:
    """
    Estimate travel budget based on number of days.
    """

    hotel_per_day = 3000
    food_per_day = 1000
    transport_per_day = 500
    activities_per_day = 1000

    hotel_cost = hotel_per_day * days
    food_cost = food_per_day * days
    transport_cost = transport_per_day * days
    activities_cost = activities_per_day * days

    total = (hotel_cost + food_cost + transport_cost + activities_cost)
    

    return (
        f"Trip Duration: {days} days\n"
        f"Hotel Cost: {hotel_cost}\n"
        f"Food Cost: {food_cost}\n"
        f"Transport Cost: {transport_cost}\n"
        f"Activities Cost: {activities_cost}\n\n"
        f"Estimated Total Budget: {total}"
    )