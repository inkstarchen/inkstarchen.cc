
## 量子计算并行性

量子并行性是量子计算的一个基本特征，它使得量子计算机可以同时计算 $f(x)$ 在多个 $x$ 取值下的函数值。假如存在一个量子电路，可以实现 $|x, y\rangle \to |x, y \oplus f(x)\rangle$ 的映射，其中 $\oplus$ 符号表示模 2 加运算。如果输入的 $y = 0$，那么第二个输出等于 $f(x)$。现在，让我们考虑输入 $x$ 处于叠加态中，如下所示：

$$
\begin{array}{c} \cfrac{|0\rangle + |1\rangle}{\sqrt{2}} \\ |0\rangle \end{array}
\quad \begin{array}{c} x \\ y \end{array}
\xrightarrow{U_f}
\begin{array}{c} x \\ y \oplus f(x) \end{array}
$$

经过该电路之后，系统的量子态转化为：

$$
\frac{|0, f(0)\rangle + |1, f(1)\rangle}{\sqrt{2}}
$$

值得注意的是，这个结果中既包含了 $f(0)$，也包含了 $f(1)$，该电路似乎对 $x$ 的两个取值同时计算了函数 $f$。在经典计算中，需要使用多个电路模块才能实现这样的并行计算，但是在量子计算中利用叠加态，可以在一个电路中同时计算多个函数值。

在上述情况下，函数 $f$ 的输入 $x$ 由一个量子比特来编码，只有 0 或者 1 两种状态；假如函数稍微复杂一些，输入 $x$ 由两个量子比特来编码，并有四种可能取值：$|00\rangle$、$|01\rangle$、$|10\rangle$、$|11\rangle$，应该怎样实现并行计算？

我们可以分别施加 H 门在两个量子比特的初态 $|0\rangle$ 上，得到：

$$
|x\rangle = \left( \frac{|0\rangle + |1\rangle}{\sqrt{2}} \right) \otimes \left( \frac{|0\rangle + |1\rangle}{\sqrt{2}} \right) = \frac{|00\rangle + |01\rangle + |10\rangle + |11\rangle}{2}
$$

再将 $|x\rangle$ 应用前文提到的量子电路，则该电路可以同时计算 $x$ 的 4 种取值对应的函数值。若将其推广到具有 $N = 2^n$ 种输入的函数，则需要 $n$ 个 H 门分别作用在 $n$ 个初态量子比特上，得到所有可能取值的平衡叠加：

$$
\frac{1}{\sqrt{2^n}} \sum_x |x\rangle
$$

应用前文提到的量子电路，最终产生具有并行计算效果的输出：

$$
\frac{1}{\sqrt{2^n}} \sum_x |x\rangle |f(x)\rangle
$$
### Deutsch问题

- **常数函数**：输出永远为0或1
- **平衡函数**：输出为0和1的数目相同

如何尝试最少且足够的次数，判断一个函数是**常数函数**还是**平衡函数**

经典计算机需要 $\frac{2^n}{2} + 1$ 次

Deutsch 算法使用的电路和前文提到的类似，但不同之处在于 $y$ 也处于叠加态，如下所示：

$$
\begin{array}{c}
|0\rangle \xrightarrow{H} \\
|1\rangle \xrightarrow{H}
\end{array}
\begin{array}{c}
|\psi_0\rangle \rightarrow |\psi_1\rangle \\
\begin{array}{c}
x \\
U_f \\
y \oplus f(x)
\end{array}
\rightarrow
\begin{array}{c}
x \\
H \\
|\psi_2\rangle \rightarrow |\psi_3\rangle
\end{array}
\end{array}
$$

其中，输入态经过两个 H 门之后，新量子态为：

$$
|\psi_1\rangle = \left[ \frac{|0\rangle + |1\rangle}{\sqrt{2}} \right] \otimes \left[ \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right]
$$

由于异或计算的特性，我们有：$|x\rangle |y\rangle \longrightarrow |x\rangle |y\oplus f(x)\rangle = |x\rangle (-1)^{f(x)}|y\rangle$

考虑输入 $|x\rangle$ 为：

$$
\left[ \frac{|0\rangle + |1\rangle}{\sqrt{2}} \right]
$$

因此 $U_f$ 的输出为：

$$
|\psi_2\rangle = \frac{|0\rangle (-1)^{f(0)}|y\rangle + |1\rangle (-1)^{f(1)}|y\rangle}{\sqrt{2}} = \frac{|0\rangle (-1)^{f(0)} + |1\rangle (-1)^{f(1)}}{\sqrt{2}} |y\rangle
$$

经过简单分类讨论我们可以得到：

$$
|\psi_2\rangle = 
\begin{cases} 
\pm \left[ \frac{|0\rangle + |1\rangle}{\sqrt{2}} \right] \otimes \left[ \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right] & \text{if } f(0) = f(1) \\
\pm \left[ \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right] \otimes \left[ \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right] & \text{if } f(0) \neq f(1)
\end{cases}
$$

对第一个量子比特施加 H 门，这可以把第一个量子比特复原为 $|0\rangle$ 或者 $|1\rangle$：

$$
|\psi_3\rangle = 
\begin{cases} 
\pm |0\rangle \otimes \left[ \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right] & \text{if } f(0) = f(1) \\
\pm |1\rangle \otimes \left[ \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right] & \text{if } f(0) \neq f(1)
\end{cases}
$$

再一次联系异或计算的定义，注意到当 $f(0) = f(1)$ 时，$f(0) \oplus f(1)$ 为 0，其余情况为 1，因此我们可以将第一个量子比特进一步改写为：

$$
|\psi_3\rangle = \pm |f(0) \oplus f(1)\rangle \otimes \left[ \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right]
$$

可以看到，最终的系统量子态中，第二个量子比特的态是固定的，而第一个量子比特的状态却与 $f(0)$ 和 $f(1)$ 都有关。对第一个量子比特进行测量，如果结果为 $|1\rangle$，那么说明 $f$ 是平衡函数，反之为常数函数。

#### 异或计算特性

将 $y$ 取为特定的量子叠加态

Deutsch 算法中，

$$
|y\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}
$$

我们来看看 CNOT 对它的作用：

$$
|y \oplus f(x)\rangle = 
\begin{cases} 
\dfrac{|0\rangle - |1\rangle}{\sqrt{2}}, & f(x) = 0 \\[10pt]
\dfrac{|1\rangle - |0\rangle}{\sqrt{2}} = -\dfrac{|0\rangle - |1\rangle}{\sqrt{2}}, & f(x) = 1
\end{cases}
$$

可以看到：

$$
|y \oplus f(x)\rangle = (-1)^{f(x)} |y\rangle
$$

这就是所谓的「异或计算的特性」。

在量子计算中，Oracle代表的功能是输入数据，输出 1 或 0