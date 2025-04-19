import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Physical constant
g = 9.81
L = 1.0

# Differential equation of forced damped pendulum
def forced_damped_pendulum(t, y, b, A, omega_d):
    theta, omega = y
    dydt = [omega, -b * omega - (g / L) * np.sin(theta) + A * np.cos(omega_d * t)]
    return dydt

# Solver
def simulate_pendulum(b, A, omega_d, y0=[0.2, 0.0], t_span=(0, 100), points=5000):
    t_eval = np.linspace(*t_span, points)
    sol = solve_ivp(forced_damped_pendulum, t_span, y0, t_eval=t_eval, args=(b, A, omega_d))
    return sol.t, sol.y[0]

# Plot multiple simulations
def plot_multiple_conditions():
    fig, axs = plt.subplots(3, 2, figsize=(14, 10))
    params = [
        (0.1, 0.5, 1.0, "Light Damping, Low Drive"),
        (0.5, 0.5, 1.0, "Medium Damping, Low Drive"),
        (1.0, 0.5, 1.0, "Heavy Damping, Low Drive"),
        (0.1, 1.2, 1.0, "Light Damping, High Drive"),
        (0.1, 1.2, np.sqrt(g / L), "Near Resonance"),
        (0.1, 1.5, 2.0, "Chaotic Behavior")
    ]

    for ax, (b, A, omega_d, title) in zip(axs.flat, params):
        t, theta = simulate_pendulum(b, A, omega_d)
        ax.plot(t, theta, lw=0.8)
        ax.set_title(title)
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Angle [rad]")
        ax.grid(True)

    plt.tight_layout()
    return fig

fig = plot_multiple_conditions()
plt.show()

fig.savefig("forced_damped_pendulum_behaviors.png", dpi=300)
