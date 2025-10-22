> 待完善 四元数 到旋转矩阵

## 3D变换矩阵

> 连接到线性代数矩阵 变换矩阵

**Scale**

$$S_{s_x,s_y,s_z} = \begin{pmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

**Translate**

$$T_{t_x,t_y,t_z} = \begin{pmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

**Rotate**

$$R_{x} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & \cos \theta & -\sin \theta & 0 \\ 0 & \sin \theta & \cos \theta & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

$$R_{y} = \begin{pmatrix} \cos \theta & 0 & \sin \theta & 0 \\ 0 & 1 & 0 & 0 \\ -\sin \theta & 0 & \cos \theta & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

$$R_{z} = \begin{pmatrix} \cos \theta & -\sin \theta & 0 & 0 \\ \sin \theta & \cos \theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

**欧拉角旋转矩阵**

$$R_{x,y,z}(\alpha,\beta,\gamma) = R_{x}(\alpha)R_{y}(\beta)R_{z}(\gamma)$$

**绕过原点的任意轴$n$旋转$\alpha$**

$$R(n,\alpha) = cos(\alpha)I  + (1-cos(\alpha))n n^T + sin(\alpha)\begin{pmatrix} 0 & -n_z & n_y \\ n_z & 0 & -n_x \\ -n_y & n_x & 0 \end{pmatrix}$$

**绕空间任意轴旋转**

> 先平移轴到到原点上，再旋转，再平移回来

## 视图 / 相机 变换(View/Camera Transform)

**先定义相机**

- 位置 $\vec{e}$
- 视角方向 $\hat{g}$
- 相机朝上方向 $\hat{t}$

**相机变换到固定位置**

- 移动到原点

$$T_{view} = \begin{pmatrix} 1 & 0 & 0 & -x_e \\ 0 & 1 & 0 & -y_e \\ 0 & 0 & 1 & -z_e \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

- 先求其逆变换

$$R^{-1}_{view} = \begin{pmatrix} x_{\hat{g} \times \hat{t}} & x_t & x_{-g} & 0 \\ y_{\hat{g} \times \hat{t}} & y_t & y_{-g} & 0 \\ z_{\hat{g} \times \hat{t}} & z_t & z_{-g} & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

> 由于旋转矩阵是正交矩阵，其逆矩阵即是转置矩阵

$$R_{view} = \begin{pmatrix} x_{\hat{g} \times \hat{t} & y_{\hat{g} \times \hat{t}} & z_{\hat{g} \times \hat{t}} & 0 \\ x_t & y_t & z_t & 0 \\ x_{-g} & y_{-g} & z_{-g} & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

### 正交投影

> 注意这里相机沿着-z方向,右手系

- 抛弃Z轴坐标
- 然后转换并缩放到$[-1,1]^3$上

$$M_{ortho} = \begin{pmatrix} \frac{2}{r-l} & 0 & 0 & & 0 \\ 0 & \frac{2}{t-b} & 0 & 0  \\ 0 & 0 & \frac{2}{n-f} & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 & -\frac{r+l}{2} \\ 0 & 1 & 0 & -\frac{t+b}{2} \\ 0 & 0 & 1 & -\frac{n+f}{2} \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

### 透视投影(perspective projection)

> GAMES101 理解

- $y' = \frac{ny}{z} \quad x' = \frac{nx}{z}$

$$\begin{pmatrix} x \\ y \\ z \\ 1 \end{pmatrix}  \Rightarrow \begin{pmatrix} nx/z \\ ny/z \\ unknown \\ 1 \end{pmatrix} == \begin{pmatrix} nx \\ ny \\ nz \\ unknown \\ z \end{pmatrix}$$

$$M_{persp \rightarrow ortho} = \begin{pmatrix} n & 0 & 0 & 0 \\ 0 & n & 0 & 0 \\ ? & ? & ?(n+f) & ?(-nf) \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

由远平面中心点和近平面的上任一点的变换可得第三行向量的关系$(0,0,A,B)$

$$\begin{array}{c} An + B = n^2 \\ Af + B = f^2 \end{array} \Rightarrow \begin{array}{c} A = n + f \\ B = -nf \end{array}$$

再做正交投影，便有下式($n$代表近平面，同时可替换为焦距)


$$\begin{pmatrix} n & 0 & 0 & 0 \\ 0 & n & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \\ 1 \end{pmatrix} = \begin{pmatrix} nx/z \\ ny/z \\ 1 \end{pmatrix}$$

