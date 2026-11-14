import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

s_real = 0
s_imag = 1


def frequency_formula(t, s_real = 0, s_imag = 1, r = 1):
    return r * np.exp(-(s_real + s_imag * 1j) * t)

inputs = np.linspace(0, 8 * 2 *  np.pi, 8000)
outputs = frequency_formula(inputs)

fig, ax = plt.subplots(
    figsize=(6, 8),
    subplot_kw={"projection": "polar"}
)

l, = ax.plot(np.angle(outputs), np.abs(outputs), label="e^(it)") # ne samo inputs jer to ne primjenuje omeaga i freq, vec samo t


ax_slider_s_real = plt.axes([0.25, 0.14, 0.65, 0.03], facecolor="lightgoldenrodyellow")
ax_slider_s_imag = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")

s_real_slider = Slider(ax_slider_s_real, "Real Part", -3.0, 3.0, valinit=s_real, valstep=0.1)
s_imag_slider = Slider(ax_slider_s_imag, "Imaginary Part", -3.0, 3.0, valinit=s_imag, valstep=0.1)


def update(val):
    s_r = s_real_slider.val
    s_i = s_imag_slider.val

    # Update the outputs based on the new s_real and s_imag values
    outputs = frequency_formula(inputs, s_r, s_i)

    # Update signal
    l.set_data(np.angle(outputs), np.abs(outputs))


    fig.canvas.draw_idle()

s_real_slider.on_changed(update)
s_imag_slider.on_changed(update)

plt.show()