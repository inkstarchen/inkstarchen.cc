## 线性映射

### 定义
对于从线性空间$V_1(F)$到$V_2(F)$的一个映射$\sigma$，若

$$ \begin{array}{c} \forall \alpha , \beta \in V_1, \; \forall \lambda, \mu \in F \; 有：\\ \sigma(\lambda\alpha+\mu\beta)=\lambda\sigma(\alpha)+\mu\sigma(\beta) \end{array}$$

则称映射$\sigma$是**线性的**

## 像和核

### 定义

设$\sigma$是线性空间$V_1(F)到V_2(F)$的线性映射

- $V_1$的所有元素在$\sigma$下的像所组成的集合

$$\sigma(V_1)=\{ \beta | \beta = \sigma (\alpha), \alpha \in V_1 \}$$

称为**$\sigma$的像** (或称$\sigma$的值域)

- $V_2$的零元$0_2$在$\sigma$下的完全原像

$$\sigma^{-1}(0_2)=\lbrace\alpha|\sigma(\alpha)=0_2,\alpha\in V_1\rbrace$$

称为**$\sigma$的核**


> $\sigma(V_1)$和$\sigma^{-1}(0_2)$也常记作$Im\sigma$和$Ker\sigma$


### 定理
* （1）线性映射$\sigma:V_1->V_2$是单射$<=>\sigma^{-1}(0_2)=\lbrace0_1\rbrace$

### 运算

#### 定义

设$\sigma,\tau\in L(V_1,V_2),$规定

- $\sigma$ 与 $\tau$ 之和 $\sigma+\tau$ 为:

$$(\sigma+\tau)(\alpha)=\sigma(\alpha)+\tau(\alpha),\qquad\alpha\in V_1,$$

- $\lambda$ 与 $\sigma$ 的数量乘积 $\lambda\sigma$ 为:

$$(\lambda\sigma)(\alpha)=\lambda(\sigma(\alpha)),\qquad\alpha\in V_1.$$

## 线性映射的矩阵表示

### 定义

设$\sigma$是$V_1$到$V_2$的一个映射,$B_1$和$B_2$分别为两个空间的基，我们把$\sigma(\varepsilon_1),\sigma(\varepsilon_2),...,\sigma(\varepsilon_n)$关于基$B_2$的坐标按列排成的矩阵$M(\sigma)$,即

$$M(\sigma)=\begin{pmatrix}a_{11} & a_{12} & ...& a_{1n} \\ a_{21} & a_{22} &... & a_{2n} \\ \vdots& & & \vdots\\a_{m1} & a_{m2} &\cdots &a_{mn}\end{pmatrix}.$$

称为$\sigma关于B_1和B_2$的矩阵.


## 线性映射的秩
### 定义
* 设$\sigma\in L(V_1,V_2),$如果$\sigma(V_1)$是$V_2$的有限维子空间，则$\sigma(V_1)$的维数称为$\sigma$的秩，记作$r(\sigma)$,即

$$r(\sigma)=dim\sigma(V_1)$$

### 定理
* 设$\sigma\in L(V_1,V_2),$如果$dim(V_1)=n$,则

$$r(\sigma)+dim(Ker\sigma)=n.$$

设$\sigma\in L(V_1,V_2),$如果$V_1和V_2$都是n维线性空间，则下列命题等价：

1. $秩(\sigma)=n$(或说$\sigma$满秩);

2. $\sigma$是单射;

3. $\sigma$是满射;

4. $\sigma$是可逆线性映射.


## 双线性函数 二次型

### 定义
* 我们称$f$为线性空间V(F)上的一个双线性函数，如果$f$是$V\times V$到F的映射，而且$\forall \alpha,\beta,\alpha_i,\beta_i \in V,k_i \in F(i = 1,2),均有$$$(1)f(\alpha,k_1\beta_1+k_2\beta_2)=k_1f(\alpha,\beta_1)+k_2f(\alpha,\beta_2),$$$$(2)f(k_1\alpha_1+k_2\alpha_2,\beta)=k_1f(\alpha_1,\beta)+k_2f(\alpha_2,\beta).$$
### 定理
* 设线性空间$V(F)$的双线性函数$f(\alpha,\beta)$在基$B_1=\lbrace \varepsilon_1,\varepsilon_2,\cdots,\varepsilon_n\rbrace$和$B_2=\lbrace \eta_1,\eta_2,\cdots,\eta_n\rbrace$下的度量矩阵分别为A和B，如果$$(\eta_1,\eta_2,\cdots,\eta_n)=(\varepsilon_1,\varepsilon_2,\cdots,\varepsilon_n)C,$$则$$B=C^TAC$$
### 定义
* 我们称n阶矩阵A相合于B$(记作A\simeq B),如果存在可逆矩阵C，$使得$$B=C^TAC$$容易验证其为一种等价关系
* 线性空间$V(F)$上的一个双线性函数$f(\alpha,\beta)$如果$\forall\alpha,\beta \in V,$都有：$$(1)f(\alpha,\beta)=f(\beta,\alpha),则f(\alpha,\beta)叫做对称双线性函数；$$$$(2)f(\alpha,\beta)=-f(\beta,\alpha),则f(\alpha,\beta)叫做反对称双线性函数$$
* n个元$x_1,x_2,\cdots,x_n$的二次齐次多项式$$f(x_1,x_2,\cdots,x_n)=\sum_{i=1}^na_{ii}x_i^2+\sum_{1\leq i < j \leq n}2a_{ij}x_ix_j$$（其中系数$a_{ij}$是数域$F$中的数），叫做数域$F$上的n元二次型（简称二次型）

## 齐次线性方程组

### 定理
* 设矩阵$A\in M_{m\times n}(F),若r(A)=r,则$齐次线性方程组$AX=0$的解空间$N(a)是F^n的一个n-r维子空间.$
### 非齐次线性方程组
#### 定理
* 对于非齐次线性方程组$AX=b$，下列命题等价：
	* （1）$AX=b$有解；
	* （2）$b\in R(A),即b可被A的列向量组线性表示；$
	* （3）$r(A,b)=r(A),即增广矩阵的秩等于系数矩阵的秩.$
* 若非齐次线性方程组$AX=b$有解，则其一般解为$$X=X_0+\bar{X},$$其中$X_0是AX=b的一个特解；\bar{X}是AX=0的一般解.$

## 可对角化条件

### 定理
* n维线性空间$V(F)$的线性变换$\sigma$(或$A\in M_n(F))$可对角化的充分必要条件为$\sigma(或A)$有n个线性无关的特征向量
* n维线性空间$V(F)$的线性变换$\sigma$的每个特征值$\lambda_i$的重数大于或等于其特征子空间$V_{\lambda_i}$的维数
* n维线性空间$V(F)$的线性变换$\sigma$可对角化的充分必要条件是：$\sigma$的每个特征值的重数等于其特征子空间的维数，而且$\sigma$的不同特征值$\lambda_1,\lambda_2,\cdots,\lambda_m$的重数$r_1,r_2,\cdots,r_m$之和等于n.