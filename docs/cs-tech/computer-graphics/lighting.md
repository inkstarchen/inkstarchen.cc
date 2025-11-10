## 颜色

光源所提供的实际上是一个基础颜色值.

> 在考虑材质后，我们可以对光源进一步引入各个分量的强度.

而乘以物体颜色这一操作事实上只是光线作用的简化，即以一定比例吸收和反射光源的颜色分量.

```c++
glm::vec3 lightColor(0.33f, 0.42f, 0.18f);
glm::vec3 toyColor(1.0f, 0.5f, 0.31f);
glm::vec3 result = lightColor * toyColor; // = (0.33f, 0.21f, 0.06f);
```

## 基础光照

### Phong Lighting Model

Phong Lighting Model 提供了一种对光源效果的模拟.他将光照分为下述三个部分

- 环境(Ambient)： 一个环境光照常量，用于模拟世界基础环境光
- 漫反射(Diffuse)： 漫反射光，用于模拟物体的漫反射效果
- 镜面反射(Specular)： 镜面反射光，用于模拟物体的镜面反射效果

#### 环境光照

- 若是考虑光的多方向发散反弹，对一个物体产生间接的影响，则称其为**全局光照(Global Illumination)**算法

- 如果仅仅是用一个常量光照来模拟环境，则称其为**环境光照(Ambient Lighting)**

#### 漫反射光照

- 考虑光源与面位置的方向，与面法向的夹角值，来对光源颜色做变换.

#### 镜面光照

- 考虑视点与面位置的方向，与反射光方向的夹角，设置衰减参数，即（反光度， shininess）

## 材质

- 即物体对于光源作用做出反应的一系列参数

## 投光物体

### 平行光

没有固定位置，只有光源方向

### 点光源(Point Light)

只有位置，没有方向。

增加了距离衰减项(Attenuation)

### 聚光灯(Spot Light)

有方向位置，还有指定聚光半径的切光角，即固定了照亮范围

#### 平滑光照边缘

增加衰减项$I = \frac{\theta - \gamma}{\epsilon}$

## 多光源系统

- 我们不希望在 `main` 函数中计算所有光源，而是将其封装到GLSL函数中.

## 纹理映射

坐标系统：从左下角的(0,0)到右上角的(1,1)

## 阴影映射(Shadow Mapping)

> 扩展高级算法：**全向阴影贴图**和**级联阴影贴图**

**思想**：从光源视角渲染场景，将生成的深度值存储到纹理中，获得一个**深度贴图（depth map**或**阴影贴图（shadow map）**

**步骤**：

- 生成深度贴图

```c++
unsigned int depthMapFBO;
glGenFramebuffers(1, &depthMapFBO);

const unsigned int SHADOW_WIDTH = 1024, SHADOW_HEIGHT = 1024;

unsigned int depthMap;
glGenTextures(1, &depthMap);
glBindTexture(GL_TEXTURE_2D, depthMap);
glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT, 
             SHADOW_WIDTH, SHADOW_HEIGHT, 0, GL_DEPTH_COMPONENT, GL_FLOAT, NULL);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT); 
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);  

glBindFramebuffer(GL_FRAMEBUFFER, depthMapFBO);
glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, depthMap, 0);
glDrawBuffer(GL_NONE);
glReadBuffer(GL_NONE);
glBindFramebuffer(GL_FRAMEBUFFER, 0);
```

- 渲染深度贴图的时候确保变换是灯光方的.
- 仅仅使用顶点着色器的坐标变换，片段着色器可以为空，因为深度测试总是开启
- 渲染片段着色器时新增加一个到灯光视角的变换坐标输入（在顶点着色器中计算），然后变换至灯光式视角下的深度，与深度测试的采样进行比较改变颜色.

### 失真的解决

根据角度增加偏移量，使得得到的深度小于表面

- 但是会导致阴影悬浮的问题
    - 解决办法：由于偏移到物体内部，那么直接将物体正面剔除，深度采物体反面的内部

### 点阴影

**omnidirectional shadow maps**

> 关注点光源产生的阴影

**主要思想**：使用立方体贴图，来保存每个方向上的深度信息

**流程**:

- 创建一个立方体贴图
- 每个面一个深度贴图.
- 直接将立方体贴图作为深度缓冲区的贴图（几何着色器，中有layer可以控制渲染到哪个面）
- 深度直接用距离除以远平面
- 直接再立方体贴图上进行采样，而不用将顶点坐标转换到灯光视角

### PCF（Percentage-closer filtering）

1. 2D图像周边采样取平均值
2. 在点阴影下则是3D周边点采样取平均值

## Cascaded Shadow Mapping（级联阴影贴图）

想要解决的问题：
- 只对视野区域的物体进行阴影渲染
- 阴影正交投影与视锥体不合适
- 阴影距离变大，分辨率就下降

多层阴影贴图渲染

- 将视锥体分层
- 计算紧密贴合视锥体的正交投影矩阵
- 每个视锥体渲染一个阴影贴图
- 将所有的阴影贴图传给片段着色器
- 根据片段的深度选择对应的阴影贴图

问题是：不同层间的阴影有明显分界线

OpenGL 有以下特性

```glsl
uniform sampler2DArray shadowMap;
texture(depthMap, vec3(TexCoords, currentLayer))
```


## 参考资料

[LearnOpenGL | 颜色](https://learnopengl-cn.github.io/02%20Lighting/01%20Colors/)

[LearnOpenGL | 基础光照](https://learnopengl-cn.github.io/02%20Lighting/02%20Basic%20Lighting/)

[LearnOpenGL | 材质](https://learnopengl-cn.github.io/02%20Lighting/03%20Materials/)

[LearnOpenGL | 投光物体](https://learnopengl-cn.github.io/02%20Lighting/05%20Light%20casters/)

[LearnOpenGL | 多光源系统](https://learnopengl-cn.github.io/02%20Lighting/06%20Multiple%20lights/)

[LearnOpenGL | 阴影映射](https://learnopengl-cn.github.io/05%20Advanced%20Lighting/03%20Shadows/01%20Shadow%20Mapping/)

[LearnOpenGL | PointShadows](https://learnopengl.com/Advanced-Lighting/Shadows/Point-Shadows)
