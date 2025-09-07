# -*- coding: utf-8 -*-
"""


@author: Lenovo
"""

# Swap the first and last digits of a number
number  = int(input("Enter a num: "))
num_str = str(abs(number))
if len(num_str) == 1:
    swapped = num_str
else:
    swapped = num_str[-1] + num_str[1:-1] + num_str
swapped_num = int(swapped) if number >= 0 else -int(swapped)
print( swapped_num)
