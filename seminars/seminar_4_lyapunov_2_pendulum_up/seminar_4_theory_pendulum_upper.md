# Lyapunov Stability Analysis of Pendulum in Upper Equilibrium Position

Consider the equation of a mathematical pendulum without friction with a control input $a(t)$:
$$
\ddot{\theta} + \sin(\theta) = a(t)
$$
where $\theta$ is the angle of deviation from the vertical. We assume that the constants (acceleration due to gravity $g$ and pendulum length $L$) are equal to one.

## Upper Equilibrium Position

The upper unstable equilibrium position corresponds to $\theta = \pi$ and $\dot{\theta} = 0$. Our goal is to stabilize this position using linear feedback.

## Linear Feedback for Stabilization

Introduce control based on the deviation from the target state $(\pi, 0)$ and the angular velocity:
$$
a(t) = k_1 (\theta - \pi) + k_2 \dot{\theta}
$$
where $k_1$ and $k_2$ are feedback coefficients.

Substituting this control into the pendulum equation, we get the closed-loop system:
$$
\ddot{\theta} + \sin(\theta) = k_1 (\theta - \pi) + k_2 \dot{\theta}
$$

## System in State Space

Let the state vector be $s = [s_1, s_2]^T = [\theta, \dot{\theta}]^T$. The system of first-order equations is:
$$
\begin{cases}
\dot{s}_1 = s_2 \\
\dot{s}_2 = -\sin(s_1) + k_1 (s_1 - \pi) + k_2 s_2
\end{cases}
$$
The equilibrium point of interest is $s_e = [\pi, 0]^T$.

## Stability Analysis by Lyapunov's First Method (Linearization)

Linearize the system around the equilibrium point $s_e = [\pi, 0]^T$.
Let $f(s) = \begin{bmatrix} s_2 \\ -\sin(s_1) + k_1 (s_1 - \pi) + k_2 s_2 \end{bmatrix}$.
The Jacobian matrix $A = \frac{\partial f}{\partial s} \bigg|_{s_e}$ is:
$$
A = \begin{bmatrix} \frac{\partial f_1}{\partial s_1} & \frac{\partial f_1}{\partial s_2} \\ \frac{\partial f_2}{\partial s_1} & \frac{\partial f_2}{\partial s_2} \end{bmatrix} \bigg|_{s_1=\pi, s_2=0}
= \begin{bmatrix} 0 & 1 \\ -\cos(s_1) + k_1 & k_2 \end{bmatrix} \bigg|_{s_1=\pi, s_2=0}
$$
$$
A = \begin{bmatrix} 0 & 1 \\ -\cos(\pi) + k_1 & k_2 \end{bmatrix}
= \begin{bmatrix} 0 & 1 \\ -(-1) + k_1 & k_2 \end{bmatrix}
= \begin{bmatrix} 0 & 1 \\ 1 + k_1 & k_2 \end{bmatrix}
$$
The characteristic equation is $\det(A - \lambda I) = 0$:
$$
\det \begin{bmatrix} -\lambda & 1 \\ 1 + k_1 & k_2 - \lambda \end{bmatrix} = (-\lambda)(k_2 - \lambda) - (1 + k_1) = \lambda^2 - k_2 \lambda - (1 + k_1) = 0
$$
For asymptotic stability of the linearized system (all eigenvalues $\lambda$ have negative real parts), according to the Routh-Hurwitz criterion, it is necessary and sufficient that all coefficients of the characteristic polynomial $P(\lambda) = \lambda^2 - k_2 \lambda - (1 + k_1)$ are positive (with the leading coefficient being 1):
1.  $-k_2 > 0 \implies k_2 < 0$
2.  $-(1 + k_1) > 0 \implies 1 + k_1 < 0 \implies k_1 < -1$

Thus, the linearized system is stable if $k_1 < -1$ and $k_2 < 0$. By Lyapunov's first method, under these conditions, the nonlinear system is also asymptotically stable in the vicinity of the equilibrium point $(\theta, \dot{\theta}) = (\pi, 0)$.

### Damping Characteristics

The nature of the convergence to the equilibrium point depends on the roots $\lambda_{1,2} = \frac{k_2 \pm \sqrt{k_2^2 + 4(1 + k_1)}}{2}$.
- **Overdamped:** If the discriminant $k_2^2 + 4(1 + k_1) > 0$, the roots are real, distinct, and negative. The system returns to equilibrium without oscillations.
- **Critically Damped:** If the discriminant $k_2^2 + 4(1 + k_1) = 0$, the roots are real, equal, and negative ($\lambda = k_2/2$). This provides the fastest return to equilibrium without oscillation. This condition is met when $k_2 = -2\sqrt{-(1 + k_1)}$ (given $k_1 < -1$ ensures the term under the square root is positive and $k_2 < 0$).
- **Underdamped:** If the discriminant $k_2^2 + 4(1 + k_1) < 0$, the roots are complex conjugates with negative real parts. The system oscillates with decreasing amplitude as it returns to equilibrium.

For the specific case of **critical damping**, the relationship $k_2^2 = -4(1+k_1)$ must hold.

## Stability Analysis by Lyapunov's Second Method (Direct Method)

Let's confirm the result using Lyapunov's direct method. We need a Lyapunov function $L(\theta, \dot{\theta})$ that is positive definite around the equilibrium point $(\pi, 0)$ and whose time derivative is negative semi-definite.

Consider a candidate function based on the system's energy, shifted to have its minimum at $\theta = \pi$ and modified by the control terms. A suitable Lyapunov function is:
$$
L(\theta, \dot{\theta}) = \frac{1}{2} \dot{\theta}^2 - \cos(\theta) - \frac{1}{2} k_1 (\theta - \pi)^2 - 1
$$
Note: This form can be derived by considering the potential energy associated with the effective restoring force $-\sin(\theta) + k_1(\theta-\pi)$ and adding the kinetic energy. The constant term `-1` ensures $L(\pi, 0) = 0$.

Let's check properties around $(\pi, 0)$: 
- **Value at equilibrium:**
  $$
  L(\pi, 0) = \frac{1}{2}(0)^2 - \cos(\pi) - \frac{1}{2} k_1 (\pi - \pi)^2 - 1
  $$
  $$
  L(\pi, 0) = 0 - (-1) - 0 - 1 = 0
  $$
  The function is zero at the equilibrium point.

- **Positive definiteness:** We need to show $L(\theta, \dot{\theta}) > 0$ for $(\theta, \dot{\theta})$ near $(\pi, 0)$ but not equal to it. Let $\theta = \pi + \delta$, where $\delta$ is a small deviation.
  Substituting into $L$:
  $$
  L(\pi+\delta, \dot{\theta}) = \frac{1}{2} \dot{\theta}^2 - \cos(\pi + \delta) - \frac{1}{2} k_1 (\pi + \delta - \pi)^2 - 1
  $$
  $$
  L(\pi+\delta, \dot{\theta}) = \frac{1}{2} \dot{\theta}^2 + \cos(\delta) - \frac{1}{2} k_1 \delta^2 - 1
  $$
  Using the Taylor expansion for $\cos(\delta) \approx 1 - \frac{\delta^2}{2}$ for small $\delta$:
  $$
  L(\pi+\delta, \dot{\theta}) \approx \frac{1}{2} \dot{\theta}^2 + \left(1 - \frac{\delta^2}{2}\right) - \frac{1}{2} k_1 \delta^2 - 1
  $$
  $$
  L(\pi+\delta, \dot{\theta}) \approx \frac{1}{2} \dot{\theta}^2 - \frac{1}{2} \delta^2 - \frac{1}{2} k_1 \delta^2
  $$
  $$
  L(\pi+\delta, \dot{\theta}) \approx \frac{1}{2} \dot{\theta}^2 - \frac{1}{2}(1 + k_1) \delta^2
  $$
  This approximate form is a quadratic form in $\dot{\theta}$ and $\delta$. It is positive definite (and thus $L > 0$ near the equilibrium) if the coefficients are positive:
    - The coefficient $\frac{1}{2}$ for $\dot{\theta}^2$ is positive.
    - The coefficient $-\frac{1}{2}(1 + k_1)$ for $\delta^2$ must be positive. This requires $-(1 + k_1) > 0$, which simplifies to $1 + k_1 < 0$, or $k_1 < -1$.

  So, for $k_1 < -1$, the function $L(\theta, \dot{\theta})$ is positive definite in a neighborhood around $(\pi, 0).

Find the time derivative of $L$ along the system trajectories $\dot{s}_1 = s_2$, $\dot{s}_2 = -\sin(s_1) + k_1 (s_1 - \pi) + k_2 s_2$, where $s_1=\theta, s_2=\dot{\theta}$:
$$
\dot{L} = \frac{\partial L}{\partial \theta} \dot{\theta} + \frac{\partial L}{\partial \dot{\theta}} \ddot{\theta}
$$
$$
\frac{\partial L}{\partial \theta} = -(-\sin(\theta)) - \frac{1}{2} k_1 \cdot 2 (\theta - \pi) = \sin(\theta) - k_1 (\theta - \pi)
$$
$$
\frac{\partial L}{\partial \dot{\theta}} = \dot{\theta}
$$
$$
\ddot{\theta} = -\sin(\theta) + k_1 (\theta - \pi) + k_2 \dot{\theta}
$$
$$
\dot{L} = (\sin(\theta) - k_1 (\theta - \pi)) \dot{\theta} + \dot{\theta} (-\sin(\theta) + k_1 (\theta - \pi) + k_2 \dot{\theta})
$$
$$
\dot{L} = \dot{\theta} \sin(\theta) - k_1 (\theta - \pi) \dot{\theta} - \dot{\theta} \sin(\theta) + k_1 (\theta - \pi) \dot{\theta} + k_2 \dot{\theta}^2
$$
$$
\dot{L} = k_2 \dot{\theta}^2
$$
If $k_2 < 0$, then $\dot{L} = k_2 \dot{\theta}^2 \le 0$. The derivative is negative semi-definite.

### Why LaSalle's Principle? (Intuitive Explanation)

We found a Lyapunov function $L$ (like a modified energy) which never increases along trajectories ($\dot{L} \le 0$). This tells us the system is stable – it won't "run away" from the equilibrium $(\pi, 0)$.

But does it actually *go* to the equilibrium? The standard Lyapunov theorem doesn't guarantee this just from $\dot{L} \le 0$.

This is where LaSalle's principle helps. Think about it:
1.  The "energy" $L$ is always decreasing or staying constant.
2.  The system can't keep decreasing its energy forever if it's bounded. It must eventually settle down where the energy stops changing, i.e., where $\dot{L} = 0$.
3.  In our case, $\dot{L} = k_2 \dot{\theta}^2$, so $\dot{L} = 0$ happens whenever the velocity $\dot{\theta}$ is zero.
4.  **Crucial point:** Can the system just stop at *any* position where $\dot{\theta}=0$? No. It can only permanently stay in states where the dynamics allow it to remain static (or remain within the set where $\dot{\theta}=0$). This set of "allowable final states" within $\dot{L}=0$ is called the **largest invariant set**.
5.  LaSalle's principle formalizes this: trajectories converge to this largest invariant set within $\{ \dot{L} = 0 \}$.

By analyzing the system dynamics *only* within the set where $\dot{\theta}=0$, we find that the only state the system can actually "stay stuck" in is the equilibrium $(\pi, 0)$ itself. Therefore, even though $\dot{L}$ was zero along the whole $\dot{\theta}=0$ axis, the trajectories must converge specifically to $(\pi, 0)$, proving **asymptotic stability**.

---

Now, let's formally apply this principle to our system.
To prove asymptotic stability, we use LaSalle's invariance principle. Consider the set $E = \{ (\theta, \dot{\theta}) | \dot{L} = 0 \}$. This occurs when $k_2 \dot{\theta}^2 = 0$, which (for $k_2 < 0$) means $\dot{\theta} = 0$.
Find the largest invariant set $M$ contained in $E$. In $M$, we must have $\dot{\theta} = 0$ and the system dynamics must keep the state within $M$. If $\dot{\theta} = 0$, then $\ddot{\theta}$ must also be 0 for the state to remain in $M$. 
From the system equation:
$$
\ddot{\theta} = -\sin(\theta) + k_1 (\theta - \pi) + k_2 \dot{\theta} = -\sin(\theta) + k_1 (\theta - \pi) + k_2(0) = -\sin(\theta) + k_1 (\theta - \pi)
$$
We require $\ddot{\theta}=0$, which means:
$$
-\sin(\theta) + k_1 (\theta - \pi) = 0
$$

To find the invariant set within $E$ (where $\dot{\theta}=0$ and $\ddot{\theta}=0$), we analyze the condition $\ddot{\theta}=0$:
$$
-\sin(\theta) + k_1 (\theta - \pi) = 0
$$
Let's analyze the function $f(\theta) = -\sin(\theta) + k_1 (\theta - \pi)$:
1.  **Check the equilibrium point:**
    $$
    f(\pi) = -\sin(\pi) + k_1 (\pi - \pi) = -0 + k_1(0) = 0
    $$
    So, $\theta = \pi$ is indeed a solution.
2.  **Analyze the derivative:** Calculate the derivative of $f(\theta)$ to understand its behavior:
    $$
    f'(\theta) = \frac{d}{d\theta} (-\sin(\theta) + k_1 (\theta - \pi)) = -\cos(\theta) + k_1
    $$
3.  **Use the stability condition ($k_1 < -1$):** Since stability requires $k_1 < -1$, let $k_1 = -1 - \epsilon$ for some $\epsilon > 0$. Substitute this into the derivative:
    $$
    f'(\theta) = -\cos(\theta) + (-1 - \epsilon) = -(\cos(\theta) + 1) - \epsilon
    $$
4.  **Determine the sign of the derivative:** Since $\cos(\theta) \ge -1$, the term $\cos(\theta) + 1 \ge 0$. Therefore:
    $$
    f'(\theta) = -(\underbrace{\cos(\theta) + 1}_{\ge 0}) - \underbrace{\epsilon}_{> 0}
    $$
    This means $f'(\theta)$ is strictly negative ($f'(\theta) \le -\epsilon < 0$) for all $\theta$.
5.  **Conclusion about uniqueness:** Since $f(\pi) = 0$ and the derivative $f'(\theta)$ is always negative, the function $f(\theta)$ is strictly decreasing. This implies that $f(\theta) = 0$ has only one solution, which is $\theta = \pi$.

Therefore, the only state that satisfies both $\dot{\theta} = 0$ and $\ddot{\theta} = 0$ is $(\theta, \dot{\theta}) = (\pi, 0)$. This means the largest invariant set $M$ contained within $E = \{ (\theta, \dot{\theta}) | \dot{L} = 0 \}$ is the single point representing the equilibrium:
$$
M = \{ (\pi, 0) \}
$$

## Conclusion

By LaSalle's invariance principle, if the feedback coefficients $k_1 < -1$ and $k_2 < 0$ are chosen, then trajectories starting near the equilibrium point $(\theta, \dot{\theta}) = (\pi, 0)$ converge to this point. Thus, the upper equilibrium position is asymptotically stable under the linear feedback $a(t) = k_1 (\theta - \pi) + k_2 \dot{\theta}$ with the specified constraints on the coefficients. Choosing $k_2 = -2\sqrt{-(1 + k_1)}$ results in critical damping for the linearized system, providing the fastest non-oscillatory convergence. 