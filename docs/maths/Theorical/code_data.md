> **Big Idea 6**

>  A program is a piece of text, and so it can be fed as input to other programs.

- 程序和电路的最大规模.
- 某些函数的最小规模

考虑一个$s$行的NAND-CIRC program，每行有表达式$? = NAND(?,?)$，则至多有$3s$个不同变量，即

$$x[0],\dots,x[n-1],Y[0],\dots,Y[m-1],TEMP_1,\dots,TEMP_{3s-n-m}$$

将这些变量从$0$开始依次编号,则二进制编号长度至多为$log(3s)$，$s$行的NAND-CIRC program中共有$3s$个变量需要编号，则有下述推论：

每一个 $s$ 行的程序都可以被编码成长度为$3s\lceil log(3s) \rceil$的$01$串

$EVAL_{s,n,m}: \{0,1\}^{3s\lceil log(3s) \rceil + n} \rightarrow \{0,1\}^m$

!!! note "Theorem | Representing programs as strings"

    NAND-CIRC program $P$ with $\leq s$ lines $\overset{encoding}{\rightarrow} O(slogs)$ string

> 这样的函数有多少个？字符编码衍生出函数个数的计算

!!! note "Theorem | Counting programs"
    For every $s,n,m \in \mathbb{N}$

    $$|SIZE_{n,m}(s)| \leq 2^{O(slogs)}$$

    That is, there are at most $2^{O(slogs)} functions computed by NAND-CIRC programs of at most $s$ lines

> 程序与字符串之间的一一映射，使得其变换的数目在有限范围内.

但是考虑$f:\{0,1\}^n \rightarrow \{0,1\}$,这样的函数总数有$2^{2^n}$个，是呈现指数倍增长.所有当$n$很大时，能够用较小电路计算的函数只是所有函数中的很小一部分.

!!! note "Theorem | Counting argument lower bound"
    There is a constant $\delta > 0$, such that for every sufficiently large $n$, there is a function $f:\{0,1\}^n \rightarrow \{0,1\}$ such that $f \notin SIZE_n(\frac{\delta 2^n}{n}). That is, the shortest NAND-CIRC program to compute $f$ requires more than $\delta \cdot 2^n /n $ lines.

> 通过放缩即可得到，它所能够表示的电路数目，仍然小于函数的可能数目.其意义是：当$n$较大时，一定存在函数，其所需的程序的行数是指数级的.

$\exists f: \{0,1\}^n \rightarrow \{0,1\}$ cannot be computed by any $P$ with $\leq \frac{2^n}{cn}$ lines.





**什么叫可编程电路？**

encoding of a NAND-CIRC program $P$ with $s$ lines $n$ inputs and $m$ outputs

$$EVAL_{s,n,m}(px)= \begin{cases}{c} P(x) && if \; P \; is \; a \; valid \; encoding \\ o^m && otherwise \end{cases}$$

!!! note "Theorem | Bounded Universality of NAND-CIRC programs"

    $\forall s, n, m \exists$ NAND-CIRC program $U_{s,n,m}$ that computes $EVAL_{s,n,m}$


!!! note "Theorem | Efficient bounded universality of NAND-CIRC programs"
    For every $s,n,m \in \mathbb{N}$ there is a NAND-CIRC program of at most $O(s^2logs)$ lines that computes the function $EVAL_{s,n,m} : \{0,1\}^n \rightarrow \{0,1\}^m$ defined above (where $S$ is the number of bits needed to represent programs of $s$ lines)

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

> $g_i(V,i,a) = \begin{cases}{c} a && if \; i = j \\ V[j], && if \; i \neq j \end{cases}$, $j$的编码长度为$log3s$,而单位比较则通过$LOOKUP$来实现，因此规模为$O(slogs)$

