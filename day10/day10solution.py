#!/usr/bin/env python

f = open(r"day10input.txt", "r")
numbers = sorted([int(l.split()[0]) for l in f.readlines()])

def findDif(last_number):
    dif = []
    for n in numbers:
        dif.append(n-last_number)
        last_number = n
    dif.append(3)
    return dif

def findArrs(dif):
    temp_list = []
    mult_list = []
    for n in dif:
        if n != 3:
            temp_list.append(n)
        elif n == 3:
            if len(temp_list) > 3:
                mult_list.append((len(temp_list)-1)*2+(len(temp_list)-3))
            elif len(temp_list) > 1:
                mult_list.append((len(temp_list)-1)*2)
            print(temp_list)
            print(mult_list)
            temp_list = []
    r2 = 1
    for x in mult_list:
        r2 = r2 * x
    return r2

dif = findDif(0)
r1 = dif.count(1)*(dif.count(3))

print("Result Part 1: ", r1)
print("Result Part 2: ", findArrs(dif))

#For part 2 I'm creating a list for every sequence of 1's between 3's, then finding all possible combinations in the list and multiplying all of them.
