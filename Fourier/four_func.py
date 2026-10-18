import numpy as np

def complex_mean(complex):
    sum = 0
    for c in complex:
        sum += c
    return sum / len(complex)

def angle_compex(complex):
    return np.arctan(np.imag(complex) / np.real(complex))

def radius_complex(complex):
    return np.sqrt(np.imag(complex)**2 + np.real(complex)**2)