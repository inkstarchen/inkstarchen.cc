# 特征值与特征向量

### 定义
* 设$\sigma$是线性空间$V(F)$的一个线性变换，如果存在$数\lambda_0\in F和$非零向量$\xi\in V,使得$$$\sigma(\xi)=\lambda_0\xi,$$则称数$\lambda_0 为\sigma 的$一个特征值，称非零向量$\xi为\sigma$的属于其特征值$\lambda_0$的特征向量.
* 设矩阵$A\in M_n(F)$,如果存在数$\lambda_0\in F$和非零向量$X\in F^n$,使得$$AX=\lambda_0X,$$则称数$\lambda_0为A$的一个特征值，称非零向量$X为A$的属于其特征值$\lambda_0$的特征向量.$$f(\lambda)=|\lambda E-A|$$上式被叫做矩阵$A$的特征多项式
### 定理
* n阶矩阵$A=(a_{ij})_{n\times n}的特征多项式为$$$f(\lambda)=\lambda^n+b_1\lambda^{n-1}+\cdots+b_k\lambda^{n-1}+\cdots+b_{n-1}\lambda+b_n,$$其中系数$b_k=(-1)^kS_k,S_k为A的全体k阶主子式之和，即$$$S_k=\sum_{1\leq i_1< i_2<\cdots<i_k\leq n}\left | \begin{matrix}a_{i_1i_1} & a_{i_1i_2}&\cdots& a_{i_1i_k}\\ a_{i_2i_1} & a_{i_2i_2} & \cdots & a_{i_2i_k}\\ \vdots & & & \vdots \\ a_{i_ki_1} & a_{i_ki_2} & \cdots & a_{i_ki_k} \end{matrix} \right |.$$
* 推论若n阶矩阵$A=(a_{ij})_{n\times n}$的n个特征值为$\lambda_1,\lambda_2,\cdots,\lambda_n,则$$$(1)\quad \sum_{i=1}^n\lambda_i=\sum_{i=1}^na_{ii},\qquad(2)\quad\prod_{i=1}^n\lambda_i=|A|$$
* 若矩阵$A与B$相似，则它们的特征多项式相等，即$$|\lambda E-A|=|\lambda E-B|$$
* 设$\lambda_j和V_{\lambda_j}(j=1,\cdots,m)$式n维线性空间$V(F)的线性变换\sigma和m$个互不相同的特征值及相应的特征子空间，则$m$个特征子空间的和是直和，即$$dim(V_{\lambda_1}+V_{\lambda_2}+\cdots+V_{\lambda_m})=\sum_{j=1}^mdimV_{\lambda_j}$$
* 推论1：若$\lambda_1,\cdots,\lambda_m$,是$\sigma$的互不相同的特征值，则$$V_{\lambda_i}\cap\sum_{j\neq i}V_{\lambda_j}=\lbrace0\rbrace,\qquad i=1,\cdots,m.$$由此又可得，$\lambda_i \neq \lambda_j$时，$V_{\lambda_1}\cap V_{\lambda_j}=\lbrace 0 \rbrace$,这表明一个特征向量不能属于两个不同的特征值
* 推论2：$\sigma$的不同特征值$\lambda_1,\cdots,\lambda_m$对应的特征向量$\xi_1,\cdots,\xi_m$是线性无关的，这时因为：如果$\xi_1,\cdots,\xi_m$线性相关，则存在$\xi_j$可由其他特征向量线性表出，不妨设$$\xi_1=c_2\xi_2+\cdots,c_m\xi_m.$$于是$\xi_1\in V_{\lambda_1}\cap\sum_{j=2}^m V_{\lambda_j}$，这与推论一矛盾
* 推论3：$\sigma$的不同特征值$\lambda_1,\cdots,\lambda_m$的特征子空间$V_{\lambda_1},V_{\lambda_2},\cdots,V_{\lambda_m}$的基向量合在一起构成的向量组是线性无关的，这个线性无关的向量组是$V_{\lambda_1}+V_{\lambda_2}+\cdots+V_{\lambda_m}$的基.