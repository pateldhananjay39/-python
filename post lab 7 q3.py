# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 16:58:36 2025

@author: Lenovo
"""

import numpy as np
arr1 = np.array([1, 3, 5, 7])
arr2 = np.array([3, 4, 5, 6])
common = np.intersect1d(arr1, arr2)
print(common)
