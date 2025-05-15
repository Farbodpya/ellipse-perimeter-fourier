import matplotlib.pyplot as plt

def plot_errors(r_vals, error_fourier, error_ramanujan, degree):
    plt.figure(figsize=(10, 6))
    plt.plot(r_vals, error_fourier, label=f'Fourier Degree {degree} Approximation Error', color='green')
    plt.plot(r_vals, error_ramanujan, label='Ramanujan Approximation Error', color='blue')
    plt.xlabel('Axis Ratio b/a')
    plt.ylabel('Relative Error (%)')
    plt.title(f'Relative Error vs True Perimeter\n(Fourier Degree {degree} vs Ramanujan)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
