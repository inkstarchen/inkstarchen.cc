## Resolver `::`的用途
- 访问命名空间的成员
- 访问一个类的静态变量
- 在类声明外定义一个成员函数


## 析构函数
- 构造函数和析构函数都没有返回值，且必须和类同名
- 析构函数不能带有参数
## 向上转型
- 用衍生类来创建实例，但是用基类来使用

```c++ linenums="1"
Manager pete("Pete", "444-55-6666", "Bakery");
Employee *emp_ptr = &pete;
```

## 衍生类

```c++ linenums="1"
class Shape {
    ...
}

class Ellipse : public Shape {
    ...
}
```

## String 类

```cpp title="String class" linenums="1"

赋值运算符

char char1[20];
char char2[20] = "jaguar";

string str1;
string str2 = "jaguar";

char1 = char2; # illegal
str1 = str2; # legal

直接拼接

str1 += str2;
str1 += "lalala";

构造函数
string(const char *cp, int len);
string(const string& s2, int pos);
string(const string& s2, int pos, int len);

子串函数
s.substr(int pos, int len);

修改字符串
assign();赋值
insert(const string&, int len);
insert(int pos, const string& s);
erase();
append();
replace();

搜索
find();
```

## 文件I/O

```cpp title="File I/O" linenums="1"
#include <ifstream>
#include <ofstream>

ofstream File1("C:\\test.txt");
File1 << "Hello world" << std::endl;
ifstream File2("C:\\test.txt"); 
std::string str;
File1 >> str;
```

## 类声明示例
```c++ title="class declaration" linenums="1"
class Point
{
    public:
    void init(int x, int y);
    void move(int dx, int dy);
    void print() const;

    private:
        int x;
        int y;
};

void Point::init(int ix, int iy){
    x = ix; y = iy;
}
void Point::move(int dx, int dy){
    x += dx; y += dy;
}
void Point::print() const{
    cout << "x = " << x << ", y = " << y << endl;
}

void S::f(){
    ::f(); # 递归使用
    ::a++; # 使用全局变量
    a--;   # 使用类范围内的变量
}
```
#### 初始化
```cpp title="初始化" linenums="1"
class Point
{
    private:
        const float x, y;
        Point(float xa = 0.0 , float ya = 0.0)
        : y(ya), x(xa) {}
};
```

#### 复制构造函数
```cpp title="复制构造函数" linenums="1"
T::T(const T&);
使用引用的形式是为了显式的参数
```

- 如果你没有提供一个复制构造函数，则将使用C++自带的复制构造函数

- 以下情况复制构造函数会被使用

```c++ title="复制构造函数的使用" linenums="1"
--------During call by value
void roster(Person);
Person child("Ruby");
roster(child);
--------During initialization
Person baby_a("Fred");
// these use the copy ctor. not assignment
Person baby_b = baby_a;
Person baby_b(baby_a);
--------During function return
Person captain(){
    Person player("George");
    return player;
}
```

- 不复制的优化

```c++ title="不复制的优化" linenums="1"
Person copy_func(char *who){
    Person local(who);
    local.print();
    return local; // copy ctor called
}

Person nocopy_func(char *who){
    return Person(who);
} // no copy needed!
```

- 使用你自己的复制构造函数不要依赖于默认的
- 如果你不需要，就声明一个私有的复制构造函数


```c++ title="指针复制函数" linenums="1"
Person::Person(const char *s){
    name = new char[::strlen(s) + 1];
    ::strcpy(name, s);
}
```



#### 参数传递方式

```cpp title="参数传递方式" linenums="1"
void f(Student i);
//  创建一个新的对象
void f(Student *p);
// 最好使用const 如果不需要修改对象
void f(Student& i);
// 最好使用const 如果不需要修改对象
```

!!! tip "参数传递方式"
    - 如果想要保存对象，就传递对象
    - 如果想要取值，传递常量指针或常量引用
    - 如果想要修改，传递指针和引用
    - 如果想要在函数中创建，传出一个对象
    - 只传出传入的指针和引用
    - 永远不要使用`new`创建对象并返回指针

#### 默认参数
```cpp title="默认参数" linenums="1"
int harpo(int n, int m = 4, int j =5);
int chico(int n, int m = 6, int j ); //illeagal
int groucho(int k = 1, int m = 2, int n = 3);
```

#### 常量成员函数
> 常量对象，不能调用非常量成员函数
> 常量成员变量需要在初始化列表中构造

```cpp title="常量成员函数" linenums="1"
int Date::set_day(int d){
    //... error check d here...
    day = d;
}

int Date::get_day() cont {
    day++; // ERROR modifies data member
    set_day(12); // ERROR calls non-constmember
    return day;
}
```

### Stash 容器
- 用于容纳其它对象的对象

```cpp title="Stash" linenums="1"
struct Stash {
    int size;
    int quantity;
    int next;
    unsigned char* storage;
    void initialize(int sz);
    void cleanup();
    int add(const void* element);
    void* fetch(int index);
    int count();
    void inflate(int increase);

}
```

## 静态成员变量


使用 static 关键字来把类成员定义为静态。这意味着所有此类的对象都共用此变量。

```cpp
class class_name {
    public:
        static int var_1; # 静态变量
        int var_2;        # 实例变量
    public:
        func{
            int var_local;# 局部变量
        };
};
```
- 静态成员变量的初始化不能放在类定义中，但可以在类的外部使用范围解析运算符::来重新声明静态变量来进行初始化。
```cpp
int class_name::var_1 = 0;
```

## 静态成员函数
- 在函数内部和类内部之外不要使用静态关键词
- 静态成员函数即使在类对象不存在的情况下也能被调用，只需要使用类名加范围解析运算符::来访问。
- 静态成员函数只能访问静态成员数据、其他静态成员函数和类外部的其他函数,不能访问类的this指针.
```cpp
class class_name{
    public:
        static int getCount(){}
}
使用
<class name>::<static member>
<object variable>.<static member>
```

## 全局对象
```c++ title="全局对象" linenums="1"
#include "X.h"
X global_x(12, 34);
X global_x2(8, 16);

int  main()...
```

## 继承
```c++ title="继承" linenums="1"
class Base {
    public:
        void f(){}
};
class Child : public Base{
    public:
        using Base::f;
        void f(int i){}
};
```

### DVD\CD

```c++ title="DVD\CD" linenums="1"
class Item{ ... }
class DVD : public Item {...}
class CD : public Item {...}
```

- make member functions protected
- keep member variables private

## 代码重用
```c++ title="代码重用" linenums="1"
class Person {...};
class Currency {...};
class SavingsAccount {
    public:
        SavingsAccount(const char* name, const char * address, int cents);
        ~SavingsAccount();
        void print();
    private:
        Person m_saver;
        Currency m_balance;
};
```

## 对象设计

### TicketMachine

!!! tip "OOP思想"
    - 万事万物都是对象
    - 一个程序就是一系列对象告诉相互该怎么去做
    - 每个对象都有它自己内存
    - 每个对象都有一个种类
    - 相同种类的对象可以接收相同的信息

```cpp title="TicketMachine" linenums="1"
class TicketMachine
{
    public:
        void showPrompt();
        void getMoney();
        void printTicket();
        void showBalance();
        void printError();
    private:
        const int PRICE;
        int balance;
        int total;
};
```

## 抽象类
- 只有virtual函数，只有接口，没有函数体
- 不能被实例化，一定要有衍生类并满足所有条件

### 优点

- 模型化
- 确保正确的行为
- 在不定义实现的情况下定义接口

## 迭代器
迭代器是一种对象，它允许访问集合中的元素，并返回集合中的下一个元素。

- 可以作为参数

`copy ( L.begin(), L.end(), V.begin()  );
`

## typedef

- `typedef	PB	map<Name,list<PhoneNum> >;`

## map
使用`fo.count()`函数来检查元素存在性