import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

plt.figure(figsize=[9,4])

plt.subplot(1, 2, 2)
plt.plot(x, np.sin(x))

plt.subplot(1, 2, 1)
plt.plot(x, np.cos(x))

# subplot(1, 2, 1) means a grid with one row, two columns, and select the first position. 
# The next subplot(1, 2, 2) selects the second position.

plt.show()