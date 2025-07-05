## 指标计算

#### Performance

CPU Time $=$ CPU Clock Cycles $\times$ Clock Cycle Time $=\frac{CPU\quad Clock \quad Cycles}{Clock\quad Rate}$

Average cycles per instruction(CPI)

$$CPI=\frac{CPU\_Clock\_Cycle}{Instuction\_Count}$$

#### Amdahl's Law

$$Speedup_{overall}=\frac{Execution\_time_{old}}{Excution\_time_{new}}=\frac{1}{(1-Fraction_{enhanced})+\frac{Fraction_{enhanced}}{Speedup_{enhanced}}}$$

#### 吞吐量

$$TP=\frac{n}{T}$$

$$TP=\frac{n}{\sum^m_{i=1}\delta t_i+(n-1)max(\delta t_1,\delta t_2,\cdots,\delta t_m)}$$

$$TP=\frac{n}{n+m-1}TP_{max}$$

$$TP_{max} = \frac{1}{max(\delta t_1, \delta t_2, \cdots, \delta t_m)}$$
#### 加速比

$$sp = (n×m×\delta t_0)/(m+n-1)\delta t_0$$

#### 效率

$$\eta = (n×m× \delta t_0)/(m+n-1)\delta t_0 × m$$

### 可靠性

Mean time to ailure (MTTF)
Mean time to repair (MTTR)
Mean time between failures (MTBF) = MTTF + MMTR

Module availability = MTTF / MTBF

## 分页机制
### 基本思想

将地址空间等分成某一固定大小的页；每一页大小由硬件或操作系统决定。
- 将进程的逻辑地址空间分成若干大小相等的片，称为页面或页
- 内存空间分成与页大小相等的若干存储块，称为物理块或页框
- 在为进程分配内存时，以块为单位，将进程中的若干页装入多个可以不相邻的块中