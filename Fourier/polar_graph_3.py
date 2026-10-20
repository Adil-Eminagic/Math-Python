import numpy as np
import matplotlib.pyplot as plt
from four_func import complex_mean, angle_compex, radius_complex
from matplotlib.widgets import Slider


omega = 1

def euler_formula(t, omega, r = 1):
    return r * np.exp( omega * -1j * t)

def frequency_formula(t, o = 1, r = 1):
    return np.sin(4 * t) * euler_formula(t, omega=o, r = r)

plt.figure(figsize=[6,6])

inputs = np.linspace(0 * omega, 2* np.pi, 1000)

outputs = frequency_formula(inputs, o=4)

ax = plt.subplot(111, polar=True)

l, = ax.plot(inputs, np.abs(outputs), label="e^(it)") 


ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")
slider = Slider(ax_slider, "Omega", 0.1, 5.0, valinit=omega, valstep=0.3)

def update(val):
    outputs = frequency_formula(inputs, val)

    # Update signal
    l.set_data(np.angle(outputs), np.abs(outputs))

    average = np.mean(outputs)

    center.set_data(
        [np.angle(average)],
        [np.abs(average)]
    )

    fig.canvas.draw_idle()

slider.on_changed(update)


plt.show()