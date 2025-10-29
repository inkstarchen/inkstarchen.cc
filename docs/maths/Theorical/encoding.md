

## Introduction


位-值 数字系统 是伟大的发明，拓展了我们表达的边界，它使我们能够表达极大的数量。

- 我们所日常使用以及在计算机中抽象使用的位-值数字系统是十进制。任何其它的位-值系统向十进制的转化实际上是由一个由乘法和加法组成的算法系统.

### Integer multiplication: an example of an algorithm

计算机的出现越发要求我们使用更加高效的算法

> 理论计算机科学关注算法与计算的固有性质。

### Extended Example: A faster way to multiply (optional)

Karatsuba multiplication 可以在$O(n^{log_23})$的复杂度下完成乘法运算.

$$(10\bar{x} + \underline{x}) \times (10\bar{y} + \underline{y}) = 100 \bar{x}\bar{y} + 10(\bar{x}\underline{y} + \underline{x}\bar{y}) + \underline{x}\underline{y}$$

> **Lemma 0.5**

> 对于任意非负整数$x,y$，当给定输入$x,y$ **Algorithm 0.4** 会输出$x\cdot y$

</br>


> **Lemma 0.6**

> 如果$x,y$是至多为 $n$ 位的整数，**Algorithm 0.4** 会在输入$x,y$上花费$O(n^{\log_23})$操作.

在此之后仍有很多的改进算法出现


### Algorithms beyond arithmetic

### On the importance of negative results

不可能的结果是世界的法则

## Computation and Representation

> 当谈论计算时，我们首先要区分**任务本身** 和 **任务的实现**

**首先聚焦于对计算任务的定义**

- 将所有的计算对象都抽象成01串

### Representing natrual numbers

为得到一个数字结构的表示，我们需要一个单射函数.

!!! note "**natural numbers to strings**"

	$$NtS(n) = \begin{cases}0 && if & n = 0 \\ 1 && if & n = 1 \\ NtS(\lfloor n/2 \rfloor)\cdotp parity(n) && if & n>1 \end{cases}$$

### Representations beyond natural numbers

> 没有所谓“正确”的表示，我们一直在寻找“最佳”的表示

!!! note "*Signed Magnitude Representation*"
	为表示集合 $\mathcal{Z} = \{ \dots, -3, -2, -1, 0, +1, +2, +3, \dots\}$有如下函数

	$$ZtS(m) = \begin{cases} 0 NtS(m) & m\geq 0 \\ 1 NtS(m) & m<0 \end{cases}$$

!!! note "*Twos Complement Representation*"
	为表示集合 $\mathcal{Z} = \{ -2^n, -2^n +1, \dots, 2^n - 1\}$有如下函数:

	$$ZtS_n(k) = \begin{cases} NtS_{n+1}(k) && 0 \leq k \leq 2^n - 1 \\ Nts_{n+1}(2^{n+1} + k) && -2^n \leq k \leq -1 \end{cases} ,$$

!!! note "Rational Numbers Representation"
	引入带分隔符的三元集合$\{00,11,01\} \subset \{0,1\}^2$,重复串确保数串可被识别.$0 \rightarrow 
	
	> 00; 分隔符\rightarrow 01; 1 \rightarrow 11$

	- 简单的字符串拼接：$E(1,6)$与$E(3,2)$ 不可分
		- 这是由于 $E(1)$ is a prefix of $E(3)$
	- 引入分隔符后的映射：$E(1,6) \rightarrow 1,110 \rightarrow 11 \; 01 \; 111100$

> **Big Idea 1**

> 如果我们能够将类型 $T$ 的对象表示为字符串，那么我们也能表示类型$T$的对象组成的元组.

!!! note "记号"
	我们将 $\{0,1\}^\infty$ 作为集合$\{f|f:\mathbb{N}\rightarrow \{0,1\}\}$ 的记号

> 由康托尔定理的推论：布尔函数的集合是不可数的.

!!! info "**Definition | 前缀和后缀**"

	$x$ is a prefix of $y$ if  $y=xz$ for some $z\in \Sigma^*$
	
	$x$ is a suffix  of $y$ if $y = zx$ for some $z\in \Sigma^*$

!!! info "Definition | Prefix free encoding"

	$E:A\rightarrow\{0,1\}^*$ is prefix-free encoding if $E(x)$ is not a prefix of $E(x')$ for any $x\neq x'$.

!!! note "Theorem | Prefix-free implies tuple encoding"
	$E:A\rightarrow\{0,1\}^*$ is prefix-free encoding

	$\bar{E}(a_0,a_1,\dots,a_n) = E(a_1)E(a_1)\dots E(a_n)$

!!! note "Lemma"
	如果 $\exists$ 单射 $E:A\rightarrow \{0,1\}^*$ 那么 $\exists$ prefix-free $E':A \rightarrow \{0,1\}^*$ 使得 $|E'(a)| \leq 2 | E(a)| + 2$ fro any $a \in A$

	进一步我们能够证明 $|E'(a)| \leq |E(a)| + O(log|E(A)|)$

- 可编码 $\leftrightarrow$ 可数

大部分问题可被抽象成01的输入和输出 $\leftrightarrow f:\{0,1\}^* \rightarrow \{0,1\}^*$ 

> **Big Idea 2**

> A function is not the same as a program. A program computes a function

!!! note "**一些记号**"
	- alphabet $\Sigma = \{0,1\},\Sigma^n = \Sigma \times \dots \times \Sigma$
	- $= \{(a_1,a_2,\dots,a_n):a_i \in \Sigma \} \rightarrow a_1a_2\dots a_n$binary string of length $n$
	- $\Sigma^2 = \{00, 01, 11,10\}.$
	- $\Sigma^3 = \{000,001,\dots,111\}$
	- $\Sigma^0 = \{e\} \rightarrow empty \quad string$
	- $\Sigma^* = \Sigma^0 \cup\Sigma^1 \cup \Sigma^2 \cup\dots = \cup_{n\geq 0} \Sigma^n$


**可数(Countable)条件**

1. A is countable
2. A in finite or $\exists$ bijection $f:A\rightarrow N$
3. $\exists$ one-to-one $g:A\rightarrow N$
4. $\exists$ onto function $h:N\rightarrow A$


!!! note "**Lemma**" 

	$\{0,1\}^*$ is countable

	**proof:**
	
	$\{0,1\}^0 \cup \{0,1\}^1 \cup \dots$

	按从小到大顺序排列元素

	$\forall x \in \{0,1\}^* f(x)=\begin{cases}0, && if & x =e \\ 2^{|x|} + StN(|x|) && if & |x| \geq 1 \end{cases}$

!!! note "**Theorem**"

	$A$ is countable if and only if $\exists$ one-to-one function $E:A\rightarrow\{0,1\}^*$


> **the number of problem is uncountable**

