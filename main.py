import numpy as np
import time
from mpmath import mp, pi as mpi
from perimeter_methods import true_perimeter, ramanujan_perimeter, k_true
from fourier_fit import fit_fourier, perimeter_corrected_fourier
from utils import compute_theta_vals, compute_error
from plot import plot_errors

# Set precision
mp.dps = 10000
PI = mpi

# Setup values
r_vals = np.linspace(0.2, 1.0, 100)
a_vals = np.ones_like(r_vals)
b_vals = r_vals

# Compute true k(r)
print("Computing k(r)...")
start_k = time.time()
k_vals = k_true(r_vals, PI)
end_k = time.time()
print(f"k(r) time: {end_k - start_k:.4f} s\n")

# Fit Fourier
theta_vals = compute_theta_vals(r_vals, PI)
degree = 30
params = fit_fourier(theta_vals, k_vals, degree)

# Compute perimeters
print("Computing true perimeter...")
start_true = time.time()
P_true = true_perimeter(a_vals, b_vals)
print(f"True time: {time.time() - start_true:.4f} s")

print("Computing Ramanujan perimeter...")
start_ram = time.time()
P_ramanujan = ramanujan_perimeter(a_vals, b_vals)
print(f"Ramanujan time: {time.time() - start_ram:.4f} s")

print("Computing Fourier approximation...")
start_fourier = time.time()
P_fourier = perimeter_corrected_fourier(a_vals, b_vals, params, PI)
print(f"Fourier time: {time.time() - start_fourier:.4f} s")

# Compute error
err_fourier = compute_error(P_true, P_fourier)
err_ramanujan = compute_error(P_true, P_ramanujan)

# Plot
plot_errors(r_vals, err_fourier, err_ramanujan, degree)

# Print stats
print(f"\nFourier Max Error: {np.max(err_fourier):.2e}%")
print(f"Fourier Mean Error: {np.mean(err_fourier):.2e}%")
print(f"Ramanujan Max Error: {np.max(err_ramanujan):.2e}%")
print(f"Ramanujan Mean Error: {np.mean(err_ramanujan):.2e}%")
