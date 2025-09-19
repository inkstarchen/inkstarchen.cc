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
#### Single- and Multi-Tasking
Modern OSes support multi-tasking
- To start a new program, the OS simply creates a new process (via a system-call called fork() on a UNIX system)


```c title='自定义Signal'
#include <signal>
#include <stdio.h>

void handler(int sig){
	fprintf(stdout,"I don't want to die!\n");
	return;
}

main() {
	signal(SIGINT,handler);
	while(1);
}
```
