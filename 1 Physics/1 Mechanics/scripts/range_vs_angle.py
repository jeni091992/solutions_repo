import numpy as np
import matplotlib.pyplot as plt

# Parameters
v0 = 20  # Initial velocity (m/s)
g = 9.81  # Gravitational acceleration (m/s^2)
angles = np.linspace(0, 90, 500)  # Angles in degrees

# Calculate range
ranges = (v0**2 * np.sin(2 * np.radians(angles))) / g

# Handle edge case where angle is 90 degrees
ranges[np.isclose(angles, 90)] = 0  # Set range to 0 for 90 degrees

# Plot
plt.figure(figsize=(8, 6))
plt.plot(angles, ranges)
plt.title("Range vs Angle of Projection")
plt.xlabel("Angle (degrees)")
plt.ylabel("Range (meters)")
plt.grid()

# Save the plot as an image
plt.savefig("range_vs_angle.png", dpi=300)  # Save as PNG with high resolution
plt.show()