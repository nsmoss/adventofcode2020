#!/usr/bin/env python

from itertools import combinations

xmas_code = open("day9input.txt").read().splitlines()
pre_length = 25

def findsum(preamble, current_num):
    return [pair for pair in combinations(preamble, 2) if sum(pair) == current_num]

def find_bad_num(number_set):
    code_pointer = pre_length
    ruleworks = True
    while ruleworks == True:
        preamble = list(map(int, xmas_code[code_pointer - pre_length:code_pointer]))
        current_num = int(xmas_code[code_pointer])
        valid_combos = findsum(preamble, current_num)
        if valid_combos == []:
            ruleworks = False
            return(current_num)
        else:
            code_pointer += 1

def find_weakness(number_set):
    num_sum = 0
    bad_num = find_bad_num(number_set)
    start_pointer = 0
    while num_sum != bad_num:
        num_pointer = start_pointer + 1
        num_tracker = list(map(int, [number_set[start_pointer], number_set[num_pointer]]))
        while num_sum < bad_num:
            num_sum = sum(num_tracker)
            num_pointer += 1
            num_tracker.append(int(number_set[num_pointer]))
        if num_sum > bad_num:
            num_sum = 0
            start_pointer += 1
    finaltracker =  num_tracker[:-1]
    return min(finaltracker) + max(finaltracker)

if __name__ == "__main__":
    print(find_bad_num(xmas_code))
    print(find_weakness(xmas_code))
