# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 15:16:24 2025

@author: Lenovo
"""

# Convert a list of multiple integers into a single integer
nums = [1, 2, 3, 4]
single_integer = int(''.join(map(str, nums)))
print(single_integer)
