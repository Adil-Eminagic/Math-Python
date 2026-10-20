import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from four_func import complex_mean, angle_compex, radius_complex


omega = 1.0
freq = 1
time = 0

def euler_formula(t, o = 1, r = 1):
    return r * np.exp( o * -1j * t) # why - ?

def frequency_formula(t, o = 1, f = 1, r = 1):
    return np.sin(f * t) * euler_formula(t, o = o, r = r)

inputs = np.linspace(0, 2*  np.pi, 1000)
outputs = frequency_formula(inputs)

fig, ax = plt.subplots(
    figsize=(6, 8),
    subplot_kw={"projection": "polar"}
)

l, = ax.plot(np.angle(outputs), np.abs(outputs), label="e^(it)") # ne samo inputs jer to ne primjenuje omeaga i freq, vec samo t

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

inital_value = frequency_formula(time, omega, freq)

tm, = ax.plot(
    [np.angle(inital_value)],
    [np.abs(inital_value)],
    marker="o",
    markersize=12,
    color="black",
    markeredgecolor="blue",
    linestyle="None",
    label="Curret value"
 )


# marker="o"	Draw a circular point
# markersize=12	Set the point's size
# color="red"	Set its color
# linestyle="None"	Don't draw a connecting line
# markeredgecolor="black"	Optional black outline

ax_slider_omega = plt.axes([0.25, 0.14, 0.65, 0.03], facecolor="lightgoldenrodyellow")
ax_slider_freq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")
ax_slider_time = plt.axes([0.25, 0.06, 0.65, 0.03], facecolor="lightgoldenrodyellow")

omega_slider = Slider(ax_slider_omega, "Omega", 0.1, 5.0, valinit=omega, valstep=0.1)
freq_slider = Slider(ax_slider_freq, "Frequency", 0.0, 5.0, valinit=freq, valstep=1)
time_slider = Slider(ax_slider_time, "Time", 0.0, 2 * np.pi, valinit=time, valstep=0.1)


def update(val):
    o = omega_slider.val
    f = freq_slider.val

    outputs = frequency_formula(inputs, o, f)

    # Update signal
    l.set_data(np.angle(outputs), np.abs(outputs))

    average = np.mean(outputs)

    center.set_data(
        [np.angle(average)],
        [np.abs(average)]
    )

    current = frequency_formula(time_slider.val, o, f)

    tm.set_data([np.angle(current)], [np.abs(current)])

    fig.canvas.draw_idle()

omega_slider.on_changed(update)
freq_slider.on_changed(update)
time_slider.on_changed(update)


plt.show()