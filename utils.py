import numpy as np

def compute_theta_vals(r_vals, PI):
    return np.array([float(PI * (r - 0.2) / 0.8) for r in r_vals])

def compute_error(true_vals, approx_vals):
    return 100 * np.abs(approx_vals - true_vals) / true_vals
