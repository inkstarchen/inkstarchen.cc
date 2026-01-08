

> 定长的输入输出, finite function $f:\{0,1\}^n \rightarrow \{0,1\}^m$

## **boolean circuit:**

> 布尔电路可以对应到一个函数，也可以对应到离散数学中的有向无环图(directed acyclic graph)

$AND(a,b) = \begin{cases} 1 && if a=b=1 \\ 0 && otherwise \end{cases}$

> 同样可以写出OR NOT 的表达式，进一步推出$XOR(a,b) = a + b \; mod \; 2$

$MAJ_3 (x_0, x_1,x_2) = \begin{cases} 1, && if \; x_1 + x_2 + x_3 \geq 2 \\ 0, && otherwise \end{cases}$

> 可用OR,AND模拟，任意两个为1

考虑一个**布尔电路的组成**，等效于一个有向无环图$G = (V,E)$: 定义电路的规模大小为 $|c| = s$

- $n$ inputs nodes: $x[0], \dots, x[n-1]$
    - 没有入边(no in-arc)， 不少于一个出边($\geq 1$ out-arc)
- $s$ gates:
    - $\land, \lor$ | 2 in-arc, 1 out-arc
    - $\lnot$ | 1 in-arc, 1 out-arc
- $m$ output nodes: $Y[0], \dots, Y[m-1]$

**符号化表示**

$$x \in \{0,1\}^n \; \begin{array}{c} x_0 \rightarrow x[0] \\ x_1 \rightarrow x[1] \\  \vdots \\ x_{n-1} \rightarrow x[n-1] \end{array} \rightarrow \begin{array}{c} Y[0] \\ Y[1] \\ \vdots \\ Y[m-1] \end{array}$$

- 电路记作：$C(x)$

于是我们可以用电路逻辑编写代码: `temp_1 = AND(x[0],x[1])` 

这称为 AON-CIRC program, 这是与布尔电路等价的编程语言

其代码规模定义为 $|P| = \#lines = s$


于是我们可以定义什么叫做 “AON-CIRC program $P$ to compute a function $f$”

!!! note "Definition | Computing a function via AON-CIRC programs"
    Let $f: \{0,1\}^n \rightarrow \{0,1\}^m$, and $P$ be a valid AON-CIRC program with $nn$ inputs and $m$ outputs. We say that $P$ computes $f$ if $P(x) = f(x)$ for every $x \in \{0,1\}^n$.

!!! note "**Theorem**|Equivalence of circuits and straight-line programs"

    A function $f$ is computable by a boolean circuit with $s$ gates if and only if it is computable by an AON-CIRC program with $s$ lines.



## **NAND circuit**

> 这是另一种极其有用的定义计算的函数

!!! note "Theorem | NAND computes AND,OR,NOT"
    - $NOT(a) = NOT(AND(a,a)) = NAND(a,a)$
    - $AND(a,b) = NAND(NAND(a,a),NAND(b,b))$
    - $OR(a,b) = NAND(NAND(a,b),NAND(a,b))$

$$\begin{array}{c} NAND  \; circuit \leftrightarrow boolean \; circuit \\ s \Rightarrow \leq 2s  \\ \leq 3s \Leftarrow s \end{array}$$

!!! note "Theorem | NAND is a universal operation"
    For every Boolean circuit $C$ of $s$ gates, there exists a NAND circuit $C'$ of at most $3s$ gates that computes the same function as $C$.

> **Big  Idea 3**

> Two models are equivalent in power if they can be used to compute the same set of functions.

目前为止我们有以下四个概念: 它们可以依次转换 

1. boolean circuit
2. AON-CIRC straight-line program
3. NAND-CIRC straight-line program 
4. NAND circuit

> 这些概念都是对于有限计算的模型, 我们的目的是定义计算.

!!! note "Definition | Universal function"
    We say that $\mathcal{F}$ is a universal set of operations (also known as a universal gate set) if there exists a $\mathcal{F}$ program to compute the function NAND


**Example:**

$\begin{cases} ONE(a,b) = 1 \\ ZERO(a,b)=0 \\ IF(a,b,c) = \begin{cases} b , & if \; a=1 \\ c, & if \; a = 0 \end{cases} \end{cases}$ is universal.

**Proof:**

$$NAND(a,b) = \begin{cases} 1, & if \; a= 0 \\ \begin{cases} 1, & if \; b = 0 \\ 0, & otherwise \end{cases} \end{cases}$$

$$NAND(a,b) = IF(a,IF(b,ZERO(a,b),ONE(a,b)), ONE(a,b))$$
