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

**重要概念**

1. encoding scheme $\leftrightarrow$ countable
2. problem $\leftrightarrow f:\{\0,1\}^* \rightarrow \{0,1\}^*$ 

- alphabet $\Sigma = \{0,1\},\Sigma^n = \Sigma \times \dots \times \Sigma$
- $= \{(a_1,a_2,\dots,a_n):a_i \in \Sigma \} \rightarrow a_1a_2\dots a_n$binary string of length $n$
- $\Sigma^2 = \{00, 01, 11,10\}.$
- $\Sigma^3 = \{000,001,\dots,111\}$
- $\Sigma^0 = \{e\} \rightarrow empty \quad string$
- $\Sigma^* = \Sigma^0 \cup\Sigma^1 \cup \Sigma^2 \cup\dots = \cup_{n\geq 0} \Sigma^n$

**concatenation** : $xy = a_1a_2\dots a_nb_1b_2\dotsb_n$

- $x$ is a prefix of $y$ if  $y=xz$ for some $z\in \Sigma^*$
- $x$ is a suffix  of $y$ if $y = zx$ for some $z\in \Sigma^*$

**Encoding**

- $E:A \rightarrow \{0,1\}^*$ one-to-one  $E(x)\neq E(x')$ if $x \neq x'.$

1. Natural numbers $N$

$$NtS(n) = \begin{cases}0 && if & n = 0 \\ 1 && if & n = 1 \\ NtS(\lfloor n/2 \rfloor)\cdotp parity(n) && if & n>1 \end{cases}$$

2. $N\times N$

- $E(1,6)=Nts(1)Nts(6)=1 \quad 110,E(3,2)=11 \quad 10.$
	- not one-to-one！$E(1)$ is a prefix of $E(3)$
- $E(1,6) \rightarrow 1,110 \rightarrow 11 \quad 01 \quad 111100$
- $0 \rightarrow 00; ,\rightarrow 01; 1 \rightarrow 11$
	- prefix-free encoding.

**prefix-free encoding**

$E:A\rightarrow\{0,1\}^*$ is prefix-free encoding if $E(x)$ is not a prefix of $E(x')$ for any $x\neq x'$.

**Lemma 1:**

- $E:A\rightarrow\{0,1\}^*$ is prefix-free encoding
- $\bar{E}(a_1,a_2,\dots,a_n) = \begin{cases}E(a_1)E(a_2)\dots E(a_n) && if & n \geq 1 \\ e && if & n = 0 \end{cases}$
- $\Rightarrow \bar{E}$ is one-to-one

**proof:**

$\exists(a_1,\dots,a_{k_a})\neq(b_1,\dots,b_{k_b})\in A^*$

$\bar{E}(a_1,\dots,a_{k_a}) = \bar{E}(b_1,\dots,b_{k_b})$

if $\exists a_i \neq b_i$ / if $a_i = b_i$ for $i=1,\dots,k_a$

**Lemma 2:**

- if $\exists$ one-to-one $E:A\rightarrow \{0,1\}^*$
- then $\exists$ prefix-free $E':A \rightarrow \{0,1\}^*$
- such that $|E'(a)| \leq 2 | E(a)| + 2$ fro any $a \in A$
- Furthermore $|E'(a)| \leq |E(a)| + O(log|E(A)|)$

**proof:**

$E(a) = 010 \rightarrow 00110001$
- $0\rightarrow 00$
- $1\rightarrow 11$
- append $01$

**Theorem**

if $\exists$ one-to-one $E:A\rightarrow \{0,1\}$

**Countable**

1. A is countable
2. A in finite or $\exists$ bijection $f:A\rightarrow N$
3. $\exists$ one-to-one $g:A\rightarrow N$
4. $\exists$ onto function $h:N\rightarrow A$

**inter proof:**

 $(2) \rightarrow (3)$ is trival
 $(3) \rightarrow (2)$ assume $A$ is infinite
 $\forall a \in A, f(a)=|\{a' \in A: g(a') < g(a)\}|$

**Lemma 3:** $\{0,1\}^*$ is countable

**proof:**
$\{0,1\}^0 \cup \{0,1\}^1 \cup \dots$

按从小到大顺序排列元素

$\forall x \in \{0,1\}^* f(x)=\begin{cases}0, && if & x =e \\ 2^{|x|} + StN(|x|) && if & |x| \geq 1 \end{cases}$

**Theorem:**

$A$ is countable if and only if $\exists$ one-to-one function $E:A\rightarrow\{0,1\}^*$

**Proof:**

- countable
- $\exists$ one-to-one $f:A\rightarrow N$
- $\exists$ bijection $g:N\rightarrow \{0,1\}^*$
- $\Rightarrow \exists$ one-to-one $h:A\rightarrow\{0,1\}^*$

> input must countable

**the number of problem is uncountable**

**proof:**

- $f:\{0,1\}^* \rightarrow \{0,1\}^*$
- $F=\{ f|f:N\rightarrow (0,1)\}$
- $g(i)=\begin{cases} 0, && f_i(i) = 1 \\ 1, && f_i(I) = 0 \end{cases} \quad f_i$ for any $i$
- $g\neq f_i$ for any $i$ but $g \in F$ 矛盾
