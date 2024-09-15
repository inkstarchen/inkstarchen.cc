## 基本语法
**头文件**
```
#include <iostream>
```
**命名空间**
```
using namespace std;
```
**输出**
```
cout << "Hello World!" << endl; 
```
**注释**
```
...
int main() {
    /* 这是注释 */
 
    /* C++ 注释也可以
     * 跨行
     */ 
    cout << "Hello World!";
    cout << "Hello World!"; // 输出 Hello World!
    return 0;
}
```

## 数据类型
### typedef 声明

```
typedef type newname;
typedef int feet;
feet distance;
```

几点说明:
* typedef只是对已经存在的类型增加一个类型名，而没有创造新的类型.
* 当不同源文件中用到同一类型数据(尤其像数组、指针、结构体、共用体等类型数据)时，常用typedef声明一些数据类型，把它们单独放在一个头文件中，然后再需要用到他们的文件中用#include命令把他们包含进来，以提高编程效率.

### 枚举类型
枚举类型中，more第一个名称值为0，以此类推，但也可以给予初值。
```
enum color {red, green=5, blue} c;
c = red;
```

* 不一定要在main中定义


### 类型转换
#### 静态转换 (Static Cast)
在转换时不做任何检查.
```
int i = 10;
float f = static_cast<float>(i);
```
#### 动态转换 (Dynamic Cast)
动态转换在运行时进行类型检查，不能转换则返回空指针或引发异常.
```
class Base {};
class Derived : public Base {};
Base* ptr_base = new Derived;
Derived* ptr_derived = dynamic_cast<Derived*>(ptr_base);// 将基类指针转换为派生类指针.
```

#### 常量转换 (Const Cast)
用于将const类型的对象转换为非const类型的对象,只能用于转换掉const属性，不能改变对象的类型.
```
const int i = 10;
int& r =  const_cast<int&>(i);
```
#### 重新解释转换(Reinterpret Cast)
将一个数据类型的值重新解释为另一个数据类型的值.
```
int i = 10;
float f = reinterpret_cast<float>(i);
```
