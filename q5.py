# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 15:15:34 2025

@author: Lenovo
"""

# Find common items from two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common)
