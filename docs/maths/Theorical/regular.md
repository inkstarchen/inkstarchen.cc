> 我们现在要表示无限长输入的函数，并且将介绍一种简单的表示模型，以及其与正则表达式的等效性.

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

每一个布尔函数$F:\{0,1\}^* \rightarrow \{0,1\}$ 可以对应一个language $L_F = \{ x \in \{0,1\}^*: f(x) = 1 \}$

反向转换可以有 $f_L(x) = \begin{cases} 1 & if \; x \in A \\ 0 & if \; x \notin A \end{cases}$

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
