#!/usr/bin/env python

adapters = list(map(int, open("day10input.txt").read().splitlines()))
my_adapter = max(adapters) + 3
outlet_joltage = 0
adapters.append(my_adapter)
adapters.append(outlet_joltage)
adapters.sort()

current_joltage = outlet_joltage
one_diff = []
three_diff = []

while current_joltage != my_adapter:
    diff_tracker = []
    adapter_index = adapters.index(current_joltage)
    max_joltage = current_joltage + 3
    for adapter in adapters[adapter_index + 1:adapter_index + 4]:
        if adapter <= max_joltage:
            diff_tracker.append(adapter)
            if adapter == current_joltage + 1 and adapter not in one_diff:
                one_diff.append(adapter)
            if adapter == current_joltage + 3 and adapter not in three_diff:
                three_diff.append(adapter)
        current_joltage = min(diff_tracker)

print(len(one_diff) * len(three_diff))
