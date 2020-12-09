#!/usr/bin/env python

import copy

rawdata = [instruction.split() for instruction in open("day8input.txt").read().splitlines()]

def loop_calc(data_set):
   
    instruction_pointer = 0
    instruction_line = data_set[instruction_pointer]
    accumulator = 0
    func_data = data_set.copy()

    try:
        while instruction_line != "command used":
            instruction = instruction_line[0]
            inst_value = instruction_line[1]
            polarity = inst_value[0]
            pol_value = int(inst_value[1:])
            func_data[instruction_pointer] = "command used"
    
            if instruction == "nop":
                instruction_pointer += 1
                instruction_line = func_data[instruction_pointer]
            if instruction == "acc":
                if polarity == "-":
                    accumulator -= pol_value
                    instruction_pointer += 1
                if polarity == "+":
                    accumulator += pol_value
                    instruction_pointer += 1
                instruction_line = func_data[instruction_pointer]
            if instruction == "jmp":
                if polarity == "-":
                    instruction_pointer -= pol_value
                if polarity == "+":
                    instruction_pointer += pol_value
                instruction_line = func_data[instruction_pointer]
        return accumulator, False
    except:
        return accumulator, True

def calc_finish(data_set):
    line_pointer = 0
    for instruction_line in data_set:
        datatry = copy.deepcopy(data_set)
        if instruction_line[0] == "nop":
            datatry[line_pointer][0] = "jmp"
            attempt = loop_calc(datatry)
            if attempt[1] == True:
                print(attempt[0])
                break
        elif instruction_line[0] == "jmp":
            datatry[line_pointer][0] = "nop"
            attempt = loop_calc(datatry)
            if attempt[1] == True:
                print(attempt[0])
                break
        line_pointer += 1

if __name__ == "__main__":
    print(loop_calc(rawdata)[0])
    calc_finish(rawdata)

