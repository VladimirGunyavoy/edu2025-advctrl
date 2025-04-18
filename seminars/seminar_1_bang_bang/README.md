# Seminar 1: Bang-Bang Control

This seminar introduces time-optimal bang-bang control for simple systems (e.g., double integrator).

## Key Topics

*   Time-Optimal Control
*   Bang-Bang Principle (Maximum Principle context)
*   Double Integrator System ($\ddot{x}=a$)
*   Phase Plane Analysis
*   Switching Curves
*   Control with Saturation

## Mathematical Foundation

*   System Dynamics: $\ddot{x} = a$, where control $a \in [-A_{max}, +A_{max}]$.
*   State Vector: $\mathbf{s} = [x, \dot{x}]^T$.
*   Bang-Bang Control Law: Control $a$ switches between $-A_{max}$ and $+A_{max}$ to reach the target state (origin) in minimum time.
*   Switching Curve: A curve in the phase plane (x, $\dot{x}$) where the optimal control switches sign. For the double integrator, it is typically parabolic: $x = -\frac{\dot{x}^2}{2A_{max}}\text{sign}(\dot{x})$.

## Running the Code / Interactive Exploration

*   **Desmos Links:** The interactive solutions for Problems 0-3 are available on Desmos (see links below). These allow exploring the concepts visually.
*   **Google Colab:** The `Plot Generator` code is available on Google Colab for generating trajectory plots.
*   **Local Script:** The `src/plot_generator.py` script can be run locally (requires `numpy`, `matplotlib`, `pickle`) to generate plots, potentially using the data in `src/random_trajectories.pkl`.

## Online Materials & Solutions

### Problem 0: Speed Control with Different Starting Conditions
- [Solution in Desmos](https://www.desmos.com/calculator/numk1ubgbr)

### Problem 1: Speed Control with Different Start and Finish
- [Solution in Desmos](https://www.desmos.com/calculator/cgouaw8ahm)

### Problem 2: Acceleration Control with Different Finish
- [Solution in Desmos](https://www.desmos.com/calculator/xkuqwc3ubl)

### Problem 3: Acceleration Control by Variants
- [Solution in Desmos](https://www.desmos.com/calculator/rpaq75ttlt)
- Different starting positions
- Different starting speeds
- Different finishing conditions

In this model:
- The k indicator shows the area
- You can change the switching time
- You can change the finishing time
- You can change the initial acceleration
- There are 9 different variants, with variant 10 being universal
- Variable g is for a special case

### Problem 3: Universal Solution
- [Solution in Desmos](https://www.desmos.com/calculator/kfdvir7dps?lang=ru)
- Solves for any area of initial states
- You can drag the green point "State" for different initial conditions

### Plot Generator
- [Code in Google Colab](https://colab.research.google.com/drive/1svjSiBcK5cCZ2ykVEje-vD4uFnX7DgY5?usp=sharing)
- Generates different trajectories of bang-bang stabilizations
- The code generates and saves images that you can find in the working directory

## Local Files and Descriptions

*   `img/`: Contains visualizations related to the seminar:
    *   `phase_portrait.png`: A plot showing the phase portrait for the system under bang-bang control.
    *   `bang_bang_simulations.png`: Shows multiple simulation trajectories for different initial conditions or parameters.
    *   `full_solution.gif`: An animated GIF demonstrating the evolution of the system state or the solution across the phase plane.
*   `src/`: Contains supplementary code:
    *   `plot_generator.py`: Python script used to generate trajectories or plots related to bang-bang control (the source for some images in `img/` or the Colab notebook).
    *   `random_trajectories.pkl`: A pickle file containing pre-generated trajectory data, used by `plot_generator.py` or the Colab notebook.
