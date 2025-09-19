- 软件设计具有多样性，取决于你的构建策略
- 最主要的问题在于库函数的编写者，他们要考虑到很多特定的情况，让库函数能够适应

例如智能指针：

- 单线程或多线程
- 支持或不支持自动类型转换
- 优化性能

> 一个设计在最终完成之前经常要被复用好几次，而且每一次都有所修改

> 内行的设计者知道：不是解决任何问题都要从头做起。他们更愿意复用以前使用过的解决方案

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

## 引言

### 描述设计模式

对于设计模式的描述，事实上也可以类比到对于知识的描述

- **模式名和分类**：简洁地描述了模式的本质

- **意图**：回答设计模式做什么？基本原理和意图是什么？它解决什么特定的问题？

- **别名**：模式的其它名称

- **动机**：说明一个设计问题以及如何用模式中的类、对象来解决该问题的具体情景。

- **适用性**：在什么情况下可以使用该模式？

- **结构**

- **参与者**：设计模式中的类或对象以及它们各自的职责

- **协作**：模式的参与者怎样协作以实现它们的职责

- **效果**：模式怎样支持他的目标？使用模式的效果和所需做的权衡是什么？系统结构的哪些方面可以独立改变？

- **实现**：实现模式时需要知道的一些提示、技术要点及应避免的缺陷，以及是否存在某些特定于实现语言的问题。

- **代码示例**

- **已知的应用**

- **相关模式**