#!/usr/bin/env python

import copy

adapters = list(map(int, open("day10test.txt").read().splitlines()))
my_adapter = max(adapters) + 3
outlet_joltage = 0
adapters.append(my_adapter)
adapters.append(outlet_joltage)
adapters.sort()

def find_path(adapter_list):
    current_joltage = outlet_joltage
    one_diff = []
    two_diff = []
    three_diff = []
    full_path = [current_joltage]
    split_options = []

    while current_joltage != my_adapter:
        diff_tracker = []
        adapter_index = adapter_list.index(current_joltage)
        max_joltage = current_joltage + 3
        for adapter in adapter_list[adapter_index + 1:adapter_index + 4]:
            if adapter <= max_joltage:
                diff_tracker.append(adapter)
                if adapter == current_joltage + 1 and adapter not in one_diff:
                    one_diff.append(adapter)
                if adapter == current_joltage + 2 and adapter not in two_diff:
                    two_diff.append(adapter)
                if adapter == current_joltage + 3 and adapter not in three_diff:
                    three_diff.append(adapter)
            current_joltage = min(diff_tracker)
            if len(diff_tracker) > 1 and len(split_options) < 1:
                split_options.append(adapter_index)
                split_options.append(diff_tracker)
        full_path.append(current_joltage)
    return full_path, split_options

def find_all_paths(adapter_list):
    all_path_options = []
    original_path = find_path(adapter_list)
    all_path_options.append(original_path[0])
    new_path_index = original_path[1][0] + 1
    new_path_options = original_path[1][1]
    for index_options in new_path_options[1:]:
        adapters_copy = copy.deepcopy(adapters)
        adapters_copy[new_path_index] = index_options
        all_path_options.append(find_path(adapters_copy)[0])
    return all_path_options
    
if __name__ == "__main__":
    print(find_all_paths(adapters))
