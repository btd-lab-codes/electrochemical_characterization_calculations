import numpy as np

def calculate_ks_nicholson(delta_Ep, D, v, n, T=298.15):
    """
    Calculate the heterogeneous electron transfer rate constant (ks) 
    using the Nicholson method.
    
    Parameters:
    delta_Ep : float
        Peak-to-peak potential separation in millivolts (mV).
    D : float
        Diffusion coefficient in cm^2/s.
    v : float
        Scan rate in V/s.
    n : int
        Number of electrons transferred.
    T : float, optional
        Temperature in Kelvin. Default is 298.15 K.
        
    Returns:
    float
        The rate constant ks in cm/s.
    """
    # Constants
    F = 96485.33 # Faraday constant (C/mol)
    R = 8.314    # Gas constant (J/mol*K)
    
    # Nicholson's empirical dimensionless parameter psi
    # Ref: Nicholson, R. S. (1965). Theory of Stationary Electrode Polarography. 
    # Analytical Chemistry, 37(11), 1351-1355.
    # Polynomial fit common in literature for delta_Ep in mV:
    if delta_Ep < 61:
        # Reversible limit
        return float('inf')
    elif delta_Ep > 214:
        # Irreversible limit
        return float('-inf')
    
    # Empirical fit for psi vs Delta Ep
    # One common fit for psi (approximate):
    psi = (-0.6288 + 0.0021 * delta_Ep) / (1 - 0.017 * delta_Ep)
    
    # k_s = psi * [pi * D * v * (nF/RT)]^0.5
    # Note: pi * D * v * (nF/RT) is often termed 'a'
    a = (n * F * v) / (R * T)
    ks = psi * np.sqrt(np.pi * D * a)
    
    return ks

# Sample Data & Result
if __name__ == "__main__":
    # Assumptions for sample data
    d_ep = 212  # Peak separation in mV
    diff_coeff = 7e-6 #1.0e-5  # D in cm^2/s
    scan_rate = 0.1  # v in V/s
    electrons = 1
    
    ks_result = calculate_ks_nicholson(d_ep, diff_coeff, scan_rate, electrons)
    
    print("--- Nicholson Method Result ---")
    print(f"Peak Separation (delta_Ep): {d_ep} mV")
    print(f"Scan Rate (v): {scan_rate} V/s")
    print(f"Calculated ks: {ks_result:.2e} cm/s")