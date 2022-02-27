# Copyright (C) 2022 Robert T. Chen
#
# Import the relevant modules
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    # Prints the names of the 10 stations at which the current relative level is highest, with the relative level alongside
    for station, highest_rel_level in stations_highest_rel_level(stations, 10):
        name = station.name
        print(name, highest_rel_level)

if __name__ == "__main__":
    run()
