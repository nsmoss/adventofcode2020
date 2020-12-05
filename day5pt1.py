#!/usr/bin/env python

def generate_plane():
    plane_length = [row for row in range(128)]
    plane_width = [column for column in range(8)]
    return plane_length, plane_width

def split_plane(seat_values, seat_range):
    seat_tracker = seat_range
    for value in seat_values:
        if value == "F" or value == "L":
            seat_tracker = seat_tracker[:len(seat_tracker)//2]
        if value == "B" or value == "R":
            seat_tracker = seat_tracker[len(seat_tracker)//2:]
    return seat_tracker[0]

def find_seat_max(inputfile):
    seats = open(inputfile).read().splitlines()
    plane_length, plane_width = generate_plane()
    max_seatID = 0
    for seat in seats:
        row = split_plane(seat[:7], plane_length)
        column = split_plane(seat[7:], plane_width)
        seatID = int(row) * 8 + int(column)
        if seatID > max_seatID:
            max_seatID = seatID
    return(max_seatID)

if __name__ == "__main__":
    print(find_seat_max("day5input.txt"))
