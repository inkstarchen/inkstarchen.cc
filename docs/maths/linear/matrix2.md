# 行列式

## 方阵乘积的行列式
### 定理 
* 若$A,B\in M_n(F),则$$$|AB|=|A||B|.$$
* n阶矩阵A可逆的充要条件是$|A|\neq 0$
### 伴随矩阵
s$$A^*=\begin{pmatrix}A_{11} & A_{21} & \cdots &A_{n1} \\ A_{12}& A_{22} & \cdots & A_{n2}\\ \vdots & & & \vdots \\ A_{1n} & A_{2n} & \cdots &A_{nn} \end{pmatrix},$$
A*称为A的伴随矩阵有
* $AA^*=A^*A=|A|E$
* $A(\frac{1}{|A|}A^*)=(\frac{1}{|A|}A^*)A=E$
* $A^{-1}=\frac{1}{|A|}A^*.$

### 定义
* 矩阵$A=(a_{ij})_{m\times n}的任意k行（i_1<i_2<\cdots<i_k行）和任意k列（j_1<j_2<\cdots<j_k列）的交点上的k^2个元素排成的行列式$$$\left | \begin{matrix} a_{i_1j_1} &a_{i_1j_2} &\cdots &a_{i_1j_k}\\ a_{i_2j_1} & a_{i_2j_2} &\cdots &a_{i_2j_k}\\ \vdots & & & \vdots \\ a_{i_kj_1} & a_{i_kj_2}& \cdots &a_{i_kj_k}\end{matrix} \right |$$
* 称为矩阵$A$的一个$k$阶子行列式，简称$A$的$k$阶子式，当上式等于零时，称为$k$阶零子式，否则叫非零子式.当$A$为方阵且上式中$j_t=i_t(t=1,2,\cdots,k)$时，称为$A的k阶主子式$
* 如果矩阵$A存在r阶$非零子式，而所有r+1阶子式（如果有的话）都等于零，则矩阵$A$的非零子式的最高阶数为$r$因为所有$r+1$阶子式都等于零，可以根据按一列（行）的展开式推出所有更高阶的子式也都等于零.
* 矩阵$A$的非零子式的最高阶数$r$称为$A$的行列式秩.
### 定理
* 秩（A）=r的充要条件是$A$的行列式的秩为r.
* 若$A为n阶$矩阵，则齐次线性方程组$AX=0$有非零解的充要条件为，$|A|=0,即秩（A）<n$

## 行列式一列（行）的展开式
### 定义
* 在n阶行列式$D=|a_{ij}|_{n\times n}中$，去掉元素$a_{ij}$所在的第$i$行和第$j$列的所有元素而得到的n-1阶行列式，称为元素$a_{ij}$的余子式子，记作$M_{ij}$，并把数$$A_{ij}=(-1)^{i+j}M_{ij}$$称为元素$a_{ij}$的代数余子式.
### 定理
* 设$D=|a_{ij}|_{n\times n},则$$$D=\sum_{k=1}^na_{kj}A_{kj}=a_{1j}A_{1j}+a_{2j}A_{2j}+\cdots+a_{nj}A_{nj},\qquad j=1,\cdots,n,$$$$D=\sum_{k=1}^na_{ik}A_{ik}=a_{i1}A_{i1}+a_{i2}A_{i2}+\cdots+a_{in}A_{in},\qquad i=1,\cdots,n.$$上式称为D对第$j$列的展开式，下式称为D对$i$行的展开式，
* n阶行列式$D=|a_{ij}|_{n\times n}$的某一列（或行）元素与另一列（或行）相应元素的代数余子式的乘积之和等于零，即$$\sum_{k=1}^na_{kj}A_{ki}=a_{1j}A_{1i}+a_{2j}A_{2i}+\cdots +a_{nj}A_{ni}=0,\quad j\neq i,$$$$\sum_{k=1}^na_{jk}A_{ik}=a_{j1}A_{i1}+a_{j2}A_{i2}+\cdots + a_{jn}A_{in} = 0,\quad j\neq i.$$

## 子空间的交、和与直和

### 定义
* 设$W_1$,$W_2$是线性空间$V(F)$的两个子空间，则$$W_1{\cap}W_2={\lbrace}{\alpha|\alpha\in W_1 且\alpha\in W_2}{\rbrace},$$$$W_1+W_2={\lbrace\alpha|\alpha=\alpha_1+\alpha_2,\alpha_1\in W_1,\alpha_2\in W_2}{\rbrace}$$分别称为$W_1,W_2$的交与和.
### 子空间的维数公式

$$dimW_1+dimW_2=dim(W_1+W_2)+dim(W_1{\cap}W_2).$$
### 直和的定义
* 设$W_1,W_2$是$V(F)$两个子空间，如果$W_1{\cap}W_2={\lbrace}0{\rbrace}$,则$W_1,W_2$叫做$W_1$与$W_2$的直和，记作$W_1,{\oplus}W_2.$
### 定理 对子空间$W_1,W_2,$下列命题等价：
（1）$W_1+W_2$是直和，即$W_1{\cap}W_2={\lbrace}0{\rbrace};$
（2）$W_1+W_2$中的每个向量${\alpha}$的分解式${\alpha}={\alpha_1+\alpha_2}({\alpha_1\in W_1,\alpha_2 \in W_2},)$是唯一的
（3）零向量0的分解式$0={\alpha_1+\alpha_2({\alpha_1\in W_1,\alpha_2 \in W_2},)},$仅当${\alpha_1,\alpha_2}=0$才成立
（4）$dim({W_1+W_2})=dimW_1+dimW_2.$


