柯西分布
- 不存在数学期望和方差
- 特征函数$e^{i\mu t - \lambda|t|}$
$$p(x)=\frac{1}{\pi}\cdot \frac{\lambda}{\lambda^2+(x-\mu)^2},-\infty< x < \infty,\lambda>0，\mu常数$$
#### 帕斯卡(Pascal)分布

> 在伯努利概型中，每次成功得概率为$p$，记知道第$r$次成功时的次数为$\xi$.

$$P(\xi = k) = \left(\begin{array}{ll} 
k-1 \\
r-1 
\end{array}\right)p^{r}q^{k-r}$$

#### 退化分布
$$P(\xi =c) = 1$$
#### 两点分布\伯努利分布
$$\left[\begin{array}{ll}
x_1 & x_2 \\
p & q\\
\end{array}\right], \qquad p,q>0, p+q=1.$$
#### 二项分布

$$P(k,n)=\frac{C^k_n}{2^n}, P(k,n)=C^k_np^kq^{n-k}$$

即伯努利概型中$k$次成功的概率

##### 泊松定理
假定$p$与$n$有关，记作$p_n$。考虑$n\to \infty$的情况，有下面的定理：
如果存在正常数$\lambda$，当$n\to \infty$时，有$np_n \to \lambda$，则

$$\lim_{n\to\infty} b(k;n,p)=\frac{\lambda^k}{k!}e^{-\lambda}，\qquad k=0,1,2,\cdots.$$

通常,$p$与$n$无关，但当$n$很大,$p$很小，而$np$不是非常大时，可以近似地取$np=\lambda$

#### 几何分布

$$p(\xi = k)=pq^{k-1}$$

#### 超几何分布

$$P(\xi = k ) = \frac{\left(\begin{array}{ll} M\\ k \end{array} \right)\left(\begin{array}{ll} N-M\\ n-k \end{array} \right)}{\left(\begin{array}{ll} N\\ n \end{array} \right)}$$

1. n维正态分布
设$B=(b_{ij})$为$n$维正定对称矩阵，$|B|$为其行列式,$B^{-1}$为其逆，又设$x=(x_1,x_2,\cdots,x_n)',a=(a_1,a_2,\cdots,a_n)',$则称

$$p(x)=\frac{1}{(2\pi)^{n/2}|B|^{1/2}}exp\{-\frac{1}{2}(x-a)'B^{-1}(x-a)\}$$

为$n$维正态密度函数，若此随机向量$\xi$具有此密度函数，则称$\xi$服从$n$维正态分布，记作$\xi ~N(a,B).$

- 性质5：设$\xi = (\xi_1,\cdots,\xi_n)'~N(a,B),C=(c_{ij})_{m×n}$为$m×n$矩阵，则

$$\eta=C\xi 服从m元正态分布N(Ca,CBC')$$

| 分布名称               | 概率分布或密度函数$p(x)$                                                                                                     |   数学期望 | 方差      | 特征函数              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- | -----: | ------- | ----------------- |
| 退化分布$$D(x-c)$$     | $$p_c =1$$$$(c为常数)$$                                                                                                |  $$c$$ | $$0$$   | $$e^{ict}$$       |
| 伯努利分布<br>(两点分布)    | $$p_k=\left\{\begin{array}{ll} q, && k=0 \\ p, && k=1, \end{array}\right.$$$$0<p<1, q=1-p$$                         |  $$p$$ | $$pq$$  | $$pe^{it}+q$$     |
| 二项分布<br>$$B(n,p)$$ | $$b(k;n,p)=\left(\begin{array}{ll} n \\ k \end{array}\right)p^kq^{n-k},$$<br>$$k=0,1,\cdots,n,$$$$0<p<1,$$$$q=1-p$$ | $$np$$ | $$npq$$ | $$(pe^{it}+q)^n$$ |
| 0                  |                                                                                                                     |        |         |                   |
