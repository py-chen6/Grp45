from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

def test_stations_by_distance():
    stations = build_station_list()
    x = stations_by_distance(stations, (52.2053, 0.1218))    
    assert isinstance(x, list)

def test_stations_within_radius():
    stations = build_station_list()
    x = stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert isinstance(x, list)
    
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