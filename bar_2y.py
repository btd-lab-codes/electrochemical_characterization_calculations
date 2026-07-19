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

def plot_bar_2y(data_left, data_right, categories, x_label, y_label_left, y_label_right):

# X-axis position setups
    x = np.arange(len(categories))
    width = 0.30  # Width of each bar

# 1. Initialize the figure and the primary (left) axis
    fig, ax1 = plt.subplots(figsize=(8, 6))

# Plot the first set of bars on the left axis
    bar1 = ax1.bar(x - width/2, data_left, width, color='lightblue', label=y_label_left)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label_left, color='black')
    ax1.tick_params(axis='y', labelcolor='black')

# 2. Create the secondary (right) axis sharing the same X-axis
    ax2 = ax1.twinx()

# Plot the second set of bars on the right axis
    bar2 = ax2.bar(x + width/2, data_right, width, color='blue', label=y_label_right)
    ax2.set_ylabel(y_label_right, color='black')
    ax2.tick_params(axis='y', labelcolor='black')

# Align X-ticks with the center of the bar groups
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories)

    ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    #ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
# Combine legends from both axes
    #bars = [bar1, bar2]
    #labels = [b.get_label() for b in bars]
    #ax1.legend(bars, labels, loc='upper left')

    #plt.title('Bar Graph with Two Data Series and Dual Y-Axes')
    plt.tight_layout()
    plt.show()
    return fig