import matplotlib.pyplot as plt


def area_under_curve(E_data, I_data, size):
    plt.figure(figsize=size)
    plt.plot(E_data, I_data, color='red', marker='o', linestyle='--', label='Growth Rate')
    plt.show()