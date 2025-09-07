# -*- coding: utf-8 -*-
"""


@author: Lenovo
"""

# Calculate product of all digits of a number
number = int(input("Enter a num: "))
n = abs(number)
product = 1 if n > 0 else 0
if n == 0:
    product = 0
while n > 0:
    product *= n % 10
    n //= 10
print( product)
