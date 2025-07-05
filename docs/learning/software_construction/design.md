- 软件设计具有多样性，取决于你的构建策略
- 最主要的问题在于库函数的编写者，他们要考虑到很多特定的情况，让库函数能够适应

例如智能指针：

- 单线程或多线程
- 支持或不支持自动类型转换
- 优化性能

## 设计
- 目的：可理解，可维护，可重用，可拓展
- 一个软件要么可维护，要么被舍弃

tip：

- 减少耦合性，类之间的依赖性要降低
    - 通过回调或消息机制
- 增高内聚性，一个类要代表一个定义完全的实体，和方法要专一解决一个逻辑问题

- 如果一个方法解决了多余一个逻辑问题，那么他太长了
- 如果一个类表示了超过一个逻辑实体，那么他太长了

- 代码重复性越高，设计越烂，维护越难
### 考虑的问题
- 需要多少种类的类
- 什么时候去定义一个类
- 有哪些接口和数据
- 是否需要继承
- 是否需要虚函数

**responsibility-driven design**

- 每个类要负责维护和处理他自己的数据

**Refactoring and testing**

- 类和方法需要不时地去重构，来维持搞内聚性和低耦合性

**Thinking ahead**

- 在设计类之前，先考虑其未来的改变和用途
## Policy-based design

```c++ title="creator_example" linenums="1"
template <class T>
struct PrototypeCreator {
	PrototypeCreator(T* pObj = 0)
	:pPrototype_(pObj)   {}
	T* Create() {
	return pPrototype_ ? pPrototype_-	>Clone() : 0;
}
T* GetPrototype() { return pPrototype_; }
void SetPrototype(T* pObj) { pPrototype_ = pObj;  }
private:
T* pPrototype_;
};

```

### 模板模板技术

- 可以让宿主决定他实例化的类型

```c++ title="template_template" linenums="1"
template
< class T,
template <class> class CheckingPolicy,
template <class> class ThreadingModel >
class SmartPtr;

typedef SmartPtr<Widget, NoChecking, SingleThreaded> WidgetPtr;
typedef SmartPtr<Widget, EnforceNotNull, SingleThreaded> SafeWidgetPtr;

template <
class T,
template <class> class CheckingPolicy,
template <class> class ThreadingModel >
class SmartPtr: public CheckingPolicy<T>, public ThreadingModel<SmartPtr> {
T* operator->()  {
	typename ThreadingModel<SmartPtr>::Lock guard(*this);
    // typename 告诉编译器这是一个类型
	CheckingPolicy<T>::Check(pointee_);
	return pointee_;
}
private:
	T* pointee_;
};


```
```c++ title="template_template" linenums="1"
// Library code
template <class CreationPolicy>
class WidgetManager : public CreationPolicy
{
...
};

WidgetManager< OpNewCreator<Widget> > wgtManager;


// Library code
template <template <class Created> class CreationPolicy>
class WidgetManager : public CreationPolicy<Widget>
{
...
};

WidgetManager< OpNewCreator> wgtManager;
```
