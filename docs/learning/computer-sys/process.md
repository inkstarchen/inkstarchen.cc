## 进程

> 进程是资源分配和保护的单元

- 代码(也称text)：初始存储在磁盘中的可执行文件中
- 数据段：全局变量
- 程序计数器：指向当前正在执行的指令（代码中的地址）

![](./assets/init_stack.png)

总物理空间图例

![](./assets/physical_stack.png)

## 线程

> 线程是执行单元|Linux中Task_struct与线程对应

## Systme Calls
- 当用户程序要做一些特权操作时需要调用的系统调用.

![](./assets/sys-call.png)