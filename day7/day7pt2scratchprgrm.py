#!/usr/bin/env python

initial_types = [bag.strip(".").split(" contain ") for bag in open("day7test.txt").read().splitlines()]
clean_bag_list = [bag.split(", ") for bags in initial_types for bag in bags]
clean_bag_types = {" ".join(clean_bag_list[i]): clean_bag_list[i + 1] for i in range(0, len(clean_bag_list), 2)}

print(clean_bag_types)

def bag_contents(outercolor):
    bag_tracker = {}
#    bag_value = []
    for outerbag in clean_bag_types:
        if outercolor in outerbag:
            for innerbag in clean_bag_types.get(outerbag):
                bag_details = innerbag.split(" ", 1)
                if bag_details[0].isnumeric():
                    bag_tracker[bag_details[1]] = bag_details[0]
    return bag_tracker

def calculate_value(key, value):
        
    return

def all_bag_contents(outercolor):
    color_list = outercolor
    color_dict = {}

    for color in color_list:
        color_dict.clear()
        color_dict.update(bag_contents(color))
    color_list = [newcolor for newcolor in color_dict]
    firstval = int(color_dict[color_list[0]])
    secondval = int(color_dict[color_list[1]])

def total_bags(outercolor):
    bag_tracker = outercolor
    bag_value = 0
    tracker_length = len(bag_tracker)

    if bag_tracker == []:
        return 0

    for color in bag_tracker:
        for outerbag in clean_bag_types:
            if color in outerbag:
                for innerbag in clean_bag_types.get(outerbag):
                    bag_details = innerbag.split(" ", 1)
                    if bag_details[0].isnumeric():
                        bag_value = int(bag_details[0])
                        bag_tracker.append(bag_details[1])
        bag_tracker.remove(color)
    return bag_value + (bag_value * total_bags(bag_tracker))

# Function from Part 1 for Reference
def find_outerbag_color(bagcolor): 
    outerbags = bagcolor
    startlength = len(outerbags)
    
    for color in outerbags:
        for outerbag in clean_bag_types:
            for innerbag in clean_bag_types.get(outerbag):
                if color in innerbag:
                    singular_bag = outerbag.rstrip("s")
                    if singular_bag not in outerbags:
                        outerbags.append(singular_bag)
    
    return len(outerbags) - 1

# Executing function
def bag_options(bagcolor):
    return find_outerbag_color([bagcolor])

#if __name__ == "__main__":
#    print(all_bag_contents(["shiny gold bag"]))
