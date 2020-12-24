!/usr/bin/env python

starting_nums = [14,1,17,0,3,20]
all_nums_spoken = {num:turn for turn, num in enumerate(starting_nums)}

current_spoken = 0
for numspoken in range (6, 29999999):
    if current_spoken in all_nums_spoken:
        current_num = numspoken - all_nums_spoken[current_spoken]
        all_nums_spoken[current_spoken] = numspoken
        current_spoken = current_num
    else:
        all_nums_spoken[current_spoken] = numspoken
        current_spoken = 0
        
print(current_spoken)
