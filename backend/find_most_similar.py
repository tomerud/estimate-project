from .estimate_cost import estimate_cost

def find_most_similar(destination, month, origin, duration, travelerType, estimatedCost, dev_weight, far_away_weight, weather_weight, culture_weight):
    print("find_most_similar called with:")
    print(f"destination: {destination}, month: {month}, origin: {origin}, duration: {duration}")
    print(f"travelerType: {travelerType}, estimatedCost: {estimatedCost}")
    print(f"dev_weight: {dev_weight}, far_away_weight: {far_away_weight}, weather_weight: {weather_weight}, culture_weight: {culture_weight}")
    
    # Return the arguments as a list for now
    return [destination, month, origin, duration, travelerType, estimatedCost, dev_weight, far_away_weight, weather_weight, culture_weight]
