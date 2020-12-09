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

def find_seat(inputfile):
    seats = open(inputfile).read().splitlines()
    plane_length, plane_width = generate_plane()
    possible_seats = [i for i in range(1024)]
    my_seat_options = []
    for seat in seats:
        row = split_plane(seat[:7], plane_length)
        column = split_plane(seat[7:], plane_width)
        seatID = int(row) * 8 + int(column)
        if seatID in possible_seats:
            possible_seats.remove(seatID)
    for seat in possible_seats:
        if int(seat) + 1 not in possible_seats:
            if int(seat) - 1 not in possible_seats:
                return seat

if __name__ == "__main__":
    print(find_seat("day5input.txt"))
