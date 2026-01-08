  参考内容：[超详细易懂FFT](https://blog.csdn.net/Flag_z/article/details/99163939)

离散傅里叶变换（DFT）

  

$$X[k]=\sum^{N-1}_{n=0}x[n]\cdot e^{-i\frac{2\pi}{N}kn}$$

  

- $x[n]$:时域信号

- $X[k]$:频域信号

- $k$:频率索引$(k=0,1,\dots)$

  

由于不同频率的正弦波的内积为0，只有频率相同的波才能得到内积值

  

所以计算的过程实际上是在问“信号和这个频率的正弦波有多相似”


**分解视角：** 傅里叶变换就是将一个复杂的时域信号分解成若干个简单的正弦波和余弦波

**逼近视角：** 一个函数能够使用无穷多个周期函数的线性组合来逼近.

在欧拉公式 $e^{i\theta} = cos\theta + i sin\theta$的统一下，Fourier 变换可以表示为：

- **从时域到频域：** $F(u) = \int^\infty_{-\infty} f(x) e^{-i2\pi ux}dx$
- **从频域到时域：** $f(x) = \int^\infty_{-\infty}F(u)e^{i2\pi ux}du$

至此我们获得了一个信号的时域(spatial domain)和频域(frequency domain)两个视角的信息.

> 从卷积的视角看$F(u)=\int^{\infty}_{-\infty} f(x)e^{-i2\pi ux}dx$。其实有离散版本的傅里叶变换，就是明显的卷积。而上式可以理解为连续信号的卷积.

### 参考资料

[傅里叶变换 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2)