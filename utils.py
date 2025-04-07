import random
from DB.helpers import check_destination_exists

def estimate_cost(destination, duration, travel_type):

    # Check if the destination exists
    if not check_destination_exists(destination):
        return -1

    # Convert duration to an integer
    try:
        duration = int(duration)
    except ValueError:
        return -1  # Return -1 if duration is not a valid integer

    # Calculate the base cost
    base_cost = duration * 200

    # Adjust the cost based on the travel type
    if travel_type.lower() == "backpacker":
        return base_cost * 0.7
    elif travel_type.lower() == "expensive":
        return base_cost * 2
    else:
        return base_cost