# Problem 2

# Investigating the Dynamics of a Forced Damped Pendulum

## 🎯 Motivation

The forced damped pendulum is a captivating example of nonlinear dynamics, where damping, restoring forces, and periodic driving interact to create complex behaviors—from periodic motion to chaos. It models real-world systems like mechanical oscillators, climate cycles, and electric circuits.

---

## 🧠 Theoretical Foundation

### Governing Equation:

\[
\frac{d^2\theta}{dt^2} + b\frac{d\theta}{dt} + \frac{g}{L} \sin(\theta) = A \cos(\omega_d t)
\]

- \( \theta(t) \): angular displacement
- \( b \): damping coefficient
- \( A \): amplitude of driving force
- \( \omega_d \): driving frequency
- \( g \): acceleration due to gravity
- \( L \): length of pendulum

### Small-Angle Approximation:

For small \( \theta \), \( \sin(\theta) \approx \theta \). The equation becomes:

\[
\theta'' + b \theta' + \frac{g}{L} \theta = A \cos(\omega_d t)
\]

This describes a driven damped harmonic oscillator with resonance near:

\[
\omega_d \approx \sqrt{\frac{g}{L}}
\]

---

## 🔬 Analysis of Dynamics

By varying parameters, we explore the system’s rich behavior:

- **Damping \(b\)**: controls energy loss rate
- **Amplitude \(A\)**: influences transition to chaos
- **Frequency \( \omega_d \)**: resonance & quasi-periodicity

---

## 🧪 Python Simulation Code

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Physical parameters
g = 9.81
L = 1.0

# Differential equation
def pendulum(t, y, b, A, omega_d):
    theta, omega = y
    dydt = [omega, -b * omega - (g / L) * np.sin(theta) + A * np.cos(omega_d * t)]
    return dydt

# Solver
def solve_pendulum(b, A, omega_d, y0, t_span=(0, 100), points=10000):
    t_eval = np.linspace(*t_span, points)
    sol = solve_ivp(pendulum, t_span, y0, t_eval=t_eval, method='RK45', args=(b, A, omega_d))
    return sol

# Plot functions
def plot_time_series(sol):
    plt.figure(figsize=(10, 4))
    plt.plot(sol.t, sol.y[0])
    plt.title('Angle vs Time')
    plt.xlabel('Time [s]')
    plt.ylabel('Angle [rad]')
    plt.grid(True)
    plt.show()

def plot_phase_portrait(sol):
    plt.figure(figsize=(6, 6))
    plt.plot(sol.y[0], sol.y[1], lw=0.5)
    plt.title('Phase Portrait')
    plt.xlabel('Angle [rad]')
    plt.ylabel('Angular Velocity [rad/s]')
    plt.grid(True)
    plt.show()

def plot_poincare_section(sol, omega_d):
    T_drive = 2 * np.pi / omega_d
    sample_times = np.arange(0, sol.t[-1], T_drive)
    sampled_indices = np.searchsorted(sol.t, sample_times)
    sampled_theta = sol.y[0][sampled_indices % len(sol.y[0])]
    sampled_omega = sol.y[1][sampled_indices % len(sol.y[1])]
    plt.figure(figsize=(6, 6))
    plt.plot(sampled_theta, sampled_omega, 'o', markersize=2)
    plt.title('Poincare Section')
    plt.xlabel('Angle [rad]')
    plt.ylabel('Angular Velocity [rad/s]')
    plt.grid(True)
    plt.show()

def plot_bifurcation(y0, b, omega_d, A_range, sample_point=-100):
    theta_vals = []
    A_vals = []
    for A in A_range:
        sol = solve_pendulum(b, A, omega_d, y0)
        T_drive = 2 * np.pi / omega_d
        sample_times = np.arange(0, sol.t[-1], T_drive)
        sampled_indices = np.searchsorted(sol.t, sample_times)
        sampled_theta = sol.y[0][sampled_indices[sample_point:]]
        theta_vals.extend(sampled_theta)
        A_vals.extend([A] * len(sampled_theta))
    plt.figure(figsize=(10, 6))
    plt.plot(A_vals, theta_vals, 'k.', markersize=0.5)
    plt.title('Bifurcation Diagram')
    plt.xlabel('Driving Amplitude A')
    plt.ylabel('Angle [rad]')
    plt.grid(True)
    plt.show()

# Run example
b = 0.5
A = 1.2
omega_d = 2.0
y0 = [0.1, 0.0]

sol = solve_pendulum(b, A, omega_d, y0)
plot_time_series(sol)
plot_phase_portrait(sol)
plot_poincare_section(sol, omega_d)

# Bifurcation diagram
A_values = np.linspace(0.5, 1.5, 500)
plot_bifurcation(y0, b, omega_d, A_values)
