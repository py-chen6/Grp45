# Copyright (C) 2022 Robert T. Chen
#
# Import the relevant modules
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Write a program that prints a list of tuples
    (station name, town, distance), for the 10 closest and the 10 furthest stations
    from the Cambridge city centre, (52.2053, 0.1218)"""

    # Build list of stations
    stations = build_station_list()

    # Build list of (station name, station town, distance from Cam city centre)
    distance_list = stations_by_distance(stations, (52.2053, 0.1218))
    
    print(distance_list[:10])
    print(distance_list[-10:])

if __name__ == "__main__":
    run()