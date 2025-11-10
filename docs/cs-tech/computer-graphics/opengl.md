
**什么是GLFW?**:是一个开源的、跨平台的库，专门用于创建和管理 OpenGL 和 Vulkan 应用程序所需的窗口、上下文和输入。
### 注意事项

#### 顶点坐标

**顶点坐标**在经过**顶点着色器**后应该变为**标准化设备坐标**

> 当然，假如你的顶点着色器没有做任何变换，只是直接将坐标传递给了片段着色器，那么你应该在将数据传递给顶点着色器之前就将坐标变换为标准化设备坐标。

### 基础特性

**缓冲对象类型**：
> 可以同时绑定多个缓冲，只要它们类型不同
- `GL_ARRAY_BUFFER`：顶点缓冲对象
#### 顶点缓冲对象（Vertex Buffer Objects，VBO）

- **作用**：在 GPU 内存中存储顶点信息，批次发送数据到显卡.
- **使用**：

1. 新建缓冲区
```c++
unsigned int VBO; # 待存储ID
glGenBuffers(1, &VBO); # 新建一个缓冲对象
```
2. 绑定缓冲

```c++
glBindBuffer(GL_ARRAY_BUFFER, VBO); 
```

绑定后，任何（在`GL_ARRAY_BUFFER`目标上的）缓冲调用，都会用来配置当前的缓冲（VBO），比如如下调用：

3. 缓冲调用
```c++
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW)
```

- **参数解释**:指定显卡管理数据模式
	- `GL_STATIC_DRAW` ：数据不会或几乎不会改变。
	- `GL_DYNAMIC_DRAW`：数据会被改变很多。
	- `GL_STREAM_DRAW `：数据每次绘制时都会改变。


#### 顶点数组对象（Vertex Array Object，VAO）

> 配置顶点属性，实际上在配置与shader的交互信息

- **作用**：在配置顶点属性指针时，只需调用一次。
- **保存内容**：
	- `glEnableVertexAttribArray`和`glDisableVertexAttribArray`的调用。
	- 通过`glVertexAttribPointer`设置的顶点属性配置。
	- 通过`glVertexAttribPointer`调用与顶点属性关联的顶点缓冲对象。

- **使用**：

1. 创建

```c++
unsigned int VAO;
glGenVertexArrays(1, &VAO);
```

2. 绑定与使用

```c++
// ..:: 初始化代码（只运行一次 (除非你的物体频繁改变)） :: .. 
// 1. 绑定VAO 
glBindVertexArray(VAO); 
// 2. 把顶点数组复制到缓冲中供OpenGL使用 
glBindBuffer(GL_ARRAY_BUFFER, VBO); 
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW); 
// 3. 设置顶点属性指针 
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0); glEnableVertexAttribArray(0); 

[...] 

// ..:: 绘制代码（渲染循环中） :: .. 
// 4. 绘制物体 
glUseProgram(shaderProgram); 
glBindVertexArray(VAO); 
someOpenGLFunctionThatDrawsOurTriangle();
```

### 使用记录




#### 数学变换
`glm::radians()`：将角度制变换为弧度制

#### 绘制模式
绘制参数:

`GL_TRIANGLE_FAN`:将第一个顶点作为中心顶点，接下来的顶点两两与中心顶点组成一个三角形.
- **示例输入**：`V0,V1,V2,V3,V4,...`
- **实际三角形**:`V0,V1,V2` \ `V0,V2,V3` \ `V0,V3,V4` ...
- **使用代码**:` glDrawArrays(GL_TRIANGLE_FAN, 0, static_cast<GLsizei>(_vertices.size()));`
