> 优化问题在整体上不可解

理论解释了我们能对优化问题做什么，不能做什么

Part1 Chaps 1-4 Black-Box model of optimization problem

## General Formulation of the Problem
- $x = (x^{(1)},\dots,x^{(n)})^T \in R^n$
- $f_0(\cdot),\dots,f_m(\cdot)$ 是定义在t $Q \subseteq R^n$上的一些实值函数
- general minimization problem:

$$ min\quad f_0(x),$$
$$s.t. \quad f_j(x)\&0,\quad j=1\dots m,$$
$$x\in Q$$
- $\&$ 可以是$\leq,\geq,$或$=$
- 我们将$f_0(\cdot)$称为问题的目标函数(objective function)

$$f(x)=(f_1(x),\dots,f_m(x))^T$$

称为**函数约束向量（vector of funtional constraints）**,并且集合$Q$被称为**基本可行集(basic feasible set)**

$$\mathcal{F}=\{x\in Q | f_j(x) \leq 0, j=1\dots m$$

被称为问题的可行集（以上以最小化问题为例）

**对于最小化问题的类型，存在一个自然的分类：**

- **有约束问题(constrained problems)**:$\mathcal{F} \subsetneq R^n$
- **无约束问题(unconstrained problems):**$\mathcal{F} = R^n$
- **光滑问题(smooth problems):** 所有的$f_j(x)$都是可微的（differentiable）
- **非光滑问题(nonsmooth problems)：** 存在不可微(nondifferentiable)的分量$f_k(x)$
- **线性约束问题（linearly constrained problems):** 所有泛函约束是线性的。进一步划分：
	- **线性优化问题：** 如果$f_0(x)$也是线性的，那么就是**线性优化问题**
	- **二次优化问题：** 如果$f_0(x)$是二次的，那么就是**二次优化问题**
	- **二次约束的二次问题：** 如果所有$f_j$是二次的，那么就是一个**二次约束的二次问题(quadratically constrained quadratic problem)**

**基于可行集属性的分类法：**

- 问题称为**可行的(feasible)**，如果$\mathcal{F} \neq \emptyset$
- 问题称为**严格可行的(strictly feasible)**，如果存在$x \in \mathcal{F}$,对于所有不等式约束满足$f_j(x) < 0$  (或者 $>0$)，对于所有等式约束满足$f_j(x)=0$ (Sater condition)

**区分解的不同类型：**

- $x^*$称为问题的优化**全局解(global solution)**，如果对于所有的$x \in \mathcal{F}$,有：

$$f_0(x^*) \leq f_0(x)$$

在这种情况下，$f_0(x^*)$称为问题的（全局）**最优值**(optimal value)

- $x^*$ 称为问题的**局部解**（local solution）,如果对于所有的$x \in NBR(x^*,\delta)\cap \mathcal{F}$,有：

$$f_0(x^*) \leq f_0(x)$$


### 优化问题的例子

#### Example 1.1.1

- 类比：计划的开销，资源的需求数量，或者系统的可靠性

令$x^{(1)},\dots,x^{(n)}$作为我们的**设计变量**(design variables)，我们可以固定一些决策的泛函特征:$f_0(x),\dots,f_m(x)$。将最重要的特征$f_0$作为我们的目标函数.对其它的特征做一些边界约束$a_j \leq f_j(x) \leq b_j$，就得到了一个优化问题

$$\underset{x\in Q}{min}\; f_0(x),$$
$$s.t.\; a_j\leq f_j(x)\leq b_j,\; j\; = \;1\dots m.$$
其中$Q$代表结构约束(structural constraints)，例如非负性，变量的界限.

#### Example 1.1.2
或者初始问题如下：
$$Find \;x\in \mathcal{R}^n \;such\; that\; f_j(x)=a_j,\;j= 1\dots m$$

其中$a_j \in \mathcal{R}, \; j=1\dots m.$ 然后我们就能够考虑这样的问题：

$$\underset{x\in \mathcal{R}^n}{min}\; \overset{m}{\underset{j=1}{\sum}}(f_j(x)-a_j)^2$$
如果后面问题的优化值为0，则我们说此问题有解。
在非线性分析中，这类问题是普遍存在的。

#### Example 1.1.3

有时候我们的决策变量$x^{(1)},\dots x^{(n)}$必须是整数，这可以 用如下约束来描述：

$$sin(\pi x^{(i)}) = 0, \quad i = 1\dots n.$$
因此我们能够得到整数优化问题：
$$\underset{x \in Q}{min} \; f_0(x),$$
$$s.t. \; a_j \leq f_j(x) \leq b_j, \;j= 1\dots m$$
$$sin(\pi x^{(i)} ) = 0, \; i = 1 \dots n.$$
### 数值方法的性能

我们无法说出解决一个特定问题的最佳方法，考虑一个答案为$x^*=0$ 的问题$\mathcal{P}$，那么一个永远返回$0$的方法在这个问题上的性能是无可比拟的，但是它无法解决其它有特定答案的问题。

但是我们能够寻找对特定一类的问题$\mathcal{P} \in P$的最佳解决方案。

- 因此一个方法$\mathcal{M}$在一类问题上的性能是其效率的自然特征

假设方法$\mathcal{M}$没有一个特定问题$\mathcal{P}$的完整信息，问题其已知部分被称为此问题的一个**模型**,用$\Sigma$表示。

- 为识别并解决问题$\mathcal{P}$，所搜集数据的过程被称为一个 **oracle**$\mathcal{O}$，是一个单位. 回答方案的连续询问。

固定$\Sigma$和$\mathcal{O}$。我们就能定义$\mathcal{M}$在$(\Sigma,\mathcal{O})$上的性能为在其最差的问题$\mathcal{P}_w$上的性能.

- $\mathcal{M}$在$\mathcal{P}$上的性能是方法$\mathcal{M}$求解问题$\mathcal{P}$所需的计算花费(computational efforts)的总量。

- 求解问题代表找到一个$\mathcal{P}$的准确的为$\epsilon > 0$的逼近解
- 停止准则记为$\mathcal{J}_\epsilon$

这样一来我们就有了对一个问题类的描述

$$\mathcal{P} \equiv (\Sigma, \mathcal{O}, \mathcal{J}_\epsilon)$$
### 普遍迭代过程

- 输入：初始点$x_0$和准确度$\epsilon > 0$
- 初始化：设置$k = 0$，初始信息集$I_{-1} = \emptyset$

**主循环：**
1. 在$x_k$调用$oracle \mathcal{O}$
2. 更新信息集：$I_k = I_{k-1} \cup (x_k , \mathcal{O}(x_k))$
3. 对$I_k$运用方法$\mathcal{M}$的规则，形成点$x_{k+1}$
4. 检查停止条件$\mathcal{J}_\epsilon$.如果满足，则形成输出$\bar{x}$，否则设置$k:=k+1$且转到步骤1

#### 定义复杂度
- **解析复杂度**(analytical complexity)：求解问题$\mathcal{P}$，达到准确率$\epsilon$，所需要调用$oracle$的数量
- **算数复杂度**（arithmetical complexity）：求解问题$\mathcal{P}$，达到准确率$\epsilon$，所需要的算术操作的总数量(包括$oracle$和方法的工作)

#### 求解复杂度

对于$oracle$，有一个标准的假设，让我们能得到优化问题解析复杂度的大部分结果。这个假设称为**局部黑盒概念**(local black box concept)

- 一个数值方法唯一可获得的信息是$oracle$的回答
- $oracle$是局部的，问题再离测试点$x$足够远处的微小变化，只要是与问题类的描述兼容的，不会改变在$x$处的答案.

标准形式(1.1.1)称为优化问题的一个泛函模型。通常对于这样的模型，标准的假定和函数分量的光滑性相关。根据光滑程度的不同，我们可以使用不同类型的$oracle$

- 零阶$oracle$（zero-order oracle）:
	- 返回$f(x)$的值
- 一阶$oracle$（first-order oracle）：
	- 返回$f(x)$和梯度$\nabla f(x)$的值
- 二阶$oracle$（second-order oracle）：
	- 返回$f(x)$，梯度$\nabla f(x)$，和 Hessian$\nabla^2 f(x)$的值
## 全局优化的复杂度界限

我们考虑下面一个问题：

$$\underset{x\in \mathcal{B_n}}{min} \; f(x).$$
这是一个没有泛函约束的有约束最小化问题。其基本可行集是$\mathcal{B}_n$ ，即一个$\mathcal{R}^n$上的$n$维盒子:

$$\mathcal{B}_n = \{x \in \mathcal{R}^n | 0 \leq x^{(i)} \leq 1, i = 1, \dots n\}.$$

我们用范数$\mathcal{l}_\infty$ 来测量$\mathcal{R}^n$中的距离

$$||x||_\infty = \underset{1 \leq i \leq n}{max}|x^{(i)}|.$$
假设，对于这个范数，目标函数$f(x)$在$\mathcal{B}_n$上是Lipschitz连续的(Lipschitz continuous)：

$$|f(x) - f(y)| \leq L||x-y||_\infty, \forall x, y \in \mathcal{B}_n$$
其中$L$是某个Lipschitz常量 （Lipschitz constant）

考虑一个简单解决方法 Uniform Grid Method.

- 方法$\mathcal{G}(p)$, $p \geq 1$
- 构造$(p+1)^n$个点 $x_{(i_1,\dots, i_n)}=(\frac{i_1}{p},\frac{i_2}{p},\dots,\frac{i_n}{p})$ 其中$(i_1,\dots,i_n) \in \{0, \dots, p\}^n$
- 在所有点$x_(i_1,\dots, i_n)$中，找到点$\bar{x}$,具有最小的目标函数值
- 返回结果$(\bar{x},f(\bar{x}))$

**Theorem 1.1.1**

令$f^*$是问题(1)的全局最优值。那么

$$f(\bar{x}) - f^* \leq \frac{L}{2p}$$**proof**：参考原书 P11 或 PPT

我们将这个问题总结成一个问题类：我们的目标是

$$Find \; \bar{x} \in \mathcal{B}_n : \quad f(\bar{x}) - f^* \leq \epsilon$$

**Corollary 1.1.1**

对于由上述问题、假设构成的问题类，方法$\mathcal{G}$的分析复杂度最多是

$$\mathcal{A}(\mathcal{G}) = (\lfloor \frac{L}{2\epsilon}\rfloor + 1)^n$$
**proof：** 具体查看PPT或原书
- 取 $p$ 值，使得问题类被解决
- 分析方法所用开销, 根据需要取$p = \lfloor \frac{L}{2\epsilon} \rfloor + 1$，一共构造并计算了$p^n$个点

我们仍然需要确定这问题类的下界

**resisting oracle**:
- 从一个空函数开始，试图用最坏可能的方式回答这个方法的每一个调用
- 这个回答必须和前面的回答以及问题类的描述兼容

为了弄明白resisting oracle如何工作，考虑如下一个问题类$\mathcal{l}$

- 模型: $\underset{x \in \mathcal{B}_n}{min} f(x),$ $f(x)$在$\mathcal{B}_n$上是$l_\infty$Lipschitz连续的
- Oracle：零阶局部黑盒
- 逼近解：寻找$\bar{x} \in \mathcal{B}_n: f(\bar{x}) -f^* \leq \epsilon$

**Theorem 1.1.2**
对于零阶方法，要取得$\epsilon$精度（这里$\epsilon < \frac{1}{2}L$),则$l$的解析复杂度至少为$(\lfloor \frac{L}{2\epsilon} \rfloor)^n$

**proof:** 具体见ppt或原书P13
