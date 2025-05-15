from mpmath import mpf, sqrt, ellipe, pi as mpi
import numpy as np

def true_perimeter(a, b):
    results = []
    for a_, b_ in zip(a, b):
        a_mp = mpf(a_)
        b_mp = mpf(b_)
        e = sqrt(1 - (b_mp / a_mp)**2)
        results.append(float(4 * a_mp * ellipe(e**2)))
    return np.array(results)

def k_true(r, PI=mpi):
    results = []
    for ri in r:
        a = mpf(1)
        b = mpf(ri)
        e = sqrt(1 - (b / a)**2)
        true_p = 4 * a * ellipe(e**2)
        k = true_p / (PI * (a + b))
        results.append(float(k))
    return np.array(results)

def ramanujan_perimeter(a, b):
    return np.pi * (3 * (a + b) - np.sqrt((3 * a + b) * (a + 3 * b)))
