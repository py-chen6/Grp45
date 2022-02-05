from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

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
 
    assert radius_list == []