


## 滤波器实践部分

### 高斯滤波

- 实际作用：通过平均，去除掉了图像中高频的部分，保留低频变化的部分，使得图像更加平滑.

  

- 高斯核则是通过高斯函数的采样得来的


```python title="高斯核"

for i in range(ksize[0]):

    for j in range(ksize[1]):

        x = i - center_x

        y = j - center_y

        # 二维高斯函数

        kernel[i, j] = (1 / (2 * math.pi * sigmaX * sigmaY)) * \

                        math.exp(-(x**2 / (2 * sigmaX**2) + y**2 / (2 * sigmaY**2)))

  

kernel /= np.sum(kernel) #归一化

```

  

### 中值滤波(Median Filter)

  

- 使用邻域的中位数来替换中心像素，需要做填充处理

- 示例代码通过标识位和`cv`库得到每个像素上的一个邻域堆叠，然后取每个像素上的中值.

  

```py title="中值滤波"

pad = ksize // 2

# 存储每个偏移卷积结果

neighbors = []

for dy in range(-pad, pad+1):

    for dx in range(-pad, pad+1):

        # 构造一个在 (dy, dx) 位置为1，其余为0的卷积核

        kernel = np.zeros((ksize, ksize), np.float32)

        kernel[pad+dy, pad+dx] = 1.0

        # 用 filter2D 提取对应邻域的像素

        shifted = cv2.filter2D(src, -1, kernel)

        neighbors.append(shifted)

  

# 把所有邻域堆叠 → 在最后一维取中值

neighbors = np.stack(neighbors, axis=-1)   # (H, W, ksize*ksize)

result = np.median(neighbors, axis=-1).astype(src.dtype)

```

  

### 双边滤波(BilateralFilter)

  

> 同时考虑空间距离和颜色距离的滤波方式

  

$$I_{filtered}(p) = \frac{1}{W_p} \underset{q \in \Omega_p}{\sum} I(q) \cdot e^{-\frac{|q-p|^2}{2\sigma_s^2}} \cdot e^{-\frac{|I(q)-I(p)|^2}{2\sigma_r^2}}$$

  

- $p$：当前像素位置

- $q$：邻域像素位置

- $\sigma_s$：空间标准差

- $\sigma_r$：颜色标准差

- $I(q)$: 邻域像素的像素值

- $I(p)$: 当前像素的像素值

- $W_p = \underset{q \in \Omega_p}{\sum}$ ： 空间核 颜色核 $\rightarrow$归一化因子

  
  

```py title="双边滤波" linenums="1"

def bilateralFilter(src, d, sigmaColor, sigmaSpace):

    '''

    INPUT:

    src: input image

    d:  Diameter of each pixel neighborhood that is used during filtering.

    sigmaColor: Filter sigma in the color space

    sigmaSpace: Filter sigma in the coordinate space.

    OUTPUT:

    dst: return image

    '''

    H, W, C= src.shape

    pad = d // 2

    result = np.zeros_like(src, dtype=np.float32)

  

    # 获得边缘填充的图像数据

    padded_src = np.pad(src, ((pad, pad), (pad, pad),(0,0)), mode='edge')

    # 预计算空间高斯核

    y, x = np.mgrid[-pad:pad+1, -pad:pad+1]

    spatial_kernel = np.expand_dims(np.exp(-(x**2 + y**2) / (2 * sigmaSpace**2)),axis=-1)

    temp_src = padded_src.astype(np.float32)

    for i in range(pad,H):

        for j in range(pad,W):

            # 获得卷积的区域

            region = temp_src[i - pad:i + pad + 1, j - pad:j + pad + 1]

            center_val = temp_src[i, j] # 中心像素RGB shape:（3, ）

  

            # 颜色权重

            diff2 = np.sum((region - center_val)**2, axis=2, keepdims=True)

            diff2 = np.clip(diff2, 0, 1e6)

  

            # 颜色核

            range_kernel = np.exp(-diff2 / (2 * sigmaColor**2))

            weights = range_kernel * spatial_kernel

  

            # 归一化

            weights /= np.sum(weights, axis=(0,1), keepdims=True)

            # 卷积操作

            result[i, j] = np.sum(region * weights, axis=(0, 1))

  

    return np.clip(result, 0, 255).astype(np.uint8)

```

  

> 注意颜色距离使用RGB的欧式距离,可直接调用`cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)`

## 图像拼接

存在重复结构时可能出现 具有歧义性的匹配

![[assets/cv-incorrect-match.png]]
#### Ratio test
- 比率得分  

  $$
  \text{比率得分} = \frac{\| f_1 - f_2 \|}{\| f_1 - f_2' \|}
  $$

  其中：  
  - $f_2$ 是在 $l_2$ 中与 $f_1$ **最佳匹配** 的项；  
  - $f_2'$ 是在 $l_2$ 中与 $f_1$ **次佳匹配** 的项。  

- 模糊匹配（Fuzzy Matching）会产生较大的比率得分。


![[assets/cv-incorrect-ratio.png]]

#### 相互最近邻

另一种策略：寻找相互最近邻 

- $f_2$ 是 $f_1$ 在 $l_2$ 中的最近邻  
- $f_1$ 是 $f_2$ 在 $l_1$ 中的最近邻

#### 运动估计问题

-  **特征跟踪**
	- 提取特征（兴趣）点并在多帧图像中“跟踪”它们 
	- 输出：稀疏点的位移  

- **光流**
	- 恢复每个像素的图像运动  
	- 输出：密集位移场（光流）  

**两个问题，一种方法**：  

卢卡斯–卡纳德方法

![[assets/cv-motionestimation-1.png]]
已知两帧图像，如何估计点的平移？  

这与特征匹配有何不同？  

 **卢卡斯–卡纳德方法的关键假设**

1. **小运动**：点的移动距离不大  
2. **亮度恒常性**：同一点在每一帧中看起来相同  
3. **空间一致性**：点的移动方式与其邻近点相似

# 亮度恒常性

> 提示：u,v 是运动距离


- **亮度恒常性方程：**

$$
I(x, y, t) = I(x + u, y + v, t + 1)
$$

- **假设小运动下的泰勒展开：**

沿 $x, y$ 方向的图像导数  
帧间差异：

$$
I(x + u, y + v, t + 1) \approx I(x, y, t) + I_x \cdot u + I_y \cdot v + I_t
$$

因此：

$$
I(x + u, y + v, t + 1) - I(x, y, t) = I_x \cdot u + I_y \cdot v + I_t
$$

得到 **亮度恒常性约束方程（Brightness Constancy Constraint Equation, BCCE）**：

$$
I_x \cdot u + I_y \cdot v + I_t \approx 0 
\quad \Rightarrow \quad 
\nabla I \cdot 
\begin{bmatrix} u \\ v \end{bmatrix}
+ I_t = 0
$$
- **空间一致性约束**  
  - 假设像素的邻域具有相同的 $(u, v)$  
  - 若使用 $5 \times 5$ 的窗口，则每个像素可得到 25 个方程：

$$
\begin{bmatrix}
I_x(p_1) & I_y(p_1) \\
I_x(p_2) & I_y(p_2) \\
\vdots & \vdots \\
I_x(p_{25}) & I_y(p_{25})
\end{bmatrix}
\begin{bmatrix}
u \\
v
\end{bmatrix}
=
-\begin{bmatrix}
I_t(p_1) \\
I_t(p_2) \\
\vdots \\
I_t(p_{25})
\end{bmatrix}
$$
# 最小二乘解

$$
\begin{bmatrix}
I_x(p_1) & I_y(p_1) \\
I_x(p_2) & I_y(p_2) \\
\vdots & \vdots \\
I_x(p_{25}) & I_y(p_{25})
\end{bmatrix}
\begin{bmatrix}
u \\[4pt]
v
\end{bmatrix}
=
- \begin{bmatrix}
I_t(p_1) \\
I_t(p_2) \\
\vdots \\
I_t(p_{25})
\end{bmatrix}
$$

- 方程数多于变量数  
- 因此我们求解 $\min_d \|A d - b\|^2$  
- 关于 $d$ 的最小二乘解由下式给出：

$$
(A^\top A)\, d = A^\top b
$$

即对窗口内所有像素求和得到正规方程：(梯度向量的协方差矩阵)

$$
\begin{bmatrix}
\sum I_x I_x & \sum I_x I_y \\[4pt]
\sum I_x I_y & \sum I_y I_y
\end{bmatrix}
\begin{bmatrix}
u \\[4pt]
v
\end{bmatrix}
=
- \begin{bmatrix}
\sum I_x I_t \\[4pt]
\sum I_y I_t
\end{bmatrix}
$$

> 可以解释人眼的错觉

对窗口内所有像素求和。

- **$A^\top A$** 应该是可逆且良态的  
  - **$A^\top A$** 的特征值 $\lambda_1$ 和 $\lambda_2$ 不应太小  
  - 这让你联想到什么吗？  
    - ✅ **Harris 角点检测器**的判断准则：  
      图像局部梯度的协方差矩阵（也就是 $A^\top A$）的特征值越大，表示该点在两个方向上都有显著变化——即为角点。
![[assets/cv-motion-aperture.png]]
![[assets/cv-motion-aperture2.png]]
这个过程中潜在的误差来源是什么？

- 假设 AᵀA 容易求逆
- 假设图像中没有太多噪声

当我们的假设不成立时：

- 亮度恒常性**不**满足
- 运动量**不小**
- 点的运动方式与其邻近点**不一致**
![[assets/cv-motion-reduce.png]]

> 工具：paperwithcode

# 逆扭曲（Inverse Warping）

- 从其在 $f(x, y)$ 中的对应位置  
  $$(x, y) = T^{-1}(x', y')$$  
  获取每个像素 $g(x', y')$。

- 即：对输出图像中的每个像素 $(x', y')$，  
  在输入图像中找到其**反变换位置** $(x, y)$，  
  然后通过插值获取 $f(x, y)$ 的值。

- ✅ 优点：不会出现“空洞”问题（相比正向扭曲）。
![[assets/cv-imagewarping-inversewarping.png]]

# 如何计算变换？

$$
\begin{bmatrix}
x' \\[4pt]
y' \\[4pt]
1
\end{bmatrix}
\cong
T
\begin{bmatrix}
x \\[4pt]
y \\[4pt]
1
\end{bmatrix}
$$

---

1. **图像匹配**  
   每个匹配点 $(x, y) \leftrightarrow (x', y')$ 提供一个方程。

2. **求解变换矩阵 $T$**  
   根据多个匹配点，利用最小二乘或 RANSAC 等方法估计 $T$。

![[assets/cv-imagestitching.png]]
$$
\begin{bmatrix}
x' \\[4pt]
y' \\[4pt]
1
\end{bmatrix}
=
\begin{bmatrix}
a & b & c \\[4pt]
d & e & f \\[4pt]
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\[4pt]
y \\[4pt]
1
\end{bmatrix}
=
\begin{bmatrix}
ax + by + c \\[4pt]
dx + ey + f \\[4pt]
1
\end{bmatrix}
$$

- 对于 $n$ 个匹配点：

$$
\begin{bmatrix}
x_1 & y_1 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & x_1 & y_1 & 1 \\
x_2 & y_2 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & x_2 & y_2 & 1 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
x_n & y_n & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & x_n & y_n & 1
\end{bmatrix}
\begin{bmatrix}
a \\[3pt]
b \\[3pt]
c \\[3pt]
d \\[3pt]
e \\[3pt]
f
\end{bmatrix}
=
\begin{bmatrix}
x_1' \\[3pt]
y_1' \\[3pt]
x_2' \\[3pt]
y_2' \\[3pt]
\vdots \\[3pt]
x_n' \\[3pt]
y_n'
\end{bmatrix}
$$

$\underset{2n \times 6}{A}$  $\underset{6 \times 1}{t}$  $\underset{2n \times 1}{b}$

![[assets/cv-imagestitching-project.png]]

$$
\begin{bmatrix}
x_i' \\
y_i' \\
1
\end{bmatrix}
\cong
\begin{bmatrix}
h_{00} & h_{01} & h_{02} \\
h_{10} & h_{11} & h_{12} \\
h_{20} & h_{21} & h_{22}
\end{bmatrix}
\begin{bmatrix}
x_i \\
y_i \\
1
\end{bmatrix}
$$

---

$$
x_i' = \frac{h_{00}x_i + h_{01}y_i + h_{02}}{h_{20}x_i + h_{21}y_i + h_{22}}
$$

$$
y_i' = \frac{h_{10}x_i + h_{11}y_i + h_{12}}{h_{20}x_i + h_{21}y_i + h_{22}}
$$

---

由此得到线性方程形式：

$$
x_i'(h_{20}x_i + h_{21}y_i + h_{22}) = h_{00}x_i + h_{01}y_i + h_{02}
$$

$$
y_i'(h_{20}x_i + h_{21}y_i + h_{22}) = h_{10}x_i + h_{11}y_i + h_{12}
$$

$$
\begin{bmatrix}
x_1 & y_1 & 1 & 0 & 0 & 0 & -x_1' x_1 & -x_1' y_1 & -x_1' \\
0 & 0 & 0 & x_1 & y_1 & 1 & -y_1' x_1 & -y_1' y_1 & -y_1'
\end{bmatrix}
$$

$$
\begin{bmatrix}
x_n & y_n & 1 & 0 & 0 & 0 & -x_n' x_n & -x_n' y_n & -x_n' \\
0 & 0 & 0 & x_n & y_n & 1 & -y_n' x_n & -y_n' y_n & -y_n'
\end{bmatrix}
$$

$$
\begin{bmatrix}
h_{00} \\
h_{01} \\
h_{02} \\
h_{10} \\
h_{11} \\
h_{12} \\
h_{20} \\
h_{21} \\
h_{22}
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0 \\
\vdots \\
0 \\
0
\end{bmatrix}
$$

$\underset{2n \times 9}{A}$  $\underset{9 \times 1}{h}$  $\underset{2n \times 1}{0}$


定义了一个最小二乘问题：最小化 $\|A h - 0\|^2$。

- 由于 $h$ 是在尺度意义下定义的，求解单位向量 $\hat{h}$。  
- 解：$\hat{h}$ 为 $A^\top A$ 的最小特征值对应的特征向量。  
- 需要 4 个或更多点才能求解。

> 一定要加约束条件，让最后一个 $h$ 等于 $1$ 或 让 $h$ 的$norm = 1$


# RANSAC（随机抽样一致性）

> 用于去除错误匹配的基本手段

- 通用版本：

  1. 随机选择 $s$ 个样本  
     - 通常 $s$ 为能够拟合模型的最小样本量  
  2. 对这些样本拟合一个模型（例如变换矩阵）  
  3. 统计与该模型大致匹配的内点数量  
  4. 重复 $N$ 次  
  5. 选择具有最大内点集的模型



# 柱面投影

- $(X, Y, Z)$  
- 单位圆柱体  

$$
x' = r\tan^{-1}\left(\frac{x}{f}\right)
$$  

$$
y' = \frac{ry}{\sqrt{x^2 + f^2}}
$$  

$(x', y')$ 是柱面坐标，$(x, y)$ 是图像坐标（原点在图像中心），$r$ 是圆柱半径，$f$ 是焦距。

## SIFM

## 运动重构(Structure from Motion, SfM)

  

> 从一系列场景的图像中重现出相机位置和3D结构  
#### 旋转矩阵 $R$

$$

R =

\begin{bmatrix}

1 & 12 & 13 \\

21 & 22 & 23 \\

31 & 32 & 33

\end{bmatrix}

$$
##### 各行的几何意义

- **第1行**：相机坐标系 $\hat{x}_c$ 轴在世界坐标系中的方向  

- **第2行**：相机坐标系 $\hat{y}_c$ 轴在世界坐标系中的方向  

- **第3行**：相机坐标系 $\hat{z}_c$ 轴在世界坐标系中的方向  

## 相机标定流程
### 步骤 1：采集图像

拍摄已知几何形状物体的图像，例如标定板。

**求解步骤**：
1. 通过 QR 分解从 $P$ 的前三列得到 $K$ 和 $R$

2. 计算内参矩阵的逆 $K^{-1}$

3. 将 $P$ 的最后一列乘以 $K^{-1}$ 得到平移向量 $t$

### 运动恢复结构 (Structure from Motion, SfM)
#### 已知参数

- 两个视图/相机的**内参**：$f_x, f_y, o_x, o_y$

- 内参矩阵 $K$ 对于两个相机都是已知的
#### 未知参数

- 相机的**外参**（相机间的相对位置和朝向）

- 场景点的 3D 坐标
#### SfM 求解步骤

1. 内参已知

假设每个相机的内参矩阵 $K$ 已知

2. 寻找对应点

在两幅图像中找到一些可靠的**对应点**

3. 估计相对位姿

求解相机间的相对位置 $t$ 和朝向 $R$  

4. 三角化

计算场景点的 **3D 位置**

### Epipolar Geometry

> 要求两个相机之间的约束关系

$x_l$和$x_r$不知道，先转换成$u_l$和$u_r$ 图像平面上的匹配点.
### 三角化 Triangulation

> 已知匹配关系，相机位置关系，就能通过射线求交得到三维点的位置，这些三维点就是点云.

## 多目三维重建

- 第三张图和前一张图做匹配，然后计算camera pos
### 集束优化
所有三维的点，投影回所有二维图像里，做 *再投影误差* 优化
同时优化点的位置和相机参数

### 深度图计算流程
- 相机标定
- 图像校正
- 计算视差
- 估计深度

### Multi-view Stereo（多视角立体重建）

假设一个深度，根据约束将一张图中的点其投影到其它图中，计算相似度.

就能计算出参考图像中的深度图.

#### PatchMatch

**假设：**相邻点间的偏移量相似

- 传播补充：将像素深度答案赋给相邻的像素，假如结果变得更好了则保留.


