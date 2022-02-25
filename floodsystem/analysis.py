import matplotlib
import numpy as np

# Task 2F
def polyfit(dates, levels, p):
    dates_floats = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(dates_floats - dates_floats[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly, dates_floats[0]