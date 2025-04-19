# Problem 2

## 🧠 **General Solutions for the Forced Damped Pendulum**

### **1. Full Nonlinear Equation**

The forced damped pendulum is governed by the second-order nonlinear ODE:

\[
\frac{d^2\theta}{dt^2} + b\frac{d\theta}{dt} + \frac{g}{L}\sin(\theta) = A\cos(\omega_d t)
\]

This is **nonlinear**, **non-autonomous**, and **second-order**, with:
- **Damping**: \( b\frac{d\theta}{dt} \)
- **Restoring force**: \( \frac{g}{L} \sin(\theta) \)
- **External driving**: \( A\cos(\omega_d t) \)

❗**General solutions to this equation cannot be written in closed form.** Numerical techniques are necessary.

---

### **2. Linearized Case (Small-Angle Approximation)**

For small oscillations \( \theta \ll 1 \), we use:

\[
\sin(\theta) \approx \theta
\]

Then the equation becomes:

\[
\frac{d^2\theta}{dt^2} + b\frac{d\theta}{dt} + \frac{g}{L} \theta = A\cos(\omega_d t)
\]

This is a **linear inhomogeneous second-order ODE**, with the general solution:

\[
\theta(t) = \theta_h(t) + \theta_p(t)
\]

#### 🔹 Homogeneous Solution (\( \theta_h \)):

\[
\frac{d^2\theta}{dt^2} + b\frac{d\theta}{dt} + \omega_0^2 \theta = 0
\quad\text{where } \omega_0 = \sqrt{\frac{g}{L}}
\]

Solving this gives:

- **Underdamped**: \( b^2 < 4\omega_0^2 \)

\[
\theta_h(t) = e^{-\frac{b}{2}t}(C_1\cos(\omega_1 t) + C_2\sin(\omega_1 t)) \quad \text{where } \omega_1 = \sqrt{\omega_0^2 - \left(\frac{b}{2}\right)^2}
\]

- **Critically damped**: \( b^2 = 4\omega_0^2 \)
- **Overdamped**: \( b^2 > 4\omega_0^2 \)

Each case leads to exponential decay of oscillations.

#### 🔹 Particular Solution (\( \theta_p \)):

We seek a steady-state solution of the form:

\[
\theta_p(t) = B\cos(\omega_d t - \delta)
\]

Where:
- \( B \): amplitude of response
- \( \delta \): phase shift between driving force and response

Substitute into the linearized equation to get:

\[
B = \frac{A}{\sqrt{(\omega_0^2 - \omega_d^2)^2 + b^2\omega_d^2}} \\
\delta = \tan^{-1}\left( \frac{b\omega_d}{\omega_0^2 - \omega_d^2} \right)
\]

---

### **3. Resonance Behavior**

- Resonance occurs when the driving frequency \( \omega_d \) is near the natural frequency \( \omega_0 \)
- The system’s response peaks when:

\[
\omega_{\text{res}} = \sqrt{\omega_0^2 - \frac{b^2}{2}}
\]

The amplitude increases dramatically unless damping \( b \) is large.

---

### **4. Numerical and Chaotic Solutions (Full Nonlinear Case)**

For larger amplitudes, the small-angle approximation breaks down, and **nonlinear effects dominate**, especially when:
- \( A \) is large (strong driving)
- \( b \) is small (weak damping)

#### 🌪 Chaos Emerges When:
- There's sensitive dependence on initial conditions
- The system exhibits non-periodic, bounded trajectories
- Phase space trajectories fill a region instead of forming closed loops

These must be analyzed using:
- **Numerical Integration** (e.g., Runge-Kutta)
- **Poincaré Maps**
- **Lyapunov Exponents**
- **Bifurcation Diagrams**

---

### **5. Summary of Behavior by Regime**

| Regime                   | Behavior                      | Solution Type                   |
|--------------------------|-------------------------------|----------------------------------|
| Small-angle, no drive    | Simple Harmonic Motion        | Analytic                         |
| Small-angle, with drive  | Linear resonance               | Analytic (steady-state + decay) |
| Full equation, weak drive| Quasiperiodic or periodic     | Numerical                        |
| Full equation, strong drive| Chaotic                     | Numerical                        |

---

### Graphical Representations of Motion

The plots below show the angular motion of the forced damped pendulum under various parameter regimes:

![Forced Damped Pendulum Behaviors](./images/forced_damped_pendulum_behaviors.png)

