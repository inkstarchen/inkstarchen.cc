# 无界函数反常积分

> 条目质量：中 | 可查阅，但是无用，无例子

$$设函数f(x)在(a,b]上有定义，且在x=a的任一右邻域内无界，在任何内闭区$$
a为瑕点，任何有限区间都可积，若a->+∞存在极限，则称其收敛
瑕点在中间，则拆分为两部分（两个反常积分都收敛）

基于积分限的变换（sinx找配套cos，tanx找cotx）

### 无限区间上反常积分敛散性的判别
#### Cauchy 收敛原理
* 反常积分$\int^{+\infty}_af(x)dx$收敛的充分必要条件是：对任意给定的$\varepsilon>0$,存在$A_0\geq a,$使得对任意$A,A'\geq A_0,有$$$|\int^{A'}_Af(x)dx|<\varepsilon$$
### 定义
* 设$f(x)$在任意有限区间$[a,A]\subset [a,+\infty)$上可积，且$\int_a^{+\infty}|f(x)|dx收敛$，则称$\int_a^{+\infty}f(x)dx$绝对收敛（或称$f(x)在[a,+\infty)上绝对可积$）
* 若$\int_a^{+\infty}f(x)dx$收敛而非绝对收敛，则称$\int_a^{+\infty}f(x)dx$条件收敛（或称$f(x)$在$[a,+\infty)$上条件可积）
### 比较判别的极限形式
$$\frac{f(x)}{g(x)}$$
### Abel判别法
* $\int_a^{+\infty}f(x)dx$收敛，$g(x)在[a,+\infty)$上单调有界;
### Dirichlet判别法
* $F(A)=\int_a^Af(x)dx在[a,+\infty)上有界,g(x)在[a,+\infty)$上单调且$\lim_{x\to +\infty}g(x)=0$.
**有限域积分必定收敛，故只需要讨论趋向无限的点的收敛情况*