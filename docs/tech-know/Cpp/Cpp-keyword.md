## new
动态分配空间
```c++ title="new" linenums="1" 
new int;
new Stash;
new int[10];
```

## delete
释放动态分配的空间

- 当释放对象指针时，只会调用对象的析构函数，再释放空间。不会删除对象指针的空间
```c++ title="delete" linenums="1" 
delete p;
delete [] p;
```

!!! tip "new 和 delete"
    - 不要用delete去释放new没有分配的空间
    - 使用`delete []`去释放`new[]`的空间
    

## extern
表示一个变量已经在其它文件中声明

## static
只能被所有静态函数所访问，共享。

- 最好把静态变量的声明按顺序放在一个文件中 

`static local var`和函数内部声明的静态变量：静态局部变量

函数内静态变量：
- 值被整个程序记录
- 初始化只执行一次

```c++ title="static" linenums="1"
void f(){
    static int num_calls = 0;
    ...
    num_calls++;
}
```

## explicit
禁止隐式转换

```c++ title="explicit 关键字" linenums="1" hl_lines="3"
class A {
public:
    explicit A(int x) { /* ... */ } // 禁止隐式转换
};

void func(A a) {}

int main() {
    A a1(10);     // 正确：显式调用
    A a2 = A(20); // 正确：显式构造
    A a3 = 30;    // 错误：explicit 禁止隐式转换
    func(40);     // 错误：explicit 禁止隐式转换
    func(A(50));  // 正确：显式构造
}
```

## inline 
函数展开

- 增加了代码的大小韩式减少了整体的调用时间

```c++ title="inline" linenums="1"
inline int f(int i){
    return i * 2;
}
main(){
    int a = 4;
    int b = f(a);
}
```

## virtual

```c++ title="virtual" linenums="1"
class XYPos{...};
class Shape{
    public:
        Shape();
        virtual ~Shape();
        virtual void render();
        void move(const XYPos&);
        virtual void resize();
    protected:
        XYPos center;
};

class Ellipse : public Shape{
    public:
        Ellipse(float maj, float minr);
        virtual void render(); // will define own 
    protected:
        float major_axis, minor_axis;
};

class Circle : public Ellipse{
    public:
        Circle(float radius) : Ellipse(radius, radius){}
        virtual void rendor();
};

void render(Shape* p) {
    p->render(); // calls correct render function
} // for given Shape!

void func() {
    Ellipse ell(10, 20);
    ell.render(); // static -- Ellipse::render();

    Circle circ(40);
    circ.render(); // static -- Circle::render();

    render(&ell); // dynamic -- Ellipse::render();
    render(&circ); // dynamic -- Circle::render()
}




```

### cast
- `static_cast<type>(expression)`:不能消除const属性

```c++ title="static_cast" linenums="1"
char a = 'a';
int b = static_cast<char>(a);//correct

double *c = new double;
void *d = static_cast<void*>(c);//correct

int e = 10;
const int f = static_cast<const int>(e);//correct

const int g = 20;
int *h = static_cast<int*>(&g);//error: static_cast can 								not remove the const property

Class A {public: virtual test() {…}}

Class B: public A {public: virtual test() {…}}

A *pA1 = new B();
B *pB = static_cast<B*>(pA1);  //downcast not safe


```

- `dynamic_cast<type>(expression)`:检查downcast是否安全，但是跨类的转换仍然不安全，会返回一个空指针

```c++ title="dynamic_cast" linenums="1"
Class A {public: virtual test() {…}}

Class B: public A {public: virtual test() {…}}

Class C: {public: virtual test() {…}}


A *pA1 = new B();
B *pB = dynamic_cast<B*>(pA1);  //safe downcast

C *pC = dynamic_cast<C*>(pA1);  //not safe, will return a NULL 							    pointer

```

- `const_cast<type>(expression)`用于修改该const或volatile属性

```c++ title="constcast" linenums="1"
const int g = 20;
int *h = const_cast<int*>(&g); //correct

const int g = 20;
int &h = const_cast<int &>(g); //correct

const char *g = "hello";
char *h = const_cast<char *>(g); //correct

``` 

- `reinterperet_cast<type>(expression)`:二进制层重新解析

```c++ title="reinterperet_cast" linenums="1"
int a, b;
int *pA = &b;
a = reinterpret_cast<int>(pA); //correct
pA = reinterpret_cast<A*>(a);  //correct

b = reinterpret_cast<int>(a);  //Error, can not be used to 								convert int to int

```

## throw
- 触发异常然后转换到catch块