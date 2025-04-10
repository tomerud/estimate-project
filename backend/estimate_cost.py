from DB.helpers import check_city_exists
from DB.get_budget_and_flight_price import get_budget_and_flight_price

def estimate_cost(origin, destination,month, duration, travel_type):

    # Check if the destination exists
    if not check_city_exists(destination):
        return -1, -1, -1
    
    if not check_city_exists(origin):
        return -2, -2, -2
    
    try:
        duration = int(duration)
    except ValueError:
        return  -3, -3, -3
    
    daily_budget, fligth_price = get_budget_and_flight_price(origin, destination, month, travel_type)  
    print(daily_budget, fligth_price)

    total_cost = daily_budget * duration + fligth_price
    return daily_budget, fligth_price, total_cost

 