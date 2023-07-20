import pytest
from Challenge37.business_trip import business_trip, alaska_airlines_route_map

def test_possible_trip():
    assert business_trip(alaska_airlines_route_map, ['Metroville', 'Pandora']) == 82
    assert business_trip(alaska_airlines_route_map, ['Arendelle', 'New Monstropolis', 'Naboo']) == 115
def test_impossible_trip():
    assert business_trip(alaska_airlines_route_map, ['Naboo', 'Pandora']) is None
    assert business_trip(alaska_airlines_route_map, ['Narnia', 'Arendelle', 'Naboo']) is None
def test_empty_trip():
    assert business_trip(alaska_airlines_route_map, []) == 0
