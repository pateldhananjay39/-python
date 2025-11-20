# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 17:57:16 2025

@author: Lenovo
"""

import sympy as sp
n, z, w = sp.symbols('n z omega')
x = sp.cos(w * n) * sp.Heaviside(n)
X_z = z * (z - sp.cos(w)) / (z**2 - 2 * z * sp.cos(w) + 1)
print("Z-transform of x[n]=cos(omega n) u[n]:")
sp.pprint(X_z, use_unicode=True)
