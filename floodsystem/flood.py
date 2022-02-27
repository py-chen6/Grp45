# Import the relevant modules
from utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    '''Requirements for Task 2B'''
    temp_list = []
    for station in stations:
        if station.relative_water_level() is None or station.relative_water_level() <= tol:
            continue
        temp_list.append((station, station.relative_water_level()))
        sorted_temp_list = sorted_by_key(temp_list, 1, reverse=True)
    return sorted_temp_list

def stations_highest_rel_level(stations, N):
    '''Requirements for Task 2C'''
    temp_list = stations_level_over_threshold(stations, 0.8)
    return temp_list[:N]
