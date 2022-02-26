from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import numpy as np
import random

def test_plot_water_levels():
    station1 = MonitoringStation(None, None, "Station 1", None, (10, 100), None, None)
    station2 = MonitoringStation(None, None, "Station 2", None, (2, 1), None, None)
    n = random.randrange(20, 500)
    dates = list(range(n))
    levels = np.random.randint(130, size=n)
    plot_water_levels(station1, dates, levels)
    plot_water_levels(station2, dates, levels)

def test_plot_water_level_with_fit():
    station1 = MonitoringStation(None, None, "Station 1", None, (10, 100), None, None)
    station2 = MonitoringStation(None, None, "Station 2", None, (10, 100), None, None)
    n = random.randrange(20, 500)
    dates = list(range(n))
    levels = np.random.randint(130, size=n)
    plot_water_level_with_fit(station1, dates, levels, 5)
    plot_water_level_with_fit(station2, dates, levels, 3)