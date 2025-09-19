## Heine定理
### 定理描述:
* $${\lim_{x \to x_0}f(x)}=A的充分必要条件是:对于任意满足条件{\lim_{n \to \infty}x_n}=x_0,且x_n{\neq}x_0$$$$(x=1,2,3,...)的数列{\lbrace}x_n{\rbrace},相应的函数值数列{\lbrace}f(x_n){\rbrace}$$$${\lim_{n \to \infty}f(x_n)}=A$$
* 充分性证明使用反证法

## Jensen 不等式
### 定理叙述
* 若$f(x)$为区间$I$上的下凸（上凸）函数，则对于任意$x_i\in I$和满足$\sum_{i=1}^{n}\lambda_i=1$的$\lambda_i > 0(i = 1,2,...,n)$,成立$$f(\sum_{i=1}^{n}\lambda_ix_i)\leq\sum_{i=1}^{n}\lambda_if(x_i)\quad(f(\sum_{i=1}^{n}\lambda_ix_i)\geq \sum_{i=1}^n\lambda_if(x_i))$$
  特别地，取$\lambda_i = \frac{1}{n}(i=1,2,...,n),$就有$$f(\frac{1}{n}\sum_{i=1}^nx_i)\leq\frac{1}{n}\sum_{i=1}^nf(x_i)\quad(f(\frac{1}{n}\sum_{i=1}^{n}x_i)\geq\frac{1}{n}\sum_{i=1}^{n}f(x_i)).$$
## L'Hospital法则
### 定理叙述
* 设函数$f(x)和g(x)在(a,a+d]上可导(d是某个正常数)$且$g'(x)\neq0$.若此时有$$\lim_{x \to a^+}f(x)=\lim_{x \to a^+}g(x)=0$$或$$\lim_{x\to a^+}g(x)=\infty,$$且$\lim_{x\to a^+}\frac{f'(x)}{g'(x)}$存在（可以是有限数或$\infty$），则成立$$\lim_{x\to a^+}\frac{f(x)}{g(x)}=\lim_{x \to a^+}\frac{f'(x)}{g'(x)}.$$
* 