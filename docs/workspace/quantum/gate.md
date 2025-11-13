
## 量子非门

量子非门: $X|\phi \rangle = \beta | 0 \rangle + \alpha |1 \rangle , \; X = \left[ \begin{array}{ll} 0 & 1 \\ 1 & 0 \end{array} \right]$

## Hadamard门
Hadamard 门（H 门）是一个基础的量子门，它可以让 $|0\rangle$ 和 $|1\rangle$ 转变为叠加态，它的矩阵表示为：

$$
H = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
$$

当 H 门作用在 0 态或者 1 态上时，可以产生叠加态：

$$
H | 0 \rangle = \frac{1}{\sqrt{2}} (|0\rangle + |1\rangle) = |+\rangle, \quad H | 1 \rangle = \frac{1}{\sqrt{2}} (|0\rangle - |1\rangle) = |-\rangle
$$

## Pauli门

前文所述的量子 X 门的矩阵表示被称为 Pauli-X 矩阵。Pauli 矩阵的完整集合为：

$$
\sigma_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad
\sigma_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}, \quad
\sigma_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}
$$

**与 Pauli-Y、Z 矩阵对应的量子门称为 Y 门和 Z 门。**

量子 X 门可以实现 $|0\rangle \rightarrow |1\rangle$ 的转变，反之亦然。如果观察 $|0\rangle$ 和 $|1\rangle$ 在 Bloch 球上的位置，你会发现 $|0\rangle$ 到 $|1\rangle$ 恰好需要绕 x 轴旋转 $\pi$ 的角度。

类似的，Y 门和 Z 门对一个量子态的作用为让其绕着 y 轴和 z 轴旋转 $\pi$ 的角度。

![[assets/quan-gate.png]]

## 相位旋转门
> 暂时不知道其用途

相位旋转门作用于量子比特的态矢量时，会引入一个特定的相位因子，改变量子态的相对相位；具体而言，相位的旋转是通过调整量子比特的状态矢量与某个特定基态的相对相位来实现的。

相位旋转门可以改变量子态的相对相位，但不改变其概率分布。它在量子算法中有广泛的应用，如量子相位估计、量子傅里叶变换等。

需要注意的是，相位旋转门与其他门操作（如 Pauli 门、Hadamard 门等）不同，它不涉及量子比特的旋转操作，而是旋转相位。这使得相位旋转门具有独特的功能和作用。常见的相位旋转门有 P 门、T 门、S 门。

P 门是一个相位旋转门，它将量子比特的相位进行旋转，带有一个输入参数用于确定具体相位；S 门是 P 门的特例，其中相位参数 $\phi$ 等于 $\frac{\pi}{2}$，T 门是另一个相位旋转门，它将量子比特的相位旋转 $\frac{\pi}{4}$：

$$
P(\phi) = \begin{bmatrix} 1 & 0 \\ 0 & e^{i\phi} \end{bmatrix}, \quad 
S = \begin{bmatrix} 1 & 0 \\ 0 & i \end{bmatrix}, \quad 
T = \begin{bmatrix} 1 & 0 \\ 0 & e^{i\frac{\pi}{4}} \end{bmatrix}
$$

## 参数旋转门

> 同样不知道其用途

参数旋转门是量子计算中的一种基本门，它允许根据给定参数执行量子态的旋转操作。在单量子比特系统中，最常见的参数旋转门是绕 X 轴、Y 轴和 Z 轴的旋转门，分别记为 $R_X(\theta)$、$R_Y(\theta)$ 和 $R_Z(\theta)$，其中 $\theta$ 是旋转角度，对应矩阵表示如下：

$$
R_X(\theta) = \begin{bmatrix} \cos \frac{\theta}{2} & -i \sin \frac{\theta}{2} \\ -i \sin \frac{\theta}{2} & \cos \frac{\theta}{2} \end{bmatrix}, \quad
R_Y(\theta) = \begin{bmatrix} \cos \frac{\theta}{2} & -\sin \frac{\theta}{2} \\ \sin \frac{\theta}{2} & \cos \frac{\theta}{2} \end{bmatrix}, \quad
R_Z(\theta) = \begin{bmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{bmatrix}
$$

容易验证 $H = iR_Y\left( \frac{\pi}{2} \right) R_Z(\pi) = iR_X(\pi) R_Y\left( \frac{\pi}{2} \right)$，与 Bloch 球上的物理图像相符，即 Hadamard 门可以看作是量子态先绕 Z 轴旋转 $\pi$，再绕 Y 轴旋转 $\pi/2$（等于先绕 Y 轴旋转 $\pi/2$，再绕 X 轴旋转 $\pi$）。

## 任意门构建（酉矩阵分解）

事实上，对任意一个 $2 \times 2$ 的酉矩阵都有如下的分解：

$$
U = e^{i\alpha} \begin{bmatrix}
e^{-i\beta/2} & 0 \\
0 & e^{i\beta/2}
\end{bmatrix} \begin{bmatrix}
\cos\frac{\gamma}{2} & -\sin\frac{\gamma}{2} \\
\sin\frac{\gamma}{2} & \cos\frac{\gamma}{2}
\end{bmatrix} \begin{bmatrix}
e^{-i\delta/2} & 0 \\
0 & e^{i\delta/2}
\end{bmatrix}
$$

其中，中间的矩阵就是线性代数中的旋转矩阵（绕 y 轴），而其前后的两个矩阵可以理解为在特定平面内的旋转（绕 z 轴）。这个分解可以对任意单位比特操作进行精确描述。

例如，对于具有如下酉矩阵 $U_1$ 可做分解：

$$
U_1 = \begin{bmatrix}
0.707 & -0.707i \\
0.707i & 0.707
\end{bmatrix}, \quad U_1 = R_z\left(-\frac{\pi}{4}\right) \cdot X \cdot R_z\left(-\frac{\pi}{2}\right)
$$

## 复合系统的矩阵表示

对于包含多个量子比特的复合系统，我们规定态矢量中的每个量子比特按从左到右的顺序依次编号，记为 $q_0$、$q_1$、⋯⋯，并在量子电路图中从上至下依次绘制每个量子比特。

初态为 $|00\rangle$，$q_0$ 经过 $X$ 门状态变为 $|1\rangle$，$q_1$ 经过 $Z$ 门状态变为 $|0\rangle$。

$$
q_0 : |0\rangle \rightarrow [X] - |1\rangle
$$

$$
q_1 : |0\rangle \rightarrow [Z] - |0\rangle
$$

若将两个单量子门视作一个整体，可以通过张量积的形式构成一个双量子门。

$$
\begin{aligned}
X \otimes Z &= \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \otimes \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{bmatrix} \\
X \otimes Z |00\rangle &= \begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix} = |10\rangle
\end{aligned}
$$

## 受控门(CNOT门)

CNOT 门是一种受控门，其中一个量子比特（称为控制比特）的状态决定了另一个量子比特（称为目标比特）是否进行翻转操作：当控制比特为 $|1\rangle$ 时，翻转目标比特的状态；当控制比特为 $|0\rangle$ 时，保持目标比特的状态不变。其矩阵表示形式为：

$$
CNOT = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}
$$


- **作用：** 制备纠缠态

若以 $q_0$ 为 CNOT 门的控制比特，$q_1$ 为目标比特，则会将 $|10\rangle$ 和 $|11\rangle$ 的振幅交换，如下所示：

$$
|a\rangle = \begin{bmatrix} a_{00} \\ a_{01} \\ a_{10} \\ a_{11} \end{bmatrix}
$$

$$
\text{CNOT}|a\rangle = \begin{bmatrix} a_{00} \\ a_{01} \\ a_{11} \\ a_{10} \end{bmatrix}
$$

以量子态 $|q_0 q_1\rangle = |00\rangle$ 为例，首先 $q_0$ 通过一个 H 门，再将 CNOT 门作用在两个量子比特上，则有：

$$
|q_0\rangle \otimes |q_1\rangle \xrightarrow{\text{H gate on } q_0} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle)
$$

$$
\xrightarrow{\text{CNOT gate}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$$


## 量子隐形传态

> 利用想要发送的量子态与手中的量子纠缠作用，将对方手中的量子态变换到与目标量子态相近的态，同时解纠缠.

Alice 要传递一个量子态 $|\phi \rangle = \alpha |0 \rangle + \beta |1 \rangle$

解决：Alice只需要用经典信道向Bob传输两个bit的经典信息。

### 详细介绍

假设 Alice 和 Bob 是一对老朋友，他们上一次见面的时候各自拿走了一对处于贝尔态的纠缠量子比特中的一个，也就是说：

$$
|\phi_{AB}\rangle = \frac{1}{\sqrt{2}} |00\rangle + \frac{1}{\sqrt{2}} |11\rangle
$$

- Alice 拿走的量子比特
- Bob 拿走的量子比特

现在他们相隔千里，Alice 手上有另一个处于量子态 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ 的量子比特想要发送给 Bob，但是 Alice 却陷入如下的困境：

1. 假如 Alice 不知道 $|\psi\rangle$ 是一个怎样的量子态，她手上只有一份量子比特，由于量子不可克隆原理及量子态坍缩，她无法测得两个参数 $\alpha, \beta$ 的确切取值
2. 就算 Alice 知道 $\alpha, \beta$ 的取值，它们也有可能是无穷位的实数。

量子隐形传态为 Alice 和 Bob 的量子态传输提供了可能，事实上，Alice 只需要用经典信道向 Bob 传输两个比特的经典信息。Alice 和 Bob 端的操作电路如下图所示。首先，Alice、Bob 持有的三个量子比特构成的初始整体量子态可表示为：

$$
|\psi_0\rangle = \frac{1}{\sqrt{2}}[\alpha|0\rangle(|00\rangle + |11\rangle) + \beta|1\rangle(|00\rangle + |11\rangle)]
$$

然后，Alice 首先将她要发送的量子比特以及她持有的纠缠量子比特经过一个 CNOT 门，那么整体的量子态变为：

$$
|\psi_1\rangle = \frac{1}{\sqrt{2}}[\alpha|0\rangle(|00\rangle + |11\rangle) + \beta|1\rangle(|10\rangle + |01\rangle)]
$$

紧接着，Alice 又将 $|\psi\rangle$ 对应的量子比特经过一个 H 门，则现在系统整体的量子态变为：

$$
|\psi_2\rangle = \frac{1}{2} [\alpha(|0\rangle + |1\rangle)(|00\rangle + |11\rangle) + \beta(|0\rangle - |1\rangle)(|10\rangle + |01\rangle)]
$$

重新组织各个项，将其改写为 Alice 持有的量子比特和 Bob 的一个量子比特的张量积形式：

$$
|\psi_2\rangle = \frac{1}{2} [|00\rangle (\alpha|0\rangle + \beta|1\rangle) + |01\rangle (\alpha|1\rangle + \beta|0\rangle) + |10\rangle (\alpha|0\rangle - \beta|1\rangle) + |11\rangle (\alpha|1\rangle - \beta|0\rangle)]
$$

在该式中，第一项中 Alice 处在 $|00\rangle$，而 Bob 持有的量子比特已经转变为 $\alpha|0\rangle + \beta|1\rangle$ —— 这刚好是 Alice 想要传送给 Bob 的态 $|\psi\rangle$。

由该式可以知道，若 Alice 对手上持有的量子比特进行测量，则测量结果与 Bob 端的量子比特的态的对应关系为：

$$
\begin{cases} 
00 \longleftrightarrow |\psi_{3}(00)\rangle \equiv \alpha|0\rangle + \beta|1\rangle \\
01 \longleftrightarrow |\psi_{3}(01)\rangle \equiv \alpha|1\rangle + \beta|0\rangle \\
10 \longleftrightarrow |\psi_{3}(10)\rangle \equiv \alpha|0\rangle - \beta|1\rangle \\
11 \longleftrightarrow |\psi_{3}(11)\rangle \equiv \alpha|1\rangle - \beta|0\rangle 
\end{cases}
$$

现在，Alice 可以测量持有的量子比特，并将结果通过经典信道发送给 Bob，这只需要两个经典比特的数据；反过来，Bob 可根据接收到的经典数据对持有的量子比特进行操作，进而恢复 $|\psi\rangle$。

- 如果 Alice 测量结果为 $00$，Bob 不需要做任何事；
- 如果结果为 $01$，那么 Bob 需要使用 X 门来修正量子态；
- 如果结果为 $10$，那么 Bob 需要使用 Z 门来修正量子态；
- 如果结果为 $11$，那么 Bob 需要先使用 X 门再作用 Z 门来修正量子态。

Bob需要根据Alice的结果来对电路做调整，因此**量子隐形传态也不能突破光速限制**

## SWAP门及CSWAP门

SWAP 门是一个非常简单但重要的两量子比特门，它用于交换两个量子比特的状态。SWAP 门的操作非常直观：它将两个量子比特的状态互换，将第一个量子比特的状态赋予第二个量子比特，并将第二个量子比特的状态赋予第一个量子比特。SWAP 门的矩阵形式及 Qiskit 可视化如下：

$$
SWAP = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

SWAP 门可以用来生成和操作纠缠态。通过交换两个量子比特的状态，可以创建新的纠缠态。

可以给 SWAP 门添加控制端，使之成为 CSWAP，即受控的 SWAP 门，又被称为 Fredkin 门。

## Toffoli门

Toffoli 门，有时也称为 CCNOT 门或者 CCX 门，是一个三量子比特门，它在经典计算中执行了一个非常重要的逻辑操作，即布尔逻辑中的 AND 门。具体来说，Toffoli 门的操作如下：

如果前两个量子比特（通常称为控制比特）都处于状态 $|1\rangle$ 时，它会对第三个量子比特（通常称为目标比特）执行一个非门操作。如果其中任何一个或两个控制比特处于 $|0\rangle$ 状态，它不会执行非门操作，目标比特保持不变。

$$
\text{Toffoli} = 
\begin{pmatrix}
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0
\end{pmatrix}
$$

Toffoli 门的广义形式：除了标准的 CCNOT 门，还有更通用的多量子比特门，例如 CCCNOT、CCCCNOT 等，具体取决于控制比特的数量。