import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2

# Data for the planets
planets = ['Earth', 'Mars', 'Jupiter']
radii = [6.371e6, 3.390e6, 69.911e6]  # Radii in meters
masses = [5.972e24, 6.39e23, 1.898e27]  # Masses in kg

# Calculate first and second cosmic velocities (orbital and escape velocities)
v1 = np.sqrt(G * np.array(masses) / np.array(radii))  # Orbital velocity (v₁)
v2 = np.sqrt(2 * G * np.array(masses) / np.array(radii))  # Escape velocity (v₂)

# Plotting
x = np.arange(len(planets))

plt.figure(figsize=(10, 6))

# Plot v₁ and v₂ side by side for each planet
bar_width = 0.35
plt.bar(x - bar_width / 2, v1 / 1e3, bar_width, label='Orbital Velocity (v₁) [km/s]', color='blue')  # Convert m/s to km/s
plt.bar(x + bar_width / 2, v2 / 1e3, bar_width, label='Escape Velocity (v₂) [km/s]', color='red')  # Convert m/s to km/s

# Labels and title
plt.xlabel('Planets')
plt.ylabel('Velocity (km/s)')
plt.title('Cosmic Velocities by Planet')
plt.xticks(x, planets)
plt.legend()

# Show plot
plt.tight_layout()
plt.savefig('cosmic_velocities.png', dpi=300)
plt.show()
