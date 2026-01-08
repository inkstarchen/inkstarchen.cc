## 进程
### 进程控制块(PCB)

- 每个进程有且仅有一个进程控制块：随进程创建而分配，随进程结束而释放

**进程控制块包含的内容**

- 进程标识符PID，和PPID
- 进程状态：运行，等待……
- 程序计数器：执行下一个指令的位置
- CPU寄存器：与此进程相关的寄存器的数据内容
- CPU调度信息：优先级，调度队列指针
- 内存管理信息：被此进程申请的内存
- 统计信息：占有的CPU，从进程开始的时钟时间，时间限制
- I/O状态信息：被此进程申请的I/O设备，打开的文件链表



**进程状态**

- **New**: 进程正在被创建
- **Running**: 进程的指令正在被执行
- **Waiting**:进程在等待某个事件发生
- **Ready**: 进程在等待被某个处理器执行
- **Terminated**: 进程完成执行

![](assets/Pasted_image_20241211195251.png)


#### 进程调度

- 使用waiting list 和 ready list

### 系统调用`fork()`

- **调用 返回**：给子进程返回0，给父进程返回子进程的pid
- 子进程拥有不同的PID

#### UNIX 系统的例子

```c title='fork() in UNIX' linenums='1'
if (fork() == 0) {
	char *const argv[] = {"ls", "-l", "/tmp/", NULL};
	execv("/bin/ls",argv);
}
```
- `fork()`系统调用创建一个新进程
- `execve()`被调用，子进程抢占执行，父进程执行`wait()`等待
- 子进程执行完毕`exit()`返回父进程

#### wait() and waitpid() 的区别
- `wait()`:等待任何一个子进程完成，返回完成的子进程的pid和exit code 
- `waitpid()`:等待特定的子进程完成


#### Stack Frame(Activation Record)

**函数运行的所需元素**

- 函数调用的参数
- 局部变量
- 函数返回的地址
- 函数返回值

**函数调用链越长，栈空间越大**


## 线程


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

- 异步关闭：立即关闭目标线程
- 延迟关闭：线程周期性检测其是否应该终止

如果一个线程将其关闭模式设置为off则直到其模式被打开才能够关闭

在Linux系统下，线程的关闭通过信号来决定

##### 关键区块(Critical section)

- 指的是一个访问共享资源的程序片段，而这些共享资源又无法同时被多个线程访问的特性。
