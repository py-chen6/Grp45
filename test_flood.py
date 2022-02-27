from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

def test_stations_level_over_threshold():
    station1 = MonitoringStation(None, None, "Station 1", None, (0.15, 0.1), None, None)
    temp_list = stations_level_over_threshold(station1, 0.8)
    assert temp_list == []

def test_stations_highest_rel_level():
    station1 = MonitoringStation(None, None, "Station 1", None, (0.15, 0.1), None, None)
    temp_list = stations_highest_rel_level(station1, 0.8)
    assert temp_list == []