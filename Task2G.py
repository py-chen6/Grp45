from floodsystem.stationdata import build_station_list, update_water_levels

def main():
    severe = []
    high = []
    moderate = []
    low = []
    no_data = []
    stations = build_station_list()
    update_water_levels(stations)

    for station in stations:
        # fetch_measure_levels(station.measure_id, dt=timedelta(days=0.2))

        # Risk can only be calculated if there is typical range to compare to
        if station.typical_range_consistent() and station.latest_level is not None:

            # Originially: Weighted average of all data in the last day
            # But since fetching that data takes too long, use latest_level instead
            # avg = np.average(levels, weights=list(range(len(levels))))
            percentage = (station.latest_level - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])
            if percentage >= 1:
                severe.append(station.name)
            elif percentage >= 0.75:
                high.append(station.name)
            elif percentage >= 0.5:
                moderate.append(station.name)
            else:
                low.append(station.name)
        else:
            no_data.append(station.name)

    severe.sort()
    high.sort()
    moderate.sort()
    low.sort()
    no_data.sort()
    print(f"Severe Risk:\n{severe}\n")
    print(f"High Risk:\n{high}\n")
    print(f"Moderate Risk:\n{moderate}\n")
    print(f"Low Risk:\n{low}\n")
    print(f"No Reliable Data:\n{no_data}\n")

if __name__ == "__main__":
    main()