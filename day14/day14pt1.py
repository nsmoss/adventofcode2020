#!/usr/bin/env python

rawdata = [line.split(" = ") for line in open("day14input.txt").read().splitlines()]
memory_values = {}
bitmask = ""

for line in rawdata:
    if line[0] == "mask":
        bitmask = line[1]
    else:
        binaryvalue = f'{int(line[1]):036b}'
        mem_location = line[0].strip("mem[]")
        for i in range(len(bitmask)):
            if bitmask[i] == "1":
                binaryvalue = binaryvalue[:i] + "1" + binaryvalue[i+1:]
            if bitmask[i] == "0":
                binaryvalue = binaryvalue[:i] + "0" + binaryvalue[i+1:]
        memory_values[mem_location] = int(binaryvalue, 2)

print(sum(memory_values.values()))
