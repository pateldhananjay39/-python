# -*- coding: utf-8 -*-
"""


@author: Lenovo
"""

# Find the sum of all natural numbers from 1 to n
n = int(input("Enter a value for n: "))
total = 0
for i in range(1, n + 1):
    total += i
print( total)
