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

### 参考资料

[LearnOpenGL | 颜色](https://learnopengl-cn.github.io/02%20Lighting/01%20Colors/)

[LearnOpenGL | 基础光照](https://learnopengl-cn.github.io/02%20Lighting/02%20Basic%20Lighting/)

[LearnOpenGL | 材质](https://learnopengl-cn.github.io/02%20Lighting/03%20Materials/)

[LearnOpenGL | 投光物体](https://learnopengl-cn.github.io/02%20Lighting/05%20Light%20casters/)

[LearnOpenGL | 多光源系统](https://learnopengl-cn.github.io/02%20Lighting/06%20Multiple%20lights/)