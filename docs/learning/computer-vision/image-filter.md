## 高斯滤波

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

## 中值滤波(Median Filter)

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
neighbors = np.stack(neighbors, axis=-1)   # (H, W, ksize*ksize)
result = np.median(neighbors, axis=-1).astype(src.dtype)
```

## 双边滤波(BilateralFilter)

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
    d: 	Diameter of each pixel neighborhood that is used during filtering. 
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