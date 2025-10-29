
## 拉格朗日乘子法(Lagrange multipliers)

**目标：** 寻找多元函数在一组约束下的极值的方法

**作用：** 可将有$d$个变量与$k$个约束条件的最优化问题转化为具有$d+k$个变量的无约束优化问题求解。

**等式约束的优化问题**

假定$x$为$d$维向量，想要寻找一个$x^*，使得目标函数$f(x)$最小，且满足$g(x)=0$。从几何上看，目标是在由$g(x)=0$确定的$d-1$维曲面上寻找能够使得$f(x)$最小化的点,此时由如下结论

- 对于约束曲面上的任意点$x$，该点的梯度$\nabla g(x)$正交于约束曲面
- 在最优点$x^*$，目标函数在该点的梯度$\nabla f(x^*)$正交于约束曲面

> 若不正交，则仍然可以在约束曲面上继续移动使得函数值继续下降.

因此在最优点$x^*$, 梯度$\nabla g(x)$和$\nabla f(x)$的方向必定相反或相同，即存在$\lambda \neq 0$使得：

$$\nabla f(x^*) + \lambda \nabla g(x^*)=0$$

$\lambda$称为拉格朗日乘子，定义拉格朗日函数

$$L(x,\lambda)=f(x)+\lambda g(x)$$

> 此时的$\lambda$可能为正，可能为负

分别对两个变量求偏导则可得到约束条件，于是原约束优化问题可转化为对拉格朗日函数的无约束优化问题,即在变量为$x$和$\lambda$的情况下寻找拉格朗日函数的极值.

**不等式约束的优化问题**

对于约束$g(x) \leq 0$，若$x^*$在$g(x) \leq 0$的区域中，则约束条件不起作用.可直接通过条件$\nabla f(x) = 0$来获得最优点.等价于将$\lambda$置零，然后对$\nabla_x L(x,\lambda)$置零得到最优点.

> 约束条件之所以不起作用，是因为$x^*$在约束范围内,只要优化到$x^*$点附近，则必然满足约束条件.

若$x^*$在$g(x) = 0$上，则和等式约束一样分析，但此时$\nabla f(x^*)$的方向必与$\nabla g(x^*)$相反，即存在常数$\lambda > 0$使得$\nabla f(x^*) + \lambda \nabla g(x^*)=0$.

> 之所以两者方向必定相反，是因为如果两者方向相同，则可以往可行区域移动，且继续使得函数值下降.与最优点在$g(x)$上矛盾

整合两种情形，必定满足$\lambda g(x) = 0$，因此不等式约束问题可以转化为在如下约束下最小化拉格朗日函数

$$g(x) \leq 0;$$

$$\lambda \geq 0$$

$$\mu_j g_j(x) = 0$$

其中$\mu_j$为不等式约束下的拉格朗日乘子，上述三个条件被称为Karush-Kuhn-Tucker（简称KKT）条件.

上述做法可以推广到多个约束，可行域$\mathcal{D} \subset \mathcal{R}^d$非空的优化问题

$$\underset{x}{min} f(x)$$

$$s.t. \; h_i(x) = 0 \; (i = 1, \dots, m),$$

$$g_j(x) \leq 0 \; (j = 1, \dots, n).$$

引入拉格朗日乘子$\lambda = (\lambda_1, \lambda_2, \dots, \lambda_m)^T$和$\mu = (\mu_1, \mu_2, \dots, \mu_n)^T$,相应的拉格朗日函数为

$$L(x, \lambda, \mu) = f(x) + \overset{m}{\underset{{i=1}}{\sum}} \lambda_i h_i(x) + \overset{n}{\underset{j=1}{\sum}} \mu_j g_j(x).$$

由不等式约束引入的KKT条件$(j = 1,2,\dots, n)$为

$$g_j(x) \leq 0, \; \mu_j \geq 0 ; \mu_j g_j(x) = 0$$

一个优化问题可以从两个角度来考察，即“主问题”（primal problem）和“对偶问题”（dual problem）.对于主问题，基于拉格朗日函数，其拉格朗日“对偶函数”(dual function) $\Gamma : \mathcal{R}^m \times \mathcal{R}^n \mapsto \mathcal{R}$,定义为

$$\Gamma(\lambda, \mu) = \underset{x \in \mathcal{D}}{inf} \; L(x,\lambda,\mu)$$

$$= \underset{x \in \mathcal{D}}{inf}(f(x) + \underset{i = 1}{\overset{m}{\sum}} \lambda_ih_i(x) + \underset{j = 1}{\overset{n}{\sum}} \mu_jg_j(x))$$

> 推导对偶问题时，通常将拉格朗日乘子对$x$求导，并令导数等于0，获得对偶函数的表达形式

若 $\tilde{x} \in \mathcal{D}$ 为主问题可行域中的点，则对任意$\mu \succeq 0$ 和 $\lambda$都有

$$\underset{i=1}{\overset{m}{\sum}} \lambda_i h_i(x) + \underset{j=1}{\overset{n}{\sum}} \mu_j g_j(x) \leq 0$$

> $\mu \succeq 0$ 表示 $\mu$ 的分量均大于零

进而有

$$\Gamma(\lambda, \mu) = \underset{x \in \mathcal{D}}{inf} L(x,\lambda,\mu)$ \leq L(\tilde{x}, \lambda, \mu) \leq f(\tilde{x})$$

> 第一个不等式由下确界定义得到，第二个不等式由增加项为非正数得到。

若著问题的最优值为$p^*$,则对任意$\mu \succeq 0$和$\lambda$都有

$$\Gamma(\lambda, \mu) \leq p^*$$

对偶函数给出了主问题最优值的下界，其取决于$\mu$和$\lambda$的值，进而引出了一个问题：基于对偶函数能获得的最好下界是什么 ？

$$\underset{\lambda, \mu}{max} \Gamma(\lambda, \mu) \; s.t. \; \mu \succeq 0$$

这就是主问题的对偶问题，其中$\lambda$和$\mu$称为“对偶变量”(dual variable),无论主问题的凸性如何，对偶问题始终是凸优化问题。

考虑对偶问题的最优值$d^*$, 显然有$d^* \leq p^*$,这称为“弱对偶性”（weak duality）成立;若$d^* = p^*$,则称“强对偶性”（strong duality）成立.此时由对偶问题能获得主问题的最优下界，但是一般的优化问题，强对偶通常不成立。

但是若满足Slater条件:则此时强对偶性成立

- 主问题为凸优化问题，如$f(x)$和$g_j(x)$均为凸函数，$h_i(x)$为仿射函数

- 可行域中至少有一点使不等式约束严格成立.

值得注意的是，强对偶性成立时，将拉格朗日函数分别对原变量和对偶变量求导，再令导数等于零，即可得到原变量与对偶变量的数值关系.

