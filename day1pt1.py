#!/usr/bin/env python3.6

def otherlines(line, listoflines):
    newlist = listoflines.copy()
    newlist.remove(line)
    return newlist

def findsum(xlist):
    for line in xlist:
#        print(xlist.index(line))
        olns = otherlines(line, xlist)
        for oln in olns:
            sum = int(line) + int(oln)
            if sum == 2020:
                print(line)
                print(oln)
                print(int(line) * int(oln))
                return

f = open("day1input.txt", "r")
lines = [line.rstrip() for line in f]

findsum(lines)
