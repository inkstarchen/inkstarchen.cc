## Cache

### VIVT(Virtually-Indexxed Virtually-Tagged) 虚拟高速缓存

用虚拟地址作为index和tag去访问cache，若命中且Cache line中的数据有效，则进一步根据offset去找到数据。若未命中，则将虚拟地址转换成物理地址，从主存中读取数据，返回给CPU和Cache
- 优点
	- 不用每次都将虚拟地址转换成物理地址，节约CPU等待时间。
- 缺点
	- 使用虚拟地址作为Tag，会引起歧义性和别名的问题
		- 歧义性：多个虚拟地址映射到同一个物理地址
		- 别名：一个虚拟地址由于进程切换等原因映射到不同的物理地址

### VIPT（Virtually-Indexed Physically-Tagged） 物理标记的虚拟高速缓存

用虚拟地址做index，物理地址做tag，需要进行转译工作。
- 进程切换时不需要对Cache进行invalidate操作（因为匹配过程中需要借助物理地址）
- 但仍然存在别名问题

### PIPT(Physically-Indexed, Physically-Tagged) 物理高速缓存

缺点：速度较慢
address translation: 地址转译

- 时间局部性：当数据被引用，很可能被再次引用
- 空间局部性：连续的数据很可能被引用

- 提前读入连续地址的数据

大小计算：$2^n \times (block\_size + tag\_size + valid\_size)$

### 块存储类型

- Direct mapped：只有一个存储点
- Set associative：多路选择
- Fully associative ：任何地方可放

**地址划分**

- Tag + Index（选择set） + Offset

**写回策略**

- 暂停流水线写回
- 缓冲写回

- 跳过cache写新数据到内存
- 将新数据写回cache

### Miss 代价

- Latency：读取第一个块数据的时间
- Bandwidth：读取剩余块的时间

引起原因：

- Compulsory（强制性）：第一次获取
- Capacity：块被舍弃，后续又获取
- Conflict：不同块，但映射到同一块缓存地址

缓存的两个架构：

- 集合缓存
- I\D分离缓存，Icache只读

![](assets/Pasted_image_20250615194847.png)