
## Recovery System

### Recovery algorithms

- 在事务执行期间保障由足够的信息能够在出错后进行恢复
- 在出错后，恢复内容保证原子性、一致性和持续性

### Log-Based Recovery

一个日志由一系列日志记录组成，这些记录保存更新操作的信息。

- 在一个稳定存储器中保存
- 保存多份拷贝

#### 过程

- 事务开始$<T_i, start>$
- 在事务写入$(X)$之前$<T_i, X, V_1, V_2>$,其中$V_1$时旧值，$V_2$是新值
- 事务完成后$<T_i, commit>$

####  两种使用 方法

- 立即更新(immediate-modification)
	- 可以保存未提交的事务信息
	- 输出块的顺序与写回的顺序可以不同
- 延后更新(deferred-modification)
	- 只有提交后的事务信息可以被保存

#### 事务提交

当提交日志记录被写入稳定存储器时，事务正式提交。

### 撤销与重做

- Undo of a log record $<T_i, X, V_1, V_2>$, writes the old value $V_1$ to $X$
	- compensation log（补偿日志）$<T_i, X, V>$
	- complete $<T_i, abort>$
	- $undo(T_i)$
- Redo of a log record $<T_i, X, V_1, V_2>$, writes the new value $V_2$ to $X$
	- $redo(T_i)$,从第一条记录开始重做

### 从错误中恢复

- 需要撤销
	- 包含$<T_i, start>$，但是没有$<T_i,commit>$ 或者$<T_i, abort>$
- 需要重做
	- 包含$<T_i,start>$，也包含$<T_i,commit>$和$<T_i,abort>$

### 检查点

- 输出保存所有的日志记录
- 向磁盘输出所有修改过的块
- 向稳定存储器输出$<checkpoint L>$
- 做检查点时停止所有更新

每次仅仅撤销和重做检查点后的事务

两个阶段

- 重做阶段
	- $<T_i, X_j, V_1, V_2>$和$<T_i,X_j,V_2>$找到则重做
	- $<T_i,start>$找到则加入撤销表,$<T_i,commit>或者<T_i,abort>$找到则从撤销表中移除
- 撤销阶段
	- $<T_i,X_j, V_1, V_2>$找到且在撤销表中，则执行撤销并写日志记录$<T_i,X_j,V_1>$
	- $<T_i, start>$找到且在撤销表中,写一个日志记录$<T_i,abort>$并将其从撤销表中移除
	- 若撤销表为空，则结束.

### 日志记录缓冲

- 直到缓冲区满了之后，才将日志记录写回稳定存储器

WAL（write-ahead logging）

- Before a block of data in main memory is output to the database, all log records pertaining to data in that block must have been output to stable storage.

### Database Buffering

- no-force policy: 提交后不一定写回

- force policy: 提交时一定写回

- steal policy: 不提交也可以写回

### 向磁盘写回块

- 获得互斥锁
	- 保证没有更新能够在块上做
- 刷新日志
- 写回块
- 释放锁

### 模糊检查点(Fuzzy Checkpointing)

- 目的：为了避免较长的中断，允许做检查点时执行更新
- 过程
	- 暂时停止所有事务的更新
	- 向稳定存储器写回检查点日志记录
	- 将所有更新过的缓冲块记录在一张表里
	- 允许事务们执行更新
	- 向磁盘输出所有更新过的缓冲块，正在输出的块不能被更新
		- 所有与缓冲块相关的日志记录都应该提前输出
	- 在磁盘的固定位置保存一个指向检查点记录的指针$last_checkpoint$
## 逻辑撤销日志(Logical Undo Logging)

- 像B+树插入和删除之类的操作，会较早地将锁释放，从而不能通过写回旧值的方式撤销操作（physical undo）
- 逻辑撤销日志，记录高层的操作像是插入和删除，而不像物理日志那样，记录磁盘上的具体数据的变化。因此在逻辑上进行撤销操作，伴随反向的操作。
- 过程
	- $<T_i,O_j, operation-begin>$其中$O_j$是执行实例的唯一标识符
	- 普通的日志记录以及物理撤销与重做信息都被记录下来
	- $<T_i,O_j,operation-end>$
- 假如 crash/rollback 在操作完成前发生
	- $operation-end$找不到，那么物理撤销信息就被用于撤销操作
- 假如 crash/rollback 在操作完成后发生
	- $operation-end$能找到，那么忽略物理撤销信息，使用逻辑撤销
- 但是重做操作还是要用到物理重做信息

事务rollback的过程

1. 如果$<T_i,X, V_1, V_2>$被找到，那么撤销并记录$<T_i,X, V_1>$
2. 如果$<T_i, O_j, operation-end, U>$被找到
	1. 使用撤销信息逻辑上回滚操作
	2. 回滚完后记录$<T_i, O_j, operation-abort>$
	3. 跳过接下来有关$T_i$的日志记录直到找到$<T_i, O_j, operation-begin>$
3. 如果找到一个只能重做的记录，就忽略
4. 如果$<T_i, O_j, operation-abort>$被找到，那么跳过所有后面有关$T_i$的日志记录,直到$<T_i,O_j,opearion-begin>$被找到
5. 当$<T_i, start>$被找到，就停止，
6. 向日志增加$<T_i,abort>

## ARIES(Algorithm for Recovery and Isolation Exploiting Semantics)

- 使用日志序列号(log sequence number(LSN))来标识日志记录
	- 在页中记录日志序列号，表示更新已经对数据库页执行
	- 线性增长
- 使用 physiological redo
	- 再删除上仅仅需要记录删除记录本身，而物理重做需要对页的大部分记录旧值和新值
	- 需要页在向磁盘输出的时候保持原子性
- 使用脏页表去避免务必要的重做
- 仅记录脏页数据的模糊检查点，并且在检查点时不需要写回脏页

### 主要的数据结构
- 标识每个日志记录的日志序列号

| LSN | TransID | PrevLSN | RedoInfo | UndoInfo |
| --- | ------- | ------- | -------- | -------- |

特殊的只重做日志记录被称为补偿日志记录(compaensation log record （CLR）)

- 用于记录在回复期间永远不需要撤销的日志操作

| LSN | TransID | Undo Next LSN | RedoInfo |
|---|---|---|---|

- UndoNextLSN 指向下一个需要被撤销的记录

- 页的日志序列号（用于避免重复的重做）
	- 记录最后一条影响页的日志记录
	- 更新一个页
		- 为页申请排他锁， 写入日志记录
		- 更新页
		- 在页日志序列号中记录
		- 释放锁
- 不同类型的日志记录
- 脏页表
	- 记录每一个在缓冲区中被更新的页
	- 包含：PageLSN，RecLSN（记录第一个使页变脏的记录号，决定了从哪里开始）
- 检查点日志记录
	- 包含：脏页表和活跃的事务表（包含LastLSN）
	- 在磁盘上有固定的位置来保存检查点记录
	- 脏页表持续被写回，而非在检查点全部写回

### ARIES 恢复算法

- Analysis pass:
	- Set $RedoLSN = min\{RecLSNs\}$ of all pages in DirtyPageTable
	- Set $undo-list =$ list of transactions in checkpoint log record
	- 从检查点向前扫描，更新撤销表与脏页表
	- 决定哪些事务要撤销
	- 哪些页在崩溃时是脏的
	- RedoLSN：重做开始的日志序列号
- Redo pass：
	- 重复历史，重做从RedoLSN开始的所有操作
		- RecLSN和PageLSNS 被用于避免重做已经在页中反映出来的操作
		- 跳过那些日志序列号小于$RecLSN$的记录
		- 除此之外，重做日志记录
- Undo pass：
	- 对于一般的日志记录，nextLSN被设置为PrevLSN
	- 对于补偿日志记录，nextLSN被设置为UndoNextLSN
		- 生成CLR时其UndoNextLSN继承前一个CLR
	- 回滚所有未完成的事务
	- 不需要撤销那些已经重做撤销的操作

#### 额外的特点
- 页之间的恢复是独立的
- 可以有保存点，并回滚回到保存点
- 细粒度上锁
- 恢复优化
	- 在重做时，脏页表可以提前获取页
	- 乱序重做也是可能的

### 主存数据库中的恢复
- 如果只有提交的数据写回磁盘则没有撤销记录
- 没有索引的重做日志