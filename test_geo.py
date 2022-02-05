from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

def test_stations_by_distance():
    '''Test Task1B'''
    # Build list of stations
    stations = build_station_list()

    # Build list of (station name, station town, distance from Cam city centre)
    distance_list = stations_by_distance(stations, (52.2053, 0.1218))
    closest_ten = distance_list[:10]
    closest_ten_rounded = [(name, town, round(dis, 3)) for name, town, dis in closest_ten]
    
    required_output = [('Cambridge Jesus Lock', 'Cambridge', 0.840), ('Bin Brook', 'Cambridge', 2.502), ("Cambridge Byron's Pool", 'Grantchester', 4.072), ('Cambridge Baits Bite', 'Milton', 5.116), ('Girton', 'Girton', 5.227), ('Haslingfield Burnt Mill', 'Haslingfield', 7.044), ('Oakington', 'Oakington', 7.128), ('Stapleford', 'Stapleford', 7.266), ('Comberton', 'Comberton', 7.735), ('Dernford', 'Great Shelford', 7.994)]
    assert required_output == closest_ten_rounded

def test_stations_within_radius():
    '''Test Task1C'''
    # Build list of stations
    stations = build_station_list()

    # Build list of of stations within 10 km of the Cambridge city centre
    # In alphabetical order
    radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)

    required_output = ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
 
    assert radius_list == required_output

def test_rivers_with_station():
    stations = build_station_list()
    x = rivers_with_station(stations)
    assert isinstance(x, set)

def test_stations_by_river():
    stations = build_station_list()   
    x = stations_by_river(stations)
    assert isinstance(x, dict)

def test_rivers_by_station_number():
    stations = build_station_list()
    x = rivers_by_station_number(stations, 10)
    assert len(x) == 10
    assert isinstance(x, list)