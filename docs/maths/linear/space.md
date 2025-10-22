## 线性空间

### 定义
$V$（一个非空集合）和$F$（一个域）满足

1. $<V:+>$是一个交换群
2. 四条性质:
	- $1{\alpha}={\alpha}$
	- ${\lambda}({\mu\alpha})=({\lambda\mu}){\alpha}$
	- $({\lambda+\mu}){\alpha}={\lambda\alpha+\mu\alpha}$
	- ${\lambda}(\alpha+\beta)={\lambda\alpha}+{\lambda\beta}$

则称$V$对于上述两种运算在域$F$上构成一个线性空间，简称$V$为域$F$上的**线性空间**，记作$V（F）$.如果$F$是实（复）数域，则称$V$为实（复）数域上的线性空间，简称**实（复）空间**.

### 有（无）限维线性空间

如果$V$中存在一个有限子集$S$，使得$L(S)=V$,  则称$V(F)$为**有限维线性空间**，;否则，称为**无穷维线性空间**.

### 验证线性空间的方法

* （数乘）从0和1入手考虑反例，正面证明
* 先考虑封闭性，再考虑单位元，逆元

## 线性子空间

### 定义

设$W$是线性空间$V(F)$的非空子集，如果$W$对$V$中的运算也构成域$F$上的线性空间，则称$W$为$V$的**线性子空间**（简称**子空间**）.

### 定理

1. 线性空间$V(F)$的非空子集$W$为$V$的子空间的充分必要条件是$W$对于$V(F)$的线性运算封闭.

## 线性空间的同构

### 定义

如果由线性空间$V_1(F)$到$V_2(F)$存在一个线性的双射$\sigma$，就说$V_1(F)和V_2(F)$是**同构的**，记作$V_1(F)\cong V_2(F).$这个$\sigma$叫做从$V_1(F)$到$V_2(F)$的一个**同构映射**

**可逆的线性变换**称为 向量空间 的**（线性）同构**

### 定理

1. 两个有限维线性空间$V_1(F)和V_2(F)$同构的充要条件是它们的维数相等.

## 线性扩张

### 定义

设$S$是线性空间$V(F)$的非空子集，我们把$S$中所有的有限子集（即$S$中任意$k$个向量$(k=1,2,3,...)$组成的子集在域$F$上的一切线性组合所组成的$V(F)$的子集合，称为$S$的线性扩张，记作$L(S)$，即

$$L(S)=\{\lambda_1\alpha_1+ \dots + \lambda_k \alpha_k | \lambda_1 , \dots ,\lambda_k \in F, \alpha_1 , \dots ,\alpha_k \in S , k \in N^* \}.$$

### 定理

线性空间$V(F)$的非空子集$S$的线性扩张$L(S)$是$V$中包含$S$的最小子空间.

## 线性相关性

### 定义

设$V(F)$是一个线性空间，$\alpha_1,\alpha_2,\dots,\alpha_m \in V$,如果存在不全为零的$\lambda_1, \lambda_2 ,\dots,\lambda_m \in F$使：

$$\lambda_1 \alpha_1 + \lambda_2 \alpha_2 + \dots + \lambda_m\alpha_m = 0 $$

成立，则称$\alpha_1,\alpha_2,\dots,\alpha_m$**线性相关**，否则称为**线性无关**.


### 定理

1. $V(F)$中的向量组$\alpha_1,\alpha_2,...,\alpha_m(m \geq 2)$线性相关的充分必要条件是

	- $\alpha_1,\alpha_2,\dots,\alpha_m$ 中有一个向量可由其余向量在域$F$上线性表示.
	
2. 若向量组$\{\alpha_1,\alpha_2,\dots,\alpha_n \}$ 线性无关，而向量组$\{\beta,\alpha_1,\alpha_2,\dots,\alpha_n\}$线性相关,则$\beta$可由$\alpha_1,\alpha_2,\dots,\alpha_n$线性表示，且表示法唯一


3. 设$V(F)$中向量组$\{ \beta_1,\beta_2,\dots,\beta_s\}$的每个向量可由另一个向量组$\{\alpha_1,\alpha_2,\dots,\alpha_r\}$线性表示，如果$s>r$，则$\{\beta_1,\beta_2,\dots,\beta_s\}$线性相关

### 等价命题
1. $\alpha_1,\alpha_2,\dots,\alpha_m(m{\geq}2)$线性无关的充分必要条件是其中任一个向量都不能由其余向量线性表示

2. (2)的推论：如果$\{\alpha_1,\alpha_2,\dots,\alpha_n\}$是$R^n$中线性无关的$n$个向量，则$R^n$中任一个向量$\alpha$可由$\alpha_1,\alpha_2,\dots,\alpha_n$线性表示，且表示法唯一.

## 有限维线性空间的基和维数

### 定义

如果线性空间$V(F)$的有限子集$B=\{\alpha_1,\dots,\alpha_n \}$线性无关，且$L(B)=V$，则称$B$为$V$的一组基，并称$n$为$V$的维数（或说$V$是$n$维线性空间）,记作

$$dimV=n.$$

### 定理

如果$$W$是$n$维线性空间$V$的一个子空间，则$W$的基可以扩充为$V$的基（即$W$的基可添加$V$中若干向量成为$V$的基

## 正交子空间和正交补

### 定义
* 设$\alpha \in V(R),W$是$V(R)$的一个子空间，如果$\forall\gamma\in W$,均有$(\alpha,\gamma)=0$,则称$\alpha与W$正交，记作$\alpha\perp W.$

* 设$W_1,W_2是V(R)$的两个子空间.如果$\forall\alpha\in W_1\beta\in W_2$均有$(\alpha,\beta) = 0$则称$W_1与W_2$互相正交，记作$W_1\perp W_2.$

* 如果子空间$W_1,W_2$正交，则$W_1+W_2$是直和.这时因为$\forall\alpha\in W_1\cap W_2$,均有$(\alpha,\alpha)=0$，故$\alpha=0$,从而$W_1\cap W_2=${0}.

* 设$W_1,W_2是V(R)的两个子空间，如果W_1\perp W_2,$且$W_1+W_2=V$,则称$W_2$是$W_1$的正交补，记作$W_1^{\perp}$

### 定理

如果$W_1$是n维欧氏空间$V(R)$的一个子空间，则$W_2=\{ \alpha|\alpha \in V  且 \alpha \perp W_1\}$ 是 $W_1$ 的正交补

### 证明

一般是用扩充的方法，特殊情况可以直接取行系数向量

## 欧氏空间的单位正交基

### 定义

设$B=\{ \varepsilon_1,\varepsilon_2,\dots,\varepsilon_n\}$ 是$n$ 维欧氏空间$V(R)$的一个子集，如果

$$(\varepsilon_i,\varepsilon_j)=\begin{cases}1,& i=j,\\ 0 , &i\neq j,\end{cases}\qquad i,j=1,2,...,n,$$

则称$B$为$V$的**单位正交基**（或称**标准正交基**）.

### 定理

1. 欧氏空间$V(R)$恒有单位正交基.

### 正交化过程

$$\beta_1=\alpha_1, \; \beta_2=\alpha_2+\lambda_{12}\beta_1.$$

$$\lambda_{12}=-\frac{(\alpha_2,\beta_1)}{(\beta_1,\beta_1)}.$$

最后再单位化.


## 内积空间

### 定义

在实空间$V(R)$上定义一个二元运算，使$V$中元素$\alpha,\beta$与一个实数相对应，记作$(\alpha,\beta),$如果$\forall \alpha,\beta \in V,\lambda\in R$满足：

1. $(\alpha,\beta)=(\beta,\alpha);$
2. $(\alpha+\beta,\gamma)=(\alpha,\gamma)+(\beta,\gamma)$
3. $(\lambda\alpha,\beta)=\lambda(\alpha,\beta);$
4. $(\alpha,\alpha)\geq 0$,等号成立当且仅当$\alpha=0$

则称实数$(\alpha,\beta)$为向量$\alpha,\beta$的内积，定义了内积的$V(R)$称为实内积空间，有限维实内积空间叫做**欧氏空间（Euclid空间）**.

### 长度定义

实内积空间$V(R)$中向量$\alpha$的长度定义为

$$|\alpha|=\sqrt{(\alpha,\alpha)}.$$

### 定理

设$V(R)$是一个内积空间，则$\forall\alpha,\beta\in V$，和$\lambda\in R$,有

1. $|\lambda\alpha|=|\lambda||\alpha|;$
2. $|(\alpha,\beta)|\leq|\alpha||\beta|;$
3. $|\alpha+\beta|\leq|\alpha|+|\beta|,$

其中（2）称为柯西-施瓦兹(Cauchy-Schwarz)不等式,（3）称为三角不等式.