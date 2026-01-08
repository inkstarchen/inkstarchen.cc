## B+ Tree索引
<div  class='grid' markdown>
![](assets/B+.png)
</div>

- 问题： 如果使用的是记录的指针，则若记录移动位置，所有的二级索引的记录都要移动位置。
- 解决：使用搜索键，而不是记录的指针。如果有需要可以假如record_id来保证唯一性

### 批量插入

- Aternative 1：bULK lOADING
    - 外部排序后，顺序插入

- Aternative 2：Bottom-up B+ tREE CONSTRUCTION
    - 外部排序，和旧数据共同重新创建树

### Non-Unique Keys

- 如果search-key不唯一，可以构造一个复合的搜索键$(a_i, A_p)$使得其唯一

## Hash Indices

#### Static Hashing
- bucket + hash function
- 优化：让桶的数量能够动态修改

<div class='grid' markdown>
<div class='card' markdown> 
example

---

![](assets/hash.png)

</div>
</div>

#### Dynamic Hashing
- 周期性重新进行哈希算法
    - 增大哈希表的大小
- 线性哈希
    - 当桶溢出时，按线性顺序分裂桶
- 可扩展哈希
    - 当存不下时扩展hash表，只分裂溢出的桶

## Log Structured Merge Trees(LSMT)

<div class='grid' markdown>
<div class='card' markdown> 
原理：

---

- 插入操作：逐层合并树，批量执行
- 删除操作：增加删除entry，合并时匹配则去除
</div>

<div class='card' markdown> 
实例

---

![](assets/LSMT.png)

</div>

</div>

### Buffer Tree
- 每个节点增加一个buffer，用于存储操作
- 若此节点的buffer满了则下推
- 积攒满了操作再批量执行


### Bitmap Indices
- 用01表示该记录是否有某属性
- 对多属性查询有优势，但单属性查询无优势
