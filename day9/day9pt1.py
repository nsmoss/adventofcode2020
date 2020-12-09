#!/usr/bin/env python

from itertools import combinations

xmas_code = open("day9input.txt").read().splitlines()

def findsum(preamble, current_num):
    return [pair for pair in combinations(preamble, 2) if sum(pair) == current_num]

def find_bad_num(number_set):
    code_pointer = 25
    ruleworks = True
    while ruleworks == True:
        preamble = list(map(int, xmas_code[code_pointer - 25:code_pointer]))
        current_num = int(xmas_code[code_pointer])
        valid_combos = findsum(preamble, current_num)
        if valid_combos == []:
            ruleworks = False
            return(current_num)
        else:
            code_pointer += 1

if __name__ == "__main__":
    print(find_bad_num(xmas_code))
