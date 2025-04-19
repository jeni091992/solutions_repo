import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24     # Mass of Earth (kg)

# Orbital radii (in meters)
radii = np.linspace(1e7, 5e8, 100)
# Periods from Kepler's Third Law
periods = 2 * np.pi * np.sqrt(radii**3 / (G * M))

# Plot T^2 vs r^3
plt.figure(figsize=(8, 5))
plt.plot(radii**3, periods**2, label='T² vs r³', color='blue')
plt.xlabel('r³ (m³)')
plt.ylabel('T² (s²)')
plt.title("Verification of Kepler's Third Law")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the figure as a PNG image
plt.savefig("keplers_law_plot.png", dpi=300)

# Optionally display it
plt.show()
