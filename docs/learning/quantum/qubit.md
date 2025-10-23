
## 量子比特的表示

量子比特是状态的线性组合，这被称为**叠加态**

$$|\phi \rangle = \alpha | 0 \rangle + \beta | 1 \rangle$$

> 除了 $|0\rangle$ 和 $|1\rangle$ 可以作为量子态的基矢态，任意两个正交归一的基向量都可以作为量子态的基矢态。

#### **例如**

另一组常用的正交归一基定义为 $|+\rangle$ 态和 $|-\rangle$ 态：

$$
|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)
$$

$$
|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)
$$

$|0\rangle$ 态和 $|1\rangle$ 态作为一组正交归一基，可以表示为向量形式：

$$
|0\rangle = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad |1\rangle = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

利用这个定义，$|+\rangle$ 态和 $|-\rangle$ 态也可以表示为向量形式：

$$
|+\rangle = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad |-\rangle = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle
$$

可以表示任一量子态，其向量形式表示为：

$$
|\psi\rangle = \begin{bmatrix} \alpha \\ \beta \end{bmatrix}
$$

在该式中，$\alpha$ 和 $\beta$ 被称为**复系数**（有时被称为**振幅**），它们描述了**量子比特的叠加状态**。

用 $|\psi\rangle$ 表示一个列向量的表示法又称为 **Dirac 符号**或 **bra-ket 表示法**，其中 ket 表示**列向量**，bra 表示**行向量**。与之对应的 bra 为 $\langle \psi |$，且 $\langle \psi |$ 为 $|\psi\rangle$ 的共轭转置，即：$\langle \psi | = [\alpha^* \ \beta^*]$，其中 $\alpha^*、\beta^*$ 为 $\alpha、\beta$ 的共轭复数。

##  向量的内积和范数

两个向量的内积是一个标量，定义为 bra 向量和 ket 向量的矩阵乘积，对于 $|\psi\rangle$，有：

$$
\langle \psi | \psi \rangle = [\alpha^* \ \beta^*] \begin{bmatrix} \alpha \\ \beta \end{bmatrix} = |\alpha|^2 + |\beta|^2 = 1
$$

内积的更一般定义为：

$$
\langle a | = [a_0^*, a_1^*, \ldots, a_n^*], \quad | b \rangle = \begin{bmatrix} b_0 \\ b_1 \\ \vdots \\ b_n \end{bmatrix}, \quad \langle a | b \rangle = \sum_{i=0}^n a_i^* b_i
$$

如果两个向量的内积为 0，则称两个向量正交。与实数域向量中"模长"的概念一致，我们通过向量与自身的内积的开方，来定义向量的范数：

$$
\| | v \rangle \| \equiv \sqrt{\langle v | v \rangle}
$$


> 当我们观测量子态时，会发生量子态的坍缩，我们将以$|\alpha|^2$的概率得到 0 态， 以$|\beta|^2$的概率得到1态.

 对于处在态 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ 的量子比特，它处在 $|0\rangle$ 和 $|1\rangle$ 之间的连续状态中。但是我们无法通过检查量子比特来确定它的量子态，也就是 $\alpha$ 和 $\beta$ 的值；相反量子力学规定我们只能获得有关量子态的有限信息。**当我们测量量子态时，会发生量子态的坍缩（又称为量子态的投影）**，我们将以 $|\alpha|^2$ 的概率得到 0 态，以 $|\beta|^2$ 的概率得到 1 态，显然有：

$$
|\alpha|^2 + |\beta|^2 = 1
$$

这被称为**归一化条件**。因此，通常量子比特的状态是二维复向量空间中的单位向量，其向量表示必须满足以下性质：

1. 向量的各分量为复数；
2. 向量的范数为 1

## 量子比特的几何表示

$$
\left| \psi \right\rangle = \cos\left(\frac{\theta}{2}\right) \left| 0 \right\rangle + e^{i\varphi} \sin\left(\frac{\theta}{2}\right) \left| 1 \right\rangle
$$

$\theta$ 和 $\varphi$ 可以视为球坐标下的分量，且量子态的范数为 1，因此一个量子比特的量子态可以可视化为 Bloch 球上的一个点。

## 多量子比特

假设有两个量子比特，类似于两个经典比特有四种可能的状态，双量子比特的系统也有四个基本状态，依次为 $|00\rangle$、$|01\rangle$、$|10\rangle$、$|11\rangle$。一对量子比特可能是这四个基本态的其中一个，也可能是四个基本态的叠加，即：

$$
|\psi\rangle = \alpha_{00}|00\rangle + \alpha_{01}|01\rangle + \alpha_{10}|10\rangle + \alpha_{11}|11\rangle
$$

如果测量这个量子系统，那么将有 $|\alpha_x|^2$ 的概率结果为 $|x\rangle$ 态。由归一化条件可知：

$$
\sum_{x \in \{0,1\}^2} |\alpha_x|^2 = 1
$$

### **测量坍缩**

如果测量其中低位量子比特，那么将有

$$
|\alpha_{00}|^2 + |\alpha_{01}|^2
$$

的概率得到 0，经过测量之后状态坍缩为：

$$
|\psi' \rangle = \frac{\alpha_{00}|00\rangle + \alpha_{01}|01\rangle}{\sqrt{|\alpha_{00}|^2 + |\alpha_{01}|^2}}
$$

注意，测量后的态被因子 $\sqrt{|\alpha_{00}|^2 + |\alpha_{01}|^2}$ 归一化后仍然满足归一化条件。


在量子力学中，量子的状态由**希尔伯特空间（Hilbert spaces）** 中的单位向量来描述。

**本质上复合系统中量子态的演化也是矩阵的乘法，与单个子系统相比，只是多了张量积的运算。**

### 纠缠态的判断

$$
|\varphi\rangle = \alpha_{00}|00\rangle + \alpha_{11}|11\rangle
$$

> **纠缠态**：第一个比特测得为 0，那么第二个比特一定为 0；第一个比特测得为 1，那么第二个比特一定为 1。

---

$$
|\varphi\rangle = \alpha|00\rangle + \alpha|01\rangle = \alpha|0\rangle \otimes (|0\rangle + |1\rangle)
$$

> **非纠缠态**：第二个比特的状态与第一个比特的测量结果无关。

**纠缠判据：**

如果一个多量子比特系统可以分解为多个单量子比特的张量积，那么这个系统被称作无关的、可分的；反之，该系统是不可分的、纠缠的。例如，如果一个双量子比特系统的量子态为：

$$
\frac{1}{2} |00\rangle + \frac{i}{2} |01\rangle - \frac{1}{2} |10\rangle - \frac{i}{2} |11\rangle
$$

它实际上可以分解为两个单量子比特的张量积：

$$
\frac{1}{2} |00\rangle + \frac{i}{2} |01\rangle - \frac{1}{2} |10\rangle - \frac{i}{2} |11\rangle = \left( \frac{1}{\sqrt{2}} |0\rangle - \frac{1}{\sqrt{2}} |1\rangle \right) \otimes \left( \frac{1}{\sqrt{2}} |0\rangle + \frac{i}{\sqrt{2}} |1\rangle \right)
$$

这意味着这个双量子比特系统仅仅是两个量子比特简单合成的！
### 量子比特运算

若有两个量子比特分别处于如下的态：

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle , \quad |\phi\rangle = \gamma|0\rangle + \delta|1\rangle
$$

则两个量子比特的张量积为：

$$
\begin{aligned}
|\psi\rangle \otimes |\phi\rangle &= \alpha\gamma|0\rangle \otimes |0\rangle + \alpha\delta|0\rangle \otimes |1\rangle + \beta\gamma|1\rangle \otimes |0\rangle + \beta\delta|1\rangle \otimes |1\rangle \\
&= \alpha\gamma|00\rangle + \alpha\delta|01\rangle + \beta\gamma|10\rangle + \beta\delta|11\rangle
\end{aligned}
$$

若使用量子态的向量表示，则该过程表示为：

$$
|\psi\rangle = \begin{bmatrix} \alpha \\ \beta \end{bmatrix}, \quad
|\phi\rangle = \begin{bmatrix} \gamma \\ \delta \end{bmatrix}, \quad
|\psi\rangle \otimes |\phi\rangle = |\psi\phi\rangle = 
\begin{bmatrix}
\alpha \times \begin{bmatrix} \gamma \\ \delta \end{bmatrix} \\
\beta \times \begin{bmatrix} \gamma \\ \delta \end{bmatrix}
\end{bmatrix}
= \begin{bmatrix} \alpha\gamma \\ \alpha\delta \\ \beta\gamma \\ \beta\delta \end{bmatrix}
$$

### 重要的量子基态（贝尔态）

贝尔态是双量子比特系统中重要的纠缠态，它们的定义如下：

$$
\begin{align*}
\left| \phi^+ \right\rangle &= \frac{1}{\sqrt{2}} \left| 00 \right\rangle + \frac{1}{\sqrt{2}} \left| 11 \right\rangle, \\
\left| \phi^- \right\rangle &= \frac{1}{\sqrt{2}} \left| 00 \right\rangle - \frac{1}{\sqrt{2}} \left| 11 \right\rangle, \\
\left| \psi^+ \right\rangle &= \frac{1}{\sqrt{2}} \left| 01 \right\rangle + \frac{1}{\sqrt{2}} \left| 10 \right\rangle, \\
\left| \psi^- \right\rangle &= \frac{1}{\sqrt{2}} \left| 01 \right\rangle - \frac{1}{\sqrt{2}} \left| 10 \right\rangle
\end{align*}
$$

**John Stewart Bell** (1928 - 1990)

这四个贝尔态**都表示两个量子比特之间的纠缠**，它们构成的集合：

$$
\left\{ \left| \phi^+ \right\rangle , \left| \phi^- \right\rangle , \left| \psi^+ \right\rangle , \left| \psi^- \right\rangle \right\}
$$

被称为**贝尔基**；任何两个量子比特的量子态向量，都可以表示为四个贝尔态的线性组合。例如：

$$
|00\rangle = \frac{1}{\sqrt{2}} |\phi^+ \rangle + \frac{1}{\sqrt{2}} |\phi^- \rangle
$$