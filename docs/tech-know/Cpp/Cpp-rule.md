# C/C++ 头文件规范

## 目录
1. 文件命名规范
2. 头文件保护
3. 包含顺序
4. 内容组织
5. 变量定义
6. 内联函数
7. 命名空间


## 文件命名规范
- **C语言**：使用 `.h` 扩展名  
  `example: network_utils.h`
- **C++**：建议使用 `.hpp` 扩展名（可选）  
  `example: my_class.hpp`
- **命名规则**：
  - 全小写字母
  - 下划线分隔单词
  - 反映主要内容  
  `example: thread_pool.h`

## 头文件保护
### 标准方式
```c
#ifndef PROJECT_MODULE_FILENAME_H
#define PROJECT_MODULE_FILENAME_H
/* 内容 */
#endif // PROJECT_MODULE_FILENAME_H
```

## 包含顺序

1. 关联的头文件
2. 系统头文件
3. 第三方库头文件
4. 项目内其他头文件

```c
#include "my_class.h"

#include <stdio.h>
#include <stdlib.h>

#include <third_party_lib.h>

#include "project/utils.h"
```

## 内容组织
建议按以下顺序组织头文件内容：

- 版权和许可信息
- 文件描述注释
- 包含保护
- 包含的其他头文件
- 前置声明
- 常量/宏定义
- 类型定义
- 函数声明
- 类定义（C++）

## 变量定义
> 避免在头文件中定义变量

```c
// 头文件中
extern int global_var;

// 源文件中
int global_var = 0;
```

## 内联函数

用语句代替函数调用
内联函数编程风格
```c
void Foo(int x, int y);
inline void Foo(int x, int y) {}
```
- inline只适合函数体内代码简单的函数使用，不能包括复杂的控制语句。
- 如果函数体复杂，则不建议使用inline，因为编译器会根据情况选择是否内联。
- 若函数体内出现循环，则执行函数体内代码时间比函数调用的开销大，不宜使用inline.

## 命名空间

```c++ title="命名空间" linenums="1"
using namespace xx; # 声明一个命名空间，可以使用不同命名空间中相同名字的变量
```


`enum class`的成员必须通过`ClassNmae::MemberName`的形式进行访问，更加安全.

```
enum class Color { Red, Green, Blue }; Color myColor = Color::Green;
```
