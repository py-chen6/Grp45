from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def main():
    stations = build_station_list()
    temp_list = inconsistent_typical_range_stations(stations)
    temp_list.sort()
    print(temp_list)

if __name__ == "__main__":
    main()