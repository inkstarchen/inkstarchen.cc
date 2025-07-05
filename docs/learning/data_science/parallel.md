## 并行理论

PRAM model
```c
for P_i, 1 <= i <= n pardo
	B(0, i):= A(i)
	for h = 1 to log n do
		if i <= n/2^h
			B(h, i):= B(h-1,2i-1) + B(h-1,2i)
		else stay idle
	for i = 1:output B(log n, 1);for i > 1:stay idle
```
$T(n) = log n +2\qquad W(n) = n+ n/2 +n/2^2 + \cdots+n/2^k +1 = 2n$

### Measuring the performance
Work load -total number of operations:$W(n)$
Worst-case running time: $T(n)$
- $W(n)$operations and $T(n)$ time
- $P(n) = W(n)/T(n)$ processors and $T(n)$ time (on a PRAM)
- $W(n)/p$ time using any number of $p\leq W(n)/T(n)$ processors (on a PRAM)
- $W(n)/p + T(n)$ time using any number of $p$ processors(on a PRAM)

## 处理器下的并行规则

### PRAM模型（Parallel Random Access Machine）
多指令多数据流（MIMID）并行机中的一种具有共享存储模型
- EREW（Exclusive Read Exclusive Write）

不允许多个处理器同时进行内存访问（读与写）

- CRCW(Concurrent Read Concurrent Write)

允许多个处理器同时进行内存访存（读与写）
写入冲突时需要冲突解决机制，如优先级、合并策略等。

- CREW（Concurrent Read Exclusive Write）
- ERCW（Exclusive Read Concurrent Write）

Harware instructions 
test-and-set
多核锁总线
compare and switch


mutex lock spin lock
spin lock(spin 浪费cpu资源)->Sleep

Semaphore相互之间使用spin lock
context switch overhead 
short spin lock
long Semaphore

Bounded-Buffer Problem
定义与写
Readers-Writers Problem

## Parallel Random Access Machine(PRAM)
Arbitrary rule
Prority rule
Common rule
#### The summation problem
归并向上计算（二分）
time cost: $O(\log n)$

W(n): work load
T(n):每项任务所需的最坏情况，在n个处理器被满足的情况下
#### Random Sampling
```c
while(there is an element larger than M){
	for(each element larger than M)
		Throw it into a random place in a new B(n^{7/8});
	Compute a new M;
}
```
为了凑出$O(n)$时间而做的设计。

#### Parallel Ranking
Stage 1:Partitioning
- $A\_Select(i) = A(1+(i-1)logn)\qquad T=O(logn)$
- $B\_Select(i) =B(1+(i-1)logn) \qquad W=O(n)$

![[images/Pasted image 20241230131043.png]]

#### A Doubly-logarithmic Paradigm
化分成$\sqrt{n}$大小的问题
再分治法处理子问题
![[images/Pasted image 20241230132149.png]]
先分割，在每个分割问题下执行$\sqrt{n}$分治法,最后使用并行法
以规模$h=loglogn$进行划分运行,凑出来的
![[images/Pasted image 20241230132524.png]]

## Lock-Based Protocols

1. **互斥锁exclusive(X) mode**: 数据可读可写
2. **共享锁shared(S) mode**: 数据可读不可写

- 只有共享锁之间能够共存

- 当锁的请求等待路线之间存在环时，就会出现死锁(deadlock)的情况
- 当一个锁的情况持续被其它抢占时，就会出现饥饿(starvation)的情况

### 两阶段锁协议(Two-Phase Locking Protocol)

- 阶段一: 增长
	- 事务只能获得锁而不能释放锁
- 阶段二：收缩
	- 事务只能释放锁而不能获得锁

这是事务之间能够以获得锁的时间节点来串行排序

- Strict 2PL：事务在提交和中断前，保持他的所有互斥锁
- Rigorous 2PL：事务在提交和中断前，保持他的所有锁

### Graph-Based Protocols

- an alternative to two-phase locking

#### Tree Protocol

- 不会有死锁，且不需要回滚
- 但是并不确保可恢复性，同时可能锁定不需要获取的信息

### 死锁解决

- 提前定义(pre-declaration)：在执行之前获取他的所有锁
- 使用图控制协议

- Wait-die scheme:non-preemptive（非抢占）
	- 旧的事务会等待新事务释放对数据的控制
	- 但新事务不会等待，而是直接回滚
- Wound-wait scheme:pre-emptive（抢占）
	- 旧事务杀死新事务使其回滚，新事物会等待
- Timeout-Based Scheme
	- 事务在等待一定时间没拿到锁时会回滚

### 死锁检测

- Wait-for graph
- 死锁恢复:全部回滚，部分回滚

### 意图锁模式

- 意图共享锁(intention-shared(IS)):显式的指定低层的树
- 意图排他锁(intention-exclusive(IX)):显式的指定低层的树的排他和共享

- shared and intention-exclusive: