finite function $f:\{0,1\}^n \rightarrow \{0,1\}^m$

> 定长的输入输出

**boolean circuit:**

> 布尔电路可以对应到一个函数，也可以对应到离散数学中的有向无环图(directed acyclic graph)

$AND(a,b) = \begin{cases} 1 && if a=b=1 \\ 0 && otherwise \end{cases}$

> 同样可以写出OR NOT 的表达式，进一步推出XOR

$MAJ_3 (x_0, x_1,x_2) = \begin{cases} 1, && if \; x_1 + x_2 + x_3 \geq 2 \\ 0, && otherwise \end{cases}$

考虑一个**布尔电路的组成**: 定义电路的规模大小为 $|c| = s$

- $n$ inputs nodes: $x[0], \dots, x[n-1]$
    - 没有入边(no in-arc)， 不少于一个出边($\geq 1$ out-arc)
- $s$ gates:
    - $\land, \lor$ | 2 in-arc, 1 out-arc
    - $\lnot$ | 1 in-arc, 1 out-arc
- $m$ output nodes: $Y[0], \dots, Y[m-1]$

**符号化表示**

$$x \in \{0,1\}^n \; \begin{array}{c} x_0 \rightarrow x[0] \\ x_1 \rightarrow x[1] \\  \vdots \\ x_{n-1} \rightarrow x[n-1] \end{array} \rightarrow \begin{array}{c} Y[0] \\ Y[1] \\ \vdots \\ Y[m-1] \end{array}$$

- 电路记作：$C(x)$

$C$ computes a function $f:\{0,1\}^n \rightarrow \{0,1\}^m$ if for every $x \in \{0,1\}^n \; c(x) = f(x)$

于是我们可以用电路逻辑编写代码: `temp_1 = AND(x[0],x[1])` 

这称为 AON-CIRC program:其代码规模定义为 $|P| = \#lines = s$

**Theorem**

A function $f$ is computable by a boolean circuit with $s$ gates if and only if it is computable by an AON-CIRC program with $s$ lines.

**NAND circuit**

- $NOT(a) = NOT(AND(a,a)) = NAND(a,a)$
- $AND(a,b) = NAND(NAND(a,a),NAND(b,b))$
- $OR(a,b) = NAND(NAND(a,b),NAND(a,b))$

$$\begin{array}{c} NAND  \; circuit \leftrightarrow boolean \; circuit \\ s \Rightarrow \leq 2s  \\ \leq 3s \Leftarrow s \end{array}$$

目前为止我们有以下四个概念: 它们可以依次转换 

1. boolean circuit
2. AON-CIRC program
3. NAND-CIRC program 
4. NAND circuit

**Theorem**

For every $n,m > 0$ and every finite function $f : \{0,1\}^n \rightarrow \{0,1\}^m$ there is a boolean circuit with $0(mn2^n)$ gates that computes $f$.

> 可以获得一个紧的界限$O(m \frac{2^n}{n})$

**Proof**

> 即将所有可能的情况对于

$$Y = (\dots \land \dots \land \dots) \lor (\dots) \lor (\dots) \lor (\dots) \lor \dots$$

| $x[0]$ | $x[1]$ | $\dots$ | $x[n-1]$ | $Y[j]$ |
| --- | --- | --- | --- | --- |
| 0 | 0 | $\dots$ | 0 | 0 |
| 0 | 0 | $\dots$ | 1 | 1 |
| $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ | $\vdots$ |

**概念**

$\mathcal{F} = \{f_1,\dots, f_k\}$ is universal if they can compute NAND

**Example:**

$\begin{cases} ONE(a,b) = 1 \\ ZERO(a,b)=0 \\ IF(a,b,c) = \begin{cases} b , & if \; a=1 \\ c, & if \; a = 0 \end{cases} \end{cases}$ is universal.

**Proof:**

$$NAND(a,b) = \begin{cases} 1, & if \; a= 0 \\ \begin{cases} 1, & if \; b = 0 \\ 0, & otherwise \end{cases} \end{cases}$$

$$NAND(a,b) = IF(a,IF(b,ZERO(a,b),ONE(a,b)), ONE(a,b))$$

**语法糖(Syntatic sugar)**

1. **Loop of fix length** 

    **Example:** `for i in range(n): ...`

    > 假如循环中有$4$行语句，展开则得到$4n$行语句

2. **User-defined procedure**

    **Example:** `def MAJ3(a,b,c): ...`

    > 假设过程中有$4$ 个语句，则`temp_1 = MAJ3(a,b,c)`的展开为4行语句

3. **confitional statement**

    **Example:** 

    ```py linenums="1"
    if(cond):
        a = ... // l1
    else:
        a = ... // l2
    ```
    > 我们可以使用$IF:\{0,1\}^3 \rightarrow \{0,1\}$，即 $IF ( cond,temp \_ a \_ 1, temp \_ a \_ 2 )$,$4$行语句来模拟.则总行数为$l_1 + l_2 + c$

**Example:** $ADD : \{0,1\}^{2n} \rightarrow \{0,1\}^{n+1}$

> 两个长度为$n$的二进制数相加

$$ADD(x_0,\dots, x_{2n-1}) = x_0\dots x_{n-1} + x_n\dots x_{2n-1} $$

```py title="伪代码" linenums="1"
def ADD(x[0],...,x[2n-1]):
    Result = [0] X (n+1)
    Carry = [0] X (n+1)
    for i in range(n):
        Result[i] = XOR(carry[i], XOR(x[i],x[i+n]))
        Carry[i+1] = MAJ3(carry[i], x[i], x[i+n])
    Result[n] = Carry[n]
    return Result
```

- Total $O(n)$ lines.

> 类似地有$Mult: \{0,1\}^{2n} \rightarrow \{0,1\}^{2n}$

> 行数 $O(n^2) \rightarrow O(n^{log_23}) \rightarrow$ even better

**Lookup:** $\{0,1\}^{2^k +k} \rightarrow {0,1}$

```py title="lookup code" linenums="1"

lookup_k+1 (x[0],...,x[2^{k+1}], i[0],...,i[k]):
    if(i[0] == 0):
        lookup_k (x[0],...,x[2^{k} - 1],i[1],...,i[k])
    else:
        lookup_k (x[2^k],...,x[2^{k+1}],i[1],...,i[k])
```

> 可以用`lookup`查表的方式去求解$f:\{0,1\}^n \rightarrow \{0,1\}^m$的电路设计, 经典的用空间换时间思想.

**第一种优化**

以$x[0],x[1],Y[0]为例$: $Y[0]$有$G_0,G_1,G_2,G_3$,四种取值

使用查表函数可得到$LOOKUP(G_0,G_1,G_2,G_3,x[0],x[1])$,这个电路对于$n$个输入变量只需要$O(2^n)$规模的电路,那么对于$m$个输出，只需要$O(m2^n)$规模的电路.这就是第一种优化.

**第二种优化**

考虑输入变量$x[0],\dots,x[n-1]$到$Y[j]$的关系表,若表中的关系以$x[0],\dots,x_[n-1]$顺序排列，则可知：若将表格以$2^{n-k}$的规模等分并记每个子表为$T_0,\dots,2^{n-k}$，则每等分的$x[0],\dots,x[k-1]$的输入是一致的.可以将其作为索引来查询子表.

整个查询结果的过程就分为两步:

1. 找子表：$LOOKUP(T_0,\dots,T_{2^{n-k}},x[0],\dots,x[k-1])$，规模为$O(2^{2^k} \cdot 2^k)$

> 考虑$\{0,1\}^2 \rightarrow \{0,1\}$共有$2^{2^2} = 16$种对应关系.推广到$\{0,1\}^k \rightarrow \{0,1\}$共有$2^{2^k}$种对应关系.$

2. 查子表: $LOOKUP(T_j[0],\dots,T_j[2^{n-k}]x[k],x[k+1],...,x[n-1])$,规模为$O(2^{n-k})$

总规模为$O(2^{2^k}\cdot 2^k + 2^{n-k})$, 令$k=log_2(n-2log_2n)$,则得到规模最小值$O(\frac{2^n}{n})$

### 定理

NAND-CIRC program $P$ with $\leq s$ lines $\overset{encoding}{\rightarrow} O(slogs)$ string

- num program \# $leq 2^{cslogs}$.
- let $s = \frac{2^n}{cn}$
- \# $\leq \frac{2^n}{2n} \cdot logs < 2^{2^n}$ 

> 这里的式子尚不明白可能需要重新看书

$\exists f: \{0,1\}^n \rightarrow \{0,1\}$ cannot be computed by any $P$ with $\leq \frac{2^n}{cn}$ lines.

考虑一个$s$行的NAND-CIRC program，每行有表达式$? = NAND(?,?)$，则至多有$3s$个不同变量，即

$$x[0],\dots,x[n-1],Y[0],\dots,Y[m-1],TEMP_1,\dots,TEMP_{3s-n-m}$$

将这些变量从$0$开始依次编号,则二进制编号长度至多为$log(3s)$，$s$行的NAND-CIRC program中共有$3s$个变量需要编号，则有下述推论：

每一个 $s$ 行的程序都可以被编码成长度为$3s\lceil log(3s) \rceil$的$01$串

$EVAL_{s,n,m}: \{0,1\}^{3s\lceil log(3s) \rceil + n} \rightarrow \{0,1\}^m$

**什么叫可编程电路？**

encoding of a NAND-CIRC program $P$ with $s$ lines $n$ inputs and $m$ outputs

$$EVAL_{s,n,m}(px)= \begin{cases}{c} P(x) && if \; P \; is \; a \; valid \; encoding \\ o^m && otherwise \end{cases}$$

### 定理2

$\forall s, n, m \exists$ NAND-CIRC program $U_{s,n,m}$ that computes $EVAL_{s,n,m}$

```py title="伪代码" linenums="1"
for i in range(3s):
    update(V,i,0)
for i in range(n):
    update(V,i,xi)
for(i,j,k) in P:
    a = get(V,j)
    b = get(b,k)
    c = NAND(a,b)
    Update(V,i,c)
for j in range(m):
    yj = get(V,j+n)
return y0, ... , y_(m-1)
```

- $get \rightarrow LOOKUP$, 规模为$O(s)$
- $update(V,i,a)$, 规模为$O(slogs)$

> $g_i(V,i,a) = \begin{cases}{c} a && if \; i = j \\ V[j], && if \; i \neq j \end{cases}$, $j$的编码长度为$log3s$,而单位比较则通过$LOOKUP$来实现，因此规模位$O(slogs)$

## Lec3

为求 $f:\{0,1\}^* \rightarrow \{0,1\}^*$的可计算性，我们可以先将其简化成$f:\{0,1\}^* \rightarrow \{0,1\}$

对所有的这类函数我们可以构造一个布尔函数(boolean function)

$$bf(x,i,c) = \begin{cases} f(x)_i  & if \; c = 0 , i <|f(x)| \\ 1 & if \; c = 1, i < |f(x)| \\ 0 & if \; i \geq |f(x)| \end{cases}$$

下面我们可以用python程序得到两者的相互转换

<div class="grid" markdown>

```py title="F(x) for f" linenums="1"
def F(x):
    res = []
    i = 0
    while BF(x,i,1):
        res.append(BF(x,i,0))
        i++
    return res
```

```py title="BF(x) for bf" linenums="1"
def BF(x,i,c):
    s = F(x)
    if i > |s|:
        return 0
    if c == 1:
        return 1
    if c == 0
        return s[i]
```
</div>

每一个布尔函数$f:\{0,1\}^* \rightarrow \{0,1\}$ 可以对应一个language $Af = \{ x \in \{0,1\}^*: f(x) = 1 \}$

反向转换可以有 $f_A(x) = \begin{cases} 1 & if \; x \in A \\ 0 & if \; x \notin A \end{cases}$

判断 $x$是否属于$Af$ $\Leftrightarrow f(x) = ?$

举一个简单的例子

$XOR:\{0,1\}^* \rightarrow \{0,1\}$ 可以写成 $XOR(x) = \overset{|x| -1 }{\underset{0}{\sum}} x_i \; mod \; 2$

假如将其写成一个python程序，它只需要将输入从头到尾遍历一遍,我们称其为 **one-pass constant-memory algorithm**

接下来我们要定义**确定性有限自动机(deterministic finite automaton, DFA)**

> 图标符号以文字解释呈现

DFA: $M = (K, s, F, S)$

- $K$: a finite set of states (圆圈)
- $s \in K$: the initial statl (左带右箭头的圆圈)
- $F \in K$: a finite set of accepting states (双圆圈)
- $S:K \times \{0,1\} \rightarrow K$ transition function ($\rightarrow$)

运作形式: 输入 $x_0 x_1 \dots x_{n-1}$

$s_0 = S \; s_1 = S(s_0,x_0) \; s_2 = S(s_1,x_1) \dots s_n = S(s_{n-1},x_{n-1})$

最终结果:$if \; s_n \in F : accept \; x_0 x_1 \dots x_{n-1} \; else: reject \; x_0 x_1 \dots x_{n-1}$

总结: $M$ computes a boolean function $f$ if $M$ accept $x \Leftrightarrow f(x) = 1$ (满足则接受)

另一表述：$M$ decides a language $A$ if $M$ accepts $x \Leftrightarrow x \in A$

$L(M) = \{ x \in \{0,1\}^*: M \; accepts \; x \}$

**一些练习：请写出下述集合的状态转移图(state diagram)**

1.$\emptyset \;$ 2.$\{0,1\}^* \;$  3.$\{e\} \;$ 4.$\{w \in \{0,1\}^*: w \; contains \; 101 \; as \; a \; substring\}$

因为这些 DFA 显然是可编码的，因此它们也是可数的. 但是 language 是不可数的. 所以 $\exists$ non-regular language 无法被DFA决定

**Theorem**

If $A$ and $B$ are regular, so is $A \cup B$

**Proof:**

$\exists M_A = (K_A, s_A, F_A, S_A)$

$\exists M_B = (K_B, s_B, F_B, S_B)$

构造一个$M = (K, s, F, S)$

- $K = K_A \times K_B$
- $s = (s_A, s_B)$
- $F = \{ (q_A,q_B) \in K_A \times K_B, q_A \in F_A \; or q_B \in F_B \}$
- $S: \forall (q_A,q_B) \in K_A \times K_B, \forall a \in \{0,1\} S(q_A,q_B,a) = (S_A(q_A,a), S_B(q_B,a))$

$L(M) = L(M_A) \cup L(M_B)$

**Theorem**

If $A$ and $B$ are regular, so is $AB$

思路: 将输入$x$分割开，分别输入两个DFA

### Non-determinism

Non-deterministic Finite automaton(NFA)

**特点**

- "next state" is not unique
- e-transition

符号标记：$N=(K,s,F,\Delta)$ transition relation $\Delta \subseteq K \times \{0,1,e\} \times K$

通过输入构建不同分支，只要有一个最终状态处在合法状态就接受

$N$ decides a language $A$ if $M$ accepts $w$ $\Leftrightarrow w \in A$

**练习：画出下述的状态转移图**

$\{w \in \{0,1\}^*: the \; second \; symbol \; from \ the \; end \; of \; w \; is 1\}$

Theorem

$NFA \Leftrightarrow DFA$
