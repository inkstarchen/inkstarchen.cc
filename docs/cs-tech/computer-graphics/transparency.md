## 混合(Blending)

>  实现物体透明度的一种技术,实际颜色为物体本身颜色和背后其它物体的颜色的不同强度结合

### 丢弃片段

以草纹理贴图为例，草的部分显示，其它部分不显示.

!!! note "OpenGL中的带透明度纹理加载"
    `glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data);`加载时将通道设置为`GL_RGBA`

    丢弃片段在着色器代码中,`discard`命令保证片段不会进一步处理.

    ```c++
    if(texColor.a < 0.1)
        discard;
    ```

> 半透明有色边框问题参照文档

### 混合

```c++
glEnable(GL_BLEND);
```

混合方程

$$C_r = C_s * F_s + C_d * F_d$$

参数设置参考文档

```c++
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
glBlendFuncSeparate(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_ONE, GL_ZERO);
glBlendEquation(GLenum mode); // 混合运算符
```

> 需要保证渲染的顺序，可参照混合文档

## 帧缓冲

> 颜色缓冲、深度缓冲、模板缓冲的总和叫做帧缓冲(Framebuffer)

```c++ title="创建帧缓冲"
unsigned int fbo;
glGenFramebuffers(1, &fbo);
glBindFramebuffer(GL_FRAMEBUFFER, fbo); // GL_READ_FRAMEBUFFER, GL_DRAW_FRAMEBUFFER
...
glBindFramebuffer(GL_FRAMEBUFFER, 0);
glDeleteFramebuffers(1, &fbo);
```

检测帧缓冲是否完整

```c++
if(glCheckFramebufferStatus(GL_FRAMEBUFFER) == GL_FRAMEBUFFER_COMPLETE)
```

**离屏渲染**：渲染到一个不显示到屏幕上的帧缓冲

### 纹理附件

> 所有渲染操作的结果会被存储在一个纹理图像中

```c++
unsigned int texture;
glGenTextures(1, &texture);
glBindTexture(GL_TEXTURE_2D, texture);

glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 800, 600, 0, GL_RGB, GL_UNSIGNED_BYTE, NULL);

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, texture, 0);
// 参数请查看文档
```

### 渲染缓冲对象附件

> 优化后的一个类型，写入和复制到其它缓冲更快.

```c++
unsigned int rbo;
glGenRenderbuffers(1, &rbo);
glBindRenderbuffer(GL_RENDERBUFFER, rbo);
glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH24_STENCIL8, 800, 600);
glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_STENCIL_ATTACHMENT, GL_RENDERBUFFER, rbo);
```

### 后期处理

#### 反相

```c++
void main()
{
    FragColor = vec4(vec3(1.0 - texture(screenTexture, TexCoords)), 1.0);
}
```

#### 灰度

```c++
void main()
{
    FragColor = texture(screenTexture, TexCoords);
    float average = 0.2126 * FragColor.r + 0.7152 * FragColor.g + 0.0722 * FragColor.b;
    FragColor = vec4(average, average, average, 1.0);
}
```

#### 核效果

> 此部分可以参照到计算机视觉部分，图像处理，只不过是使用OpenGL加shader实现.

## 深度测试

线性深度缓冲

$$F_{depth} = \frac{z - near}{far - near}$$

非线性深度缓冲

$$F_{depth} = \frac{1/z - 1/near}{1/far - 1/near}$$

- **提前深度测试**

!!! note "深度测试"
    ```c++
    glEnable(GL_DEPTH_TEST); // 当通过深度测试则存储该片段的z值

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glDepthMask(GL_FALSE); // 禁用深度写入

    glDepthFunc(GL_LESS); // 参数设置请参照文档
    ```

### 深度冲突

**解决方案**

- 物体摆放开一些
- 近平面远一些
- 更高精度的深度缓冲

## 顺序无关透明-深度剥离

- 论文资料[interactive-order-independent-transparency](https://www.gamedevs.org/uploads/interactive-order-independent-transparency.pdf)

问题引入：标准深度测试只保留最近的片元，而没有记录次远的片元.

### **深度剥离(Depth-Peeling)**

**主要思想**：将一轮的深度测试扩展到$n$轮，每一轮获得不同层的深度和颜色信息.

> OpenGL没有原生的深度剥离，使用阴影映射来替代，只不过用透明度测试来实现.

后面部分：在讨论计算复杂精度值出现的问题

> 缺点：每层都需要一次渲染

## 对偶深度剥离(DualDepthPeeling)

- 论文资料[DualDepthPeeling](https://my.eng.utah.edu/~cs5610/handouts/DualDepthPeeling.pdf)

**主要思想**：利用OpenGL特性，前后同时进行颜色混合.

### 颜色混合公式（从前往后）

> 具体过程查看资料

$$C_{dst} = A_{dst}(A_{src}C_{src}) + C_{dst}, \; A_{dst} = (1 - A_{src})A_{dst}$$

其中初始化:$A_{dst} = 1.0 , C_{dst} = 0$

!!! note "OpenGL"
    ```c++
    glEnable(GL_BLEND); 
    glBlendEquation(GL_FUNC_ADD); 
    glBlendFuncSeparate(GL_DST_ALPHA, GL_ONE, 
                        GL_ZERO, GL_ONE_MINUS_SRC_ALPHA); 
    ```

### 透明度预乘(pre-multiplied alpha)

透明度预乘：将透明度乘以颜色，从而得到预乘后的颜色.

> 与混合公式相同，需要明白混合公式每次混合后的得到的都是不透明的颜色.

### 一轮近似

> 希望通过数学的方式得到一个近似的混合方式

使用三个缓冲分别存储:$\sum[(RGB)A]$,$\sum A$, $n$

通过取平均的方式得到混合结果

$$C_{dst} = \frac{\sum[(RGB)A]}{\sum A}$$

#### 一些过程思考的内容

- framebuffer实际是绑定一个纹理输出
```

_colorBlendFbo -> _colorBlendTexture & _depthTextures[0]
_fbos -> _colorTexures & _depthTextures
```


总体采用从前往后的混合逻辑
- 所以第一次渲染完后，有第一层深度图和颜色图 | \_depthPeelingInitShader就是正常绘制.
- \_depthPeelingShader 需要接收一个深度图用于截断前面渲染过的面
	- 这里深度图和颜色都是第二层得到的了(r,g,b,a)没有任何处理
	- 这个shader中有alpha层，但是我只需要次近层的颜色，因此要关闭颜色混合
- \_depthPeelingBlendShader 需要接收一个混合后的颜色纹理.
- 所以我需要做的是，将次层的颜色纹理传入，然后和原本在colorblend已经存在的纹理进行混合
	- 混合阶段单纯是将目标色彩与刚采样得到的色彩进行混合，不要改变深度了.
	  
先检查所有的输入是否有对应的输出

> 我需要搞清楚最后的渲染结果

最后是渲染一个全屏的矩形，
- 首先只有一个物体，深度测试启用与否没有影响直接关闭.
- 同时要明白混合是与缓冲区的颜色进行混合，与是否有物体无关.由于我们的矩形是铺满屏幕的，因此只需要关闭混合模式就行.
- 查看`final`的着色器可以知道是采样颜色与设置的背景色做了混合.

检查一下逐层的渲染结果和最终混合结果

- 第一层
- 第二层：
	- 需要启用深度检测，因为我们需要写入第二层的深度图
	- 比较还是取小的，只不过我们会使用上一层的深度图去过滤掉比上一层还近的片段.
	- 这里我们同样不要启用混合，因为我们要单独渲染出这层的图像.
	- 绘制完毕后解绑对象
	- 如果没有通过深度测试的对象那么我们就直接跳出循环，说明`_colorBlendTexture`中已经是我们需要的图像了
	- 混合阶段：就是混合`_colorBlendTexture`和`_color_Textures[i]`中的图像,我们使用全屏四边形来进行两个图像的混合.
		- 深度测试无关紧要：关闭
		- 由于`_colorBlendFbo`绑定着`_depthTexture[0]`，我们不希望混合阶段干扰我们的深度剥离结果，因此关闭深度写入.
		- 由于要混合则启动混合模式.颜色混合要注意以下几点
			- 初始的渲染是预乘了透明度，且`alpha = 1 - alpha`
			- 我们由近到远混合，采用的混合公式如下
			- $C_d = A_d * A_s * C_s + C_d, A_d = (1-A_s) * A_d$
			- 由于在深度剥离的着色器中最终结果也是预乘的，而透明度没有做处理，因此预乘的关系颜色公式写为
			- $C_d = A_d * C_s + C_d, A_d = (1 - A_s)*A_d$
	- 查看第二，三层图像
	- 依次查看混合结果

## 参考资料

- [LearnOpenGL | 混合](https://learnopengl-cn.github.io/04%20Advanced%20OpenGL/03%20Blending/)
- [LearnOpenGL | 帧缓冲](https://learnopengl-cn.github.io/04%20Advanced%20OpenGL/05%20Framebuffers/)
- [LearnOpenGL | 深度测试](https://learnopengl-cn.github.io/04%20Advanced%20OpenGL/01%20Depth%20testing/)
- [图形学基础 - 着色 - 透明度混合-OIT](https://zhuanlan.zhihu.com/p/368065919)
- [关于理解 Premultiplied Alpha 的一些 Tips](https://zhuanlan.zhihu.com/p/344751308)