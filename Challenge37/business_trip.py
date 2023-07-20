# The hardest thing in this challenge is writing all of this graph.
alaska_airlines_route_map = {
    'Metroville': {'Pandora': 82, 'Arendelle': 99, 'New Monstropolis': 105, 'Naboo': 26, 'Narnia': 37},
    'Pandora': {'Metroville': 82, 'Arendelle': 150},
    'Arendelle': {'Pandora': 150, 'New Monstropolis': 42, 'Metroville': 99},
    'New Monstropolis': {'Metroville': 105, 'Arendelle': 99, 'Naboo': 73},
    'Naboo': {'Metroville': 26, 'New Monstropolis': 73, 'Narnia': 250},
    'Narnia': {'Metroville': 37, 'Naboo': 250}
}


def has_direct_flight(graph, src, dest):
    """
    Check if there is a direct flight from the departure city to the destination city.
    """
    return dest in graph.get(src, {})

def calculate_trip_cost(graph, cities):
    """
    Calculate the total cost of a trip based on the route and the airline route map.
    """

    total_cost = 0
    for i in range(len(cities) - 1):
        src = cities[i]
        dest = cities[i + 1]
        if not has_direct_flight(graph, src, dest):
            return None
        total_cost += graph[src][dest]
    return total_cost

def business_trip(graph, city_names):
    """
    Determine if the trip is possible with direct flights and calculate the total trip cost.
    """
    return calculate_trip_cost(graph, city_names)



# Test cases:
print(business_trip(alaska_airlines_route_map, ['Metroville', 'Pandora']))  
print(business_trip(alaska_airlines_route_map, ['Arendelle', 'New Monstropolis', 'Naboo']))
print(business_trip(alaska_airlines_route_map, ['Naboo', 'Pandora'])) 
print(business_trip(alaska_airlines_route_map, ['Narnia', 'Arendelle', 'Naboo']))  
print(business_trip(alaska_airlines_route_map, ['Narnia', 'Metroville', 'Naboo']))  #This case is not logical. 