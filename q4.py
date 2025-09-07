# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 15:14:31 2025

@author: Lenovo
"""

# Write a Python program to get the frequency of elements in a list.
elements = [1, 2, 2, 3, 4, 4, 5]
frequency = {}
for item in elements:
    frequency[item] = frequency.get(item, 0) + 1
print(frequency)
