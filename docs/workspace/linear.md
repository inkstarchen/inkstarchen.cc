# 向量

## 向量的表示

一个向量可以用$\vec{a}$或$\textbf{a}$表示，或者用起始点到目标点的线段表示$\vec{AB} = B - A$

- 向量拥有长度$||\vec{a}||$和方向，但没有固定起始点
- 转化为单位向量$\hat{a} = \frac{\vec{a}}{||\vec{a}||}$

## 向量的运算

- 点乘
- 叉乘

## 线性空间的基与坐标

### 定义

设$B=\{\beta_1,\beta_2,...,\beta_n\}$是$n$维线性空间$V(F)$中的一组基，如果$V$中元素$\alpha$表示为

$$\alpha=a_1\beta_1+a_2\beta_2+...+a_n\beta_n$$

则其系数组$a_1,a_2,...,a_n$叫做$\alpha$在基$B$下的坐标，记作$\alpha_B=(a_1,a_2,...,a_n).$

## 向量组的秩

### 定义

设$S$是线性空间$V(F)$的一个子集，如果$S$中存在线性无关的向量组

$$B=\{\alpha_1,..,\alpha_r\}$$

且$S$中每个向量可由$B$线性表示，则$B$中向量的个数$r$叫做$S$的秩，记作秩$(S)=r$.

> **PS:** 如果S是有限维线性空间V（F）的子空间，那么S的秩就是S的维数。

由$秩(S)$与$L(S)$的定义以及定理可得以下结论：

1. $秩(S)=r$，则$S$中任何$r+1$个向量都线性相关.因此$S$中任何线性无关的向量组至多含有$r$个向量，并把含$r$个线性无关向量的向量组称为$S$的极大线性无关组.


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

## 特征值与特征向量
### 定义

设$\sigma$是线性空间$V(F)$的一个线性变换，如果存在数$\lambda_0\in F$和非零向量$\xi \in V$,使得

$$\sigma(\xi)=\lambda_0\xi,$$

则称数$\lambda_0$为$\sigma$的一个特征值，称非零向量$\xi$为$\sigma$的属于其特征值$\lambda_0$的特征向量.

## 特征多项式

### 定义

设矩阵$A\in M_n(F)$,如果存在数$\lambda_0\in F$和非零向量$X\in F^n$,使得

$$AX=\lambda_0X,$$

则称数$\lambda_0$为$A$的一个特征值，称非零向量$X$为$A$的属于其特征值$\lambda_0$的特征向量.

$$f(\lambda)=|\lambda E-A|$$

上式被叫做矩阵$A$的**特征多项式**

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

称为 **$\sigma$的像** (或称$\sigma$的值域)

- $V_2$的零元$0_2$在$\sigma$下的完全原像

$$\sigma^{-1}(0_2)=\lbrace\alpha|\sigma(\alpha)=0_2,\alpha\in V_1\rbrace$$

称为 **$\sigma$的核**


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




### 定理

对任一个可逆矩阵$A$，都可以作若干次初等行变换将其化为单位矩阵$E$，即存在初等矩阵$P_1,P_2,\cdots,P_k,$使得

$$P_k\cdots P_2P_1A=E.$$

**推论1：**可逆矩阵$A$可以表示为若干个初等矩阵的乘积。

**推论2：**如果对可逆矩阵$A$和同阶单位矩阵$E$作同样的初等行变换，那么当$A$变为$E$时，$E$就变为$A^{-1}$.


## 矩阵的迹

对于一个 $n \times n$ 的方阵 $A$，它的迹定义为**主对角线上所有元素的和**：

$$
\operatorname{tr}(A) = \sum_{i=1}^n a_{ii}
$$

其中 $a_{ii}$ 是矩阵 $A$ 第 $i$ 行第 $i$ 列的元素。

## 矩阵的秩

### 定义
设$A=(a_{ij})_{m\times n}$是线性映射$\sigma$对应的矩阵，我们把秩$(\sigma)$也称为矩阵$A$秩，记作$秩(A)$或$r（A）$

* 矩阵$A$的$n$个列向量的秩称为$A$的列秩；
* 矩阵$A$的$m$个行向量的秩称为$A$的行秩;

### 定理
1. 设矩阵$A=(a_{ij})_{m\times n}$是$\sigma\in L(V_1,V_2)$关于$V_1$和$V_2$的基$B_1=\lbrace\sigma(\varepsilon_1),\cdots,\sigma(\varepsilon)\rbrace$和$B_2=\lbrace e_1,e_2,\cdots,e_m\rbrace$对应的矩阵，则$秩(A)=A的列秩$.

2. 对于任一矩阵$A=(a_{ij})_{m\times n}$,都有

$$A的行秩=A的列秩$$

3. 初等行变换和初等列变换都不改变矩阵的秩.

4. 若秩$(A_{m\times n})=r,$则存在可逆矩阵$P$和$Q$，使得

$$PAQ=U_r$$

其中$r$个非零行向量为$n$维单位向量$e_1,e_2,\cdots,e_r$

* 它是用双向的小于等于证明的相等，并非直接通过式子表示相等。
## 矩阵的转置

### 定义

把矩阵$A=(a_{ij})_{m\times n}$的行列依次互换得到的一个$n\times m$矩阵，称为$A$的转置矩阵，记作$A^T=(a’_{ji})_{m\times n}$,其中$a'_{ji}=a_{ij},(i=1,2,\cdots,m;j=1,2,\cdots,n)$

* 矩阵的转置运算满足以下运算律：

1. $(A^T)^T=A;$

2. $(A+B)^T=A^T+B^T$

3. $(\lambda A)^T=\lambda A^T$($\lambda$是数量)

4. $(AB)^T=B^TA^T$

5. $(A^T)^{-1}=(A^{-1})^T$

设$A=(a_{ij})_{n\times n}$,如果$\forall i,j=1,\cdots,n$均有$a_{ji}=a_{ij}$,则$A称为**对称矩阵**，如均有$a_{ji}=-a_{ij}$,则$A$称为反对称矩阵.

* $A$为对称矩阵的充要条件是$A^T=A;$
* $A$为反对称矩阵的充要条件是$A^T=-A;$


### 旋转变换

>  可以给出更加广泛的三维形式，连接到图形学的旋转

$$\begin{pmatrix} cos\theta & -sin\theta \\ sin\theta & cos\theta \end{pmatrix}$$


## 变换矩阵与齐次坐标系(Homogenous coordinates)

> 在计算机图形学和计算机视觉中常需要对图形做变换，就是通过矩阵来实现

### 缩放矩阵(Scale Matrix)

<img src="https://github.com/inkstarchen/picx-images-hosting/raw/master/20250922/scale.1vz0nnodw0.webp" style="width:400px;margin-left:200px;"/>

> 图源: GAMES101 Lingqi Yan, UC Santa Barbara

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$

### 镜像矩阵(Reflection Matrix)

<img src="https://github.com/inkstarchen/picx-images-hosting/raw/master/20250922/flect.8admj9f7y1.webp" style="width:400px;margin-left:200px;"/>

> 图源: GAMES101 Lingqi Yan, UC Santa Barbara

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$

### 形变矩阵(Shear Matrix)

<img src="https://github.com/inkstarchen/picx-images-hosting/raw/master/20250922/shear.3k8dkurqfq.webp" style="width:400px;margin-left:200px;"/>

> 图源: GAMES101 Lingqi Yan, UC Santa Barbara

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$

### 旋转矩阵(Rotationg Matrix)

<img src="https://github.com/inkstarchen/picx-images-hosting/raw/master/20250922/rotate.7axj63hmbn.webp" style="width:400px;margin-left:200px;"/>

> 图源: GAMES101 Lingqi Yan, UC Santa Barbara

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} cos\theta & -sin\theta \\ sin\theta & cos\theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$

### 齐次坐标系

#### 仿射变换(Affine Transformations)

Affine map = linear map + translation

$$\left( \begin{array}{c}x' \\ y' \end{array} \right) = \left( \begin{array}{c}a & b \\ c & d \end{array} \right) \cdot \left( \begin{array}{c}x \\ y \end{array} \right) + \left( \begin{array}{c}t_x \\ t_y \end{array} \right)$$

- 但是我们仍然想要用一个矩阵来表示变换，则需要引入**齐次坐标**(homogenous coordinates)

$$\left[ \begin{array}{c} x \\ y \\ z \\ w \end{array} \right] \leftrightarrow (\frac{x}{w}, \frac{y}{w}, \frac{z}{w},1)$$

- 齐次坐标不唯一

$$\left( \begin{array}{c}x' \\ y' \\ 1 \end{array} \right) = \left( \begin{array}{c}a & b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{array} \right) \cdot \left( \begin{array}{c}x \\ y \\ 1\end{array} \right)$$


> 对逆变换的讨论请参照 矩阵可逆条目


## 矩阵可逆
* n阶矩阵A可逆的充要条件是$|A|\neq 0$

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

如果$W$是$n$维线性空间$V$的一个子空间，则$W$的基可以扩充为$V$的基（即$W$的基可添加$V$中若干向量成为$V$的基

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


## 可逆矩阵

### 定义
* 设$A\in M_n(F),$如果存在$B\in M_n(F)$,使得$$BA=AB=E,$$则称矩阵$A$是可逆的，并把$B叫做A$的逆矩阵
* 逆矩阵具有唯一性
### 定理
* 设$B,A\in M_n(F),若AB=E,则必有BA=E,即A,B互为逆矩阵.$
* 主对角元都是非零数的对角阵是可逆的，且$a_{ii} ->a_{ii}^{-1}$
### 求逆矩阵
* 建立增广矩阵，进行初等变换


## 实对称矩阵的对角化

### 定义
* 设$A=(a_{ij})\in M_{m\times n}(C)(C为复数域)$，我们把$\bar{A}=\bar{(a_{ij})}_{m\times n}$叫做$A$的共轭矩阵，其中$\bar{a_{ij}}$是$a_{ij}$的共轭复数..
### 定理
* 实对称矩阵A的特征值都是实数
* 实对称矩阵A的属于不同特征值的特征向量实正交的.
* 若A是一个n阶实对称矩阵，则存在n阶正交矩阵Q，使得$$Q^{-1}AQ=diag(\lambda_1,\lambda_2,\cdots,\lambda_n).$$

## 正交变换和正交矩阵

### 定义
* 欧氏空间$V(R)$的一个线性变换$\sigma$称为正交变换，如果$\forall \alpha,\beta\in V,$都有

$$(\sigma(\alpha),\sigma(\beta))=(\alpha,\beta).$$与之等价的条件是$$|\sigma(\alpha)|=|\alpha|$$

* 欧氏空间$V(R)的正交变换\sigma关于V$的单位正交基所对应的矩阵$A$称为正交矩阵
	* 设$A=(a_{ij})_{n\times n}=(\alpha_1,\alpha_2,\cdots,\alpha_n)是$正交变换$\sigma$在V的单位正交基 $\lbrace \varepsilon_1,\varepsilon_2,\cdots\varepsilon_n \rbrace$ 下多对应的矩阵，即
	
	$$\sigma(\varepsilon_1,\varepsilon_2,\cdots,\varepsilon_n)=(\varepsilon_1,\varepsilon_2,\cdots,\varepsilon_n)A,$$
	
	于是$a_{ij}\in R$，而且

$$(\varepsilon_i,\varepsilon_j)=(\sigma(\varepsilon_i),\sigma(\varepsilon_j))=(\sum_{k=1}^na_{ki}\varepsilon_k,\sum_{l=1}^na_{lj}\varepsilon_l)$$

$$=\sum_{k=1}^na_{ki}a_{kj}=\alpha_j^T\alpha_i$$

$$=(\alpha_i,\alpha_j)=\begin{cases}1,\qquad j=i, \\ 0,\qquad j\neq i,\end{cases}\qquad i,j=1,2,\cdots,n,$$

所以A的列向量$\alpha_1,\alpha_2,\cdots,\alpha_n$是关于$R^n$的标准内积的一组的单位正交基
	* 进一步得到$A^TA=E.$
### 定义
* n阶实矩阵$A$称为正交矩阵，如果$A^TA=E$(或：如果A的列向量组是$R^n$的一组单位正交基).
* 正交矩阵还有以下性质：
* （1）若$A$为正交矩阵，则$A^{-1}=A^T,且A^T$也是正交矩阵；
* （2）若$A$是正交矩阵，则$|A|=1或-1$;
* （3）若$A,B$都是正交矩阵，则$AB$也是正交矩阵


