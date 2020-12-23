#!/usr/bin/env python

from itertools import product

rawdata = [line.split(" = ") for line in open("day14input.txt").read().splitlines()]
memory_values = {}
bitmask = ""

for line in rawdata:
    if line[0] == "mask":
        bitmask = line[1]
    else:
        mem_location = line[0].strip("mem[]")
        binaryvalue = f'{int(mem_location):036b}'
        for i in range(len(bitmask)):
            if bitmask[i] == "1":
                binaryvalue = binaryvalue[:i] + "1" + binaryvalue[i+1:]
            if bitmask[i] == "X":
                binaryvalue = binaryvalue[:i] + "X" + binaryvalue[i+1:]
        floatnum = binaryvalue.count("X")
        if floatnum > 0:
            sequences = [x for x in product([0,1], repeat=floatnum)]
            for sequence in sequences:
                new_binary = binaryvalue
                float_iterator = 0
                for i, char in enumerate(new_binary):
                    if char == "X":
                        new_binary = new_binary[:i] + str(sequence[float_iterator]) + new_binary[i+1:]
                        float_iterator += 1
                memory_values[int(new_binary, 2)] = int(line[1])
        else:
            memory_values[int(binaryvalue, 2)] = int(line[1])

print(sum(memory_values.values()))
