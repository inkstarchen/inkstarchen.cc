


DQN TRPO AC A2C A3C PPO QMIX WQMIX MAPPO GRPO

价值估计

## 具身智能

具身智能是指一种基于**物理实体**进行**感知**和**行动**的智能系统, 其通过智能体与环境的交互获取信息、理解问题、做出决策并实现行动, 从而产生智能行为和适应性

#### 目前的问题
- 物理实体采样效率低
- 安全问题（试错过程，会损失机器人自身，损伤环境）
### 仿真平台
- MuJoCo 通用物理引擎 （基于强化学习的决策动画）
- Isaac Gym
- SAPIEN 高度拟真仿真环境
### 机械臂与灵巧手

```python
train() -> task_registry.make_env
```

```python
if args is None -> helpers.get_args() //获取训练设置 -> parse_arguments // 解析训练设置
```

参数
```python
--resume 和 --load_run 重新加载的run_name
--checkpoint 保存的模型序号
--task 任务类型
--experiment_name
--run_name
--headless 不显示图形化界面
--horovod 分布式训练
--rl_device 用于训练的设备 如cuda:0
--num_envs 创建的环境数量
--seed 随机化种子
--max_iterations 最大训练轮次
```

将策略参数化$\pi_{\theta}(a|s)$
用神经网络拟合策略

- 策略参数化的优点
	- 具有更好的收敛性质
	- 在高纬度或连续的动作空间中更有效
	- 能够学习出随机策略
- 缺点
	- 通常会收敛到局部最优而非全局最优
	- 评估一个策略通常不够高效并具有较大的方差

无梯度优化可以有效覆盖低维参数空间，但基于梯度的训练仍然是首选，因为其具有更高的采样效率

参数化策略与表格形策略

- 表格型策略：若一个策略能最大化每个状态对应得值函数，则称该策略$\pi^*$是最优得.

$$\pi^*(s) = argmax_{a \in A} q_\pi (s, a). s \in S$$
- 参数化策略：若一个策略能最大化一个给定得标量指标，称该策略$\pi^\#$是最优得

$$\pi^\#(s)=argmax_{\pi}J(\pi(s)),\pi \in \Pi$$
### 基本思想

- 利用目标函数定义策略优劣性：$J(\theta)=J(\pi_\theta)$
- 对目标函数进行优化，以寻找最优策略

**问题**

- 目标函数$J(\theta)$怎么设计？
- 该目标函数关于参数的优化方向（如梯度$\nabla_\theta J(\theta)$）如何计算？

**优化方向**

- 目标函数不可微分：使用无梯度算法进行最优参数搜索
	- 有限差分方法、交叉熵方法、遗传算法等
- 目标函数可微分：利用基于梯度的优化方法寻找最优策略$\theta_{t+1} \leftarrow \theta_t + \alpha \nabla_\theta J(\theta_t)$

### 目标函数

1. 平均价值目标： $J(\theta) = E_s[v_{\pi_\theta}(s)]=\sum_{s \in S}{d(s)v_{\pi_\theta}(s)}$
2. 平均奖励目标： $J(\theta) = \sum_{s \in S}d(s) \sum_{a \in A} \pi_\theta(a|s)r(s,a)$
3. 平均轨迹回报目标： $J(\theta)=E_{\tau - p_\theta(\tau)}[\sum_t r(s_t,a_t)]$

- $d(s)$是状态分布，满足$\sum_{s \in S} d(s) = 1$
- $p_\theta$是轨迹分布：$p_\theta(s_1,a_1,\dots,s_T) = p(s_1)\Pi_{t=1}^{T-1}\pi_\theta(a_t | s_t) p(s_{t+1}|s_t,a_t)$
- 策略$\pi$越好（即参数$\theta$越好），则对于所有状态$s$,状态价值$v_{\pi_\theta}(s)$得均值也应当越大

### 状态分布

- 策略无关的状态分布
	- 简单做法：取$d(s)$为均匀分布，即每个状态都有相同的去那种$1/|S|$
	- 另一种做法是把权重集中分配给一部分状态集合。例如，在一些任务中，一个回合只从状态$s_0$开始，那么可以设置为：$d(s_0)=1,d(s \neq s_0)=0$
	
- 策略相关的状态分布
	- 通常选用稳态状态分布
	- $d(s)$是稳态状态分布：若对一个状态转移$s\rightarrow a \rightarrow s'$,满足：

$$d(s')=\sum_{s\in S} \sum_{a \in A}p(s'|s,a)\cdot \pi_\theta(a|s)\cdot d(s) $$

### Reiniforce算法

- 对于随机策略$\pi_\theta(a|s) = P(a|s,\theta)$

重要性采样

- 采到旧数据，将其映射成新数据

$$\begin{eqnarray}
E_{X-P}[f(X)] & = & \sum P(X)f(X) \\
& = & \sum Q(X) \frac{P(X)}{Q(X)}f(X) \\
& = & E_{X-Q}[\frac{P(X)}{Q(x)}f(X)] \\
\end{eqnarray}$$

$$J(\theta) = E_{\tau - p_\theta(\tau)}[r(\tau)]=E_{\tau-p_\theta(\tau)}[\frac{p_\theta (\tau)}{p_{\theta '}(\tau)}R(\tau)]$$
$$p_\theta (\tau) =p(s_1) \Pi^{\tau}_{t=1} \pi_\theta(a_t|s_t)p(s_{t+1}|s_t,a_t)$$

- 缺点：梯度的步长难以确定
	- 采集到的数据的分布会随策略的更新而变化
	- 较差的步长产生的影响大

### 自然梯度策略

### Actor-Critic方法

### 策略优化

Actor$\pi_\theta(a|s)$：行动者，采取动作使评论家满意的策略
Critic$Q_\Phi(s,a)$：学会准确估计行动者策略采取动作价值的值函数

#### DDPG（深度确定性策略梯度）
- 动作上噪声
- 离线策略
- 带噪动作的Q网络
- 对比学习

$$ \theta^{Q'} \leftarrow \tau \theta^Q + (1-\tau)\theta^{Q'}$$
$$\theta^{\mu'} \leftarrow \tau \theta^\mu + (1-\tau) \theta^{\mu '}$$

### 随机策略方法

强化学习策略优化的目标有两种形式
- 第一种$J(\theta) = E_{\tau - p_\theta(\tau)} [\sum_t \gamma^t r(s_t,a_t)]$
- 第二种$J(\theta)=E_{s_0 - p_\theta(s_0)}[V^{\pi_\theta}(s_0)]$

#### TRPO
- 控制新旧策略的差异，避免差异过大（使用KL散度）
- 在约束策略差异的条件下求解最优步长
- 自然策略梯度
$$D_{KL}(\pi_{\theta_{old}}||\pi_{\theta_{old+\delta \theta}})\leq \epsilon$$
具体实现

- 使用KL散度约束策略更新的幅度
- 实际上使用constraint violate as penalty
	- $- \lambda(D_{KL}(\pi_{\theta '}(a_t,s_t)||\pi_{\theta}(a_t|s_t)) - \epsilon)$

### PPO(Proximal Policy Optimization)
- 目前强化学习领域中具有较好效果与算法稳定性，是应用最广泛的强化学习极限算法之一

- 截断式优化目标

$$L^{CLIP}(\theta)=\hat{E}_t[min(r_t(\theta)\hat{A}_t, clip(r_t(\theta), 1-\epsilon,1+\epsilon)\hat{A}_t)]$$
- 多步时序差分方法计算优势函数
	- 在每次迭代中，并行N个actor收集T步经验数据
	- 计算每步的$\hat{A}_t$和$L^{CLIP}(\theta)$，构成mini-batch
	- 更新参数$\theta$，并更新$\theta_{old}\leftarrow \theta$
### SAC(Soft Actor Critic)
- off-policy
- 保持策略多样性：使用熵正则化
- 避免过度探索：经验回放，熵正则化


一个更新策略需要持续一段时间，
5 次 一个平均奖励
假如，下五次的平均奖励小于前一次，则增加选择空间直到探索空间
策略好则重用，不拓展选择空间，结果不好先观望，多次结果不佳则扩展选择空间

