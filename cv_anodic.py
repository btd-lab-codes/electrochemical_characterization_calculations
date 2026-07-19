from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt

size = 16
params = {'legend.fontsize': 'x-large',
          #'figure.figsize': (15, 5),
         'axes.labelsize': size,
         'font.family' :'Times New Roman',
         'mathtext.fontset': 'custom',
         'mathtext.rm': 'Times New Roman',
         'axes.titlesize': size,
         'xtick.labelsize': size*0.7,
         'ytick.labelsize': size*0.7}
plt.rcParams.update(params)

def range_x(potential, current, st_b, st_a, f_title):
    # Assuming 'potential' and 'current' are your data arrays
    peaks_ind, _ = find_peaks(current, height=0) # height ensures it looks for upward peaks
    peak_ind = peaks_ind[np.argmax(current[peaks_ind])]
    anodic_peak_potential = potential[peak_ind]
    anodic_peak_current = current[peak_ind]

    print('--- CV Peak Analysis ---')
    print(f"Peak Current Value: {anodic_peak_current:.3f} uA")
    print(f"Peak Current Occurs at: {anodic_peak_potential:.3f} V")

    # Isolate the forward sweep (anodic branch)
    # This assumes the scan sweeps positively; adjust slicing based on your dataset
    forward_mask = np.diff(potential) > 0
    E_anodic = potential[:-1][forward_mask]
    I_anodic = current[:-1][forward_mask]

    before_peak = I_anodic[:peak_ind]
    after_peak = I_anodic[peak_ind:]

    before = E_anodic[:peak_ind]
    after = E_anodic[peak_ind:]
    # Find the point where the graph starts to flatten
    slopes_before = np.gradient(before_peak, before)
    slopes_after = np.abs(np.gradient(after_peak, after))
    slope_thres = st_b #adjust base on noise, difference between adjacent points
    slope_thres_2 = st_a
    #Find the indeces before and after the peak

    print(slopes_before, slopes_after)

    start_idx = 60+np.where(slopes_before < slope_thres)[0][0]
    end_idx = peak_ind +50 + np.where(slopes_after < slope_thres_2)[0][0]

    # The start of the peak is the minimum before the peak
    # The end of the peak is the minimum after the peak
    #start_idx = np.argmin(I_anodic[:peak_ind])
    #end_idx = peak_ind + np.argmin()

    #Extract start and end potential values
    start_potential = E_anodic[start_idx]
    end_potential = E_anodic[end_idx]
    print(f"Anodic Area Starts at: {start_potential:.3f} V")
    print(f"Anodic Area Ends at: {end_potential:.3f} V")

    plt.plot(potential, current, label='CV Data')
    plt.fill_between(E_anodic[start_idx:end_idx], I_anodic[start_idx:end_idx], color='red', alpha=0.3, label='Anodic Area')
    plt.scatter([E_anodic[start_idx], E_anodic[end_idx]], [I_anodic[start_idx], I_anodic[end_idx]], color='blue')
    plt.xlabel('Potential (V vs. Ref)')
    plt.ylabel('Current (µA)')
    plt.legend(frameon=False)
    plt.savefig(f'{f_title}.tiff', dpi=300)
    plt.show()

    potential_new = potential[start_idx:end_idx]
    current_new = current[start_idx:end_idx]

    return potential_new, current_new