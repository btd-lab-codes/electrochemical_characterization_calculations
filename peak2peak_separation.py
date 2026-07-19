import numpy as np
from scipy.signal import find_peaks
import pandas as pd

# Import data

# print(len(voltage), len(current))

def peak_separation(csv_file, voltage_loc, current_loc):
    df = pd.read_csv(csv_file)
    voltage = df.iloc[:,voltage_loc]
    current = df.iloc[:,current_loc]

# Separate data into forward and reverse segments
# CV typically scans up to a switching potential and then reverses
    forward_mask = np.diff(voltage) > 0
    E_anodic = voltage[:-1][forward_mask]
    I_anodic = current[:-1][forward_mask]

    E_cathodic = voltage[len(E_anodic):len(voltage)]
    I_cathodic = current[len(I_anodic):len(current)]

    peaks_ind, _ = find_peaks(I_anodic, height=0) # height ensures it looks for upward peaks
    peak_ind = peaks_ind[np.argmax(I_anodic[peaks_ind])]
    anodic_peak_voltage = voltage[peak_ind]
    anodic_peak_current = current[peak_ind]

    I_cathodic = -1*I_cathodic

    peaks_ind_cat, _ = find_peaks(I_cathodic, height=0)
    peak_ind_cat = peaks_ind_cat[np.argmax(I_cathodic[peaks_ind_cat+len(I_anodic)])]
    cathodic_peak_voltage = E_cathodic[peak_ind_cat+len(E_anodic)]
    cathodic_peak_current = -1*(I_cathodic[peak_ind_cat+len(I_anodic)])

# Calculate Peak-to-Peak Separation
    delta_Ep = abs(anodic_peak_voltage - cathodic_peak_voltage)

# Print the results
    #print(f"Anodic Peak Potential (E_pa): {anodic_peak_voltage: .4e} V")
    #print(f"Cathodic Peak Potential (E_pc): {cathodic_peak_voltage: .4e} V")
    #print(f"Peak-to-Peak Separation (ΔE_p): {delta_Ep * 1000: .1e} mV")

    return delta_Ep