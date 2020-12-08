#!/usr/bin/env python

initial_types = [bag.strip(".").split(" contain ") for bag in open("day7input.txt").read().splitlines()]
clean_bag_list = [bag.split(", ") for bags in initial_types for bag in bags]
clean_bag_types = {" ".join(clean_bag_list[i]): clean_bag_list[i + 1] for i in range(0, len(clean_bag_list), 2)}

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

def bag_options(bagcolor):
    return find_outerbag_color([bagcolor])

if __name__ == "__main__":
    print(bag_options("shiny gold bag"))

