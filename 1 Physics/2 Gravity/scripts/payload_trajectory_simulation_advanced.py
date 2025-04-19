import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G

# Define the mass of Earth manually
M_e = 5.972e24  # Mass of Earth in kg

# Constants
R_e = 6371e3  # Radius of Earth in meters
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2

# Initial conditions (ensure these are float64)
initial_position = np.array([R_e + 500e3, 0], dtype=np.float64)  # Initial position (500 km above Earth's surface)
initial_velocity = np.array([0, 7500], dtype=np.float64)  # Initial velocity in m/s (approximately 7.5 km/s tangential)

# Time settings
t_max = 6000  # Max time for the simulation in seconds
dt = 1  # Time step in seconds

# Equations of motion
def acceleration(position):
    r = np.linalg.norm(position)  # Distance from the Earth's center
    a = -G * M_e * position / r**3  # Gravitational acceleration vector
    return a

# Runge-Kutta 4th order integration
def runge_kutta(position, velocity, dt):
    k1v = acceleration(position) * dt
    k1r = velocity * dt
    
    k2v = acceleration(position + 0.5 * k1r) * dt
    k2r = (velocity + 0.5 * k1v) * dt
    
    k3v = acceleration(position + 0.5 * k2r) * dt
    k3r = (velocity + 0.5 * k2v) * dt
    
    k4v = acceleration(position + k3r) * dt
    k4r = (velocity + k3v) * dt
    
    # Update position and velocity
    position += (k1r + 2*k2r + 2*k3r + k4r) / 6
    velocity += (k1v + 2*k2v + 2*k3v + k4v) / 6
    
    return position, velocity

# Initialize arrays to store the results
positions = [initial_position]
velocities = [initial_velocity]
times = np.arange(0, t_max, dt)

# Perform the numerical integration
for t in times[:-1]:
    position, velocity = runge_kutta(positions[-1], velocities[-1], dt)
    positions.append(position)
    velocities.append(velocity)

# Convert positions to numpy array for easier manipulation
positions = np.array(positions)

# Plotting the trajectory with improvements
plt.figure(figsize=(10, 10))

# Plot Earth as a circle
earth_circle = plt.Circle((0, 0), R_e / 1e3, color='b', alpha=0.3, label="Earth", zorder=10)
plt.gca().add_artist(earth_circle)

# Plot the payload's trajectory
plt.plot(positions[:, 0] / 1e3, positions[:, 1] / 1e3, label="Payload Path", color='orange', linewidth=2, zorder=5)

# Initial position
plt.plot(initial_position[0] / 1e3, initial_position[1] / 1e3, 'go', label="Initial Position", markersize=8, zorder=15)

# Highlight Earth's surface
plt.plot(R_e / 1e3, 0, 'k.', label="Earth's Surface", markersize=20)

# Title and labels
plt.title("Payload Trajectory Simulation Near Earth", fontsize=16, fontweight='bold')
plt.xlabel("X (km)", fontsize=12)
plt.ylabel("Y (km)", fontsize=12)

# Grid and aspect ratio
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)

# Customize plot limits
plt.xlim(-8000, 8000)  # Set limits to show a good portion of the trajectory
plt.ylim(-8000, 8000)

# Add legend
plt.legend(loc="upper right", fontsize=12)

# Set aspect ratio to be equal
plt.gca().set_aspect('equal', adjustable='box')

# Save the plot as an image file
plt.savefig('payload_trajectory_simulation_advanced.png', dpi=300)

# Show the plot
plt.show()
