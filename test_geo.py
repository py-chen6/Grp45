from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius

def test_stations_by_distance():
    '''Test Task1B'''
    # Build list of stations
    stations = build_station_list()

    # Build list of (station name, station town, distance from Cam city centre)
    distance_list = stations_by_distance(stations, (52.2053, 0.1218))

    first_ten = [('Cambridge Jesus Lock', 'Cambridge', 0.8402364350834995), ('Bin Brook', 'Cambridge', 2.502274086951454), ("Cambridge Byron's Pool", 'Grantchester', 4.0720438555077125), ('Cambridge Baits Bite', 'Milton', 5.115589516578674), ('Girton', 'Girton', 5.227070345811418), ('Haslingfield Burnt Mill', 'Haslingfield', 7.044388165868453), ('Oakington', 'Oakington', 7.128249171700346), ('Stapleford', 'Stapleford', 7.265694306995238), ('Comberton', 'Comberton', 7.7350743760373675), ('Dernford', 'Great Shelford', 7.993861351711722)]
    assert distance_list == first_ten

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