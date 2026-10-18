import numpy as np
import matplotlib.pyplot as plt
from four_func import complex_mean, angle_compex, radius_complex



def euler_formula(t, f = 1, r = 1):
    return r * np.exp(2 * np.pi * f * 1j * t)

def frequency_formula(t, r = 1):
    return np.sin(4 * t) * euler_formula(t, r = r)

plt.figure(figsize=[6,6])

inputs = np.linspace(0, 2* np.pi, 1000)
outputs = frequency_formula(inputs)


ax = plt.subplot(111, polar=True)

ax.plot(inputs, np.abs(outputs), label="e^(it)")

# average = complex_mean(outputs)

# ax.plot(angle_compex(average), radius_complex(average), color="red")


plt.show()