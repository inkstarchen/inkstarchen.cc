## 指标计算


### 性能计算

$Performance = \frac{1}{Execution_Time}$

- Clock Cycle Time(period) : duration of a clock cycle
- Clock Rate(frequency) : cycles per second

$CPU\_Time = CPU\_Clock\_Cycles \times Clock\_Cycle\_Time = \frac{CPU\_Clock\_Cycles}{Clock\_Rate}$

- Average cycles per instruction (CPI)

$CPI = \frac{CPU\_Clock\_Cycles}{Instruction\_Count}$



### 阿姆达尔定律Amdahl’s Law

$Improved\_Execution\_Time = \frac{Affected\_Execution\_Time}{Amount\_of\_Improv ement} + Unaffected\_Execution\_Time$

$Speedup_{overall} = \frac{Execution\_time_{old}}{Execution\_time_{new}} = \frac{1}{(1-Fraction_{enhanced}) + \frac{Fraction_{enhanced}}{Speedup_{enhanced}}}$

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


平均故障时间：Mean time to failure(MTTF)

平均修复时间：Mean time to repair(MTTR)

故障间平均时间：Mean time between failures(MTBF) = MTTF + MTTR

Module availability = MTTF/MTBF

