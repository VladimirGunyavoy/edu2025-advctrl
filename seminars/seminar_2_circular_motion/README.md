# Seminar 2: Point Motion Simulation and Linear Transformations

This seminar focuses on simulating the motion of a point in 2D, particularly circular motion and harmonic oscillation, and applying linear transformations to trajectories.

## Contents

1.  **Simulation of Circular Motion:** Simulating motion with orthogonal velocity ($\mathbf{v} = \mathbf{r}^{\perp}$) and observing numerical instability (spiral) with Euler integration.
2.  **Simulation of Harmonic Oscillator:** Modeling a 2D oscillator ($\mathbf{a} = -\mathbf{r}$) showing stable circular/elliptical motion.
3.  **Linear Transformations:** Applying scaling, rotation, and shear matrices to the oscillator trajectory.
4.  **Visualization:** Plotting trajectories, state variables over time, and phase portraits.

## Key Topics

*   2D Point Motion Simulation
*   Euler Integration Method & Numerical Stability
*   Circular Motion (Orthogonal Velocity)
*   Simple Harmonic Oscillator
*   Linear Transformations (Scaling, Rotation, Shear)
*   Phase Portraits

## Mathematical Foundation

*   Position Update (Euler): $\mathbf{r}_{i+1} = \mathbf{r}_i + \mathbf{v}_i \cdot dt$
*   Velocity Update (Euler): $\mathbf{v}_{i+1} = \mathbf{v}_i + \mathbf{a}_i \cdot dt$
*   Orthogonal Velocity Condition: $\mathbf{v} = \mathbf{r}^{\perp}$ (Rotation by 90°: $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$)
*   Harmonic Oscillator Acceleration: $\mathbf{a} = -\mathbf{r}$
*   Linear Transformation: $\mathbf{s}' = A\mathbf{s}$

## Files in Directory

*   `seminar_2_solution.ipynb`: The main Jupyter Notebook. Contains explanations, Python code for simulating point motion (circular, harmonic oscillator), applying linear transformations, and generating all plots and visualizations.
*   `img/`: Empty directory (intended for plots if saved externally).
*   `README.md`: This file, providing a summary of the seminar's content and structure.

## Running the Code

*   **Jupyter Notebook:** Open and run the cells in `seminar_2_solution.ipynb`. Ensure `numpy` and `matplotlib` are installed. 