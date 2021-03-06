#!/usr/bin/env python

starting_nums = [14,1,17,0,3,20]
all_nums_spoken = starting_nums

for numspoken in range(6,2020):
    lastturn = numspoken - 1
    lastnum = all_nums_spoken[lastturn]
    if lastnum in all_nums_spoken[:-1]:
        earlier_turn = all_nums_spoken.index(lastnum)
        turn_diff = lastturn - earlier_turn
        all_nums_spoken[earlier_turn] = "used"
        all_nums_spoken.append(turn_diff)
    else:
        all_nums_spoken.append(0)

print(all_nums_spoken[-1])
