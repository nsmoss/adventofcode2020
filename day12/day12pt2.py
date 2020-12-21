#!/usr/bin/env python

nav_instructions = open("day12input.txt").read().splitlines()
ship_movement = {"east": 0, "west": 0, "north": 0, "south": 0}

def change_direction(direction, degrees, ship_direction):
    if ship_direction == "E":
        if (degrees == 90 and direction == "R") or (degrees == 270 and direction == "L"):
            return "S"
        if degrees == 180:
            return "W"
        if (degrees == 270 and direction == "R") or (degrees == 90 and direction == "L"):
            return "N"
    if ship_direction == "W":
        if (degrees == 90 and direction == "L") or (degrees == 270 and direction == "R"):
            return "S"
        if degrees == 180:
            return "E"
        if (degrees == 270 and direction == "L") or (degrees == 90 and direction == "R"):
            return "N"
    if ship_direction == "N":
        if (degrees == 90 and direction == "R") or (degrees == 270 and direction == "L"):
            return "E"
        if degrees == 180:
            return "S"
        if (degrees == 270 and direction == "R") or (degrees == 90 and direction == "L"):
            return "W"
    if ship_direction == "S":
        if (degrees == 90 and direction == "R") or (degrees == 270 and direction == "L"):
            return "W"
        if degrees == 180:
            return "N"
        if (degrees == 270 and direction == "R") or (degrees == 90 and direction == "L"):
            return "E"

def ship_move(direction, amount):
    if direction == "N":
        ship_movement["north"] += amount
    if direction == "S":
        ship_movement["south"] -= amount
    if direction == "E":
        ship_movement["east"] += amount
    if direction == "W":
        ship_movement["west"] -= amount

def find_ship_location():
    ship_direction = "E"
    for instruction in nav_instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action in ("R", "L"):
            ship_direction = change_direction(action, value, ship_direction)
        if action in ("N", "S", "E", "W"):
            ship_move(action, value)
        if action == "F":
            ship_move(ship_direction, value)

def manhattan_dist():
    return abs(ship_movement["east"] + ship_movement["west"]) + abs(ship_movement["north"] + ship_movement["south"])

if __name__ == "__main__":
    find_ship_location()
    print(manhattan_dist())
