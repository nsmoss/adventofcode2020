#!/usr/bin/env python

myFile = open("day7input.txt", "r")
content = myFile.read().splitlines()
allBags = {}


for line in content:
    line = line.replace("bags", "").replace("bag", "").strip(".")
    line = line.split("contain")
    allBags[line[0].strip()] = line[1].strip().split(',')

print(allBags)
def getBag(bags):
    total = 1
    if "no other" in allBags[bags]:
        return 1
    for colors in allBags[bags]:
        each = colors.split()
        total += int(each[0]) * getBag(" ".join(each[1:]))
    return total

print(getBag("shiny gold")-1)

