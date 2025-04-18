# Introduction to Adaptive Control

## Pendulum System Dynamics

### Plant Description:
$$S = \begin{pmatrix} \theta \\ \dot{\theta} \end{pmatrix}, \quad a = \tau$$

Where:
- $\theta$ is the angle
- $\dot{\theta}$ is the angular velocity
- $\tau$ is the applied torque

### System Equations:
$$\dot{S}_1 = S_2$$
$\dot{S}_2 = -\frac{g}{l}\sin S_1 + \frac{a}{ml^2} - C S_2^2 \operatorname{sgn}(S_2)$

Where $C$ is an unknown friction coefficient.

Note: Physically, friction should dissipate energy (implying a '-' sign). Also note the change from $\alpha$ to $a$ representing the input torque compared to the initial formula.

### Energy Expressions:
$$E_{tot} = \underbrace{\frac{1}{2}ml^2S_2^2}_{E_{kin}} + \underbrace{mgl(1-\cos S_1)}_{E_{pot}}$$

$$E_{des} = 2mgl$$

Let's say $\bar{\tau}$ is the applied torque bound.

## Energy Upswing Control

1. Define Lyapunov function:
   $$L := \frac{1}{2}(E_{des} - E_{tot})^2$$
   
   Note:
   - $L = 0 \Rightarrow E_{tot} = E_{des}$ (which is our goal)
   - $L \geq 0$ always
   - We want $\dot{L} < 0$

2. Compute $\dot{L}$:
   $\dot{L} = (E_{des} - E_{tot})(-a S_2 + C ml^2|S_2|^3)$

   Detailed derivation:
   $$\begin{align}
   \dot{L} &= \frac{d}{dt}\left[\frac{1}{2}(E_{des} - E_{tot})^2\right] \\
   &= (E_{des} - E_{tot}) \cdot \frac{d}{dt}(E_{des} - E_{tot}) \\
   &= (E_{des} - E_{tot}) \cdot \left(\dot{E}_{des} - \dot{E}_{tot}\right) \\
   \end{align}$$

   Given that $E_{des} = 2mgl$ is a constant, $\dot{E}_{des} = 0$. Now let's calculate the derivative of $E_{tot}$:

   $$\begin{align}
   \dot{E}_{tot} &= \frac{d}{dt}\left[\frac{1}{2}ml^2S_2^2 + mgl(1-\cos S_1)\right] \\
   &= ml^2S_2\dot{S_2} + mgl\sin S_1 \cdot \dot{S_1} \\
   &= ml^2S_2\dot{S_2} + mgl\sin S_1 \cdot S_2 \\
   \end{align}$$

   Substituting the expression for $\dot{S_2}$ from the system equations (with the corrected sign):
   $$\begin{align}
   \dot{S_2} &= -\frac{g}{l}\sin S_1 + \frac{a}{ml^2} - C S_2^2 \operatorname{sgn}(S_2) \\
   \end{align}$$

   We get:
   $$\begin{align}
   \dot{E}_{tot} &= ml^2S_2\left(-\frac{g}{l}\sin S_1 + \frac{a}{ml^2} - C S_2^2 \operatorname{sgn}(S_2)\right) + mgl\sin S_1 \cdot S_2 \\
   &= -mglS_2\sin S_1 + aS_2 - Cml^2S_2^3\operatorname{sgn}(S_2) + mglS_2\sin S_1 \\
   &= aS_2 - Cml^2S_2^3\operatorname{sgn}(S_2) \\
   &= aS_2 - Cml^2|S_2|^3 \\
   \end{align}$$

   Now let's return to the derivative of the Lyapunov function:
   $$\begin{align}
   \dot{L} &= (E_{des} - E_{tot}) \cdot \left(0 - \dot{E}_{tot}\right) \\
   &= (E_{des} - E_{tot}) \cdot \left(-(aS_2 - Cml^2|S_2|^3)\right) \\
   &= (E_{des} - E_{tot})(-a S_2 + C ml^2|S_2|^3) \\
   \end{align}$$

### Control Design:
$a \leftarrow \bar{\tau}\operatorname{sgn}((E_{des}-E_{tot})S_2) + Cml^2|S_2|S_2$

Problem: $C$ is unknown!

## Adaptive Control Approach

The suggestion: Let's substitute the unknown $C$ in the designed control with some estimate $\hat{C}$.

We will try to find $\hat{C}$ in such a way that would make the whole closed loop stabilized.

### Core Idea of Adaptive Control:

Define a complemented Lyapunov function:
$$L_c := L + \frac{1}{2\alpha}(\hat{C} - C)^2$$

Where $\alpha$ is the learning rate.

This leads to certainty-equivalence control.

Computing $\dot{L}_c$:
$\dot{L}_c = (E_{des} - E_{tot})(-aS_2 + Cml^2|S_2|^3) + \frac{1}{\alpha}(\hat{C} - C)\dot{\hat{C}}$

Detailed derivation:
$$\begin{align}
\dot{L}_c &= \frac{d}{dt}\left[L + \frac{1}{2\alpha}(\hat{C} - C)^2\right] \\
&= \dot{L} + \frac{1}{\alpha}(\hat{C} - C)\frac{d}{dt}(\hat{C} - C) \\
&= \dot{L} + \frac{1}{\alpha}(\hat{C} - C)\dot{\hat{C}} \quad \text{(since $C$ is a constant)}\\
\end{align}$$

Substituting the already found expression for $\dot{L}$ (which now follows from the corrected $\dot{E}_{tot}$):
$$\begin{align}
\dot{L}_c &= (E_{des} - E_{tot})(-aS_2 + Cml^2|S_2|^3) + \frac{1}{\alpha}(\hat{C} - C)\dot{\hat{C}} \\
\end{align}$$

Denoting $\Delta E = (E_{des} - E_{tot})$ and $\Delta C = \hat{C} - C$:
$$\begin{align}
\dot{L}_c &= \Delta E \cdot (-aS_2 + Cml^2|S_2|^3) + \frac{1}{\alpha}\Delta C \dot{\hat{C}} \\
\end{align}$$

Let's substitute the control law $a = \bar{\tau}\operatorname{sgn}(\Delta E \cdot S_2) + \hat{C}ml^2|S_2|S_2$ into the expression:
$$\begin{align}
\dot{L}_c &= \Delta E \cdot \left[-(\bar{\tau}\operatorname{sgn}(\Delta E \cdot S_2) + \hat{C}ml^2|S_2|S_2)S_2 + Cml^2|S_2|^3\right] + \frac{1}{\alpha}\Delta C \dot{\hat{C}} \\
&= \Delta E \cdot \left[-\bar{\tau}\operatorname{sgn}(\Delta E \cdot S_2) S_2 - \hat{C}ml^2|S_2|^3 + Cml^2|S_2|^3\right] + \frac{1}{\alpha}\Delta C \dot{\hat{C}} \\
&= \Delta E \cdot (-\bar{\tau}\operatorname{sgn}(\Delta E \cdot S_2) S_2) + \Delta E ml^2|S_2|^3 (C - \hat{C}) + \frac{1}{\alpha}\Delta C \dot{\hat{C}} \\
&= -\bar{\tau}|\Delta E \cdot S_2| - \Delta E ml^2|S_2|^3 (\hat{C} - C) + \frac{1}{\alpha}\Delta C \dot{\hat{C}} \\
\end{align}$$

Note that $-\bar{\tau}|\Delta E \cdot S_2| \leq 0$, so the first term is always non-positive. Let's denote it as $\le 0$.

$$\begin{align}
\dot{L}_c &= \underbrace{-\bar{\tau}|\Delta E \cdot S_2|}_{\leq 0} - \Delta E ml^2|S_2|^3 \Delta C + \frac{1}{\alpha}\Delta C \dot{\hat{C}} \\
&= \underbrace{-\bar{\tau}|\Delta E \cdot S_2|}_{\leq 0} + \Delta C \left(-\Delta E ml^2|S_2|^3 + \frac{1}{\alpha}\dot{\hat{C}}\right) \\
\end{align}$$

### Adaptation Law

For cancellation of the uncertain terms, we choose:
$\dot{\hat{C}} := \alpha \Delta E ml^2|S_2|^3$

Note: The formula sign changed due to the correction in the friction term sign. With this adaptation law, the term in brackets becomes zero, leading to $\dot{L}_c = -\bar{\tau}|\Delta E \cdot S_2| \le 0$.

The complete closed-loop system:

![Closed Loop System](https://via.placeholder.com/400x150)

## General Formulation

### Plant Structure:
$$\dot{S} = f(S) + g(S)a$$

Control-affine form

### Disturbed Plant:
$$\dot{S} = f(S) + g(S)a + \gamma(S)C$$

Let's assume we designed a controller $\pi(S,C)$ for the disturbed plant (under known $C$) and showed that some $L$ was indeed a Lyapunov function for the closed loop:

$$\dot{L} = \mathcal{L}_f L + \mathcal{L}_g L \pi(S,C) - \mathcal{L}_{\gamma} L C \leq -K_d(\|S\|), \forall C$$

Note: The sign of the $\mathcal{L}_{\gamma} L C$ term (here '-') depends on the specific system dynamics and the choice of $L$. It is chosen here to be consistent with the corrected pendulum example where the corresponding term $-Cml^2|S_2|^3$ appeared with a '-' sign in $\dot{E}_{tot}$.

For the disturbed plant under unknown $C$, take a complemented Lyapunov function:

$$L_c := L + \frac{1}{2\alpha}(\hat{C} - C)^2$$ 

(Assuming scalar $C$ for simplicity, matching the original notation)

Processing it (using corrected $\dot{L}$ structure):
$$\begin{align}
\dot{L}_c &= \dot{L}|_{a=\pi(S,\hat{C})} + \frac{1}{\alpha}(\hat{C} - C)\dot{\hat{C}} \\
&= \mathcal{L}_f L + \mathcal{L}_g L \pi(S,\hat{C}) - \mathcal{L}_{\gamma} L C + \frac{1}{\alpha}\Delta C \dot{\hat{C}} \\
&= (\mathcal{L}_f L + \mathcal{L}_g L \pi(S,\hat{C}) - \mathcal{L}_{\gamma} L \hat{C}) + \mathcal{L}_{\gamma} L \hat{C} - \mathcal{L}_{\gamma} L C + \frac{1}{\alpha}\Delta C \dot{\hat{C}} \\
\end{align}$$
Applying Certainty Equivalence assumption: $\mathcal{L}_f L + \mathcal{L}_g L \pi(S,\hat{C}) - \mathcal{L}_{\gamma} L \hat{C} \leq -K_d(\|S\|)$
$$\begin{align}
\dot{L}_c &\leq -K_d(\|S\|) + \mathcal{L}_{\gamma} L \hat{C} - \mathcal{L}_{\gamma} L C + \frac{1}{\alpha}\Delta C \dot{\hat{C}} \\
&= -K_d(\|S\|) + \mathcal{L}_{\gamma} L (\hat{C} - C) + \frac{1}{\alpha}\Delta C \dot{\hat{C}} \\
&= -K_d(\|S\|) + \Delta C (\mathcal{L}_{\gamma} L + \frac{1}{\alpha}\dot{\hat{C}}) \\
\end{align}$$

To achieve cancellation, we set:
$\dot{\hat{C}} = -\alpha \mathcal{L}_{\gamma} L$

Note the negative sign in the adaptation law, which ensures cancellation based on the assumption $\mathcal{L}_{\gamma} L C$ term has a negative sign in the $\dot{L}$ expression used in this general formulation.

## Remarks:
- We can show boundedness of $\hat{C}$ and convergence of $S$ (e.g., towards a small set around 0).
- Convergence $\hat{C} \rightarrow C$ is not guaranteed in general and typically requires a Persistent Excitation (PE) condition on the system trajectories.

![Parameter Estimation](https://via.placeholder.com/300x100)