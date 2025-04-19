import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure the output directory exists
output_dir = "images"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "payload_trajectories_near_earth.png")

# Set up figure
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_xlim(-2, 6)
ax.set_ylim(-3, 3)
ax.set_title("Payload Trajectories Near Earth")

# Plot Earth
earth = plt.Circle((0, 0), 1, color='skyblue', label="Earth")
ax.add_patch(earth)

# Elliptical orbit
theta = np.linspace(0, 2 * np.pi, 500)
a, b = 3, 2  # semi-major and semi-minor axes
x_ellipse = a * np.cos(theta)
y_ellipse = b * np.sin(theta)
ax.plot(x_ellipse, y_ellipse, 'b', label="Elliptical (Bound Orbit)")

# Parabolic trajectory (approximated with y = sqrt(x))
x_parabola = np.linspace(0.9, 5, 300)
y_parabola = np.sqrt(x_parabola - 0.9)
ax.plot(x_parabola, y_parabola, 'g', label="Parabolic (Escape)")

# Hyperbolic trajectory (y = 2 / x shifted and scaled)
x_hyperbola = np.linspace(1.1, 6, 300)
y_hyperbola = 2 / (x_hyperbola - 0.9)
ax.plot(x_hyperbola, y_hyperbola, 'r', label="Hyperbolic (Unbound)")

# Suborbital trajectory (part of a smaller ellipse)
theta_sub = np.linspace(-np.pi / 3, np.pi / 3, 300)
a_sub, b_sub = 2, 1
x_suborbital = a_sub * np.cos(theta_sub)
y_suborbital = b_sub * np.sin(theta_sub)
ax.plot(x_suborbital, y_suborbital, 'm', label="Suborbital (Reentry)")

# Labels and visual enhancements
ax.annotate('Earth', xy=(0, 0), xytext=(-0.5, -0.5), fontsize=10)
ax.legend(loc='upper right')
ax.axhline(0, color='gray', lw=0.5)
ax.axvline(0, color='gray', lw=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel("X (arbitrary units)")
plt.ylabel("Y (arbitrary units)")

# Save figure
plt.savefig(output_path, dpi=300)
plt.close()

print(f"Trajectory diagram saved as: {output_path}")
