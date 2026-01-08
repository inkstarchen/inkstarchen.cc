!!! note "**一阶优化条件(First order optimality conditions)**"
    令$x*$是一个可微函数$f(x)$的局部最小点，则$\nabla f(x^*)=0$

!!! info "Definition |  凸集(Convex Set)"
    A set $Q \subset \mathbb{R}^n is called **convex** if for any $x,y\in Q$ and $\alpha$ from $[0,1]$ we have 

    $$\alpha x + (1 - \alpha) y \in Q$$

> 包含x - y整段

!!! info "Definition |  凸函数(Convex Function)"
    A continuously differentiable function $f(x)$ is called **convex** on a convex set $Q$ ($f \in \mathcal{F}(Q)$) if for any $x,y \in Q$ we have 

    $$f(y) \geq f(x) + \langle \nabla f(x), y - x \rangle.$$

> 如果 $-f(x)$ 是凸的，我们称$f(x)$为凹的(**concave**)

!!! info "等价定义1"
    A continuously differentiable function $f$ belongs to the class $\mathcal{F}^1(Q) if and only if for any $x,y \in Q$ and $\alpha \in [0,1]$ we have

    $$f(\alpha x + (1-\alpha)y) \leq \alpha f(x) + (1- \alpha)f(y).$$

!!! info "等价定义2"
    A continuously differentiable function $f$ belongs to the class $\mathcal{F}^1(Q)$ if and only if for any $x, y \in Q$ we have

    $$\langle \nabla f(x) - \nabla f(y), x - y \rangle \geq 0.$$

!!! info "等价定义3"
    Let $Q$ be an open set. A twice continuously differentiable function $f$ belongs to the class $\mathcal{F}^2(Q)$ if and only if for any $x \in Q$ we have

    $$\nabla^2 f(x) \geq 0.$$

> 有意思的换元 $x_\tau = x + \tau (y-x)$

### 凸函数的性质

!!! note "性质 1"
    If $f \in \mathcal{F}^1(\mathbb{R}^n)$ and $\nabla f(x*) = 0$ then $x*$ is the global minimum of $f(x)$ on $\mathbb{R}^n$. 

>**引理1: Conic Combination**

> If $f_1$ and $f_2$ belong to $\mathcal{F}^1(Q)$ and $\alpha, \beta \geq 0$, then the function $f = \alpha f_1 + \beta f_2$ also belongs to $\mathcal{F}^1(Q)$.

>**引理2: Affine Composition**

> If $f \in \mathcal{F}^1(Q) , b \in \mathbb{R}^n$ and $A: \mathbb{R}^n \to \mathbb{R}^m$ then

> $$\phi(x) = f(Ax + b)\in \mathcal{F}^1(\hat{Q}), \hat{Q} = \{x\in \mathbb{R}^n : Ax + b \in Q\}$$


>**引理3: 逐点上确界(Pointwise maximum and supremum)**

> If $f_i(x), i \in I$, are convex, then

> $$g(x) = \underset{x \in I}{max} f_i(x)$$

>**引理4: 凸单调组合(Convex Monotone Combination)**

> **Scalar:** If $f$ is a convex function on $\mathbb{R}^n$ and $F(\cdot)$ is a convex and non-decreasing  function on $\mathbb{R}$, then $g(x) = F(f(x))$ is convex

> **Vector:** If $f_i, i=1, \dots, m$ are convex functions on $\mathbb{R}^n$ and $F(y_1, \dots, y_m)$ is convex and non-decreasing(component-wise) in each argument, then

> $$g(x) = F(f_1(x), \dots, f_m(x))$$

> is convex

>**引理5: Partial minimization**

> If $f(x,y)$ is convex in $(x,y) \in \mathbb{R}^n$ and $Y$ is a convex set, then

> $$g(x) = \underset{y \in Y}{inf} f(x,y)$$

> is convex
