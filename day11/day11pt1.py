#!/usr/bin/env python

import copy

original_rows = open("day11input.txt").read().splitlines()

def seat_layout():
    all_seat_locations = {}
    row_counter = 0
    for row in original_rows:
        seat_location = [seat for seat in range(len(row))]
        all_seat_locations[row_counter] = seat_location
        row_counter += 1
    return all_seat_locations        

def seat_checker(rows, row_input):
    work_dict = seat_layout()
    new_rows = copy.deepcopy(row_input)
    for row in work_dict:
        for seat in work_dict[row]:
            adjacent_counter = 0
            try:    
                if rows[row][seat + 1] == "#":
                    adjacent_counter += 1
            except IndexError:
                pass
            try:
                if rows[row + 1][seat] == "#":
                    adjacent_counter += 1
            except IndexError:
                pass
            try:
                if rows[row + 1][seat + 1] == "#":
                    adjacent_counter += 1
            except IndexError:
                pass
            try:
                if rows[row - 1][seat] == "#" and row - 1 >= 0:
                    adjacent_counter += 1
            except IndexError:
                pass
            try:
                if rows[row - 1][seat + 1] == "#" and row - 1 >= 0:
                    adjacent_counter += 1
            except IndexError:
                pass
            try:
                if rows[row][seat - 1] == "#" and seat - 1 >= 0:
                    adjacent_counter += 1
            except IndexError:
                pass
            try:
                if rows[row + 1][seat - 1] == "#" and seat - 1 >= 0:
                    adjacent_counter += 1
            except IndexError:
                pass
            try:
                if rows[row - 1][seat - 1] == "#" and row - 1 >= 0 and seat - 1 >= 0:
                    adjacent_counter += 1
            except IndexError:
                pass
                       
            if rows[row][seat] == "L" and adjacent_counter == 0:
                new_rows[row] = new_rows[row][:seat] + "#" + new_rows[row][seat + 1:]
            if rows[row][seat] == "#" and adjacent_counter >= 4:
                new_rows[row] = new_rows[row][:seat] + "L" + new_rows[row][seat + 1:]
    return new_rows

def seat_iterator():
    copy_rows = copy.deepcopy(original_rows)
    next_rows = seat_checker(original_rows, copy_rows)
    while copy_rows != next_rows:
        copy_rows = copy.deepcopy(next_rows)
        next_rows = seat_checker(copy_rows, next_rows)
    occupied_counter = 0
    for row in next_rows:
        for seat in row:
            if seat == "#":
                occupied_counter += 1
    return occupied_counter

print(seat_iterator())
