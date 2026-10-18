import numpy as np
import matplotlib.pyplot as plt
from four_func import complex_mean, angle_compex, radius_complex

# 1. Define sample complex numbers (Cartesian form: x + yj)
complex_numbers = [
    3 + 4j,         # Quadrant 1
    -2 + 5j,        # Quadrant 2
    -4 - 3j,        # Quadrant 3
    2 - 2j          # Quadrant 4
]


print(complex_mean(complex_numbers))
print(np.imag(complex_numbers[0]))
print(np.real(complex_numbers[0]))
print(np.imag(complex_numbers[0])/ np.real(complex_numbers[0]))
print(np.arctan(np.imag(complex_numbers[0])/ np.real(complex_numbers[0])))


print(angle_compex(complex_numbers[0]))
print(radius_complex(complex_numbers[0]))

