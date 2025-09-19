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
