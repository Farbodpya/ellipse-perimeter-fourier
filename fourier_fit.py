import numpy as np
from scipy.optimize import curve_fit

def fourier_series(theta, *a):
    N = (len(a) - 1) // 2
    result = a[0]
    for n in range(1, N + 1):
        result += a[n] * np.cos(n * theta) + a[n + N] * np.sin(n * theta)
    return result

def fit_fourier(theta_vals, k_vals, degree):
    p0 = np.zeros(2 * degree + 1)
    params, _ = curve_fit(fourier_series, theta_vals, k_vals, p0=p0)
    return params

def k_fourier(r, params, PI):
    theta = float(PI) * (r - 0.2) / 0.8
    return fourier_series(theta, *params)

def perimeter_corrected_fourier(a, b, params, PI):
    return np.array([
        k_fourier(bi / ai, params, PI) * float(PI) * (ai + bi)
        for ai, bi in zip(a, b)
    ])
