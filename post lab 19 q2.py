# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 16:18:37 2025

@author: Lenovo
"""

import numpy as np

def analyze_z_system_stability(num_coeffs, den_coeffs):
    """
    Analyzes the stability of a discrete-time system defined by its
    Z-transform function H(z) = N(z) / D(z).

    Args:
    num_coeffs (list): Coefficients of the numerator N(z).
    den_coeffs (list): Coefficients of the denominator D(z).
    These should be in descending powers of z, after clearing all negative powers of z.

    Example: For H(z) = 1 / (1 - 0.5z^-1), 
    the characteristic equation is 0.5z^-1 - 1 = 0,
    Use den_coeffs = [1, -0.5].
    """

    print("--- Z-System Stability Analysis ---")
    
    poles = np.roots(den_coeffs)
    print(f"Denominator Coefficients D(z): {den_coeffs}")
    print(f"Poles of System D(z): {poles}")
    pole_magnitudes = np.abs(poles)
    print(f"Pole Magnitudes: {pole_magnitudes}")

    is_unstable = np.any(pole_magnitudes >= 1)
    if is_unstable:
        stability_result = "Unstable (At least one pole is outside or on the unit circle, |z| >= 1)"
    else:
        stability_result = "Stable (All poles are strictly inside the unit circle, |z| < 1)"

    print(f"\nConclusion: The system is **{stability_result}**.")

# Example usage
num = [1]    # Numerator N(z)
den = [1, -0.5]   # Denominator D(z)

print("Analyzing Example System: H(z) = 1 / (1 - 0.5z^-1)")
analyze_z_system_stability(num, den)
