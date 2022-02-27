from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

def test_stations_level_over_threshold():
    statA = MonitoringStation("A", None, None, None, [1, 2], None, None)
    statB = MonitoringStation("B", None, None, None, [1, 2], None, None)
    statC = MonitoringStation("C", None, None, None, [1, 2], None, None)
    statD = MonitoringStation("D", None, None, None, [1, 2], None, None)
    statE = MonitoringStation("E", None, None, None, [2, 1], None, None) # Inconsistent case
    statF = MonitoringStation("F", None, None, None, None, None, None) # Inconsistent case

    statA.latest_level = 5
    statB.latest_level = 6
    statC.latest_level = 4
    statD.latest_level = 3
    
    stations = [statA, statB, statC, statD, statE, statF]
    rel_list = stations_level_over_threshold(stations, 2)
    assert isinstance(rel_list, list) # Check correct type of output
    assert isinstance(rel_list[0], tuple) # Check correct type of element within the output
    assert rel_list[0] == (statB, 5) # Check that the output is sorted in descending order
    assert len(rel_list) == 3 # statD, E, F should not be included