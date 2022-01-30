# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def rivers_with_station(stations):
    temp_set = set()
    for station in stations:
        temp_set.add(station.river)
    return temp_set

def stations_by_river(stations):
    temp_dict = {}
    for station in stations:
        if station.river not in temp_dict:
            temp_dict[station.river] = []
        temp_dict[station.river].append(station.name)
    return temp_dict

def sorting_function(e):
    return e[1]

def rivers_by_station_number(stations, N):
    temp_dict = {}
    for station in stations:
        if station.river not in temp_dict:
            temp_dict[station.river] = 0
        else:
            temp_dict[station.river] += 1
    temp_list = list(temp_dict.items())
    temp_list.sort(reverse=True, key=sorting_function)
    while (N != len(temp_list) and temp_list[N-1][1] == temp_list[N][1]):
        N += 1
    return temp_list[:N]

def stations_by_distance(stations, p):
    temp_list = []
    for station in stations:
        temp_list.append((station.name, station.town, haversine(station.coord, p)))
    sorted_temp_list = sorted_by_key(temp_list, 2)
    return sorted_temp_list