from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

def test_stations_level_over_threshold():
    statA = MonitoringStation("A", None, None, None, [0.1, 2.0], None, None)
    statB = MonitoringStation("B", None, None, None, [0.1, 2.0], None, None)
    statC = MonitoringStation("C", None, None, None, [0.1, 2.0], None, None)
    statD = MonitoringStation("D", None, None, None, [2.0, 0.1], None, None) # inconsistent case
    statE = MonitoringStation("E", None, None, None, None, None, None) # inconsistent case

    statA.latest_level = 1
    statB.latest_level = 2
    statC.latest_level = 3
    
    stations = [statA, statB, statC, statD, statE]
    rel_list = stations_level_over_threshold(stations, 2)
    assert isinstance(rel_list, list) # Check correct type of output
    assert isinstance(rel_list[0], tuple) # Check correct type of element within the output
    assert rel_list == [(statC, 3)] # Check that the output is exactly right