from impedance.models.circuits import Randles, CustomCircuit
from impedance.models.circuits.fitting import rmse
from impedance import preprocessing

import matplotlib.pyplot as plt
import numpy as np
from impedance.visualization import plot_nyquist
from matplotlib import colormaps as cm

size = 16
params = {'legend.fontsize': 'x-large',
          #'figure.figsize': (15, 5),
         #'axes.labelsize': size,
         'font.family' :'Times New Roman',
         'mathtext.fontset': 'custom',
         'mathtext.rm': 'Times New Roman',
         'axes.titlesize': size,
         'xtick.labelsize': size*0.7,
         'ytick.labelsize': size*0.7}
plt.rcParams.update(params)

#lower_bounds = [20, 1, 1e-3, 1e-3, 1e-9, 0.6] #gce
#upper_bounds = [100, 1e7, 1e6, 1e4, 1.0, 1.0] #gce
#initial_guess = [50, 100, .05, 100, .01, .6] #gce

#lower_bounds = [20, 1, 1e-3, 1e-3, 1e-9, 0.5] 
#upper_bounds = [1000, 1e7, 1e6, 1e4, 1.0, 1.0] 
#initial_guess = [20, 150, .5, 100, .001, .5] 

def randles_CPE_bounded(csv_file, initial_guess, lower_bounds, upper_bounds, g_title, f_title):
    randlesCPE = Randles(initial_guess=initial_guess, CPE=True)

#frequencies, Z = preprocessing.readCSV(r'eis_data/01 Bare GCE.csv')
    frequencies, Z = preprocessing.readCSV(csv_file)
    frequencies, Z = preprocessing.cropFrequencies(frequencies, Z, freqmin=0, freqmax = None)

# keep only the impedance data in the first quandrant
    frequencies, Z = preprocessing.ignoreBelowX(frequencies, Z)

    randlesCPE.fit(frequencies, Z, bounds = (lower_bounds, upper_bounds))
#randlesCPE.fit(frequencies, Z)

    f_pred = frequencies
    fit = randlesCPE.predict(f_pred)
    rmse_ = rmse(fit,Z)

#print(rmse)
    print(f'--- randlesCPE: {g_title} ---')
    print(randlesCPE)

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize = (8,8))
    plot_nyquist(Z, fmt = 'o', linestyle='none', ax=axes, markersize=6, alpha = 0.5) #, markerfacecolor='none')
    plot_nyquist(fit, fmt='none', linestyle='solid', ax=axes, linewidth=2, color='red')
    plt.title(f'{g_title}: Randles Circuit with CPE, RMSE = {rmse_: .2f}')
    axes.set_aspect('auto')
    #axes.set_aspect('equal', adjustable='box')
    axes.locator_params(axis='x', nbins=5, tight=True)
    axes.locator_params(axis='y', nbins=5, tight=True)

    plt.savefig(f'randles_{f_title}.tiff', dpi=300)
    #plt.show()

    return randlesCPE.parameters_ , randlesCPE.conf_, rmse_