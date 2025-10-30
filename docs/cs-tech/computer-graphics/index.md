## 课程分数组成

lab 30% big project 40% class 30%

## 目标

modeling, processing and displaying objects in the world in a computer.

- 建模(拆解)
	- $点\rightarrow线\rightarrow面\rightarrow体$
- 模拟行为
- 显示世界
- 交互

**数字孪生的最终目标：** 现实世界的变化能够实时地反应到数字世界中来。

**基本问题**
**主流方法**
**图形应用开发**

**帧缓冲**:

一系列屏幕缓冲：
- 用于写入颜色值的颜色缓冲
- 用于写入深度信息的深度缓冲
- 允许我们根据一些特定条件丢弃特定片段的模板缓冲
这些缓冲的结合叫做帧缓冲（Framebuffer）
- 储存在GPU内存的某处

**PBR**:

- Physically-Based-Rendering 基于物理的渲染
- 指的是一些在不同程度上都基于与现实世界的物理原理更相符的基本理论所构成的渲染技术的集合
考虑以下条件：
- DIFFUSION & REFLECTION （扩散和反射）
- TRANSLUCENCY （透明度）
- Metallic（金属属性）
- Albedo（反照率）
- Smoothness（光滑度）
- Normal Map（法线贴图）
- Height Map（高度贴图or视差贴图）
- Occlusion（遮挡剔除）

综合基本理论从而实现更加符合物理的渲染

- 没有太多可自定义扩展的地方，最多是性能调优
三个条件
- 基于微平面（Microfacet）的表面模型
- 能量守恒
- 应用基于物理的BRDF
