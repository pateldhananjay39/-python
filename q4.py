# -*- coding: utf-8 -*-
"""


@author: Lenovo
"""

# Find the first and last digit of a number
number = int(input("Enter a num: "))
n = abs(number)
last_digit = n % 10

first_digit = n
while first_digit >= 10:
    first_digit //= 10

print( first_digit)
print( last_digit)
