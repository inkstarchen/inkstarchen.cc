> 这一节中的重点是：任何函数都可被计算.

什么是语法糖？

> 使用基础块得到的新特性，我们用这些新特性简化我们的程序



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
