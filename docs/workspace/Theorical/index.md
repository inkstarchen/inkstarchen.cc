我们如何编码事物？

- 首先将事物视作符号的集合
- 再将这个符号的集合一一对应映射成01字符串.

那么，假设我们有prefix-free的映射编码，则我们能够确定它的闭包到
01字符集的映射是one-to-one的

而假设我们有一个字符集闭包到01的映射是one-to-one的，那么我们可以找到一个映射是prefix-free的。

至此我们可以将所有的事物抽象成对01字符集的考虑。

接下来我们要解决的是可数问题，我们关系一个集合是否可数，即我们考虑的对象是否可数。有以下几个等价判断

1. 字符集A可数
2. 字符集A有限 或 存在一个A到N的单射（这保证了A的大小一定是小于等于N的）
3. 存在N到A的满射（其实是同一件事）
4. 存在一个A到N的双射

这时我们可以证明$\{0,1\}^*$是可数的。再根据传递性质，证明任何集合可数都可以证明其有一个到01的单射.

在讨论计算性之前，我们首先要定义电路和程序，从而获得NAND-CIRC，我们可以证明其与布尔电路是等价的，同时存在有限的转换关系。

任意能够模拟NAND的函数或门集合都被称为通用(universal gate sets)

为增强我们对于程序的使用能力，我们要引入语法糖的概念

- 包含循环、用户定义函数、条件判断

这时我们首先要讨论一个辅助函数LOOKUP的规模$O(2^k)$

有了这个函数我们就能够确定每个可计算函数的规模不超过$O(\frac{m2^n}{n})$

当然我们也可以对NAND-CIRC进行编码我们可以确定其编码长度不超过$3s\log{\lceil 3s \rceil}$

然后我们可以确定在一定规模范围内的电路无法模拟特定规模的函数

这时我们引出一个通用计算机的概念，能够模拟任意函数在一定规模下



接下来我们要讨论计算性，首先我们可以通过调用函数证明$\{0,1\}^* \rightarrow \{0,1\}&*$与布尔函数的计算能力是等价的,因此我们可以将所有的讨论转换到布尔函数上去.

为讨论计算性我们引入一个计算模型DFA
- 包含状态集合、字符集合、初始状态、转移函数、接收状态
- 定义一个Language
- 我们说一个函数是可计算的，当且仅当它能够被DFA所模拟

显然每一个DFA都能够被编码，因此它是可数的。

但同时我们可以看到问题集合是不可数的，那么一定存在一个函数不可被计算。（这是可以被构造出来的）

接下来我们要引出正则的概念，实则能够被DFA模拟的函数都是正则的。

有了正则这个概念，我们就能够推导正则的传递了，正则语言的并与拼接都是正则的，

这里注意在考虑拼接的时候，我们需要引出NFA的概念
- 包含状态集合、字符集合（含e）、初始状态、接收状态、转移关系
- 其重要区别是允许不确定转移和空串转移

我们可以证明NFA和DFA是等价的，因此能够被NFA所模拟的函数也是正则的。

有了NFA和DFA后我们就可以介绍正则表达式了，我们可以证明正则表达式和NFA是等价可转换的。

当有了正则表达式时，我们引出Pumping theorem

我们进一步加强我们的模型到PDA，它相当于NFA增加了一个栈

- 这里有个Configuration的概念

而这时接收状态必须使得栈清空

这时我们可以得到可接收的定义

这是一个语言的判定器，我们可以相同地定义一个语言的生成器

- 包含初始字符、总字符集、未终止字符集合、变换关系
- 被语言生成器所生成的语言称为上下文无关的

我们可以证明PDA和CFL是等价的

接着我们引出一个更强的计算模型图灵机

- 存在不可计算的图灵机.HALT
- 通过归约我们能一系列证明HALTONZERO ZEROFUNC也是不可计算的
- 归约的核心是输入的等价转换

这里还有个Rice's theorem
- 一个Property函数是non-trival 且 semantic的它就是不可计算的
- non-trival指的是它不是constant function
- semantic指的是它对所有输出相同的图灵机有相同的判断

计算时间

引出P和EXP的定义

EXP包含P

O(T(n)logn)与O(T(n))中存在一个函数

证明系统

- 存在一个不完备的证明系统

P NP EXP NPC

- 3SAT O1EQ Subset SUM的转换
- NANDSAT SAT 3SAT （NP-complete）
- BPP 













































- 单射|满射构造，编码
- universal set of gates | 证明其可以模拟 NAND
- 功能门构造 | CMP | COUNT ADD SUB XOR OR IF
- $EVAL_{s,n,m}(px)$

## 前置知识

我们如何用字符串描述物体

## 有限计算（布尔电路）

- 电路与行式程序的等价性
- 通用门集（Universal gate sets）
- Existence of a circuit for every function(EVAL)
- 用字符串表示电路
- 通用电路
- lower bound on circuit size using the counting argument

## 通用计算(Uniform computation)(Turing Machine)

- 图灵机和带循环程序的等价性
- Equivalence of models (including RAM machines, $\lambda$ calculus, and cellular automata)
- 图灵机的初始化状态
- 通用图灵机的存在性
- 不可计算的函数(包括 Halting problem 和 Rice's Theorem)
- Godel's incompleteness theorem
- restricted computational models(regular and context free languages)

## 计算效率
- 运行时间的定义
- time hierarchy theorem
- 递归函数的计算效率
- P and NP, $P_{\/poly}$, NP-C
- Cook-Levin Theorem
- space bounded computation

## Randomized computation
- 概率
- 随机算法
- BPP
- amplification
- $BPP \subset P_{\/poly}$
- pseudorandom generators and derandomization