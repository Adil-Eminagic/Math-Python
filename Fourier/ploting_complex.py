
import numpy as np
import matplotlib.pyplot as plt

# Complex number
z = 2 + 3j

# Euler's formula
t = np.linspace(0, 2*np.pi, 500)
w = np.exp(1j * t)

fig, ax = plt.subplots(figsize=(7, 7))

# Plot complex point
ax.scatter(z.real, z.imag, color="red", s=80)
ax.annotate("2 + 3i", (z.real, z.imag))

# Plot Euler's formula (unit circle)
ax.plot(w.real, w.imag, label="e^(it)")

# Draw axes
ax.axhline(0, color="gray")
ax.axvline(0, color="gray")

ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_aspect("equal")
ax.grid(True)
ax.legend()

plt.show()
