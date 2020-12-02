#!/usr/bin/env python3.6


f = open("day2input.txt", "r")
lines = [line.rstrip() for line in f]

valid = 0

for line in lines:
    pwline = line.split()
    pwrange = pwline[0].split("-")
    pwletter = pwline[1].strip(":")
    pw = pwline[2]

    try:
        firstopt = (pw[int(pwrange[0])-1] == pwletter)
    except IndexError:
        firstopt = False
    try:
        secondopt = (pw[int(pwrange[1])-1] == pwletter)
    except IndexError:
        secondopt = False

    if firstopt == True and secondopt == False:
        valid += 1
    if firstopt == False and secondopt == True:
        valid += 1

print(valid)
