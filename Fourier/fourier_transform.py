import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

from four_func import complex_mean, angle_compex, radius_complex


omega = 1.0

def euler_formula(t, o = 1, r = 1):
    return r * np.exp( o * 1j * t)

def frequency_formula(t, o = 1, r = 1):
    return np.sin(4 * t) * euler_formula(t, o= o, r = r)

inputs = np.linspace(0, 2* np.pi, 1000)
outputs = frequency_formula(inputs)


fig, ax = plt.subplots(
    figsize=(6, 7),
    subplot_kw={"projection": "polar"}
)


l, = ax.plot(inputs, np.abs(outputs), label="e^(it)")

average = complex_mean(outputs)

center, = ax.plot(
    [np.angle(average)],
    [np.abs(average)],
    marker="o",
    markersize=12,
    color="red",
    markeredgecolor="black",
    linestyle="None",
    label="Center of mass"
)

ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")
slider = Slider(ax_slider, "Omega", 0.1, 5.0, valinit=omega)

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