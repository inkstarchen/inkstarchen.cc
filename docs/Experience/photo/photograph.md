> 运动模糊词条待归档，同时链接到计算机图形学

## 成像原理

**相机的原理：**

- 如果直接在物体前放置一个底片，无法得到一个好的图像。因为实物与像平面上的点并非一一对应：

- 物理学上可以通过小孔成像（Pinhole camera）的方法，尽可能让一一对应关系成立。但同时，如果孔太小会产生光的衍射现象，以及通光量不足，

想要解决成像问题，我们最好使用一个镜头（Lens）来将从一点发出的光线汇聚到一点上去.

通过几何光学的计算方法我们能够得到成像公式

$$\frac{1}{i} + \frac{1}{o} = \frac{1}{f}$$

**图像放大率(Image Magnification)**

$$m=\frac{h_i}{h_o} = \frac{i}{o}$$

当物体里透镜足够远时($o \rightarrow  \infty$)，相距近似等于焦距，即焦距决定了图像放大率。

**视场角(Field of View(FOV))**

![fov](https://github.com/inkstarchen/picx-images-hosting/raw/master/fov.lw3eecjsl.webp)

从上图可以看出，视场角取决于两个因素，焦距(foval length)和底片(sensor)的大小

从成像质量来看，底片越大（每个像素接收到的光更多，信噪比更好）,现在的工业目标就是在缩小底片的同时维持好的信噪比.


## **光圈（aperture）**

用于控制进光量的组件，在镜头中由数个光圈叶片组成来控制孔径大小。

- 光圈越大 $\rightarrow$ 开孔越大 $\rightarrow$ 进光量越大 $\rightarrow$ 照片越亮
- 光圈越小 $\rightarrow$ 开孔越小 $\rightarrow$ 进光量越小 $\rightarrow$ 照片越暗

![光圈](https://github.com/inkstarchen/picx-images-hosting/raw/master/aperture.7eh50vd8hl.webp)

摄影中通常用$f/值$的形式描述镜头光圈大小

$$f-number = \frac{f}{D}$$

其中，$f = $镜头的焦距，$D = $光圈直径

$f/值$越小则光圈开口越大

## **镜头散焦(Lens Defocus)**

<img alt="defocus" src="https://github.com/inkstarchen/picx-images-hosting/raw/master/defocus.5xazz4huc5.webp" style="width:400px; margin-left: 200px;" />


<img alt="blurcircle" src="https://github.com/inkstarchen/picx-images-hosting/raw/master/blurcircle.7i0qyljgcc.webp" style="width:400px; margin-left: 200px;" />

当焦距和像距固定时，只有一个面能成清楚的像，寻找这个平面的过程称为**对焦**

## 弥散圆与景深

**（弥散圆）Blur circle diameter:** $b = \frac{D}{i'} | i' - i|$

**景深（Depth of Field(DoF)）**

对焦完成后，对焦点的前后范围中，影像清晰的深度有多少，我们就称之为景深。

![dof1](https://github.com/inkstarchen/picx-images-hosting/raw/master/dof1.67xtsa812s.webp)

- 光圈越大( $f/值$ 越小)$\rightarrow$ 画面清晰范围越窄 $\rightarrow$ 景深越浅
- 光圈越小( $f/值$ 越大)$\rightarrow$ 画面清晰范围越广 $\rightarrow$ 景深越深

![dof2](https://github.com/inkstarchen/picx-images-hosting/raw/master/dof2.96a3vshbx3.webp)

景深的原理：当弥散圆落在一个像素内时，图像的表现就是清晰的。数学推导可得：

$$DoF: o_2 - o_1 = \frac{2coN(o-f)f^2}{f^4 - c^2N^2(o - f)^2}$$

## 快门

**快门速度（Shutter speed）**

- 控制曝光事件
- 像素的值等于光强在曝光时间内的积分

**滚动快门效果（Rolling shutter effect）**

#### 归档材料
[20250920 | 成像原理](https://inkstarchen.github.io/LifeNote/pages/62b3ce/#%E6%88%90%E5%83%8F%E5%8E%9F%E7%90%86)
[20250923 | 运动模糊](https://inkstarchen.github.io/LifeNote/pages/1c4dc6/#%E8%BF%90%E5%8A%A8%E6%A8%A1%E7%B3%8A)

* **运动模糊**：手部抖动，物体的运动

* 双倍的快门时间，就有双倍的运动模糊

**ISO（增益）**:在暗一点图上乘上一个数.（在放大信号的时候，也放大了噪声）
