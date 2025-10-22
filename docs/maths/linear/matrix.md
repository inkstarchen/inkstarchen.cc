# 矩阵

> 条目质量：低 | 是有用的，但是还需要更加详尽的解释

即元素排列的矩阵数表,当作用到基上时，代表了基之间的变换关系，矩阵的每一列都代表它变换的规则

### 定义

* 对角矩阵（方阵中非主对角线上的所有元素都是零）
* 上（下）三角矩阵：主对角线之下（上）的所有元素都是零

有关矩阵计算，先判断矩阵的阶数

一阶矩阵转置后还是其本身

秩为一的矩阵，可以写成列向量乘以行向量的形式

## 矩阵的初等变换和初等矩阵

### 定义

将单位矩阵$E$作一次初等变换所得到的矩阵称为初等矩阵，与三种初等行、列变换对应的三类初等矩阵为：

1. 将单位矩阵第$i$行（或列）乘$c$，得到初等倍乘矩阵$E_i(c)$;
2. 将单位矩阵第$i$行乘$c$加到第$j$行，或将第$j$列乘$c$加到第$i$列得到初等倍加矩阵$E_{ij}(c)$
3. 将单位矩阵的第$i,j$行（或列）对换，得到初等对换矩阵$E_{ij},$

### 定理

对任一个可逆矩阵$A$，都可以作若干次初等行变换将其化为单位矩阵$E$，即存在初等矩阵$P_1,P_2,\cdots,P_k,$使得

$$P_k\cdots P_2P_1A=E.$$

**推论1：**可逆矩阵$A$可以表示为若干个初等矩阵的乘积。

**推论2：**如果对可逆矩阵$A$和同阶单位矩阵$E$作同样的初等行变换，那么当$A$变为$E$时，$E$就变为$A^{-1}$.


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



