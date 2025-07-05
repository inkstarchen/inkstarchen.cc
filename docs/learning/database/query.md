## Basic Steps

- Parsing and translation
- Optimization
- Evaluation

### Optimization
- 使用特定的评估策略的表达式被称为评估计划(evaluation-plan)
- 优化的目的是从所有的选择中选出最低开销的那个
- 操作的开销估计不包括向磁盘写入输出

#### 磁盘开销估计

- 搜索次数
- 块读取次数
- 块写入次数

> 使用块转移次数和搜索次数来估计开销

- $t_T$-time to transfer one block
	- Assuming for simplicity that write cost is same as read cost
- $t_S$-time for one seek
- Cost for b block transfers plus $S$ seeks
	- $b * t_T + S * t_S$
> $t_S$ and $t_T$ depend on where data is stored


### Selection Operation

**File scan**

- Algorithm A1(linear search). 查询每一个文件块检验每一个记录是否满足选择条件
	- Cost estimate = $b_r$ block transfers $+ 1$ seek
	- 如果选择是在键属性上。可以在找到后停止
		- $cost = (b_r / 2)$ block transfers $+ 1$seek
	- 线性查找可以无视查询条件、记录顺序和索引的有效性

### Selections Using Indices
聚类索引（clustering index）
- 表中的数据行按照聚类索引键值的顺序实际存储在磁盘上
- 每个表只能按一种物理顺序存储
- 一般主键自动成为聚类索引

- Index scan
	- A2(clustering index, equality on key) | Retrieve a single record
		- $Cost = (h_i + 1) * (t_T + t_S)$
	- A3(clustering index, equality on nonkey) | Retrieve multiple records
		- $Cost = h_i * (t_T + t_S) + t_S + t_T *b$
	- A4(secondary index, equality on key/non-key)
		- Retrieve a single record if the search-key is a candidate key
			- $Cost = (h_i + 1) * (t_T + t_S)$
		- Retrieve multiple records if search-key is not a candidate key
			- $Cost = (h_i + n) * (t_T + t_S)$ 其中n是符合条件的记录数
	- A5(clustering index, comparison)
	- A6(no-clustering index, comparison)
	- A7(conjunctive selection using one index)
	- A8(conjunctive selection using composite index)
	- A9(conjunctive selection by intersection of identifiers)
	- A10(disjunctive selection by union of identifiers)
		- 除非所有的条件都有可用的索引，不然使用线性扫描
	- Negation
		- 线性扫描，如果满足条件的记录偏少那么使用索引获取
- Bitmap Index Scan
	- bit位较少时类似于索引扫描，bit位多时类似于线性文件扫描
	  
### Sorting

#### External Sorting Using Sort-Merge
- M 个缓冲块，N个文件块
- N < M 一轮可以合并完成
- N >= M 每轮只能合并 M -1 个
	- 一个用于输出，剩下的用于读入

合并流程：

- 生成归并段（排序后）
- 进行归并

代价分析：

**Block transfer cost**
- 内存可用 $M$ 个缓冲块，数据总块数为$b_r$，每次I/O读取和写入一个的块数$b_b$
- 初始的 Run 生成
	- 每次读取 $M$ 块数据，排序后写回，每个run就是 $M$ 块数据
	- 一共就是$\lceil \frac{b_r}{M} \rceil$个run
	- I/O代价就是 $2b_r$
- 归并阶段
	- 假设我们每次用一个块作为输出，$b_b$个块作为每个run输入
	- 则理论上用$M$ 个缓冲块我们一轮最多可以合并$\lfloor \frac{M}{b_b} \rfloor$ 个run，但要减除一个缓冲块用于输出，因此我们一轮能够合并的run为$\lfloor \frac{M}{b_b} \rfloor -1$ 
	- 归并轮数就为$\lceil \log_{\lfloor \frac{M}{b_b} \rfloor -1}{\lceil \frac{b_r}{M} \rceil} \rceil$
	- 每轮需要读写$2b_r$块，最后一轮不用写回磁盘
- 因此总代价为$b_r \times(2\lceil \log_{\lfloor \frac{M}{b_b} \rfloor -1}{\lceil \frac{b_r}{M} \rceil} \rceil + 1)$

**Seek cost**

- run生成阶段，每个run都需要一次查询读和查询写
	- $Cost = 2 \lceil \frac{b_r}{M} \rceil$
- 归并阶段，每轮都需要$\lceil \frac{b_r}{b_b} \rceil$ 次查询读和查询写,除了最后一轮不需要写
	- $Cost = \lceil \frac{b_r}{b_b} \rceil (2\lceil \log_{\lfloor \frac{M}{b_b} \rfloor -1}{(\frac{b_r}{M})}-1)$

### Join Operation

#### Nested-Loop Join

- 外层循环（Outer Loop）：遍历左表（通常为小表，称为驱动表）
- 内层循环（Inner Loop）：对左表中的每一行遍历右表，并匹配连接条件
- $Cost = b_r + n_r \times b_S$ block transfers + $b_r + n_r$ seeks

#### Block Nested-Loop Join

$Worst \quad Cost = b_r \times b_S + b_r$ block transfers + $2\times b_r$ seeks
$Best \quad Cost = b_r + b_S$ block transfers + $2$ seeks  | 所有的块刚好可以装入内存
$Improvements \quad Cost = \lceil \frac{b_r}{(M-2)} \rceil \times b_S + b_r$ block transfers + $2\lceil \frac{b_r}{M-2} \rceil$ seeks

### Indexed Nested-Loop Join

$$Cost = b_r (t_T + t_S) + n_r  \times c $$
- Where $c$ is the cost of traversing index and fetching all matching $s$ tuples for one tuple of $r$

### Merge Join

- 根据连接属性进行排序
- 进行归并算法
- 只能用于 等值连接和自然连接
- $Cost = b_r + b_S$ block transfers + $\lceil \frac{b_r}{b_b} \rceil$ + $\lceil \frac{b_S}{b_b} \rceil$ seeks + the cost of sorting if relations are unsorted

### Hash-Join
- 适用于等值连接和自然连接
- 用哈希函数来确定划分
- 如果元组$r$与元组$s$满足连接条件，那么他们的连接属性相同，从而使得哈希函数的值相同

可能会出现溢出现象，解决办法：

- 对$s_i$进一步使用不同的哈希函数进行划分
- $r_i$必须同样划分

#### 代价分析

如果递归划分不被需要那么代价是

$$3(b_r+b_s)+4 \times n_h block transfers + 2(\lceil \frac{b_r}{b_b} \rceil)+ \\lceil \frac{b_s}{b_b} \rceil ) seeks$$

如果递归划分是需要的，那么代价是

$$2(b_r + b_s) \lceil \log_{\lfloor M/b_b \rfloor -1}{(b_s /M)}\rceil + b_r + b_s block transfers + 2(\lceil b_r /b_b \rceil + \lceil b_s / b_b \rceil)\lceil \log_{\lfloor M/b_b \rfloor -1}{(b_s/M)}\rceil seeks$$

复杂连接
合取条件：使用nested loops/block nested loops 或者 一层一层计算
析取条件：使用nested loops/block nested loops 或者一个一个计算最后取并集

### 其它操作

- Duplicate elimination

通过哈希和排序， 优化：external sort-merge

- Projection
- Aggregation
- Set Operations
	- 使用哈希函数
	- $r \cup s$:
		- 将每个在$s_i$中的元组加入哈希索引，如果他们不在其中
		- 将每个在哈希索引中的元组加入结果
	- $r \cap s$:
		- 将每个$s_i$中的元组加入结果，如果他们已经在哈希索引中
	- $r - s$:
		- 从索引中删除，将剩余的元组加入结果
- Outer Join：可以通过修改Join的算法实现，加入未参加的元组
### Evaluation of Expressions
#### Materialization（物化）
每次执行一个操作，然后在磁盘上固化下来。

物化求值永远是适用的。

但是会带来额外的代价$Overall$ $cost$ $=$ Sum of costs of individual operations + cost of writing intermediate results to disk

#### Pipelining（流水线）
- 需求驱动的求值或惰性求值
- 生产者驱动的流水线或eager pipelining：父子之间存在buffer，用于数据交互
- Pipleline stages:所有在同一阶段的操作并行，只有前一阶段的的操作全部完成后，才能进行下一阶段


## Query Optimization

Steps in cost-based query optimization
- Generate logically equivalent expressions using euqivalence rules
- Annotate resultant expressions to get alternative query plans
- Choose the cheapest plan based on estimated cost

### Equivalence Rules
-  $\sigma_{\theta_1 \land \theta_2}(E) \equiv \sigma_{\theta_1}(\sigma_{\theta_2}(E))$
- $\sigma_{\theta_1}(\sigma_{\theta_2}(E)) \equiv \sigma_{\theta_2}(\sigma_{\theta_1}(E))$
- $\prod_{L_1}(\prod_{L_2}(\dots (\prod_{L_n}(E))\dots )) \equiv \prod_{L_1}(E)$ where $L_1 \subset L_2 \dots \subset L_n$
- $\sigma_{\theta}(E_1 \times E_2) \equiv E_1 \Join_{\theta} E_2$
- $\sigma_{\theta_1}(E_1 \Join_{\theta_2} E_2) \equiv E_1 \Join_{\theta_1 \land \theta_2} E_2$
- $E_1 \Join E_2 \equiv E_2 \Join E_1$
- $(E_1 \Join E_2) \Join E_3 \equiv E_1 \Join (E_2 \Join E_3)$
- $(E_1 \Join_{\theta_1} E_2) \Join_{\theta_2 \land \theta_3}E_3 \equiv E_1 \Join_{\theta_1 \land \theta_3}(E_2 \Join_{\theta_2} E_3)$ where $\theta_2$ involves attributes from only $E_2$ and $E_3$

When all the attributes in $\theta_0$ involve only the attributes of one of the expressions $(E_1)$ being joined

- $\sigma_{\theta_0}(E_1 \Join_{\theta} E_2) \equiv (\sigma_{\theta_0} (E_1)) \Join_{\theta} E_2$

> Performing the selection\projection as early as possible reduces the size of the relation to be joined.

#### Implementing Transformation Based Optimization
- Space requirements reduced by sharing common sub-expressions:
	- Same sub-expression may get generated multiple times
		- Delete duplivate sub-expressions and share one copy
- Time requirements are reduced by not generating all expressions

#### Selection Size Estimation
- $\sigma_{A=v}(r)$
	- 满足选择的记录数目$n_r/V(A,r)$
	- Equality condition on a key attribute: size estimate = 1
- $\sigma_{A \leq v}(r)$
	- c是满足条件的元组数目
	- 假设$min(A,r)和max(A,r)存在
		- $c = 0\quad if \quad v < min(A,r)$
		- $c=n_r \cdot \frac{v-min(A,r)}{max(A,r)-min(A,r)}$
		- 忽略静态信息，c被假设为$n_r/2$
#### Size Estimation of Complex Sections

> The selectivity of a condition $\theta_i$ is the probability that a tuple in the relation $r$ satisfies $\theta_i$

- 假设$s_i$是$r$中满足关系的元组数量

- 合取$\sigma_{\theta_1 \land \theta_2 \land \dots \land \theta_n}(r)$: $n_r \cdot \frac{s_1 \cdot s_2 \cdot \dots \cdot S_n}{n_r^n}$
- 析取$\sigma_{\theta_1 \lor \theta_2 \lor \dots \lor \theta_n} (r)$: $n_r \cdot (1- (1-\frac{s_1}{n_r})\cdot(1-\frac{s_2}{n_r})\cdot \dots \cdot (1-\frac{s_n}{n_r}))$
- 否定$\sigma_{\lnot \theta}(r)$: $n_r - size(\sigma_{\theta}(r))$

#### Estimation of the Size of Joins
- $R \cup S = \{R\}$ is not a key for $R$ or $S$
- $R \Join S$: $\frac{n_r \cdot n_s}{V(A,s)}$ or $\frac{n_r \cdot n_s}{V(A,r)}$
- Outer join: $size of r \Join s + size of r + size of s$

#### Estimation of Number of Distinct Values
- Selections:
	- if the selection condition $\theta$ is of the form A op r
		- $V(A, \sigma_{\theta}(r) = V(A, r) \cdot s$
	- In all the other cases: use approximate estimate of
		- $min(V(A,r), n_{\sigma_{\theta}(r)}$
- Joins
	- if all attributes in A are from r
		- $V(A, r\Join s) = min(V(A,r), n_{r\ Join s})$
	- if A contains attributes $A_1$ from r and $A_2$ from s,then estimated $V(A, r \Join s) = min(V(A_1, r)*V(A_2 - A_1, s), V(A_1-A_2, r)*V(A_2,s),n_{r\Join s})$

### Choosing Evaluation Plans
- 每个操作最低代价的算法不一定在整体上是最低代价的
	- 归并连接比哈希连接多代价，但是结果输出是排序完的，可以给外层聚合降低代价
	- nested-loop为流水线提供了契机

多层Join $r_1 \Join r_2 \Join \dots \Join r_n$
- 可以使用动态规划的方法

interesting sort order：使得后续操作能够使用更少的代价

#### Heuristic Optimization
- Perform selction early
- Perform projection early
- Perform most restrictive selction and join operations before other similar operations

### Materialized views
维护：增量视图维护
- 做差分

可以作为子查询的部分，从而减少代价

