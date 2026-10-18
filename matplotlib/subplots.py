import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)


fig, axs = plt.subplots(2, 2)

# Axes - individual plotting area

# Each subplot is a separate Axes object, and each can contain any number of lines, points, or other graphical elements.

axs[0, 0].plot(x, np.sin(x))  # plt.plot selct curretn axis, while ax.plot better approach
axs[0, 0].plot(x, np.cos(x)) # tow graphs on same axis 
axs[0, 0].xlabel = "Time"
axs[0, 0].ylabel = "Pressure"
#axs[0, 0].title = "Sound singal"



axs[0, 1].plot(x, np.cos(x))
axs[1, 0].plot(x, x**2)
axs[1, 1].plot(x, x**3)

f = plt.figure() # creating empty figure

plt.show()



# plt.plot()	Draws data on the current Axes
# plt.subplot()	Creates or selects one Axes in a subplot grid
# plt.subplots()	Creates a Figure and one or more Axes together