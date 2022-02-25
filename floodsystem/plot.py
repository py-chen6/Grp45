import matplotlib.pyplot as plt
import matplotlib.dates as da
from .analysis import polyfit

# Task 2E
def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)

    if station.typical_range_consistent():
        plt.axhline(y = station.typical_range[0], color = 'r', linestyle = '-')
        plt.axhline(y = station.typical_range[1], color = 'r', linestyle = '-')

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()

# Task 2F
def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)

    plt.plot(dates, levels)
    dates_floats = da.date2num(dates)
    plt.plot(dates, poly(dates_floats - dates_floats[0]), color='g')

    if station.typical_range_consistent():
        plt.axhline(y = station.typical_range[0], color = 'r', linestyle = '-')
        plt.axhline(y = station.typical_range[1], color = 'r', linestyle = '-')

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()

    
    plt.show()