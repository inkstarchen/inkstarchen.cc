## Data Storage Structures
<div class='grid' markdown>
<div class='card' markdown>
#### 长度固定记录（Fixed-Length Records）

---

假设：

- 记录大小固定，且小于一个磁盘块
- 每个文件都只有一类的记录，不同的关系用不同的文件
- 不允许同一记录跨块存储

删除操作:

- 选择 1: 后续记录依次向前移动
- 选择 2: 最后一条记录覆盖删除记录
- 选择 3: 维护空闲链表记录空闲空间

</div>
<div class='card' markdown>
可变长记录(Variable-Length Records)

---
单记录结构：(offset,length)s + fixed length attributes + Null bitmap + variable length attributes

![](assets/vrecord_structure.png)

分槽页结构（Slotted Page Structure）


![](assets/SPS.png)

- Slotted page (分槽页) header contains:
    - number of record entries
    - end of free space in the block
    - location and size of each record
</div>
<div class='card' markdown>
堆文件组织(Heap File Organization)

---

- 任意存储
- 插入和删除代价低，查找代价高
- 可以使用自由空间图（free-space map），记录每块的空闲率
</div>

<div class='card' markdown>
顺序文件组织(Sequential File Organization)

---

- 按照某字段(search-key)的值排序存储
- 加快查找速度，但插入和删除的代价较高
- 删除时可以使用链表,插入时有空闲则插入，没空闲时则插入到溢出块(overflow block)
- 需要不时重新组织文件来保持线性顺序
</div>

<div class='card' markdown>
多表聚簇文件组织(Multitable Clustering File Organization)

--- 

- 将多个表存储在同一文件中
- 加快多表连接操作，但堆单张表的操作变慢
- 同样可以使用链表去维护

![](assets/cluster.png)

</div>

<div class='card' markdown>
表分区(Table Partitioning)

---

- 一个关系中的记录分成多份，存储在不同的文件中。
- 例如按年份划分存储。或按常用性管理不同的存储设备上的存储记录

</div>

</div>
