#!/usr/bin/python3


def uniq_add(my_list=[])
if len(my_list) == 0:
    return 0
new = sorted(my_list)
sum = new[0]
checked = new[0]
for n in new[1:]:
    if n != checked:
        sum += n
        checked = n
        return sum
