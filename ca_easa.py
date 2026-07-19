import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

size = 16
params = {'legend.fontsize': 'x-large',
         'figure.figsize': (12, 6),
         'axes.labelsize': size,
         'font.family' :'Times New Roman',
         'mathtext.fontset': 'custom',
         'mathtext.rm': 'Times New Roman',
         'axes.titlesize': size,
         'xtick.labelsize': size*0.9,
         'ytick.labelsize': size*0.9}
plt.rcParams.update(params)

def ca_easa(ca_data, start, end, g_title, f_title, g_color):
    ca_data = np.array(ca_data)
    time = np.array(ca_data[:,0])
    current = np.array(ca_data[:,1])
    indices = np.where((time >= start) & (time <= end)) #Assume the working indices
    time_trunc = time[indices]
    current_trunc = np.absolute(current[indices])

    #print(time_trunc, current_trunc)
    time_root = time_trunc**(-1/2)

    # Perform linear regression
    result = stats.linregress(time_root, current_trunc*1e-6)

    # Calculate additional metrics
    r_squared = result.rvalue ** 2

    # Print statistical summary
    print(f"___ {g_title}: Linear Regression Statistics ___")
    print(f"Slope (beta_1):       {result.slope:.4e}")
    print(f"Intercept (beta_0):   {result.intercept:.4e}")
    print(f"R-value (Correlation): {result.rvalue:.4f}")
    print(f"R-squared (R²):       {r_squared:.4f}")
    print(f"P-value:              {result.pvalue:.4e}")
    print(f"Std Error (Slope):    {result.stderr:.4e}")
    print(f"Std Error (Intercept): {result.intercept_stderr:.4e}")

    slope_m = result.slope

    Fc = 96485 # Faraday constant C/mol
    Dc = 7e-6 # Diffusion coefficient of the probe for ferrocyanide at RT cm2/s
    Co = 5e-6 # 5 mM (5e-6 mol/mL) solutio of ferrocyanide in 1.0 M KCl
    ne = 1 # number of electrons = 1 for Ferrocyanide

    easa = cottrell_A(slope_m, ne, Fc, Co, Dc)
    print('--- EASA w/ y-int ---')
    print(f'EASA = {easa: .4e}')

    # Plot the data and the regression line
    plt.scatter(time_root, current_trunc*1e-6, edgecolor=g_color, facecolor = 'none', label=g_title)
    plt.plot(time_root, result.intercept + result.slope * time_root, linewidth = 2, color=g_color, label=f'Fit: y={result.slope:.2e}x + {result.intercept:.2e}')
    plt.xlabel(r'$t^{-1/2}$, $s^{-1/2}$')
    plt.ylabel(r'Current, A')
    #plt.title(f'Cottrell Line: {g_title}')
    plt.legend(frameon=False)
    plt.grid(False)


    plt.savefig(f'cotrell_{f_title}.tiff', dpi=300)
    #plt.show()

    return easa, time_root, result

def cottrell_A(m_, n_, F_, C_0, D_):
        EASA = m_*np.pi/(n_*F_*C_0*np.sqrt(D_))
        return EASA