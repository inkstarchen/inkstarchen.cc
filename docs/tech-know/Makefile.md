## 存在的目标
- 划分组成部分
- 当文件修改时执行最小程度的编译
- 更容易地维护项目结构、依赖和创建

## 包含的内容
- 项目结构(文件，依赖)
- 创建文件的指令

### 示例

```makefile
sum: main.o sum.o
    gcc -o sum main.o sum.o

main.o: main.c sum.h
    gcc -c main.c

sum.o: sumc.c sum.h
    gcc -c sum.c


------- 替代版本 --------

sum: main.o sum.o
    gcc -o $@ main.o sum.o

main.o sum.o: sum.h
    gcc -c $*.c
```

### 更加详尽的示例
```makefile
BASE    = /home/blufox/base
CC      = gcc
CFLAGS  = -O -Wall
EFILE   = $(BASE)/bin/compare_sorts
INCLS   = -I$(LOC)/include
LIBS    = $(LOC)/lib/g_lib.a \
          $(LOC)/lib/h_lib.a
LOC     = /usr/local

OBJS = main.o another_qsort.o chk_order.o \
       compare.o quicksort.o

$(EFILE): $(OBJS)
    @echo "linking..."
    @$(CC) $(CFLAGS) -o $@ $(OBJS) $(LIBS)

$(OBJS):compare_sorts.h
    $(CC) $(CFLAGS) $(INCLS) -c $*.c

clean:
    rm *~ $(OBJS)
```

### 条件示例

```makefile
sum:main.o sum.o
    gcc -o sum main.o sum.o

main.o:main.c sum.h
    gcc -c main.c

ifeq($(USE_SUM), 1)

sum.o:sum1.c sum.h
    gcc -c sum1.c -o $@

else
sum.o:sum2.c sum.h
    gcc -c sum2.c -o $@

endif
```