
### 线程Thread

**单个线程包含的内容**
- 线程ID
- 程序计数器 
- 寄存器集合 
- 栈

**线程间共享的内容**
- 代码段(code section)
- 数据段(data section)
- 堆(动态申请的内存)
- open files and signals
**线程的优势**
- 所需资源更少
- 能共享资源
- 响应性更快：用户向服务器申请，服务器根据申请新建一个线程，继续监听用户的申请
- 扩展性更好

**线程的劣势**
- 线程间隔离性不好，一个线程挂了，整个进程都会挂掉
- 线程比进程的内存约束性更强
- 没有内存隔离的优势

### 用户线程与内核线程的对应模型
#### Many-to-One Model
**优点**：多线程效率高
**缺点**：

- 无法发挥多核的优势
- 一个线程阻塞了则所有线程阻塞

#### One-to-One Model
**缺点**：

- 每创建一个线程都需要进kernel
- 比Many-to-One 慢
- 开销大

#### Many-to-Many Model
- 用户线程阻塞，则内核可以新建一个线程，防止阻塞其他用户线程



### Thread Libraries
In C/C++: pthreads and Win32 threads
#### Pthreads
在内核层或用户层提供

In C/C++: **OpenMP**
In Java: Java Threads

> In modern JVMs, application threads are mapped to kernel threads

### Thread Issues
- 调用`fork()`时，可以只创建一个线程的子进程，也可以复制所有的线程
#### Signals
- 信号处理，可以是默认的，也可以用户自定义
- `signal()` and `kill()` 都是系统调用

- 大多数的UNIX版本下：一个线程可以决定其接受的信号
- On Linux: 比较复杂，但是有很多教程和手册
#### 线程关闭目标线程
两种方式

- 异步关闭 ：立即关闭目标线程
- 延迟关闭：线程周期性检测其是否应该终止

如果一个线程将其关闭模式设置为off则直到其模式被打开才能够关闭

在Linux系统下，线程的关闭通过信号来决定

##### 关键区块(Critical section)
- 指的是一个访问共享资源的程序片段，而这些共享资源又无法同时被多个线程访问的特性。
