> **我们为什么需要概率论**？
> 因为我们需要在掌握不完全信息的情况下做出决策.。

> 不同的理论有不同的视角，若一个问题要用特定的理论去解决，那么必须要遵循其理论的视角。

> 若无法处理特殊化的问题， 或许可以先解决一般化的问题再进行推广。


## 几何概率

当有无限个样本点时。$事件A_g=\{任取一个样本点，它落在区域g\subset\Omega\}$,则$A_g$的概率定义为

$$P(A_g)=\frac{g的测度}{\Omega的测度}$$

这样定义的概率被称为**几何概率**

> **主要的思想**：在样本数为无限时，通过引入测度来实现概率计算。即从比较**样本个数**推广到比较**样本集体的测量值**.

---

> 前面的概率都是我们朴素地去理解，通过数和测量比较的方法去定义概率。接下来我们需要更加规范的表达，来加深我们对于概率的理解.


### 条件概率与事件的独立性

> 首先我们需要引入 **事件** 的概念, 所谓 概率 就是事件发生可能性的一种度量.

#### 条件概率的定义

$$P(A|B)=\frac{P(AB)}{P(B)}$$

#### 全概率公式，贝叶斯公式

全概率公式： 对信息的综合推断

$$P(B)=\sum^{\infty}_{i=1}P(A_i)P(B|A_i)$$

- 要求: $A_i$两两互斥，且总体构成完备事件组  $\cup^{\infty}_{i=1}A_i = \Omega$

贝叶斯公式：利用已知信息反推原事件的概率

$$P(A_i|B)=\frac{P(A_i)·P(B|A_i)}{\sum^{\infty}_{k=1}P(A_k)·P(B|A_k)}$$

#### 事件独立性

独立性:即事件$A$的发生不会影响事件$B$的发生的概率

$$P(AB)=P(A)P(B)$$

## 随机变量与分布函数

>其更加推进的一步是：从等可能事件推广到了概率在不同事件上的分布.故称随机变量。

### 离散型随机变量及其分布

#### 随机变量的概念

用于表示随机实验的结果，$w$为样本点，则$\xi$可表示为依$w$不同而取不同值得函数.$\xi =\xi(w)$

#### 离散型随机变量

$$\left[\begin{array}{ll}
x_1& x_2 & \cdots &x_n &\cdots&\\
p(x_1)&p(x_2)&\cdots &p(x_n) &\cdots&
\end{array}\right]$$

分布列如上：

### 分布函数与连续性随机变量
#### 分布函数

> 我们希望将分布列推广，从而对所有的随机变量有统一的概率表达方式

$$F(x)=P(\xi \leq x) \qquad -\infty<x<\infty$$

#### 连续性随机变量及密度函数

> 针对连续性的随机变量，我们可以更进一步地研究其概率在整个域上的分布情况，而非总体的情况.

- 定义：若随机变量$\xi$可取某个区间（有限或无限）中的一切值，并且存在某个非负的可积函数$p(x)$，使分布函数$F(x)$满足

$$F(x)=\int^x_{-\infty}p(y)dy,\qquad -\infty < x<\infty,$$

则称$\xi$为连续型随机变量，称$p(x)$为$\xi$的概率密度函数，简称为密度函数.

### 随机向量

> 当同时研究多个变量的概率关系时，我们就要将随机变量替换成随机向量.同时引出联合分布以及边际分布的概念.

所谓边际分布，即考虑到其他变量的所有可能的情况下，某一变量的概率分布情况.

#### 分布函数

其分布函数与一元分布有类似的性质.但同时也有额外条件

$$F(b_1,b_2)-F(a_1,b_2)-F(b_1,b_2)+F(a_1,a_2)\geq 0$$

#### 连续性随机向量

并无其他，将加减法转换成了积分运算.

### 随机变量的独立性

> 只需要看其随机变量的边际分布能否推得联合分布.

### 随机变量的函数及其分布

简单的变换：卷积公式

1.当$\xi_1$与$\xi_2$仙湖独立，各自有密度函数$p_1(x),p_2(x)$时，$\xi_1 + \xi_2$的密度函数为

$$p_\eta(z)=\int^{\infty}_{-\infty}p_1(x)p_2(z-x)dx$$

2.若$(\xi_1, \xi_2)$是连续型随机变量，则$\eta=\xi_1/\xi_2$是连续型随机变量，其密度函数为

$$p_\eta(z)=\int^{\infty}_{-\infty}p(zx,x)|x|dx$$

3.次序统计量的分布

$\xi_1^* = min\{\xi_1,\xi_2,\cdots,\xi_n\}, \xi_n^*=max\{\xi_1,\xi_2,\cdots,\xi_n\}$

(1).$\xi_n^*$的分布函数

$$P(\xi_n^*\leq x)= P(\xi_1 \leq x,\xi_2 \leq x,\cdots,\xi_n\leq x)=[F(x)]^n$$

(2).$\xi_1^*$的分布函数

$$P(\xi_1^* > x) = [1-F(x)]^n,\qquad P(\xi_1^*\leq x) = 1-[1-F(x)]^n$$

(3).$(\xi_1^*,\xi_n^*)$的联合分布函数

$$F(x,y)=P(\xi_1^*\leq x, \xi_n^*\leq y) = [F(y)]^n-[F(y)-F(x)]^n$$

#### 随机向量的变换
$$q(y_1,\cdots,y_n)=p(x_1(y_1,\cdots,y_n),\cdots,x_n(y_1,\cdots,y_n))|J|$$


## 数字特征与特征函数
### 数学期望
>我们不仅希望了解事情发展的可能性，还希望了解一个行动是否有益，是否有期望的收益，多大程度上能得到期望的收益.


- 离散型随机变量的数学期望

简单计算

- 连续型随机变量的数学期望

积分计算
#### 数学期望的基本性质

1. 若$|\xi|\leq\eta$,且$E\eta$存在，则$E\xi$存在，且$|E\xi|\leq E|\xi|\leq E\eta$

2. 若$E\xi_1,\cdots,E\xi_n$存在，则对任意常数$c_1,\cdots,c_n$，及$b$,$E(\sum^n_{i=1}c_i\xi_1+b)$存在，且

$$E(\sum^n_{i=1}c_i\xi_i+b)=c_i\sum^n_{i=1}E\xi_i+b$$

#### 条件期望

即条件概率下的期望、同时存在全期望公式.

### 方差、协方差与相关系数
#### 概率方差

> 对于随机变量可能取值离散程度度量的一个指标

$$Var\xi = E(\xi - E\xi)^2，\qquad Var\xi = E\xi^2 -(E\xi)^2 $$

#### 协方差
- 定义：设$\xi_i$和$\xi_j$的联合分布函数为$F_{ij}(x,y).$若$E|(\xi_i-E\xi_i)(\xi_j-E\xi_j)|<\infty,$称

$$E(\xi_i-E\xi_i)(\xi_j-E\xi_j)=\int^{\infty}_{-\infty}\int^{\infty}_{-\infty}(x-E\xi_i)(y-E\xi_j)dF_{ij}(x,y)$$

为$\xi_i$和$\xi_j$的协方差,记作$Cov(\xi_i,\xi_j).$

- 性质1 $Cov(\xi,\eta)=Cov(\eta,\xi)=E\xi \eta - E\xi E\eta$

协方差矩阵$\Sigma = \frac{1}{n-1} X^TX$

#### 相关系数

$$r_{\xi\eta}=Cov(\xi^*,\eta^*)=\frac{E(\xi-E\xi)(\eta-E\eta)}{\sqrt{Var\xi Var\eta}}$$

不相关则上式为0.
#### 矩

原点矩:$m_k = E\xi^k$

中心矩:$c_k=E(\xi-E\xi)^k$

其代表随机变量的一系列的数字特征，具有普遍意义

### 特征函数

> 特征函数是随机变量分布的另外一种描述形式，即包含了此随机变量分布的所有特征

#### 定义

设$\xi$为实随机变量，称

$$f(t)=Ee^{it\xi},\space -\infty < t < \infty$$

为$\xi$的特征函数(characteristic function)

- 离散型计算

$$f(t)=\sum^{\infty}_{n=1}p_ne^{itx_n}$$

- 连续性计算

$$f(t)=\int^{\infty}_{-\infty}e^{itx}p(x)dx$$

- 练习各种分布的特征函数计算

#### 性质
#### 逆转公式与唯一性定理

逆转公式

- 设分布函数$F(x)$的特征函数为$f(t)$,令$x_1,x_2$是$F(x)$的连续点，则

$$F(x_2)-F(x_1)=\lim_{T\to\infty}\frac{1}{2\pi}\int^T_{-T}\frac{e^{-itx_1}-e^{-itx_2}}{it}f(t)dt$$

唯一性定理

- 分布函数可由特征函数唯一确定.

逆傅里叶变换

- 设$f(t)$是特征函数，且$\int^\infty_{-\infty}|f(t)|dt < \infty (f(t) 绝对可积)$,则分布函数$F(x)$的导数存在且连续.此时

$$F'(x)=\frac{1}{2\pi}\int^\infty_{-\infty}e^{-itx}f(t)dt$$

## 正态分布（高斯分布）

$X ~  N(\mu, \sigma^2)$

### 一维高斯分布

$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

### 二维高斯分布

$$G(u,v) = \frac{1}{2\pi\sigma^2}\cdot e^{-\frac{u^2+v^2}{2\sigma^2}}$$

## 柯西分布
- 不存在数学期望和方差
- 特征函数$e^{i\mu t - \lambda|t|}$

$$p(x)=\frac{1}{\pi}\cdot \frac{\lambda}{\lambda^2+(x-\mu)^2},-\infty< x < \infty,\lambda>0，\mu常数$$



## 帕斯卡(Pascal)分布

> 在伯努利概型中，每次成功得概率为$p$，记知道第$r$次成功时的次数为$\xi$.

$$P(\xi = k) = \left(\begin{array}{ll} 
k-1 \\
r-1 
\end{array}\right)p^{r}q^{k-r}$$

## 退化分布

$$P(\xi =c) = 1$$

## 两点分布\伯努利分布

$$\left[\begin{array}{ll}
x_1 & x_2 \\
p & q\\
\end{array}\right], \qquad p,q>0, p+q=1.$$

## 二项分布

$$P(k,n)=\frac{C^k_n}{2^n}, P(k,n)=C^k_np^kq^{n-k}$$

即伯努利概型中$k$次成功的概率

## 泊松定理

假定$p$与$n$有关，记作$p_n$。考虑$n\to \infty$的情况，有下面的定理：

如果存在正常数$\lambda$，当$n\to \infty$时，有$np_n \to \lambda$，则

$$\lim_{n\to\infty} b(k;n,p)=\frac{\lambda^k}{k!}e^{-\lambda}，\qquad k=0,1,2,\cdots.$$

通常,$p$与$n$无关，但当$n$很大,$p$很小，而$np$不是非常大时，可以近似地取$np=\lambda$

## 几何分布

$$p(\xi = k)=pq^{k-1}$$

## 超几何分布

$$P(\xi = k ) = \frac{\left(\begin{array}{ll} M\\ k \end{array} \right)\left(\begin{array}{ll} N-M\\ n-k \end{array} \right)}{\left(\begin{array}{ll} N\\ n \end{array} \right)}$$

1. n维正态分布
设$B=(b_{ij})$为$n$维正定对称矩阵，$|B|$为其行列式,$B^{-1}$为其逆，又设$x=(x_1,x_2,\cdots,x_n)',a=(a_1,a_2,\cdots,a_n)',$则称

$$p(x)=\frac{1}{(2\pi)^{n/2}|B|^{1/2}}exp\{-\frac{1}{2}(x-a)'B^{-1}(x-a)\}$$

为$n$维正态密度函数，若此随机向量$\xi$具有此密度函数，则称$\xi$服从$n$维正态分布，记作$\xi ~N(a,B).$

- 性质5：设$\xi = (\xi_1,\cdots,\xi_n)'~N(a,B),C=(c_{ij})_{m×n}$为$m×n$矩阵，则

$$\eta=C\xi 服从m元正态分布N(Ca,CBC')$$

| 分布名称 | 概率分布或密度函数$p(x)$ | 数学期望 | 方差 | 特征函数 |
| ---| --- | --- | ---- | --- |
| 退化分布 <br> $D(x-c)$ | $p_c =1$ ($c$为常数) |  $c$ | $0$ | $e^{ict}$ |
| 伯努利分布<br>(两点分布) | $p_k=\begin{cases}{ll} q, && k=0 \\ p, && k=1, \end{cases}$ <br> $0<p<1, q=1-p$| $p$ | $pq$ | $pe^{it}+q$ |
| 二项分布<br>$B(n,p)$ | $b(k;n,p)=\left(\begin{array}{ll} n \\ k \end{array}\right)p^kq^{n-k},$ <br> $k=0,1,\cdots,n,$ <br> $0<p<1,$ <br> $q=1-p$ | $np$ | $npq$ | $(pe^{it}+q)^n$ | |0 |   |     |     |  |
