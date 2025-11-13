## Young不等式

**常见形式**: $\forall a, b \geq 0 , and \; p,q >1 \;s.t.\; \frac{1}{p} + \frac{1}{q}=1$,有

$$ab \leq \frac{a^p}{p} + \frac{b^q}{q}$$

**证明思路**：

1. 利用凸函数的定义：
    - 函数$f(X) = \frac{x^p}{p}$ 对 $x \geq 0$是凸函数
    - 凸函数定义：$f(y) \geq f(x) + f'(x)(y-x)$
2. 对$x=a,y=b^{q-1}$应用凸性公式:

$$\frac{a^p}{p} + \frac{b^q}{q} - ab \geq 0$$


常用于证明Holder不等式

## Holder不等式

设 $x=(x_1,\dots,x_n), y=(y_1,\dots,y_n) \in \mathbb{R}^n$，$p,q>1$ 满足：

$$\frac{1}{p} + \frac{1}{q} = 1.$$

则有：

$$|\underset{i=1}{\overset{n}{\sum}} x_iy_i| \leq \left(\underset{i=1}{\overset{n}{\sum}} |x_i|^p\right)^{1/p} \left(\underset{i=1}{\overset{n}{\sum}} |y_i|^q\right)^{1/q} = \|x\|_p \|y\|_q$$

> 当 $q=p=2$时，就是著名的 Cauchy-Schwarz不等式。

**积分形式**

$$\left|\int f(x)g(x)dx\right| \leq \left(\int |f(x)|^pdx\right)^{1/p} \left(\int |g(x)|^qdx\right)^{1/q}$$

### 证明

#### 有限维向量形式

将$a=\frac{|x_i|}{\|x\|_p}, b = \frac{|y_i|}{\|y\|_q}$,代入 Young不等式，有：

$$\frac{|x_i|}{\|x\|_p} \cdot \frac{|y_i|}{\|y\|_q} \leq \frac{1}{p}(\frac{|x_i|}{\|x\|_p})^p + \frac{1}{q}(\frac{|y_i|}{\|y\|_q})^q$$

对所有项求和，则得到：

$$\underset{i=1}{\overset{n}{\sum}}|x_iy_i| \leq \|x\|_p \|y\|_q$$

#### 积分形式

设 $f \in L^p, g \in L^q, \frac{1}{p} + \frac{1}{q} = 1$

1. 规范化函数

$$F(x) = \frac{f(x)}{\|f\|_p}, G(x) = \frac{g(x)}{\|g\|_q}$$

2. 应用Young不等式

对于每个点$x$:

$$F(x)G(x) \leq \frac{F(x)^p}{p} + \frac{G(x)^q}{q}$$

3. 对空间积分

$$\int F(x)G(x)dx \leq \frac{1}{p}\int F(x)^pdx + \frac{1}{q}\int G(x)^qdx = \frac{1}{p} + \frac{1}{q} = 1$$

4. 还原到原函数

$$\int |f(x)g(x)|dx = \|f\|_p\|g\|_q \int F(x)G(x)dx \leq \|f\|_p\|g\|_q$$