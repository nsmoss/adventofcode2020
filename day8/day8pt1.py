#!/usr/bin/env python

rawdata = [instruction.split() for instruction in open("day8input.txt").read().splitlines()]

def loop_calc(data_set):
    
    instruction_pointer = 0
    instruction_line = data_set[instruction_pointer]
    accumulator = 0
    
    while instruction_line != "command used":
        instruction = instruction_line[0]
        inst_value = instruction_line[1]
        polarity = inst_value[0]
        pol_value = int(inst_value[1:])
        rawdata[instruction_pointer] = "command used"
    
        if instruction == "nop":
            instruction_pointer += 1
            instruction_line = rawdata[instruction_pointer]
        if instruction == "acc":
            if polarity == "-":
                accumulator -= pol_value
                instruction_pointer += 1
                instruction_line = rawdata[instruction_pointer]
            if polarity == "+":
                accumulator += pol_value
                instruction_pointer += 1
                instruction_line = rawdata[instruction_pointer]
        if instruction == "jmp":
            if polarity == "-":
                instruction_pointer -= pol_value
                instruction_line = rawdata[instruction_pointer]
            if polarity == "+":
                instruction_pointer += pol_value
                instruction_line = rawdata[instruction_pointer]
    
    return accumulator

if __name__ == "__main__":
    print(loop_calc(rawdata))

