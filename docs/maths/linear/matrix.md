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
* 将单位矩阵$E$作一次初等变换所得到的矩阵称为初等矩阵，与三种初等行、列变换对应的三类初等矩阵为：$$(1)将单位矩阵第i行（或列）乘c，得到初等倍乘矩阵E_i(c);$$$$(2)将单位矩阵第i行乘c加到第j行，或将第j列乘c加到第i列得到初等倍加矩阵E_{ij}(c)$$$$(3)将单位矩阵的第i,j行（或列）对换，得到初等对换矩阵E_{ij},$$
### 定理
* 对任一个可逆矩阵A，都可以作若干次初等行变换将其化为单位矩阵E，即存在初等矩阵$P_1,P_2,\cdots,P_k,$使得$$P_k\cdots P_2P_1A=E.$$
* 推论：可逆矩阵A可以表示为若干个初等矩阵的乘积。
* 推论：如果对可逆矩阵A和同阶单位矩阵E作同样的初等行变换，那么当A变为E时，E就变为$A^{-1}$.

## 矩阵的运算
### 定义
设$A=(a_{ij})_{m\times n},B=(b_{ij})_{m\times n},A,B\in M_{m\times n}(F),\lambda \in F,我们规定$$$A+B=(a_{ij}+b_{ij})_{m\times n},$$$$\lambda A=(\lambda a_{ij})_{m\times n}$$
### 矩阵乘法

* 定义
设$A=(a_{ij})_{p\times m},B=(b_{ij})_{m\times n},我们规定A与B之乘积AB=C=(c_{ij})$是一个$p\times n$型矩阵，它的第$i$行，第$j$列元素$$c_{ij}=\sum_{k=1}^ma_{ik}b_{kj}=a_{i1}b_{1j}+a_{i2}b_{2j}+\cdots+a_{im}b_{mj},$$$$i=1,\cdots,p;j=1,\cdots,n.$$
	* PS:乘积AB当且仅当A的列数等于B的行数时才有意义，否者A不能左乘B
	* 满足结合律、数乘交换、左右分配律
### 定理
* 设$\sigma\in L(V_1,V_2)$关于$V_1和V_2$的基$B_1和基B_2$的矩阵$A=(a_{ij})_{m\times n}$如（4-11）式子$$\sigma(\varepsilon_1,\varepsilon_2,\cdots,\varepsilon_n)=(e_1,e_2,\cdots,e_m)A,\qquad\qquad(4-11)$$$\alpha与\sigma(\alpha)$如(4-12)式$$\alpha=(\varepsilon_1,\varepsilon_2,\cdots,\varepsilon_n)X,\qquad\sigma(\alpha)=(e_1,e_2,\cdots,e_m)Y$$则$$Y=AX.$$
* $AB=0$

## 矩阵的秩

### 定义
* 设$A=(a_{ij})_{m\times n}$是线性映射$\sigma$对应的矩阵，我们把秩$(\sigma)$也称为矩阵$A$秩，记作秩(A)或r（A）
* 矩阵A的n个列向量的秩称为A的列秩；
* 矩阵A的m个行向量的秩称为A的行秩;
### 定理
* 设矩阵$A=(a_{ij})_{m\times n}是\sigma\in L(V_1,V_2)关于V_1和V_2的基B_1=\lbrace\sigma(\varepsilon_1),\cdots,\sigma(\varepsilon)\rbrace$[[矩阵的秩]]和$B_2=\lbrace e_1,e_2,\cdots,e_m\rbrace$对应的矩阵，则秩(A)=A的列秩.
* 对于任一矩阵$A=(a_{ij})_{m\times n},都有$$$A的行秩=A的列秩$$
* 初等行变换和初等列变换都不改变矩阵的秩.
* 若秩$(A_{m\times n})=r,$则存在可逆矩阵P和Q，使得$$PAQ=U_r$$其中r个非零行向量为n维单位向量$e_1,e_2,\cdots,e_r$
* 它是用双向的小于等于证明的相等，并非直接通过式子表示相等。
## 矩阵的转置

### 定义
* 把矩阵$A=(a_{ij})_{m\times n}$的行列依次互换得到的一个$n\times m$矩阵，称为A的转置矩阵，记作$A^T=(a’_{ji})_{m\times n}$,其中$a'_{ji}=a_{ij},(i=1,2,\cdots,m;j=1,2,\cdots,n)$
* 矩阵的转置运算满足以下运算律：$$(1)(A^T)^T=A;\qquad(2)(A+B)^T=A^T+B^T\qquad(3)(\lambda A)^T=\lambda A^T(\lambda是数量$$$$(4)(AB)^T=B^TA^T;\qquad (5)(A^T)^{-1}=(A^{-1})^T$$
* 设$A=(a_{ij})_{n\times n}，$如果$\forall i,j=1,\cdots,n$均有$a_{ji}=a_{ij}$,则A陈伟对称矩阵，如均有$a_{ji}=-a_{ij},$则A称为反对称矩阵.
* A为对称矩阵的充要条件是$A^T=A;$
* A为反对称矩阵的充要条件是$A^T=-A;$


### 旋转变换

>  可以给出更加广泛的三维形式，连接到图形学的旋转

$$\begin{pmatrix} cos\theta & -sin\theta \\ sin\theta & cos\theta \end{pmatrix}$$

