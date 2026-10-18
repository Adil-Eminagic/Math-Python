import numpy as np
import matplotlib.pyplot as plt

# 1. Define sample complex numbers (Cartesian form: x + yj)
complex_numbers = [
    3 + 4j,         # Quadrant 1
    -2 + 5j,        # Quadrant 2
    -4 - 3j,        # Quadrant 3
    2 - 2j          # Quadrant 4
]

# 2. Extract polar properties (theta in radians, r as magnitude)
thetas = [np.angle(z) for z in complex_numbers]
radii = [np.abs(z) for z in complex_numbers]

# 3. Create a continuous complex function to plot as a curve (e.g., a spiral)
t = np.linspace(0, 2 * np.pi, 200)
complex_spiral = (t / 2) * np.exp(1j * t)  # z = r * e^(i*theta)
spiral_thetas = np.angle(complex_spiral)
spiral_radii = np.abs(complex_spiral)

# 4. Initialize the polar plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})

# Plot the continuous complex curve
ax.plot(spiral_thetas, spiral_radii, color='gray', linestyle='--', label='Complex Curve')

# Plot individual complex points and draw vector lines from the origin
for i, (theta, r) in enumerate(zip(thetas, radii)):
    # Draw vector line
    ax.plot([0, theta], [0, r], linewidth=1.5)
    # Draw point marker
    ax.scatter(theta, r, s=50, zorder=3, label=f'z{i+1}: {complex_numbers[i]}')

# 5. Customize the grid layout
ax.set_title("Complex Plane (Polar Coordinates)", va='bottom', fontsize=14)
ax.set_rmax(6)                         # Set maximum radial limit
ax.set_rlabel_position(45)             # Move radial labels away from axes
ax.grid(True)                          # Ensure background grid is visible
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Display plot
plt.show()
