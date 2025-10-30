## MySQL InnoDB事务的隔离级别有四级
1. 未提交读（READ UNCOMMITTED）：另一个事务修改了数据，但尚未提交，而本事务中的SELECT会督导这些未提交的数据
2. 提交读（READ COMMITED）：本事务读取到的是最新的数据（其他事务提交后的）。问题是，在同一个事务里，前后相同的SELECT会读到不同的结果
3. 可重复读（REPEATABLE READ）：在同一个事务里，SELECT的结果是事务开始时时间点的状态，因此，同样的SELECT操作读到的结果会是一致的。
4. 串行化（SERIALIZABLE）：读操作会隐式获取共享锁，可以保证不同事务间的互斥。