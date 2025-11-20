# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 19:15:40 2025

@author: Lenovo
"""

import csv

with open(r"C:\Users\Lenovo\Downloads\data-1.csv", mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)