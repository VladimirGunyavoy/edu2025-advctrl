import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Function to plot a phase portrait
def plot_phase_portrait(ax, system_ode, k1, k2, X, Y, t_span, t_eval, title, eigenvalues):
    """Plots the phase portrait for a given system on the provided axes."""
    # Calculate vector field
    U, V = np.zeros(X.shape), np.zeros(Y.shape)
    NI, NJ = X.shape
    for i in range(NI):
        for j in range(NJ):
            x = X[i, j]
            y = Y[i, j]
            yprime = system_ode(0, [x, y], k1, k2) # t=0 is arbitrary for autonomous system
            U[i, j] = yprime[0]
            V[i, j] = yprime[1]

    # Plot vector field using streamplot for better visualization
    ax.streamplot(X, Y, U, V, color='grey', linewidth=0.5, density=1.5, arrowstyle='->', arrowsize=1)

    # Simulate and plot trajectories from multiple initial conditions
    initial_points = [
        (1, 1), (-1, 1), (1, -1), (-1, -1),
        (0.5, 0), (-0.5, 0), (0, 0.5), (0, -0.5)
    ]
    colors = plt.cm.viridis(np.linspace(0, 1, len(initial_points)))

    for idx, y0 in enumerate(initial_points):
        sol = solve_ivp(system_ode, t_span, y0, args=(k1, k2), dense_output=True, t_eval=t_eval)
        ax.plot(sol.y[0], sol.y[1], color=colors[idx], linewidth=1.5, label=f'Start ({y0[0]},{y0[1]})')
        ax.plot(sol.y[0, 0], sol.y[1, 0], 'o', color=colors[idx]) # Start point
        ax.plot(sol.y[0, -1], sol.y[1, -1], 's', color=colors[idx]) # End point

    # Formatting the plot
    ax.set_xlim([X.min(), X.max()])
    ax.set_ylim([Y.min(), Y.max()])
    ax.set_xlabel(r'$\theta$')
    ax.set_ylabel(r'$\dot{\theta}$')
    ax.set_title(title)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.plot(0, 0, 'ro', markersize=8, label='Equilibrium (0,0)') # Mark equilibrium

    # Add eigenvalue info to title or as text
    eig_text = "Eigenvalues: " + ", ".join([f'{e:.2f}' for e in eigenvalues])
    ax.text(0.05, 0.95, eig_text, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=dict(boxstyle='round,pad=0.3', fc='wheat', alpha=0.5)) 