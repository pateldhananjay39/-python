# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 18:45:45 2025

@author: Lenovo
"""

with open(r"C:\Users\Lenovo\Downloads\ict.txt", "r") as file:
    text = file.read()
    lines = text.splitlines()
    words = text.split()
    characters = list(text)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", len(characters))
