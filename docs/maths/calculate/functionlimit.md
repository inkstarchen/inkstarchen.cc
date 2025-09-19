> 条目质量：中 | 定义完全，但缺少例子，四则运算定理的解释缺失
### 极限的定义
$${\lim_{x \to x_0}f(x)=A} <=>{\forall\delta>0},{\forall}x（0<|x-x_0|<{\delta}):|f(x)-A|<{\varepsilon}.$$
### 极限的性质
* （1）极限的唯一性
	* $$设A与B都是函数f(x)在点x_0的极限，则A=B$$
* （2）局部保序性
	* $$若{\lim_{x \to x_0}f(x)=A,{\lim_{x \to x_0}g(x)=B}},且A>B,则存在{\delta}>0,当0<|x-x_0|<{\delta}时，成立$$$$f(x)>g(x)$$
* （3）局部有界性
	* $$若{\lim_{x \to x_0}f(x)=A},则存在{\delta}>0,使得f(x)在O(x_0,{\delta}){\backslash}{\lbrace}x_0{\rbrace}中有界$$
* （4）夹逼性
	* $$若存在r>0,使得当0<|x-x_0|<r时，成立$$$$g(x){\leq}f(x){\leq}h(x)$$$$且{\lim_{x \to x_0}g(x)}={\lim_{x \to x_0}h(x)}=A,则{\lim_{x \to x_0 }f(x)}=A.$$
### 四则运算定理前提：
* $$设{\lim_{x \to x_0}f(x)}=A,{\lim_{x \to x_0}=B}$$
### 左极限和右极限

### 函数极值
* 设$f(x)$在$(a,b)$上有定义，$x_0\in(a,b)$,如果存在点$x_0$的某个邻域$O(x_0,\delta)\subset(a,b)$,使得$$f(x)\leq f(x_0),\quad x\in O(x_0,\delta),$$则称$x_0$是$f(x)$的一个极大值点，$f(x_0)$称为相应的极大值.