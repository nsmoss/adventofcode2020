#!/usr/bin/env python

rawdata = open("day13test.txt").read().splitlines()
bus_lines = [bus for bus in rawdata[1].split(",")]

possible_departures = []
t_tracker = []
for line in bus_lines:
    if line.isnumeric():
        possible_departures.append(int(line))
        t_tracker.append(bus_lines.index(line))

new_departures = possible_departures
while new_departures[1] != (new_departures[0] + 1):
    new_departures = [sum(i) for i in zip(new_departures, possible_departures)]
    
print(new_departures)

