import numpy as np
import matplotlib.pyplot as plt
from four_func import complex_mean, angle_compex, radius_complex


def euler_formula(t, omega, r = 1):
    return r * np.exp( omega * -1j * t)

def frequency_formula(t, o = 1, r = 1):
    return np.sin(4 * t) * euler_formula(t, omega=o, r = r)

plt.figure(figsize=[6,6])

inputs = np.linspace(0 , 2* np.pi, 1000)
outputs = frequency_formula(inputs, o=4)


ax = plt.subplot(111, polar=True)

# ax.plot(inputs, np.abs(outputs), label="e^(it)") this didn't work because youyou don't adding omega for inouts, if omega is 2, each oringal input must be multiplied by 2

ax.plot(np.angle(outputs), np.abs(outputs), label="e^(it)")


average = complex_mean(outputs)

ax.plot(angle_compex(average), radius_complex(average), color="red")


plt.show()