import numpy as np
from scipy.integrate import simpson as simps

def calculate_surface_coverage(E, I, v, A, n, T=298.15):
    """
    Calculate the surface coverage (Gamma) by integrating the area 
    under the CV peak.
    
    Parameters:
    E : array-like
        Potential values in Volts (V).
    I : array-like
        Current values in Amperes (A).
    v : float
        Scan rate in V/s.
    A : float
        Electrode area in cm^2.
    n : int
        Number of electrons.
    T : float, optional
        Temperature in Kelvin.
        
    Returns:
    float
        Surface coverage Gamma in mol/cm^2.
    """
    # Constants
    F = 96485.33 # C/mol
    
    # Calculate Charge (Q)
    # Q = integral(I dt) = integral(I dE) / v
    # Use Simpson's rule for integration
    area_under_peak = simps(y=I, x=E) 
    # Current I is usually negative for reduction or positive for oxidation.
    # Take absolute value for charge.
    Q_result = abs(area_under_peak) / v #v = V/s, Q is in uC
    
    # Gamma = Q / (n * F * A)
    surface_coverage = (Q_result*(10**6)) / (n * F * A)
    
    print("--- Surface Coverage Result ---")
    print(f"Charge (Q): {Q_result:.2e} C")
    print(f"Surface Coverage (Gamma): {surface_coverage:.2e} pmol/cm^2")

    return surface_coverage

