# Copyright (C) 2022 Robert T. Chen
#
# Import the relevant modules
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    # Print the name of each station at which the current relative level is over 0.8
    for station, rel_level in stations_level_over_threshold(stations, 0.8):
        name = station.name
        print(name, rel_level)

if __name__ == "__main__":
    run()
