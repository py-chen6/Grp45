from floodsystem.analysis import polyfit
from matplotlib.dates import date2num
import numpy as np
import datetime
import random

def test_polyfit():
    n = random.randrange(20, 500)
    dates = []
    now = datetime.datetime.utcnow()
    for i in range(n):
        dates.append(now + datetime.timedelta(seconds=i))
    levels = np.random.randint(130, size=n)
    m = random.randrange(10)
    a, b = polyfit(dates, levels, m)
    assert isinstance(a, np.poly1d)
    assert isinstance(b, float)
    assert a.order == m
    assert b == date2num(now)