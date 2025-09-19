## 迭代器的分类
- 输入迭代器：只读，只支持自增
- 输出迭代器：只写，只支持自增
- 前向迭代器：读写，只支持自增


- 迭代器提供一种按顺序访问容器而不用关心容器细节的方法

- 算法中使用的统一接口
```c++ title="迭代器示例" linenums="1"
template <class InputIterator, class T>
InputIterator find (InputIterator first, InputIterator last, const T& val){
    while(first != last && &*first != val){
        ++first;
    }
    return first;
}

```

- 定义value_type
```c++ title="value_type" linenums="1"
template <class T>
struct myIter {
typedef  T value_type;
T* ptr;
myIter(T *p = 0):ptr(p) {}
T& operator*() { return *ptr; }
}

template <class I>
typename I::value_type func(I iter)
{ return *iter; }

// code
myIter<int> iter(new int(8));
Cout << func(*iter);

```

### 偏特化
- 使得迭代器能够使用指针类型的模板
```c++ title="偏特化" linenums="1"
template<class T>
class C<T*>
{
public:
	C() {cout<<“template T*”<<endl;}
}

template<class T>
class iterator_traits<T *>
{
public:
	typedef T value_type;
	typedef  T* pointer_type;
	……
}

```