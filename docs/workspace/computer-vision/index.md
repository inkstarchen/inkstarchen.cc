## image matching

### Detection

怎么进行边缘检测？（Harris' Corner Detector）

- 窗口中每个点计算梯度
- PCA分析，根据特征值分解的情况判断边缘检测
- 具有光强变化不变性、平移不变性、选择不变性
- 为了找到合适的尺度就进行不同层次的缩放选择
- 图像镜子他

怎么进行区域模式检测?(Blob Detector)

- 使用高斯核过滤器（LoG）
- 可以用DoG进行近似

### Descriptor

SIFT是如何对点进行描述的？
- 尺度已经被DoG决定了
- 对旋转和尺寸具有不变性
- 可以解决光照上大的变化

### Matching

1. 暴力匹配寻找最近的一个匹配点（定义距离函数）
2. Ratio test 如何检测出具有多匹配的点
3. Mutual nearest neighbor 与Ratio test区别


## Motion estimation

有两个问题，
Lucas-Kannade method 的基本假设