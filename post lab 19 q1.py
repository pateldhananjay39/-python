# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 16:13:21 2025

@author: Lenovo
"""

import numpy as np

def analyze_unit_step_z_transform():
    """
    Computes the Z-transform of the unit step function u[n] and verifies 
    its stability based on the pole location.

    The analytical Z-transform of the unit step is H(z) = z / (z - 1).
    """
    pole = 1.0

    print("--- Z-Transform Analysis of Unit Step Function u[n] ---")
    print(f"Analytical Z-Transform H(z) = z / (z - 1)")
    print(f"The single pole of the system is located at z = {pole}")
    magnitude = np.abs(pole)
    print(f"Pole Magnitude: |z| = {magnitude}")

    if magnitude < 1:
        stability_result = "Stable"
    else:
        stability_result = "Unstable (Pole is on the unit circle at z=1)"

    print(f"\nConclusion: The system is **{stability_result}**.")

# Run the analysis
analyze_unit_step_z_transform()
