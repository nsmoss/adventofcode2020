#!/usr/bin/env python

import os

def createslope(inputfile, outputfile):
    os.remove(outputfile)
    fr = open(inputfile, "r")
    fa = open(outputfile, "a")
    lines = [line.rstrip() for line in fr]
    for line in lines:
        newline = line * 100
        fa.write(newline + os.linesep)
    fr.close()
    fa.close()
    return outputfile

def gosledding(inputfile, rightmod, downmod):
    fr = open(inputfile, "r")
    lines = [line.rstrip() for line in fr]
    desiredlines = lines[::downmod]
    treecount = 0
    sledpos = 0
    for line in desiredlines:
        try:
            if line[sledpos] == "#":
                treecount += 1
            sledpos += rightmod
        except IndexError:
            break
    return(treecount)

def runcourse(inputfile, outputfile, rightmod, downmod):
    return gosledding(createslope(inputfile, outputfile), rightmod, downmod)

def multirun():
    inputfile = input("Enter input file: ")
    outputfile = input("Enter desired output file: ")
    numberofruns = int(input("Number of runs (Default 1): ") or "1")
    
    result = 1
    for i in range(numberofruns):
        rightmod = int(input("Enter right slope for Run {}: ".format(i+1)))
        downmod = int(input("Enter down slope for Run {} (Default 1): ".format(i+1)) or "1")
        result = result * runcourse(inputfile, outputfile, rightmod, downmod)
    print(result)

if __name__ == "__main__":
    multirun()
