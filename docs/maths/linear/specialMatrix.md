# 特殊矩阵分类

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
## 相抵标准型
### 定义
* 设$A,B\in M_{m\times n}(F),$如果A经过初等变换可以化为B，就称A相抵于B,（或说A等价于B），记作$A\cong B$.（其充要条件是秩(A)=秩(B)）
### 定理
* 设$A\in M_n(F),$则下列命题等价：$$(1)A可逆；\quad(2)r(A)=n;\quad(3)A的n个列（行）向量线性无关;$$$$(4)齐次线性方程组AX=0只有零解$$
* $$秩(A+B)\leq秩(A)+秩(B),$$$$秩(AB)\leq min(秩(A),秩(B))$$


## 正定二次型

* 定义
	* n元实二次型$$ f(x_1,x_2,...,x_n)=X^TAX$$称为正定二次型，如果$${\forall}X{\ne}0,(X{\in}R^n)$$恒有$$X^TAX>0$$正定二次型$$X^TAX$$所对应的矩阵A叫做正定矩阵.
* 基本结论：
	* （1）n元实二次型（标准型）$$f=(x_1,x_2,...,x_n)=d_1x_1^2+d_2x_2^2+...+d_nx_n^2$$正定的充分必要条件是$$d_i>0(i=1,2,...,n).$$
	* 一个二次型的正定性可由其相合标准形（或规范形）来判定
		* 可使用配方法或相应的初等行列变换
* 定理：
	* 1.对于n阶实对称矩阵A，下列命题等价：
		* $$(1).X^TAX是正定二次型（或A是正定矩阵）$$
		* $$(2).A的正惯性指数为n，即A{\simeq}E$$
		* $$(3).存在可逆矩阵P，使得A=P^TP$$
		* $$(4).A的n个特征值λ_1,λ_2,...,λ_n都大于零$$
		利用这一定理可以证明若$$A为正定矩阵，则A^{-1}也是正定矩阵.$$
		* **上述可以用于等价判断正定性**
	* 2.A正定的必要条件
		* $$(1).A的主对角元a_{ii}>0(i=1,2,...,n)$$
		* $$(2).A的行列式detA>0.$$
		* **上述可以用于简单的初步判断正定性**
	* 3.A正定的充分必要条件
		* A的n个顺序主子式（左上角主子式）都大于零
$$detA_k=det \begin{pmatrix} a_{11} & a_{12} &\cdots & a_{1k}\\ a_{21} & a_{22} & \cdots & a_{2k}\\ \vdots & & & \vdots \\ a_{k1} & a_{k2} & \cdots & a_{kk} \end{pmatrix}>0,\qquad k=1,2,\cdots,n.$$
		* （充分性证明思路：数学归纳法+矩阵分块（进行初等变换）+定理1）
		* ps：需要充分利用有关正定性的所有有关概念去辅助判断
	* 若A是n阶正定矩阵，则存在正定矩阵B使得$$A=B^2$$
* 定义：
	* 如果n元实二次型$$X^TAX$$$$满足{\forall}X{\ne}0恒有：$$
		* $$(1).X^TAX<0,则称之为负定二次型，相应地称A为负定矩阵；$$
		* $$(2).X^TAX{\geq}0,则称之为半正定二次型，相应地称A为半正定矩阵；$$
		* $$(3).X^TAX>0,则称之为正定二次型，相应地称A为正定矩阵；$$
		* 除此以外称为不定二次型
		* 半正（负）定地充要条件是A的正（负）惯性指数等于r（A）
		* A半正定的充分必要条件是，A的各阶主子式>=0

## 正交变换和正交矩阵

### 定义
* 欧氏空间$V(R)$的一个线性变换$\sigma$称为正交变换，如果$\forall \alpha,\beta\in V,$都有$$(\sigma(\alpha),\sigma(\beta))=(\alpha,\beta).$$与之等价的条件是$$|\sigma(\alpha)|=|\alpha|$$
* 欧氏空间$V(R)的正交变换\sigma关于V$的单位正交基所对应的矩阵$A$称为正交矩阵
	* 设$A=(a_{ij})_{n\times n}=(\alpha_1,\alpha_2,\cdots,\alpha_n)是$正交变换$\sigma在V的单位正交基$$\lbrace\varepsilon_1,\varepsilon_2,\cdots,\varepsilon_n\rbrace$下多对应的矩阵，即$$\sigma(\varepsilon_1,\varepsilon_2,\cdots,\varepsilon_n)=(\varepsilon_1,\varepsilon_2,\cdots,\varepsilon_n)A,$$于是$a_{ij}\in R$，而且$$(\varepsilon_i,\varepsilon_j)=(\sigma(\varepsilon_i),\sigma(\varepsilon_j))=(\sum_{k=1}^na_{ki}\varepsilon_k,\sum_{l=1}^na_{lj}\varepsilon_l)$$$$=\sum_{k=1}^na_{ki}a_{kj}=\alpha_j^T\alpha_i$$$$=(\alpha_i,\alpha_j)=\begin{cases}1,\qquad j=i, \\ 0,\qquad j\neq i,\end{cases}\qquad i,j=1,2,\cdots,n,$$所以A的列向量$\alpha_1,\alpha_2,\cdots,\alpha_n$是关于$R^n$的标准内积的一组的单位正交基
	* 进一步得到$A^TA=E.$
### 定义
* n阶实矩阵$A$称为正交矩阵，如果$A^TA=E$(或：如果A的列向量组是$R^n$的一组单位正交基).
* 正交矩阵还有以下性质：
* （1）若$A$为正交矩阵，则$A^{-1}=A^T,且A^T$也是正交矩阵；
* （2）若$A$是正交矩阵，则$|A|=1或-1$;
* （3）若$A,B$都是正交矩阵，则$AB$也是正交矩阵

## 实二次型的标准性 实对称矩阵的相合标准形

### 定理
* （主轴定理）对于任一个n元二次型$f(x_1,x_2,\cdots,x_n)=X^TAX,$都存在正交变换$X=QY,使得$$$X^TAX=Y^T(Q^TAQ)Y=\lambda_1y_1^2+\cdots+\lambda_ny_n^2.$$其中$\lambda_1,\cdots,\lambda_n$是实对称矩阵A的n个特征值，Q的n个列向量是A属于$\lambda_1,\cdots,\lambda_n$的n个单位正交的特征向量.
* （惯性定理）实对称矩阵A的正、负惯性指数是由A唯一确定的.


## 线性变换在不同基下的矩阵表示 相似矩阵

### 定理
* 设线性变换$\sigma\in L(V,V),B_1=\lbrace\alpha_1,\cdots,\alpha_n\rbrace和$$B_2=\lbrace\beta_1,\cdots,\beta_n\rbrace$是线性空间$V(F)$的两组基，基$B_1$变为基$B_2$的变换矩阵为C，如果$\sigma$在基$B_1$下的矩阵为$A$,则$\sigma$关于基$B_2$所对应的矩阵为$C^{-1}AC.$
### 定义
* 如果对于$A,B\in M_n(F)$，存在可逆矩阵$C\in M_n(F)$,使得$$C^{-1}AC=B,$$则称$A$相似于$B$，记作$A\sim B$.