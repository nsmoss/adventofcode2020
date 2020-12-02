#!/usr/bin/env python3.6


f = open("day2input.txt", "r")
lines = [line.rstrip() for line in f]

valid = 0

for line in lines:
    pwline = line.split()
    pwrange = pwline[0].split("-")
    pwletter = pwline[1].strip(":")
    pw = pwline[2]

    pwcount = pw.count(pwletter)
    if pwcount >= int(pwrange[0]) and pwcount <= int(pwrange[1]):
        valid += 1

print(valid)
