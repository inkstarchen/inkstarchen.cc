## 贝叶斯决策论

贝叶斯决策论(Bayesian decision theory)是概率框架下实施决策的基本方法.

> 分类任务中，假设所有相关概率都已知的理想情形，选择最优的类别标记。

给定 $N$ 个类别，令 $\lambda_{ij}$代表将第$j$类样本误分类为第$i$类所产生的损失，则基于后验概率将样本$x$分到第$i$类的条件风险为：

$$R(c_i|x) = \overset{N}{\underset{j=1}{\sum}}\lambda_{ij}P(c_j|x)$$

**贝叶斯判定准则(Bayes decision rule)**

$$h^*(x) = \underset{c \in \mathcal{Y}}{arg \; min}R(c|x)$$

- $h^*$称为 **贝叶斯最优分类器(Bayes optimal classifier)**,其总体风险称为**贝叶斯风险(Bayes risk)**
- 反映了**学习性能的理论上限**

两种基本策略：

- **判别式(discrimnative)模型** 
    - 思路：直接对$P(c|x)$建模
    - 代表：决策树、BP神经网络、SVM

- **生成式(generative)模型**
    - 思路：先对联合概率分布$P(x,c)$建模，再由此获得$P(c|x)$
    - 代表：贝叶斯分类器

### 极大似然估计

**先假设某种概率分布形式，再基于训练样例对参数进行估计**


假定$P(x | c)$具有确定的概率分布形式，且被参数$\theta_c$唯一确定.则任务就是利用训练集$D$来估计参数$\theta_c$

> 估计结果的准确性严重依赖于所假设的概率分布形式是否符合潜在的真实分布

### 朴素贝叶斯分类器(naive Bayes classifier)

**三个假设**

- 概率模型假设
- 样本独立同分布假设
- **属性条件独立性假设（attribute conditional independence assumption）**

$$P(c|\textbf{x}) = \frac{P(c)P(\textbf{x}|c)}{P(\textbf{x})}$ = \frac{P(c)}{P(\textbf{x})} \overset{d}{\underset{i=1}{\prod}}P(x_i|c)$$

$P(\textbf{x})$对所有类别相同，于是

$$h_{nb}(x) = \underset{c \in \mathcal{Y}}{arg \; max}P(c)\overset{d}{\underset{i=1}{\prod}}P(x_i|c)$$

- 估计 $P(c) = \frac{|D_c|}{|D|}$
- 估计 $P(\textbf{x}|c)$
    - 对于离散属性,令 $D_{c,x_i}$表示$D_c$中在第$i$个属性上取值为$x_i$的样本组成的集合，则$P(x_i|c) = \frac{|D_{c,x_i}|}{|D_c|}$
    - 对于连续属性，考虑概率密度函数，假定$p(x_i|c) \sim \mathcal{N}(\mu_{c,i},\sigma_{c,i}^2)$,则有$p(x_i|c) = \frac{1}{\sqrt{2\pi}\sigma_{c,i}}e^{-\frac{(x_i-\mu_{c,i})^2}{2\sigma_{c,i}^2}}$

#### 拉普拉斯修正(Laplacian correction)

若某个属性值在训练集中没有与某个类同时出现过，则概率连乘时将“抹去”其它属性提供的信息.

令 $N$ 表示训练集 $D$ 中可能的类别数，$N_i$表示第$i$个属性可能的取值数

$$\hat{P}(c) = \frac{|D_c| + 1}{|D| + N}, \; \hat{P}(x_i|c) = \frac{|D_{c,x_i}| + 1}{|D_c| + N_i}$$

> 假设了属性值与类别的均匀分布，额外引入的bias

#### 朴素贝叶斯分类器的使用

- 如果对预测要求高：则预计算所有概率估值，使用时查表
- 如果数据更替频繁：则不进行然后训练，收到预测请求时再估值（懒惰学习，lazy learning）
- 如果数据不断增加：则基于现有估值，对新样本设计的概率估值进行修正（增量学习, incremental learning）

###  半朴素贝叶斯分类器

### 其它分类器

**AODE(Averaged One-Dependent Estimator)**

- 尝试将每个属性作为超父构建 SPODE
- 将拥有足够训练数据指出的 SPODE 集成起来作为最终结果

**高阶依赖** 提高泛化性能

- 明显障碍：随着 $k$ 的增加，估计$P(x_i|y,\textbf{pa}_i)$所需样本数将以指数级增加

### 贝叶斯网(Bayesian network)

$$B = \langle G, \Theta \rangle$$

也称为 **信念网**（brief network）

强调

- 输入信息的主观本质
- 对贝叶斯条件的依赖性
- 因果与证据推理的区别

#### 三变量间的典型依赖关系

- 用有向无环图来建模变量间的依赖关系.

#### 分析条件独立性

**有向分离(D-separation)**

道德图(moral graph)

#### 评分函数

通常基于信息论准则

例如 **最小描述长度（MDL, Minimal Description Length）**

给定数据集 $D$, 贝叶斯网$B = \langle G, \Theta \rangle$ 在 $D$ 上的评分函数：

$$s(B | D)$$

### 推断

- 基于已知属性变量的观测值

#### 吉布斯采样