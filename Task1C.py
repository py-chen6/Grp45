# Copyright (C) 2022 Robert T. Chen
#
# Import the relevant modules
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Write a program that returns a list of stations within 10 km of the
    Cambridge city centre (coordinate (52.2053, 0.1218))"""

    # Build list of stations
    stations = build_station_list()

    # Build list of of stations within 10 km of the Cambridge city centre
    # In alphabetical order
    radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)
    
    print(radius_list)

if __name__ == "__main__":
    run()