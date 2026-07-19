import numpy as np

def calculate_ks_eis(Rct, C, A, n, T=298.15):
    """
    Calculate the heterogeneous electron transfer rate constant (ks) 
    from Charge Transfer Resistance (Rct) using EIS data.
    
    Formula: ks = RT / (n^2 * F^2 * A * Rct * C)
    """
    # Constants
    F = 96485.33 # Faraday constant (C/mol)
    R = 8.314    # Gas constant (J/mol*K)
    
    # Calculation
    denominator = (n**2) * (F**2) * A * Rct * C
    ks = (R * T) / denominator
    
    return ks

# Sample Data & Result
if __name__ == "__main__":
    r_ct = 150.0  
    concentration_mM = 5.0  
    concentration_mol_cm3 = concentration_mM * 1e-6 
    electrode_area = 0.07 
    electrons = 1
    
    ks_result = calculate_ks_eis(r_ct, concentration_mol_cm3, electrode_area, electrons)
    
    print("--- EIS Kinetics Result ---")
    print(f"Charge Transfer Resistance (Rct): {r_ct} Ohms")
    print(f"Concentration: {concentration_mM} mM")
    print(f"Calculated ks: {ks_result:.2e} cm/s")