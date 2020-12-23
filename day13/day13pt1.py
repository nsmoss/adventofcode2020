#!/usr/bin/env python

rawdata = open("day13input.txt").read().splitlines()
earliest = int(rawdata[0])
busses = [bus for bus in rawdata[1].split(",") if bus != "x"]

def find_depart(busID, departable):
    closest_departure = 0
    while closest_departure < departable:
        closest_departure += busID
    return closest_departure
    
possible_departures = []
bus_tracker = []
for bus in busses:
    possible_departures.append(find_depart(int(bus), earliest))
    bus_tracker.append(int(bus))
earliest_bus = (min(possible_departures))
print((earliest_bus - earliest) * bus_tracker[possible_departures.index(earliest_bus)])
