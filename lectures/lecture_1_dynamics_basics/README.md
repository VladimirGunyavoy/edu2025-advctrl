# Lecture 1: Basics of Dynamical Systems and Control

This directory contains materials for the introductory lecture on the basics of dynamical systems and control theory.

## Content Overview (`dynamical_systems_basics.md` / `.pdf`)

- **Control System Architecture:** Introduction to the main components of a control system (Controller, Plant) and the feedback loop concept (action, state, observation).
- **Plant Dynamics:**
    - Definition of system state ($s$).
    - State transition laws for discrete-time systems ($s_{t+1} = P(s_t, a_t)$).
    - Representation of continuous-time dynamics using differential equations ($\dot{s} = P(s, a)$).
    - Relationship between continuous and discrete dynamics via time discretization.
- **Lyapunov Function Analysis:**
    - Introduction to Lyapunov functions ($L(s)$) as a tool for stability analysis.
    - **Continuous Time:** Analyzing stability by examining the time derivative of the Lyapunov function ($\dot{L} = \langle \nabla_s L, \dot{s} \rangle$). A negative derivative indicates stability.
    - **Discrete Time:** Analyzing stability by examining the difference in the Lyapunov function between time steps ($\Delta L_t = L_{t+1} - L_t$). A negative difference indicates stability.

**Note:** The Markdown file (`dynamical_systems_basics.md` - *note the potential typo in the original filename*) is an automatically converted version of the original PDF (`dynamical_systems_basics.pdf`). Please refer to the PDF for definitive accuracy. 