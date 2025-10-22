## 矩阵的运算

### 定义

设$A=(a_{ij})_{m\times n},B=(b_{ij})_{m\times n},A,B\in M_{m\times n}(F),\lambda \in F$,我们规定

$$A+B=(a_{ij}+b_{ij})_{m\times n},$$

$$\lambda A=(\lambda a_{ij})_{m\times n}$$

### 矩阵乘法

#### 定义

设$A=(a_{ij})_{p\times m},B=(b_{ij})_{m\times n}$,我们规定$A$与$B$之乘积$AB=C=(c_{ij})$是一个$p\times n$型矩阵，它的第$i$行，第$j$列元素

$$c_{ij}=\sum_{k=1}^ma_{ik}b_{kj}=a_{i1}b_{1j}+a_{i2}b_{2j}+\cdots+a_{im}b_{mj},$$

- $i=1,\cdots,p;j=1,\cdots,n.$

> PS:乘积AB当且仅当A的列数等于B的行数时才有意义，否者A不能左乘B

> 矩阵运算满足结合律、数乘交换、左右分配律

### 定理

设$\sigma\in L(V_1,V_2)$关于$V_1$和$V_2$的基$B_1$和基$B_2$的矩阵$A=(a_{ij})_{m\times n}$如（4-11）式子

$$\sigma(\varepsilon_1,\varepsilon_2,\cdots,\varepsilon_n)=(e_1,e_2,\cdots,e_m)A,\qquad\qquad(4-11)$$

$\alpha与\sigma(\alpha)$如(4-12)式

$$\alpha=(\varepsilon_1,\varepsilon_2,\cdots,\varepsilon_n)X,\qquad\sigma(\alpha)=(e_1,e_2,\cdots,e_m)Y \qquad\qquad(4-12)$$

则$Y=AX.$

* $AB=0$