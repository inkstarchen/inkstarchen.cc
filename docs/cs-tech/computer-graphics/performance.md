## 视锥体剔除

- 首先要定义构成视锥体的平面
    - 法向 | 距离
- 然后定义视锥体，由六个平面组成
- 计算每个平面的法向和面上一点

### Bounding volume

包围体积：有球形碰撞盒、AABB、OBB系列，越精细，所需的开销越大，当然剔除的精度越好.

### 一些解释

基础代码解释


```c++
glVertexAttribPointer(
    3,                    // location - 属性位置索引
    4,                    // size - 每个顶点的分量数量
    GL_FLOAT,             // type - 数据类型
    GL_FALSE,             // normalized - 是否归一化
    stride,               // stride - 步长（字节）
    (void*)(0 * unitSize) // pointer - 数据偏移量
);

    // 设置顶点除数，即隔几个实例更新一遍数据
    glVertexAttribDivisor(3, 1);
```

```c++
glGenTransformFeedbacks(1, &_transformFeedback) // 生成变换反馈对象
glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, _transformFeedback) //

glGenBuffers(1, &_transformFeedbackResultBuffer); //用于接收反馈对象.
glBindBuffer(GL_TRANSFORM_FEEDBACK_BUFFER, _transformFeedbackResultBuffer);
glBufferData(GL_TRANSFORM_FEEDBACK_BUFFER, _amount * sizeof(int), nullptr, GL_DYNAMIC_DRAW);

glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 0, _transformFeedbackResultBuffer); // 绑定缓冲到特定索引
glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, 0);
```

相机参数：

- fovy
- aspect
- znear
- zfar
- transform的接口可以获得相机的各个方向的向量.

Frustum需要构建的变量
四个平面
- Left、Right、Bottom、Top、Near、Far
平面需要的构建变量
> 已经实现了通过相机点和法向量构建平面的方法,同时构建时`normal`自动标准化,现在就是如何得到法向量的问题
- 法向量 normal
- 原点到平面的符号距离`signedDistance = dot(normal,-camera.position)`，以法向量方向为正.|  这需要平面上一个点作为辅助点，即相机点.
- 判断点是否在平面的正面只需要通过`distance = dot(normal,point) + signedDistance`
	- 为正:在平面正方向，为0:在平面上，为负：在平面负方向

最后计算还是在世界坐标系下进行剔除的判断计算，因为平面坐标都是在世界坐标系下的。

我们现在要做的是将aabb进行变换

最核心的思想，由于以原点为中心的立方体的八个角点代表了(x,y,z)的各个符号组合.

我们现在将原始坐标投影通过变换到变换后的坐标系上，再将其投影回原始的坐标系。由于符号组合的任意性，所以一定有一个由中心到角点的向量，经过两次变换后使得其x、y或z变为最大.

$$ \begin{bmatrix} u_x & u_y & u_z \\ v_x & v_y & v_z \\ w_x & w_y & w_z \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} u_x x + u_y y + u_z z \\ v_x x + v_y y + v_z z \\ w_x x + w_y y + w_z z \end{bmatrix} $$

$$x' = \begin{bmatrix} u_x \\ v_x \\ w_x \end{bmatrix} $$ 是 $x$ 在变换后坐标系的投影。

$|x'|$ 的大小代表了对 $x$ 轴的缩放。

## Deffered Shading（延迟渲染）

> 最重要的思想，推迟那些开销大的渲染流程，比如说光线渲染.

- 第一个轮：几何轮，渲染场景，获得几何信息至一个帧缓冲中，称其为 **G-buffer**，包含以下信息
	- Position
	- Normals
	- Albedo（反照率）
	- Specular （反射率）
- 第二轮：光照轮
	- 利用上一轮的buffer渲染光照结果.

缺点：
- 无法进行混合，也就是无法正常渲染透明物体.
- 且只能使用统一的光照流程

### 与前向渲染的混合

- 延迟渲染完后进行光立方体的前向渲染。
- 将深度图复制到后续的渲染过程中`glBlitFramebuffer`
- 这样我们能够对特定的一些物体和效果进行混合，而其它的不需要混合效果和特殊效果的物体就通过延迟渲染来做.

### 多光源渲染

> 引入光照体积，只计算在光照体积内的对应的光源影响

$$Frac = \frac{I_{max}}{Attenuation}$$

解出光照被截断的距离

事实上：GPU并行运行时，会执行所有分支，只不过会丢弃部分的结果.

### 资料

[Learn OpenGL | Frustum Culling](https://learnopengl.com/Guest-Articles/2021/Scene/Frustum-Culling)

[LearnOpenGL | 延迟渲染](https://learnopengl.com/Advanced-Lighting/Deferred-Shading)