#!/usr/bin/env python

import os

def createslope(inputfile, outputfile):
    os.remove(outputfile)
    fr = open(inputfile, "r")
    fa = open(outputfile, "a")
    lines = [line.rstrip() for line in fr]
    for line in lines:
        newline = line * 35
        fa.write(newline + os.linesep)
    fr.close()
    fa.close()

def gosledding(inputfile):
    fr = open(inputfile, "r")
    lines = [line.rstrip() for line in fr]
    treecount = 0
    sledpos = 0
    for line in lines:
        try:
            if line[sledpos] == "#":
                treecount += 1
            print(sledpos)
            sledpos += 3
        except IndexError:
            print(sledpos)
            break
    print(treecount)

if __name__ == "__main__":
    createslope("day3input.txt", "day3slope.txt")
    gosledding("day3slope.txt")
