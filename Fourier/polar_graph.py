import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


def euler_formula(t, f = 1, r = 1):
    return r * np.exp(2 * np.pi * f * 1j * t)

# n - signal frequency

def frequency_formula(t, r = 1, n = 1):
    return np.sin(n * t) * euler_formula(t, f=4, r = r)

plt.figure(figsize=[6,6])

inputs = np.linspace(0, 2 * np.pi, 1000)
outputs = frequency_formula(inputs, n = 4)


ax = plt.subplot(111, polar=True)

ax.plot(inputs, np.abs(outputs), label="e^(it)")
ax.plot()


plt.show()