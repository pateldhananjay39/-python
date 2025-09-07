# -*- coding: utf-8 -*-
"""


@author: Lenovo
"""

# Count the number of digits in a number
def count_digits(number):
    count = 0
    n = abs(number)
    if n == 0:
        return 1
    while n != 0:
        n //= 10
        count += 1
    return count

num = int(input("Enter a num: "))
print( count_digits(num))
