# -*- coding: utf-8 -*-
"""
@author: Lenovo
"""

# Print the reverse of a number
number = int(input("Enter a num: "))
n = abs(number)
reverse = 0
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
if number < 0:
    reverse = -reverse
print( reverse)
