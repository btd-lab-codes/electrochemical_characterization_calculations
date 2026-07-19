import matplotlib.pyplot as plt
import numpy as np

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

def plot_3y(categories, y_left, y_right1, y_right2, label_yl, label_yr1, label_yr2, label_xaxis, label_yaxisl, label_yaxisr):
    x = np.arange(len(categories))  # Label locations
    width = 0.25  # Width of each bar

    # Set up the figure and the first (left) axis
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot the first bar on the left axis
    bar1 = ax1.bar(
        x - width, y_left, width, label=label_yl, color="purple"
    )

    # Create the second (right) axis sharing the same x-axis
    ax2 = ax1.twinx()

    # Plot the second and third bars on the right axis
    bar2 = ax2.bar(
        x, y_right1, width, label=label_yr1, color="red"
    )
    bar3 = ax2.bar(
        x + width, y_right2, width, label=label_yr2, color="pink"
    )

    # Configure labels, ticks, and titles
    ax1.set_xlabel(label_xaxis)# fontsize=12)
    ax1.set_ylabel(label_yaxisl, color="black")# fontsize=12)
    ax1.tick_params(axis="y", labelcolor="black")
    #ax1.set_yscale('log')

    ax2.set_ylabel(label_yaxisr, color="black")# fontsize=12)
    #ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    #y1_min, y1_max = ax1.get_ylim()
    #print(y1_min, y1_max)

    #import ks_nicholson as ksn
    
    #y2_min = ksn.calculate_ks_nicholson(y1_min*1000, 1.0e-5, 0.1, 1, T = 298.15) #similar to assemble_ks.py
    #y2_max = ksn.calculate_ks_nicholson(y1_max*1000, 1.0e-5, 0.1, 1, T = 298.15) #similar to assemble_ks.py

    y2_min = 1e-4
    y2_max = 1e0

    ax2.set_ylim(y2_min, y2_max)
    ax2.set_yscale('log')
    ax1.axhline(y=61, color='purple', linestyle='--')
    ax1.text(x=0.1, y=61.1, s='Reversible limit', verticalalignment='bottom')
    ax1.text(x=0.1, y=213.1, s='Irreversible limit', verticalalignment='bottom')

    ax1.axhline(y=213, color='purple', linestyle='--')
    ax2.axhline(y=1.5e-1, color='red', linestyle='--') #61 delta Ep
    ax2.axhline(y=6.4e-4, color='red', linestyle='--') #213 delta Ep
    ax2.text(x=2, y=1.5e-1, s='Reversible limit', verticalalignment='bottom')
    ax2.text(x=2, y=6.4e-4, s='Irreversible limit', verticalalignment='bottom')

    # Ensure X-ticks are perfectly centered under the group of 3 bars
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories)

    # Handle the legend (combining labels from both axes)
    bars = [bar1, bar2, bar3]
    labels = [b.get_label() for b in bars]
    ax1.legend(bars, labels, loc="upper right", frameon = False)
    #ax2.legend(frameon = 'False')
    plt.tight_layout()

    #plt.savefig('ks_cv_eis.tiff', dpi=300)
    plt.show()

    return fig