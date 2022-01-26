# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    tempSet = set()
    for station in stations:
        tempSet.add(station.river)
    return tempSet

def stations_by_river(stations):
    tempDict = {}
    for station in stations:
        if station.river not in tempDict:
            tempDict[station.river] = []
        tempDict[station.river].append(station.name)
    return tempDict