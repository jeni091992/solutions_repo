# Investigating the Range as a Function of the Angle of Projection

## Motivation
Projectile motion offers a rich framework for exploring fundamental principles of physics. This document analyzes how the range of a projectile depends on its angle of projection, considering various parameters like initial velocity and gravitational acceleration.

## Theoretical Foundation
### Governing Equations
The motion of a projectile is governed by the following equations:
- Horizontal motion: \( x(t) = v_0 \cos(\theta) t \)
- Vertical motion: \( y(t) = v_0 \sin(\theta) t - \frac{1}{2} g t^2 \)

The range \( R \) can be derived as:
\[ R = \frac{v_0^2 \sin(2\theta)}{g} \]

### Family of Solutions
Discuss how variations in initial velocity \( v_0 \), gravitational acceleration \( g \), and launch height affect the trajectory.

## Analysis of the Range
### Dependence on Angle of Projection
Investigate the relationship between the range and the angle of projection \( \theta \). Include a graph showing \( R \) vs. \( \theta \).

### Influence of Other Parameters
Analyze how changes in \( v_0 \) and \( g \) modify the range.

## Practical Applications
- Sports: Predicting the trajectory of a soccer ball.
- Engineering: Designing projectile launch systems.
- Astrophysics: Modeling rocket trajectories.

## Implementation
### Python Simulation
```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
v0 = 20  # Initial velocity (m/s)
g = 9.81  # Gravitational acceleration (m/s^2)
angles = np.linspace(0, 90, 500)  # Angles in degrees

# Calculate range
ranges = (v0**2 * np.sin(2 * np.radians(angles))) / g

# Plot
plt.figure(figsize=(8, 6))
plt.plot(angles, ranges)
plt.title("Range vs Angle of Projection")
plt.xlabel("Angle (degrees)")
plt.ylabel("Range (meters)")
plt.grid()
plt.show()
```
