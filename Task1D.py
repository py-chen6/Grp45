from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def main():

    stations = build_station_list()

    tempSet = rivers_with_station(stations)
    sortedList = sorted(tempSet)
    print(f"{len(tempSet)} stations. First 10 - {sortedList[:10]}")

    tempDict = stations_by_river(stations)
    for x in ['River Aire', 'River Cam', 'River Thames']:
        tempDict[x].sort()
        print(tempDict[x])

if __name__ == "__main__":
    main()