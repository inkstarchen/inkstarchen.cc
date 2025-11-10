## 泛光
> 一种显示光源的效果.

Bloom与HDR是两种不同的技术.但Bloom在HDR下能更好地起效.

- 通过阈值获得亮光区域
- 通过模糊过滤器得到光照图
- 和原先的HDR图进行融合

### MRT(Multiple Render Targets)
声明多个片段着色器输出，能够在一个渲染阶段中获得多个图像.

### 实现模糊核

> 高斯模糊的性质让我们可以通过两阶段模糊来实现

### 混合材质

## SSAO (screen-space ambient occlusion)

AO(环境光遮蔽)
- 使用深度图来进行遮蔽
- 引入随机方向性，足够覆盖大部分情况，但是会引入噪声
- 采样是生成点的坐标，然后比较其
我们采用一个normal-oriented hemisphere，我们不考虑片段内部几何的影响

### Sample buffers

SSAO需要几何信息来确定遮蔽系数.
- 每个片段的位置向量
- 每个片段的法向量
- 每个片段的albedo color
- 采样核
- 每个片段的随机旋转向量

## HDR（high dynamic range）

> 相对于 LDR(low dynamic range) 0 -1

HDR到LDR的映射过程叫做 tone mapping，存在不同的算法.

我们在渲染时，总是将色彩值截断在0-1之间，如果叠加的色彩值超过1.0，就会都被截断在1.0，这会使得画面损失细节.

一种好的处理方法是，让色彩值暂时地超过1.0，最后再将他们转换成原来的范围.
高动态范围还能让我们正确地声明光源的亮度，从而做出区分。

> 我们需要使用`GL_RGB16F,GL_RGBA16F,GL_RGB32F 或 GL_RGBA32F`来存储,这些被称为 floating point framebuffer

###  Reinhard tone mapping
```glsl

void main()
{             
    const float gamma = 2.2;
    vec3 hdrColor = texture(hdrBuffer, TexCoords).rgb;
  
    // reinhard tone mapping
    vec3 mapped = hdrColor / (hdrColor + vec3(1.0));
    // gamma correction 
    mapped = pow(mapped, vec3(1.0 / gamma));
  
    FragColor = vec4(mapped, 1.0);
}    
```

```glsl
uniform float exposure;
void main() { const float gamma = 2.2;
vec3 hdrColor = texture(hdrBuffer, TexCoords).rgb;
 // exposure tone mapping 
vec3 mapped = vec3(1.0) - exp(-hdrColor * exposure); 
// gamma correction 
mapped = pow(mapped, vec3(1.0 / gamma)); 
FragColor = vec4(mapped, 1.0); }
```


### 参考资料
[LearnOpenGL | Bloom](https://learnopengl.com/Advanced-Lighting/Bloom)