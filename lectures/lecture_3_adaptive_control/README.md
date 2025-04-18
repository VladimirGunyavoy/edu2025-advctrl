# Adaptive Control Basics

This directory contains materials related to the basics of Adaptive Control.

## Content Overview (`adaptive_control_basics.md` / `.pdf`)

- **Pendulum System Dynamics:** Introduction to the pendulum system as an example, including its state description, equations of motion with an unknown friction coefficient.
- **Energy Upswing Control:** Design of a control law based on energy and Lyapunov functions to swing the pendulum up. Highlights the problem of the unknown friction parameter.
- **Adaptive Control Approach:** Introduces the core idea of adaptive control using a certainty-equivalence approach. A complemented Lyapunov function is defined, incorporating an estimate of the unknown parameter.
- **Adaptation Law:** Derivation of the adaptation law for the parameter estimate ($\dot{\hat{C}}$) to ensure stability (negative semi-definite derivative of the complemented Lyapunov function).
- **General Formulation:** Extends the concept to a general control-affine system with unknown parameters, showing how to derive a general adaptation law using Lyapunov stability analysis.
- **Remarks:** Discusses the boundedness of estimates and state convergence, mentioning the Persistent Excitation (PE) condition often required for parameter convergence.

**Note:** The Markdown file (`adaptive_control_basics.md`) is an automatically converted version of the original PDF (`adaptive_control_basics.pdf`). Please refer to the PDF for definitive accuracy. 