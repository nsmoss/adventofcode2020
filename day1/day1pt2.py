#!/usr/bin/env python3.6

def otherlines(line, listoflines):
    newlist = listoflines.copy()
    newlist.remove(line)
    return newlist

def findsum(xlist):
    for line in xlist:
        olns = otherlines(line, xlist)
        for oln in olns:
            rolns = otherlines(oln, olns)
            for roln in rolns:
                sum = int(line) + int(oln) + int(roln)
                if sum == 2020:
                    print(line)
                    print(oln)
                    print(roln)
                    print(int(line) * int(oln) * int(roln))
                    return

f = open("day1input.txt", "r")
lines = [line.rstrip() for line in f]

findsum(lines)
