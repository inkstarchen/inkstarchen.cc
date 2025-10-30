## 脑机接口


>脑机接口：建立大脑与外部设备的直接交互，绕过神经和肌肉实现信息传递

### 主要的探究的问题

- **接收神经信号：**如何通过传感器从皮肤表面或组织内部获得神经信号
- **理解神经信号：**如何解析获得的神经信号
- **利用神经信号：**利用神经信号能够做什么
- **生成神经信号：**如何生成神经信号传递给大脑

### 目的

- 理解大脑活动
- 从神经信号或模式识别大脑活动（这模式指什么）Signal Processing
- 将其转换成能被机器理解的指令
- 将外部信息转换成大脑的反馈信号


### 应用领域

- 假肢控制(怎么接收大脑信号或肌肉信号,怎么分析信号,怎么转换成机器信号)
- 恢复感官功能(像生物结构一样激发大脑:首先要理解原先的信号是怎样的,同时做到如何去激发和调试)
- 辅助交流
- 康复训练
- 通过神经信号激发增强记忆和认知功能
- 神经科学研究
- VR\AR控制(就是直接将神经信号转换成控制信号)

### 脑机接口的分类

**非侵入式（Non-Invasive）**

- EEG(Electroencephalography)
	- EEG measeres the elecric activity, which means that voltage difference is recorded. it needs to be recorded symultaneously.
	- amplifier needed(far from the neurons)
- MEG(magnetoencephalgraphy)
	- MEG record the magnetic feilds, and it has better spatial resolution than EEG.Because it pass through the skull and scalp, whereas the electrical fields are volume condected through these tissues.
- PET(position emission tomography)
	- 利用正电子的湮灭效应产生的伽马射线,检查伽马射线,来显示脑区的电子含量,检测大脑活动
- fMRI(functional magnetic resonance imaging)
	- Tubingen fMRI-Brain Computer Interface
- fNIRS(near-infrared spectroscopy)
	- 利用红外光谱分析血液流动变化,从而间接检测大脑活动

**半侵入式（Semi-Invasive）**

- ECoG （Electrocorticography）

**侵入式（Invasive(Implanted Micro Electrodes)）**

- Single unit
- Multiple unit
	- 疤痕组织的形成会使得信号逐渐减弱


## 机器人学

### 机器人地图的分类
- 尺度地图(Metric Map)
- 拓扑地图(Topological Map)
- 语义地图

#### 具体地图

- 占据栅格地图(Occupancy Grid Map)
- 八叉树地图
- 点云地图
- ESDF地图

#### 路径搜索
- 基于采样的方法
    - PRM(Probabilistic Road Map)
    - RRT(Rapidly-exploring Random Trees)
    - RRT*
- 基于搜索的方法：均有一个对应的状态空间图
    - 图搜索:DF,BFS
    - Dijkstra,A*
    - JPS(Jump Point Search)

### 群体机器人

#### 群体行为特点

- 有限的局部信息，个体对于整体结构没有全局性了解
- 简单的个体规则，个体遵从简单行为规则，而形成全局结构
- 全局结构涌现出有利功能

> 自然界生物是如何在动态环境中执行复杂的任务，且没有任何控制和集中式的协调？

> 大量个体仅能观察部分的环境信息是如何解决全局的问题？

> 群体的认知能力是如何从个体有限的认知能力中涌现出来的？

#### 群体机器人的定义
- Dorigo and Sahin(2004)定义
- Sharkey（2007）定义

#### 群体智能的关键机制

通过局部的个体之间相互作用涌现出具有全局效果的结构
- 聚合（Aggregation）
- 图案形成(Pattern Formation)
- 自组装(Self-assembly)
- 群体搬运(Collective Transport)
- 群体探索(Collective Exploration)

#### 集群算法

基于Virtual Structures的编队控制VRB(virtual rigid body)

虚拟势场法Vittual potential field（VPF）

VO（Velovity Obstacle）

**改进**：

RVO（reciprocal velocity Obstacle）

### 定位方法

#### 外部定位

- 确定机器人在世界（全局）坐标系中的位置/位姿，进行导航规划

GPS：全球定位系统

#### 视觉定位

基于空间标识的定位原理
- 激光反射板、特定标志牌
- 三个路标能够确定机器人的位置和姿态

概率融合能够避免非唯一数据关联引起的歧义。

### 脉宽调制技术

把连续变化的控制电压转化为固定频率的方波信号，方波占空比与电压大小成正比，利用方波信号控制电机调速的技术称为 **脉宽调制技术**

### 控制

**开环控制**、**闭环控制**

#### 步进电机
- 通过脉冲信号控制，线性开环控制

### 传动

传功比（减速比）：指减速机构输入速度与输出速度之比

减速作用：减小速度、增大力矩

## 加密算法

### 非对称加密算法

- 什么是对称加密？
	- 加密和解密使用同一套密钥
- 什么是密钥？
	- 在加密解密过程中所需要的关键信息，控制加密解密的结果
	- 以AES算法为例子

### AES算法

- 什么是AES算法？
	- AES是Advanced Encryption Standard的简称，高级加密标准，是一种对称加密算法标准
- AES算法怎么实现？
	- 以AES-128为例，密钥是128位的二进制序列
	- 思想：一轮一轮打乱 + 混合数据