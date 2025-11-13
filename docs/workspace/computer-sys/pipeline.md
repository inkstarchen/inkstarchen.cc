##  流水线

> 重叠执行是流水线的基础

**基本概念**: 将一个过程分成若干个子过程，每个过程用一个功能的单元实现

**设计理念**: 流水线中的每个阶段的运行时间应该均等，不然会出现瓶颈。

### 依赖

- 数据依赖 -> 数据冒险（RAW\WAR\WAW）-> 数据前递、暂停、代码调度
- 命名依赖（在改变对象命名后，仍然使用旧名）
- 控制依赖 -> 控制冒险 -> 暂停\分支预测（动态分支预测内含状态机）

### 动态分支预测

- 维护历史分支表(Branch History Table(BHT))：即状态机维护
- 分支目标缓存(Branch-Target Buffer/Branch-Target Cache)：用于快速获得分支目标地址

#### 乱序执行

将ID阶段分成两个阶段：Issue（IS）和Read Operands（RO）

- Issue：解析指令，检查结构冒险，顺序发射
- Read Operands：等待直到没有数据冲突，读取操作数，乱序执行

**计分板算法(Scoreboard Algorithm)**

**托马斯罗方法Tomasulo’s Approach**

- 缺点: 乱序执行且乱序完成，在异常中断时无法保持一致性
- 重排序缓冲(Reorder Buffer(ROB))
