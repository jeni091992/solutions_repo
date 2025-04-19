import numpy as np
import matplotlib.pyplot as plt

# Gravitational constant and Earth's mass
G = 6.67430e-11  # m^3/(kg·s^2)
M = 5.972e24      # kg (mass of Earth)
R_e = 6371000     # m (radius of Earth)

# Initial conditions
altitude = 500000  # m (500 km altitude)
initial_position = np.array([R_e + altitude, 0])  # Initial position vector (x, y)
initial_velocity = np.array([0, 7800])  # m/s (horizontal velocity)

# Time settings
time_step = 50  # s (smaller time step for higher accuracy)
total_time = 20000  # s (increase total time to allow the payload to move more)

# Define the function for the system of equations (for RK4)
def gravitational_acceleration(position):
    r = np.linalg.norm(position)  # Distance from the center of Earth
    force = -G * M * position / r**3  # Gravitational force vector
    return force

# Runge-Kutta 4th Order Integration
def rk4_step(position, velocity, dt):
    # Compute the four intermediate steps for RK4
    k1_v = gravitational_acceleration(position) * dt
    k1_r = velocity * dt

    k2_v = gravitational_acceleration(position + 0.5 * k1_r) * dt
    k2_r = (velocity + 0.5 * k1_v) * dt

    k3_v = gravitational_acceleration(position + 0.5 * k2_r) * dt
    k3_r = (velocity + 0.5 * k2_v) * dt

    k4_v = gravitational_acceleration(position + k3_r) * dt
    k4_r = (velocity + k3_v) * dt

    # Update position and velocity
    new_position = position + (k1_r + 2 * k2_r + 2 * k3_r + k4_r) / 6
    new_velocity = velocity + (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6

    return new_position, new_velocity

# Initialize arrays for storing trajectory data
positions = [initial_position]
velocities = [initial_velocity]
times = np.arange(0, total_time, time_step)

# Perform numerical integration over time
for t in times[1:]:
    position, velocity = rk4_step(positions[-1], velocities[-1], time_step)
    positions.append(position)
    velocities.append(velocity)

# Convert positions to numpy array for easier slicing
positions = np.array(positions)

# Plot the trajectory
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')

# Adjust the limits of the plot based on the trajectory
ax.set_xlim(-3e6, 3e6)  # Zoomed out range for X-axis
ax.set_ylim(-3e6, 3e6)  # Zoomed out range for Y-axis
ax.set_title("Payload Trajectory Near Earth")

# Plot Earth
earth = plt.Circle((0, 0), R_e, color='skyblue', label="Earth")
ax.add_patch(earth)

# Plot the computed trajectory
ax.plot(positions[:, 0] - R_e, positions[:, 1], label="Payload Trajectory", color='purple')

# Mark the initial position and velocity
ax.plot(positions[0, 0] - R_e, positions[0, 1], 'go', label="Initial Position")

# Adjust the quiver plot for the velocity vector, make the arrow bigger
ax.quiver(positions[0, 0] - R_e, positions[0, 1], initial_velocity[0], initial_velocity[1],
          angles='xy', scale_units='xy', color='g', label="Initial Velocity", width=0.005, scale=0.0005)

# Labels and grid
ax.legend()
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
plt.grid(True, linestyle='--', alpha=0.5)

# Save the plot as an image
plt.savefig('./images/payload_path_simulation.png')

# Show the plot
plt.show()
